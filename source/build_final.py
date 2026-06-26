import zipfile, shutil, os, re
import content as C
from deck import render_pptx, FONT_FILES, FONTDIR

RAW = "Masterclass_raw.pptx"
OUT = "Masterclass_Facebook_KevinChris_REDESIGN.pptx"

# 1) build slides
render_pptx(C.build_all(), RAW)
print("raw pptx built")

# 1b) port speaker notes from original (same slide order)
from pptx import Presentation as _P
orig=_P("orig.pptx"); new=_P(RAW)
orig_slides=list(orig.slides); new_slides=list(new.slides)
ported=0
for o,n in zip(orig_slides,new_slides):
    if o.has_notes_slide:
        t=o.notes_slide.notes_text_frame.text
        if t and t.strip():
            n.notes_slide.notes_text_frame.text=t; ported+=1
new.save(RAW)
print("notes ported:",ported)

# 2) embed fonts
# families used -> ttf path
fam_files = list(FONT_FILES.items())  # (typeface, filename)

tmp = "embed_tmp"
if os.path.exists(tmp): shutil.rmtree(tmp)
os.makedirs(tmp)
with zipfile.ZipFile(RAW) as z: z.extractall(tmp)

os.makedirs(os.path.join(tmp,"ppt","fonts"), exist_ok=True)
font_entries=[]  # (rid, typeface, partname)
for i,(fam,fn) in enumerate(fam_files,1):
    part=f"font{i}.fntdata"
    shutil.copy(os.path.join(FONTDIR,fn), os.path.join(tmp,"ppt","fonts",part))
    font_entries.append((f"rIdFont{i}", fam, part))

# 2a Content_Types
ct=os.path.join(tmp,"[Content_Types].xml")
s=open(ct,encoding="utf-8").read()
if 'Extension="fntdata"' not in s:
    s=s.replace("</Types>",'<Default Extension="fntdata" ContentType="application/x-fontdata"/></Types>')
open(ct,"w",encoding="utf-8").write(s)

# 2b presentation rels
rels=os.path.join(tmp,"ppt","_rels","presentation.xml.rels")
s=open(rels,encoding="utf-8").read()
add=""
for rid,fam,part in font_entries:
    add+=f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/font" Target="fonts/{part}"/>'
s=s.replace("</Relationships>",add+"</Relationships>")
open(rels,"w",encoding="utf-8").write(s)

# 2c presentation.xml
pres=os.path.join(tmp,"ppt","presentation.xml")
s=open(pres,encoding="utf-8").read()
# attributes on <p:presentation ...>
m=re.search(r"<p:presentation\b[^>]*>", s)
tag=m.group(0)
newtag=tag
if "embedTrueTypeFonts" not in newtag:
    newtag=newtag[:-1]+' embedTrueTypeFonts="1">'
if "saveSubsetFonts" not in newtag:
    newtag=newtag[:-1]+' saveSubsetFonts="1">'
s=s.replace(tag,newtag,1)
# build embeddedFontLst
efl='<p:embeddedFontLst>'
for rid,fam,part in font_entries:
    efl+=f'<p:embeddedFont><p:font typeface="{fam}"/><p:regular r:id="{rid}"/></p:embeddedFont>'
efl+='</p:embeddedFontLst>'
# insert after </p:notesSz> (correct schema position)
if "</p:notesSz>" in s:
    s=s.replace("</p:notesSz>","</p:notesSz>"+efl,1)
elif re.search(r"<p:notesSz[^>]*/>", s):
    s=re.sub(r"(<p:notesSz[^>]*/>)", r"\1"+efl, s, count=1)
else:
    s=s.replace("</p:presentation>", efl+"</p:presentation>")
open(pres,"w",encoding="utf-8").write(s)

# 3) repackage
if os.path.exists(OUT): os.remove(OUT)
with zipfile.ZipFile(OUT,"w",zipfile.ZIP_DEFLATED) as z:
    # write content types first
    for root,_,files in os.walk(tmp):
        for f in files:
            full=os.path.join(root,f)
            arc=os.path.relpath(full,tmp)
            z.write(full,arc)
print("embedded ->",OUT, round(os.path.getsize(OUT)/1024),"KB")
