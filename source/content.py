"""Contenu des 20 slides — Masterclass Kevin Chris Digital."""
from deck import *
import os

MED = "extract/ppt/media/"
def ic(n): return MED+f"image-{n}.png"

# dossier des photos clients (copiées dans test-1) + cache des avatars ronds
CLIENTS = os.environ.get("CLIENTS_DIR", "/home/user/test-1/assets/clients")
AVA_CACHE = "avatars_cache"; os.makedirs(AVA_CACHE, exist_ok=True)
def client_photo(slug):
    for ext in (".jpg",".jpeg",".png",".webp",".JPG",".jpeg"):
        p=os.path.join(CLIENTS, slug+ext)
        if os.path.exists(p): return p
    return None

MX = 0.92          # marge latérale
CW = W_IN-2*MX     # largeur contenu = 11.49
FONT_H="Montserrat ExtraBold"; FONT_HB="Montserrat Black"
FONT_T="Montserrat SemiBold"; FONT_TB="Montserrat Bold"
FONT_B="Inter"; FONT_BM="Inter Medium"; FONT_BS="Inter SemiBold"

# ---------- composants ----------
def bg(*glows, base_angle=110):
    out=[el("bg", grad=[(0,INK2,100),(55,INK,100),(100,INK_BOT,100)], angle=base_angle)]
    for g in glows: out.append(el("glow", **g))
    return out

def footer(num=None):
    return [
        el("text", x=MX, y=7.04, w=6, h=0.3, paras=[{"runs":[
            {"t":"KEVIN CHRIS DIGITAL","font":FONT_BS,"size":8.5,"color":TXT3,"spc":2.2}]}]),
        el("text", x=W_IN-MX-2, y=7.04, w=2, h=0.3, _pagenum=True, paras=[{"align":"r","runs":[
            {"t":"","font":FONT_BS,"size":8.5,"color":TXT3,"spc":1.5}]}]),
        el("line", x=MX, y=6.96, w=CW, h=0.012, fill=BORDER),
    ]

def kicker(x,y,text,grad=GR_PRIMARY,w=8):
    return [
        el("rrect", x=x, y=y+0.045, w=0.34, h=0.13, radius=0.065, grad=[(0,grad[0],100),(100,grad[1],100)], angle=0),
        el("text", x=x+0.5, y=y-0.05, w=w, h=0.34, paras=[{"runs":[
            {"t":text,"font":FONT_TB,"size":12.5,"grad":[(0,grad[0],100),(100,grad[1],100)],"gangle":0,"spc":3.0}]}]),
    ]

def heading(x,y,text,size=31,w=None,color=TXT):
    return [el("text", x=x, y=y, w=w or CW, h=size/50, paras=[{"runs":[
        {"t":text,"font":FONT_H,"size":size,"color":color}]}])]

def subtitle(x,y,text,w=None,size=14.5,color=TXT2):
    return [el("text", x=x, y=y, w=w or CW, h=0.5, paras=[{"line":1.18,"runs":[
        {"t":text,"font":FONT_B,"size":size,"color":color}]}])]

def chip(x,y,d,iconfile,grad=GR_PRIMARY,pad=0.22, tint=WHITE):
    """icon chip carré arrondi avec dégradé"""
    return [
        el("rrect", x=x, y=y, w=d, h=d, radius=d*0.30, grad=[(0,grad[0],100),(100,grad[1],100)], angle=125,
           shadow={"blur":16,"dist":6,"alpha":45,"color":grad[1]}),
        el("icon", x=x+pad, y=y+pad, w=d-2*pad, h=d-2*pad, file=iconfile, tint=tint),
    ]

def numbadge(x,y,d,num,grad=GR_PRIMARY):
    return [
        el("rrect", x=x, y=y, w=d, h=d, radius=d*0.30, fill=CARD_HI, line=BORDER_HI, line_w=1),
        el("text", x=x, y=y, w=d, h=d, valign="middle", paras=[{"align":"c","runs":[
            {"t":num,"font":FONT_HB,"size":d*46,"grad":[(0,grad[0],100),(100,grad[1],100)],"gangle":90}]}]),
    ]

def card(x,y,w,h,fill=CARD,line=BORDER,radius=0.16,shadow=True):
    e=el("rrect", x=x,y=y,w=w,h=h,radius=radius,fill=fill,line=line,line_w=1.1)
    if shadow: e["shadow"]={"blur":22,"dist":11,"alpha":40}
    return [e]

def textbox(x,y,w,h,paras,valign="top"):
    return [el("text", x=x,y=y,w=w,h=h,valign=valign,paras=paras)]

def bullets(items, size=12.5, gap=7, color=TXT2, lh=1.16, marker=BLUE):
    paras=[]
    for i,it in enumerate(items):
        paras.append({"space_before":0 if i==0 else gap,"line":lh,"runs":[
            {"t":"—  ","font":FONT_BS,"size":size,"color":marker},
            {"t":it,"font":FONT_B,"size":size,"color":color}]})
    return paras

# =====================================================================
def slide_cover():
    s=bg({"cx":12.4,"cy":6.9,"r":4.7,"color":VIOLET,"alpha":42},
         {"cx":0.4,"cy":0.3,"r":3.6,"color":BLUE,"alpha":34},
         {"cx":10.6,"cy":0.7,"r":2.4,"color":CYAN,"alpha":20})
    s+=[el("line", x=MX, y=1.02, w=2.2, h=0.02, grad=[(0,BLUE,100),(100,VIOLET,100)], angle=0)]
    s+=kicker(MX,1.18,"MASTERCLASS LIVE  ·  CRÉATION & MONÉTISATION", w=11)
    s+=[el("text", x=MX, y=1.92, w=11.7, h=2.5, paras=[
        {"line":1.0,"runs":[{"t":"Créer du contenu","font":FONT_HB,"size":58,"color":TXT}]},
        {"line":1.0,"space_before":4,"runs":[
            {"t":"& monétiser ","font":FONT_HB,"size":58,"color":TXT},
            {"t":"Facebook","font":FONT_HB,"size":58,"grad":[(0,BLUE,100),(100,VIOLET,100)],"gangle":0}]},
    ])]
    s+=subtitle(MX,4.42,"La méthode claire, simple et adaptée à l'Afrique — même si tu pars de zéro, "
                "et même si ton pays n'est pas encore éligible.", w=10.4, size=15.5)
    # presenter card
    s+=card(MX,5.5,6.4,1.18,fill=CARD,line=BORDER)
    s+=chip(MX+0.26,5.74,0.7,ic("1-1"),grad=GR_PRIMARY,pad=0.16)
    s+=textbox(MX+1.18,5.66,5.1,1.0,[
        {"runs":[{"t":"Kevin Chris Atchof","font":FONT_TB,"size":16.5,"color":TXT}]},
        {"space_before":2,"line":1.12,"runs":[{"t":"Le créateur le plus suivi d'Afrique francophone sur la monétisation Facebook","font":FONT_B,"size":11,"color":TXT2}]},
    ],valign="middle")
    s+=[el("text", x=W_IN-MX-3, y=6.95, w=3, h=0.3, paras=[{"align":"r","runs":[
        {"t":"© Kevin Chris Digital","font":FONT_BS,"size":9.5,"color":TXT3,"spc":1}]}])]
    return s

def agenda_card(x,y,w,h,num,iconf,title,desc,grad):
    out=card(x,y,w,h)
    # grand chiffre filigrane décoratif, coin bas-droit
    out+=[el("text", x=x+w-1.6, y=y+h-1.18, w=1.45, h=1.05, valign="bottom", paras=[{"align":"r","runs":[
        {"t":num,"font":FONT_HB,"size":52,"color":CARD_HI}]}])]
    out+=chip(x+0.30,y+0.30,0.66,iconf,grad=grad,pad=0.15)
    out+=textbox(x+0.30,y+1.12,w-0.6,0.62,[{"line":1.05,"runs":[{"t":title,"font":FONT_TB,"size":14.5,"color":TXT}]}])
    out+=textbox(x+0.30,y+1.62,w-0.6,h-1.75,[{"line":1.16,"runs":[{"t":desc,"font":FONT_B,"size":11.5,"color":TXT2}]}])
    return out

def slide_agenda():
    s=bg({"cx":-0.3,"cy":-0.3,"r":3.2,"color":BLUE,"alpha":26},
         {"cx":13.2,"cy":7.6,"r":3.6,"color":VIOLET,"alpha":30})
    s+=kicker(MX,0.62,"AU PROGRAMME AUJOURD'HUI")
    s+=heading(MX,1.0,"6 étapes pour passer de zéro aux revenus",size=29)
    s+=subtitle(MX,1.66,"Environ 1h45 — pose tes questions à la fin de chaque partie.",size=13.5,color=TXT3)
    items=[("01",ic("2-1"),"Comprendre Facebook","L'algorithme et ce que Meta veut vraiment de toi.",GR_PRIMARY),
           ("02",ic("2-2"),"Créer du contenu qui performe","Niche, formats, régularité, le HOOK qui décolle.",GR_PRIMARY),
           ("03",ic("2-3"),"Les programmes de monétisation","Le CMP 2025 et les conditions d'éligibilité.",GR_GOLD),
           ("04",ic("2-4"),"Monétiser depuis un pays inéligible","La stratégie de contournement 100% légale.",GR_CYAN),
           ("05",ic("2-5"),"Gérer les restrictions","Éviter les blocages et sécuriser ta page.",GR_ROSE),
           ("06",ic("2-6"),"Diversifier tes revenus","Vendre tes propres produits avec ta page.",GR_GREEN)]
    cw=(CW-2*0.36)/3; ch=2.18; x0=MX; y0=2.36
    for i,(n,f,ti,de,gr) in enumerate(items):
        r,c=divmod(i,3)
        s+=agenda_card(x0+c*(cw+0.36), y0+r*(ch+0.32), cw, ch, n,f,ti,de,gr)
    s+=footer()
    return s

def story_card(x,y,w,h,iconf,badge,title,desc,grad):
    out=card(x,y,w,h)
    out+=chip(x+0.30,y+0.32,0.62,iconf,grad=grad,pad=0.14)
    out+=[el("rrect", x=x+1.04, y=y+0.40, w=1.5, h=0.34, radius=0.17, fill=CARD_HI, line=BORDER_HI, line_w=1)]
    out+=textbox(x+1.04,y+0.40,1.5,0.34,[{"align":"c","runs":[{"t":badge,"font":FONT_BS,"size":9.5,"grad":[(0,grad[0],100),(100,grad[1],100)],"gangle":0,"spc":0.5}]}],valign="middle")
    out+=textbox(x+0.30,y+1.12,w-0.6,0.5,[{"runs":[{"t":title,"font":FONT_TB,"size":16,"color":TXT}]}])
    out+=textbox(x+0.30,y+1.6,w-0.6,h-1.7,[{"line":1.2,"runs":[{"t":desc,"font":FONT_B,"size":12,"color":TXT2}]}])
    return out

def slide_story():
    s=bg({"cx":13.0,"cy":-0.4,"r":3.6,"color":VIOLET,"alpha":30},
         {"cx":-0.2,"cy":7.7,"r":3.2,"color":BLUE,"alpha":24})
    s+=kicker(MX,0.62,"MON HISTOIRE")
    s+=heading(MX,1.0,"J'ai vécu exactement ce que tu vis",size=30)
    cw=(CW-0.4)/2; ch=2.18; x0=MX; y0=1.95
    cards=[(ic("3-1"),"2023","Le décollage","Deux vidéos (clonage WhatsApp + LuzIA) propulsent ma page de 2 000 à plus de 12 000 abonnés. Des millions de vues.",GR_PRIMARY),
           (ic("3-2"),"L'ERREUR","L'erreur fatale","Depuis le Cameroun (pays inéligible), je configure ma monétisation avec mes vraies infos. Ma page est bloquée.",GR_ROSE),
           (ic("3-3"),"LE DÉSERT","La traversée du désert","« Tu as gâté ta page », me disaient les experts. J'ai cherché, je me suis formé, j'ai parlé à l'équipe Meta.",GR_GOLD),
           (ic("3-4"),"MAI 2024","La renaissance","Je résous le problème que personne ne savait régler. Aujourd'hui, j'aide des créateurs à débloquer leurs pages.",GR_GREEN)]
    for i,(f,b,ti,de,gr) in enumerate(cards):
        r,c=divmod(i,2)
        s+=story_card(x0+c*(cw+0.4), y0+r*(ch+0.34), cw, ch, f,b,ti,de,gr)
    s+=footer()
    return s

# =====================================================================
#  SÉPARATEUR DE SECTION
# =====================================================================
def section(num, partlabel, title, subtitle_txt, iconf, grad, glowcol):
    s=bg({"cx":11.8,"cy":3.75,"r":4.4,"color":glowcol,"alpha":40},
         {"cx":0.2,"cy":7.4,"r":3.2,"color":grad[0],"alpha":24},
         {"cx":1.0,"cy":0.2,"r":2.0,"color":grad[1],"alpha":16})
    # gros chiffre filigrane
    s+=[el("text", x=6.7, y=-0.5, w=7.0, h=8.0, valign="middle", paras=[{"align":"r","runs":[
        {"t":num,"font":FONT_HB,"size":340,"color":"111A30"}]}])]
    s+=[el("line", x=MX, y=2.62, w=2.0, h=0.02, grad=[(0,grad[0],100),(100,grad[1],100)], angle=0)]
    s+=kicker(MX,2.78,partlabel,grad=grad,w=8)
    s+=[el("text", x=MX, y=3.25, w=9.6, h=1.7, paras=[{"line":1.02,"runs":[
        {"t":title,"font":FONT_HB,"size":46,"color":TXT}]}])]
    s+=subtitle(MX,5.18,subtitle_txt,w=8.8,size=16,color=TXT2)
    # grande pastille icône
    s+=chip(11.05,2.95,1.55,iconf,grad=grad,pad=0.42)
    s+=footer_min(grad)
    return s

def footer_min(grad):
    return [el("text", x=MX, y=7.04, w=6, h=0.3, paras=[{"runs":[
        {"t":"KEVIN CHRIS DIGITAL","font":FONT_BS,"size":8.5,"color":TXT3,"spc":2.2}]}])]

# =====================================================================
#  SLIDE 5 — Algorithme
# =====================================================================
def slide_algo():
    s=bg({"cx":-0.2,"cy":0.0,"r":3.0,"color":BLUE,"alpha":26},
         {"cx":13.2,"cy":7.6,"r":3.6,"color":VIOLET,"alpha":28})
    s+=kicker(MX,0.55,"PARTIE 1 · COMPRENDRE FACEBOOK")
    s+=heading(MX,0.94,"L'algorithme, c'est ton patron exigeant",size=29)
    s+=subtitle(MX,1.6,"Il ne paie pas celui qui travaille dur, mais celui qui attire l'attention — et respecte le règlement.",size=13.5,color=TXT3)
    # grande carte gauche
    lx,ly,lw,lh=MX,2.4,5.55,4.05
    s+=card(lx,ly,lw,lh,fill=CARD2)
    s+=chip(lx+0.34,ly+0.36,0.74,ic("5-1"),grad=GR_PRIMARY,pad=0.17)
    s+=textbox(lx+1.26,ly+0.5,lw-1.5,0.7,[{"runs":[{"t":"Le petit test de visibilité","font":FONT_TB,"size":18,"color":TXT}]}],valign="middle")
    steps=[("Facebook ne montre d'abord ton contenu qu'à 1–2 % de tes abonnés.",GR_PRIMARY),
           ("S'ils réagissent vite (likes, commentaires, partages, temps de visionnage) → ton contenu décolle.",GR_GREEN),
           ("Sinon → l'algorithme l'enterre, et personne d'autre ne le verra.",GR_ROSE)]
    sy=ly+1.5
    for i,(txt,gr) in enumerate(steps):
        s+=[el("rrect", x=lx+0.34, y=sy+0.02, w=0.30, h=0.30, radius=0.15, grad=[(0,gr[0],100),(100,gr[1],100)], angle=90)]
        s+=textbox(lx+0.86,sy-0.06,lw-1.2,0.85,[{"line":1.16,"runs":[{"t":txt,"font":FONT_BM,"size":13,"color":TXT2}]}])
        sy+=0.85
    # 3 cartes droite
    rx=MX+lw+0.4; rw=CW-lw-0.4; rh=1.24; ry=2.4; gap=0.16
    rights=[(ic("5-2"),"Engagement immédiat","Les réactions dans la 1re heure décident de tout. D'où l'importance du HOOK : tes 3 premières secondes.",GR_GOLD),
            (ic("5-3"),"Temps passé","Une vidéo regardée jusqu'au bout vaut plus que 5 likes rapides. Te liker toi-même ne sert à rien.",GR_CYAN),
            (ic("5-4"),"Régularité","Quand tu disparais, l'algorithme t'oublie. Il récompense ceux qui nourrissent leur audience souvent.",GR_GREEN)]
    for i,(f,ti,de,gr) in enumerate(rights):
        cy=ry+i*(rh+gap)
        s+=card(rx,cy,rw,rh)
        s+=chip(rx+0.3,cy+0.3,0.62,f,grad=gr,pad=0.14)
        s+=textbox(rx+1.06,cy+0.26,rw-1.3,0.4,[{"runs":[{"t":ti,"font":FONT_TB,"size":14,"color":TXT}]}])
        s+=textbox(rx+1.06,cy+0.66,rw-1.32,0.55,[{"line":1.12,"runs":[{"t":de,"font":FONT_B,"size":10.8,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 6 — Écosystème Meta
# =====================================================================
def slide_ecosystem():
    s=bg({"cx":13.0,"cy":-0.2,"r":3.2,"color":BLUE,"alpha":26},
         {"cx":0.0,"cy":7.6,"r":3.4,"color":VIOLET,"alpha":26})
    s+=kicker(MX,0.55,"PARTIE 1 · COMPRENDRE FACEBOOK")
    s+=heading(MX,0.94,"L'écosystème Meta : chaque app a un rôle",size=27)
    s+=subtitle(MX,1.56,"Meta n'a pas créé ses apps pour te divertir, mais pour capter et garder ton audience. Avance progressivement.",size=13,color=TXT3)
    apps=[(ic("6-1"),"Facebook","Ton point de départ. 80 % de mes efforts. Le réseau N°1 de la monétisation chez Meta.",GR_PRIMARY),
          (ic("6-2"),"Instagram","La vitrine visuelle. Les Reels circulent entre les deux — mais une restriction sur l'un affecte l'autre.",GR_ROSE),
          (ic("6-3"),"WhatsApp","Là où tu transformes les likes en argent : la conversation privée qui convertit en client.",GR_GREEN),
          (ic("6-4"),"Messenger","Ton assistant automatisé : chatbots et réponses auto (ex. ManyChat) pour répondre à 100 personnes à la fois.",GR_CYAN),
          (ic("6-5"),"Business Suite","Ton centre de contrôle : planifier, analyser, configurer la monétisation, résoudre les restrictions.",GR_PRIMARY),
          (ic("6-6"),"Meta Ads","La régie qui finance les créateurs. Mais ne sponsorise pas la page que tu veux monétiser.",GR_GOLD)]
    cw=(CW-2*0.34)/3; ch=2.12; x0=MX; y0=2.28
    for i,(f,ti,de,gr) in enumerate(apps):
        r,c=divmod(i,3)
        x=x0+c*(cw+0.34); y=y0+r*(ch+0.3)
        s+=card(x,y,cw,ch)
        s+=chip(x+0.3,y+0.3,0.64,f,grad=gr,pad=0.15)
        s+=textbox(x+1.08,y+0.42,cw-1.3,0.5,[{"runs":[{"t":ti,"font":FONT_TB,"size":15,"color":TXT}]}],valign="middle")
        s+=textbox(x+0.3,y+1.18,cw-0.6,ch-1.3,[{"line":1.18,"runs":[{"t":de,"font":FONT_B,"size":11,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 8 — Niche & portée
# =====================================================================
def slide_niche():
    s=bg({"cx":-0.2,"cy":0.2,"r":3.0,"color":VIOLET,"alpha":26},
         {"cx":13.2,"cy":7.4,"r":3.4,"color":BLUE,"alpha":26})
    s+=kicker(MX,0.55,"PARTIE 2 · CRÉER DU CONTENU",grad=GR_ROSE)
    s+=heading(MX,0.94,"Niche rentable & portée organique",size=29)
    cw=(CW-0.4)/2; cy=1.95; ch=4.55
    # gauche
    lx=MX
    s+=card(lx,cy,cw,ch,fill=CARD2)
    s+=chip(lx+0.36,cy+0.36,0.72,ic("8-1"),grad=GR_ROSE,pad=0.17)
    s+=textbox(lx+1.26,cy+0.5,cw-1.5,0.7,[{"runs":[{"t":"Choisir sa niche","font":FONT_TB,"size":18,"color":TXT}]}],valign="middle")
    s+=textbox(lx+0.4,cy+1.4,cw-0.8,0.4,[{"runs":[{"t":"Au croisement de 3 cercles :","font":FONT_BS,"size":13,"color":TXT}]}])
    circ=["Ta passion / ton expertise","Une demande réelle de l'audience","Un potentiel de monétisation"]
    yy=cy+1.95
    for it in circ:
        s+=[el("rrect", x=lx+0.42, y=yy+0.02, w=0.26, h=0.26, radius=0.13, grad=[(0,ROSE,100),(100,VIOLET,100)], angle=90)]
        s+=textbox(lx+0.9,yy-0.04,cw-1.3,0.4,[{"runs":[{"t":it,"font":FONT_BM,"size":13,"color":TXT2}]}])
        yy+=0.5
    s+=[el("line", x=lx+0.4, y=yy+0.08, w=cw-0.8, h=0.014, fill=BORDER)]
    s+=textbox(lx+0.4,yy+0.3,cw-0.8,1.0,[{"line":1.2,"runs":[{"t":"Une niche claire = une audience fidèle = un algorithme qui comprend exactement à qui te montrer.","font":FONT_BS,"size":13,"color":TXT}]}])
    # droite
    rx=MX+cw+0.4
    s+=card(rx,cy,cw,ch)
    s+=chip(rx+0.36,cy+0.36,0.72,ic("8-2"),grad=GR_PRIMARY,pad=0.17)
    s+=textbox(rx+1.26,cy+0.42,cw-1.5,0.8,[{"line":1.05,"runs":[{"t":"Booster ta portée (gratuitement)","font":FONT_TB,"size":17,"color":TXT}]}],valign="middle")
    boost=[("Soigne ton HOOK","titre ou 3 premières secondes."),
           ("Provoque le commentaire","polarise, pose une question."),
           ("Vise le partage","un contenu utile lié à la sécurité se partage seul."),
           ("Mise sur les Reels","c'est là que l'algorithme pousse la visibilité."),
           ("Publie régulièrement","la constance bat la perfection.")]
    yy=cy+1.55
    for t1,t2 in boost:
        s+=[el("rrect", x=rx+0.4, y=yy+0.05, w=0.26, h=0.26, radius=0.13, grad=[(0,BLUE,100),(100,VIOLET,100)], angle=90)]
        s+=textbox(rx+0.86,yy-0.02,cw-1.25,0.5,[{"line":1.12,"runs":[
            {"t":t1+" — ","font":FONT_BS,"size":13,"color":TXT},
            {"t":t2,"font":FONT_B,"size":13,"color":TXT2}]}])
        yy+=0.59
    s+=footer()
    return s

# =====================================================================
#  SLIDE 10 — CMP 2025
# =====================================================================
def slide_cmp():
    s=bg({"cx":13.0,"cy":0.0,"r":3.2,"color":GOLD,"alpha":24},
         {"cx":0.0,"cy":7.6,"r":3.2,"color":BLUE,"alpha":22})
    s+=kicker(MX,0.55,"PARTIE 3 · MONÉTISATION",grad=GR_GOLD)
    s+=heading(MX,0.94,"Le Content Monetization Program (CMP) 2025",size=26)
    s+=subtitle(MX,1.54,"Depuis 2025, Facebook unifie tout. Fini les programmes dispersés (In-Stream, Ads Reels, Bonus de performance).",size=13,color=TXT3)
    cw=(CW-0.4)/2; cy=2.2; ch=1.95
    # avant
    s+=card(MX,cy,cw,ch,fill=CARD,line=BORDER)
    s+=[el("rrect", x=MX+0.34, y=cy+0.32, w=0.28, h=0.28, radius=0.14, fill=ROSE)]
    s+=textbox(MX+0.78,cy+0.28,cw-1,0.4,[{"runs":[{"t":"AVANT — programmes dispersés","font":FONT_BS,"size":12.5,"color":ROSE,"spc":0.5}]}])
    s+=textbox(MX+0.36,cy+0.92,cw-0.7,0.95,[{"line":1.25,"runs":[{"t":"Publicités In-Stream · Ads sur Reels · Bonus de performance · Abonnements · Étoiles · Contenu de marque","font":FONT_B,"size":12,"color":TXT2}]}])
    # depuis
    rx=MX+cw+0.4
    s+=card(rx,cy,cw,ch,fill=CARD2,line=BORDER_HI)
    s+=[el("rrect", x=rx+0.34, y=cy+0.32, w=0.28, h=0.28, radius=0.14, grad=[(0,GOLD,100),(100,GOLD2,100)], angle=90)]
    s+=textbox(rx+0.78,cy+0.28,cw-1,0.4,[{"runs":[{"t":"DEPUIS 2025 — un système unique : le CMP","font":FONT_BS,"size":12.5,"grad":[(0,GOLD,100),(100,GOLD2,100)],"gangle":0,"spc":0.3}]}])
    s+=textbox(rx+0.36,cy+0.92,cw-0.7,0.95,[{"line":1.25,"runs":[{"t":"Un seul programme, un seul tableau de bord centralisé. Rémunération basée sur la performance de chaque contenu.","font":FONT_B,"size":12,"color":TXT2}]}])
    # 3 features
    fw=(CW-2*0.34)/3; fy=4.5; fh=1.95
    feats=[(ic("10-1"),"Tous les formats payés","Pas seulement les vidéos : aussi les photos, les posts texte, et bientôt les stories.",GR_PRIMARY),
           (ic("10-2"),"Basé sur la performance","Vues, durée de visionnage, engagement et format déterminent tes gains.",GR_GOLD),
           (ic("10-3"),"Tout centralisé","Un tableau de bord unique pour suivre revenus, performances et conformité.",GR_CYAN)]
    for i,(f,ti,de,gr) in enumerate(feats):
        x=MX+i*(fw+0.34)
        s+=card(x,fy,fw,fh)
        s+=chip(x+0.3,fy+0.3,0.62,f,grad=gr,pad=0.14)
        s+=textbox(x+0.3,fy+1.06,fw-0.6,0.4,[{"runs":[{"t":ti,"font":FONT_TB,"size":13.5,"color":TXT}]}])
        s+=textbox(x+0.3,fy+1.44,fw-0.6,0.5,[{"line":1.14,"runs":[{"t":de,"font":FONT_B,"size":10.8,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 11 — Éligibilité
# =====================================================================
def slide_eligibility():
    s=bg({"cx":-0.2,"cy":0.0,"r":3.0,"color":GOLD,"alpha":22},
         {"cx":13.2,"cy":7.4,"r":3.4,"color":VIOLET,"alpha":26})
    s+=kicker(MX,0.55,"PARTIE 3 · MONÉTISATION",grad=GR_GOLD)
    s+=heading(MX,0.94,"Es-tu éligible ? Les conditions du CMP",size=29)
    s+=subtitle(MX,1.6,"Même avec des millions de vues, une page peut être refusée. La préparation fait la différence.",size=13.5,color=TXT3)
    cards=[(ic("11-1"),"18 ans minimum","Et une page active ou un profil en mode professionnel.",GR_PRIMARY),
           (ic("11-2"),"5 000 abonnés","Parfois l'invitation arrive avant. Mon conseil : attends 50k et des publications virales.",GR_CYAN),
           (ic("11-3"),"Conformité stricte","Contenu original, pas de droits d'auteur violés, respect des normes communautaires.",GR_GREEN),
           (ic("11-4"),"Pays éligible","Selon la liste de Meta — et elle évolue. Sinon → Partie 4.",GR_GOLD)]
    cw=(CW-0.4)/2; ch=1.34; y0=2.36
    for i,(f,ti,de,gr) in enumerate(cards):
        r,c=divmod(i,2)
        x=MX+c*(cw+0.4); y=y0+r*(ch+0.22)
        s+=card(x,y,cw,ch)
        s+=chip(x+0.3,y+0.32,0.66,f,grad=gr,pad=0.15)
        s+=textbox(x+1.12,y+0.28,cw-1.4,0.4,[{"runs":[{"t":ti,"font":FONT_TB,"size":15,"color":TXT}]}])
        s+=textbox(x+1.12,y+0.68,cw-1.4,0.6,[{"line":1.12,"runs":[{"t":de,"font":FONT_B,"size":11,"color":TXT2}]}])
    # bandeau avertissement
    wy=2.36+2*(ch+0.22)+0.04; wh=1.0
    s+=[el("rrect", x=MX, y=wy, w=CW, h=wh, radius=0.16, fill="2A1A20", line=ROSE, line_w=1.2,
           shadow={"blur":20,"dist":9,"alpha":40,"color":ROSE})]
    s+=chip(MX+0.34,wy+(wh-0.62)/2,0.62,ic("11-5"),grad=GR_ROSE,pad=0.14)
    s+=textbox(MX+1.18,wy+0.16,CW-1.5,wh-0.3,[
        {"runs":[{"t":"Le piège que beaucoup oublient","font":FONT_TB,"size":13.5,"color":ROSE}]},
        {"space_before":3,"line":1.12,"runs":[{"t":"Sans compte de règlement validé, Facebook ne pourra JAMAIS te payer — même avec des millions de vues.","font":FONT_B,"size":12,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 13 — Stratégie 4 étapes
# =====================================================================
def slide_strategy():
    s=bg({"cx":13.0,"cy":0.0,"r":3.2,"color":CYAN,"alpha":24},
         {"cx":0.0,"cy":7.6,"r":3.2,"color":BLUE,"alpha":24})
    s+=kicker(MX,0.55,"PARTIE 4 · PAYS INÉLIGIBLE",grad=GR_CYAN)
    s+=heading(MX,0.94,"La stratégie de contournement, étape par étape",size=26)
    s+=subtitle(MX,1.54,"Légale et testée sur le terrain. La condition de base : une page déjà créée et bien développée.",size=13,color=TXT3)
    steps=[("1","Ajouter un admin éligible","Un proche de confiance ou un prestataire résidant dans un pays éligible, avec contrôle total. Protège-toi via un portefeuille Business."),
           ("2","Réinitialiser ton accès","Déconnecte tes autres appareils, vide le cache, désinstalle Facebook. Active un VPN sur le pays éligible, vérifie via DNS leak test, réinstalle."),
           ("3","Attendre l'invitation","L'admin ouvre la page régulièrement depuis le pays éligible. Dès que la condition « pays » est validée, tu passes à la config."),
           ("4","Configurer SANS erreur","Les infos du compte de règlement doivent venir du pays éligible. Garde le compte de règlement sur TON propre compte pour le contrôle.")]
    cw=(CW-0.4)/2; ch=1.92; y0=2.2
    for i,(n,ti,de) in enumerate(steps):
        r,c=divmod(i,2)
        x=MX+c*(cw+0.4); y=y0+r*(ch+0.26)
        s+=card(x,y,cw,ch,fill=CARD2)
        s+=numbadge(x+0.32,y+0.32,0.66,n,grad=GR_CYAN)
        s+=textbox(x+1.16,y+0.36,cw-1.4,0.5,[{"runs":[{"t":ti,"font":FONT_TB,"size":15.5,"color":TXT}]}],valign="middle")
        s+=textbox(x+0.34,y+1.08,cw-0.66,0.8,[{"line":1.16,"runs":[{"t":de,"font":FONT_B,"size":11.5,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 14 — PayPal & déblocage
# =====================================================================
def slide_paypal():
    s=bg({"cx":-0.2,"cy":0.2,"r":3.0,"color":CYAN,"alpha":24},
         {"cx":13.2,"cy":7.4,"r":3.4,"color":VIOLET,"alpha":24})
    s+=kicker(MX,0.55,"PARTIE 4 · PAYS INÉLIGIBLE",grad=GR_CYAN)
    s+=heading(MX,0.94,"Encaisser : PayPal & déblocage du compte",size=27)
    cw=(CW-0.4)/2; cy=1.95; ch=4.55
    # gauche PayPal
    lx=MX
    s+=card(lx,cy,cw,ch,fill=CARD2)
    s+=chip(lx+0.36,cy+0.36,0.72,ic("14-1"),grad=GR_CYAN,pad=0.17)
    s+=textbox(lx+1.26,cy+0.42,cw-1.5,0.8,[{"line":1.05,"runs":[{"t":"PayPal depuis un pays inéligible","font":FONT_TB,"size":17,"color":TXT}]}],valign="middle")
    pp=["Passe par le site (pas l'appli) et change le domaine : paypal.com/fr, /de, /be…",
        "Numéro réel du pays éligible (évite les numéros virtuels).",
        "Email neuf dédié + adresse physique réelle d'un proche.",
        "Crée un compte Business + un compte perso pour retirer via Xoom vers ton mobile money."]
    yy=cy+1.55
    for it in pp:
        s+=[el("rrect", x=lx+0.4, y=yy+0.04, w=0.26, h=0.26, radius=0.13, grad=[(0,CYAN,100),(100,BLUE,100)], angle=90)]
        s+=textbox(lx+0.86,yy-0.04,cw-1.25,0.75,[{"line":1.16,"runs":[{"t":it,"font":FONT_B,"size":12.5,"color":TXT2}]}])
        yy+=0.74
    # droite déblocage
    rx=MX+cw+0.4
    s+=card(rx,cy,cw,ch)
    s+=chip(rx+0.36,cy+0.36,0.72,ic("14-2"),grad=GR_ROSE,pad=0.17)
    s+=textbox(rx+1.26,cy+0.42,cw-1.5,0.8,[{"line":1.05,"runs":[{"t":"Compte de règlement bloqué ?","font":FONT_TB,"size":17,"color":TXT}]}],valign="middle")
    s+=textbox(rx+0.4,cy+1.5,cw-0.8,1.0,[{"line":1.2,"runs":[{"t":"90 % des créateurs inéligibles tombent dans ce piège : invités à la monétisation, ils configurent… et la validation est refusée.","font":FONT_B,"size":12.5,"color":TXT2}]}])
    s+=[el("rrect", x=rx+0.4, y=cy+2.75, w=cw-0.8, h=1.05, radius=0.13, fill=CARD_HI, line=BORDER_HI, line_w=1)]
    s+=textbox(rx+0.62,cy+2.92,cw-1.2,0.8,[{"line":1.18,"runs":[
        {"t":"La solution : ","font":FONT_BS,"size":12.5,"color":GREEN},
        {"t":"un compte bien configuré + le document Meta Payout Source Transfer, signé via Docusign et envoyé au support depuis ton ordinateur.","font":FONT_B,"size":12.5,"color":TXT2}]}])
    s+=textbox(rx+0.4,cy+3.95,cw-0.8,0.5,[{"runs":[{"t":"Une fois validé, tu peux y relier ton propre PayPal.","font":FONT_BS,"size":12,"color":TXT}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 16 — Protéger & diversifier
# =====================================================================
def slide_protect():
    s=bg({"cx":13.0,"cy":0.2,"r":3.2,"color":ROSE,"alpha":22},
         {"cx":0.0,"cy":7.4,"r":3.2,"color":GREEN,"alpha":20})
    s+=kicker(MX,0.55,"PARTIE 5 · RESTRICTIONS & DIVERSIFICATION",grad=GR_ROSE,w=10)
    s+=heading(MX,0.94,"Protéger ta page & ne pas dépendre de Facebook",size=26)
    cw=(CW-0.4)/2; cy=1.95; ch=4.55
    lx=MX
    s+=card(lx,cy,cw,ch,fill=CARD2)
    s+=chip(lx+0.36,cy+0.36,0.72,ic("16-1"),grad=GR_ROSE,pad=0.17)
    s+=textbox(lx+1.26,cy+0.42,cw-1.5,0.8,[{"line":1.05,"runs":[{"t":"Éviter & gérer les restrictions","font":FONT_TB,"size":17,"color":TXT}]}],valign="middle")
    prot=["Respecte strictement les normes : pas de contenu trompeur, violent, haineux ou volé.",
          "Surveille ton score de conformité dans Meta Business Suite.",
          "Attention à la liaison Facebook–Instagram : une restriction sur l'un touche l'autre.",
          "En cas de sanction : garde ton calme et utilise les recours officiels."]
    yy=cy+1.55
    for it in prot:
        s+=[el("rrect", x=lx+0.4, y=yy+0.04, w=0.26, h=0.26, radius=0.13, grad=[(0,ROSE,100),(100,VIOLET,100)], angle=90)]
        s+=textbox(lx+0.86,yy-0.04,cw-1.25,0.8,[{"line":1.16,"runs":[{"t":it,"font":FONT_B,"size":12.5,"color":TXT2}]}])
        yy+=0.78
    rx=MX+cw+0.4
    s+=card(rx,cy,cw,ch,fill=CARD2)
    s+=chip(rx+0.36,cy+0.36,0.72,ic("16-2"),grad=GR_GREEN,pad=0.17)
    s+=textbox(rx+1.26,cy+0.42,cw-1.5,0.8,[{"line":1.05,"runs":[{"t":"Facebook est un tremplin, pas un patron","font":FONT_TB,"size":16,"color":TXT}]}],valign="middle")
    div=["Vends tes propres produits (physiques ou digitaux) : tu n'attends plus que Facebook te paie.",
         "Aligne tes produits sur ta niche et ton audience (insights Facebook).",
         "Affiliation, événements payants, services personnalisés."]
    yy=cy+1.55
    for it in div:
        s+=[el("rrect", x=rx+0.4, y=yy+0.04, w=0.26, h=0.26, radius=0.13, grad=[(0,GREEN,100),(100,CYAN,100)], angle=90)]
        s+=textbox(rx+0.86,yy-0.04,cw-1.25,0.8,[{"line":1.16,"runs":[{"t":it,"font":FONT_B,"size":12.5,"color":TXT2}]}])
        yy+=0.82
    s+=[el("rrect", x=rx+0.4, y=yy+0.18, w=cw-0.8, h=0.78, radius=0.13, grad=[(0,GREEN,16),(100,CYAN,16)], angle=90, line=BORDER_HI, line_w=1)]
    s+=textbox(rx+0.4,yy+0.18,cw-0.8,0.78,[{"align":"c","runs":[{"t":"« Ne mets pas tous tes œufs dans le même panier. »","font":FONT_BS,"size":13,"color":TXT}]}],valign="middle")
    s+=footer()
    return s

# =====================================================================
#  SLIDE 17 — Et maintenant ?
# =====================================================================
def slide_now():
    s=bg({"cx":12.6,"cy":6.9,"r":4.6,"color":VIOLET,"alpha":40},
         {"cx":0.3,"cy":0.3,"r":3.4,"color":BLUE,"alpha":32},
         {"cx":11.0,"cy":0.6,"r":2.2,"color":GOLD,"alpha":16})
    s+=kicker(MX,1.15,"ET MAINTENANT ?")
    s+=[el("text", x=MX, y=1.72, w=11.5, h=2.2, paras=[
        {"line":1.04,"runs":[{"t":"Je t'ai montré le ","font":FONT_HB,"size":44,"color":TXT},
                              {"t":"QUOI","font":FONT_HB,"size":44,"grad":[(0,BLUE,100),(100,VIOLET,100)],"gangle":0},
                              {"t":".","font":FONT_HB,"size":44,"color":TXT}]},
        {"line":1.04,"space_before":4,"runs":[{"t":"Mon pack te donne le ","font":FONT_HB,"size":44,"color":TXT},
                              {"t":"COMMENT","font":FONT_HB,"size":44,"grad":[(0,GOLD,100),(100,GOLD2,100)],"gangle":0},
                              {"t":",","font":FONT_HB,"size":44,"color":TXT}]},
        {"line":1.04,"runs":[{"t":"étape par étape.","font":FONT_HB,"size":44,"color":TXT}]},
    ])]
    rows=[(ic("17-1"),"Le guide complet, 7 chapitres, écrit à partir de mon expérience réelle"),
          (ic("17-2"),"Des tutoriels vidéo pas-à-pas pour la config et le déblocage"),
          (ic("17-3"),"Une communauté privée WhatsApp pour ne jamais rester bloqué")]
    yy=4.95
    for f,txt in rows:
        s+=chip(MX,yy,0.5,f,grad=GR_PRIMARY,pad=0.11)
        s+=textbox(MX+0.74,yy,9.8,0.5,[{"runs":[{"t":txt,"font":FONT_BM,"size":15,"color":TXT}]}],valign="middle")
        yy+=0.66
    s+=[el("text", x=W_IN-MX-3, y=6.95, w=3, h=0.3, paras=[{"align":"r","runs":[
        {"t":"© Kevin Chris Digital","font":FONT_BS,"size":9.5,"color":TXT3,"spc":1}]}])]
    return s

# =====================================================================
#  SLIDE 18 — Pricing
# =====================================================================
def slide_pricing():
    s=bg({"cx":-0.2,"cy":0.2,"r":3.0,"color":BLUE,"alpha":24},
         {"cx":13.2,"cy":7.4,"r":3.4,"color":GOLD,"alpha":24})
    s+=kicker(MX,0.5,"OFFRE SPÉCIALE DU LIVE",grad=GR_GOLD)
    s+=heading(MX,0.88,"Choisis ton niveau d'accompagnement",size=28)
    s+=subtitle(MX,1.5,"Trois façons de passer à l'action aujourd'hui.",size=13,color=TXT3)
    cw=(CW-2*0.36)/3; y0=2.02; ch=4.8
    plans=[(ic("18-1"),"LE GUIDE","Guide Complet Monétisation Facebook","9 900","FCFA",
            ["Les 7 chapitres complets","L'algorithme & la stratégie contenu","Pour démarrer seul, à ton rythme"],GR_PRIMARY,False),
           (ic("18-2"),"LE PACK","Guide + Formation Produits Digitaux","14 900","FCFA",
            ["Tout le guide inclus","Créer & vendre tes produits digitaux","Le meilleur rapport valeur / prix"],GR_GOLD,True),
           (ic("18-3"),"ACCOMPAGNEMENT","Coaching contenu + monétisation (1-to-1)","99","$",
            ["On travaille ensemble, en direct","Déblocage de page & config guidée","Places très limitées"],GR_CYAN,False)]
    for i,(f,tag,name,price,cur,feats,gr,popular) in enumerate(plans):
        x=MX+i*(cw+0.36)
        yo = y0-0.14 if popular else y0
        cho = ch+0.18 if popular else ch
        if popular:
            s+=card(x,yo,cw,cho,fill=CARD2,line=GOLD)
            s+=[el("rrect", x=x+cw/2-1.1, y=yo-0.0, w=2.2, h=0.4, radius=0.2, grad=[(0,GOLD,100),(100,GOLD2,100)], angle=0)]
            s+=textbox(x+cw/2-1.1,yo-0.0,2.2,0.4,[{"align":"c","runs":[{"t":"LE PLUS POPULAIRE","font":FONT_BS,"size":9.5,"color":"1A1206","spc":1}]}],valign="middle")
            ytop=yo+0.62
        else:
            s+=card(x,yo,cw,cho)
            ytop=yo+0.46
        s+=chip(x+cw/2-0.36,ytop,0.72,f,grad=gr,pad=0.17)
        s+=textbox(x+0.2,ytop+0.88,cw-0.4,0.4,[{"align":"c","runs":[{"t":tag,"font":FONT_TB,"size":15,"grad":[(0,gr[0],100),(100,gr[1],100)],"gangle":0,"spc":1}]}])
        s+=textbox(x+0.3,ytop+1.26,cw-0.6,0.55,[{"align":"c","line":1.06,"runs":[{"t":name,"font":FONT_B,"size":11,"color":TXT2}]}])
        # prix
        py=ytop+1.86
        s+=textbox(x+0.2,py,cw-0.4,0.55,[{"align":"c","runs":[
            {"t":price+" ","font":FONT_HB,"size":33,"grad":[(0,gr[0],100),(100,gr[1],100)],"gangle":90},
            {"t":cur,"font":FONT_TB,"size":15,"color":TXT2}]}])
        s+=textbox(x+0.2,py+0.56,cw-0.4,0.3,[{"align":"c","runs":[{"t":"PRIX LIVE","font":FONT_BS,"size":9.5,"color":TXT3,"spc":2}]}])
        # separator + features
        s+=[el("line", x=x+0.5, y=py+0.94, w=cw-1.0, h=0.012, fill=BORDER)]
        fy=py+1.12
        for ft in feats:
            s+=textbox(x+0.38,fy,cw-0.72,0.5,[{"line":1.08,"runs":[
                {"t":"✓  ","font":FONT_BS,"size":11.5,"color":gr[0]},
                {"t":ft,"font":FONT_B,"size":11,"color":TXT2}]}])
            fy+=0.42
    s+=footer()
    return s

# =====================================================================
#  SLIDE 19 — Preuve sociale
# =====================================================================
def slide_proof():
    s=bg({"cx":13.0,"cy":-0.2,"r":3.2,"color":GREEN,"alpha":22},
         {"cx":0.0,"cy":7.6,"r":3.4,"color":VIOLET,"alpha":26})
    s+=kicker(MX,0.6,"ILS L'ONT DÉJÀ FAIT",grad=GR_GREEN)
    s+=heading(MX,0.98,"Des chiffres réels de la boutique",size=30)
    s+=subtitle(MX,1.64,"Kevin Chris Digital — résultats vérifiables.",size=13.5,color=TXT3)
    stats=[("400k+","abonnés sur les réseaux",GR_PRIMARY),
           ("364","créateurs ont pris le guide",GR_GOLD),
           ("41","ont choisi le pack complet",GR_CYAN),
           ("100%","d'avis positifs sur le guide",GR_GREEN)]
    cw=(CW-3*0.34)/4; y0=2.45; ch=2.25
    for i,(num,lab,gr) in enumerate(stats):
        x=MX+i*(cw+0.34)
        s+=card(x,y0,cw,ch,fill=CARD2)
        s+=[el("rrect", x=x+0.34, y=y0+0.34, w=0.5, h=0.08, radius=0.04, grad=[(0,gr[0],100),(100,gr[1],100)], angle=0)]
        s+=textbox(x+0.3,y0+0.62,cw-0.6,1.0,[{"runs":[{"t":num,"font":FONT_HB,"size":46,"grad":[(0,gr[0],100),(100,gr[1],100)],"gangle":90}]}],valign="middle")
        s+=textbox(x+0.34,y0+1.62,cw-0.6,0.55,[{"line":1.12,"runs":[{"t":lab,"font":FONT_BM,"size":12,"color":TXT2}]}])
    # quote
    qy=5.15
    s+=[el("rrect", x=MX, y=qy, w=CW, h=1.35, radius=0.16, fill=CARD, line=BORDER, line_w=1)]
    s+=textbox(MX+0.5,qy+0.22,0.8,1.0,[{"runs":[{"t":"“","font":FONT_HB,"size":58,"grad":[(0,GREEN,100),(100,CYAN,100)],"gangle":90}]}])
    s+=textbox(MX+1.3,qy+0.24,CW-1.7,0.95,[
        {"line":1.18,"runs":[{"t":"« Là où il y a une grande volonté, il ne peut pas y avoir de grandes difficultés. »  ","font":FONT_BS,"size":15,"color":TXT},
                              {"t":"— Machiavel","font":FONT_B,"size":13,"color":TXT3}]},
        {"space_before":6,"runs":[{"t":"Depuis l'Afrique, j'encaisse tous les mois. Toi aussi, tu peux.","font":FONT_BM,"size":13,"color":TXT2}]}])
    s+=footer()
    return s

# =====================================================================
#  SLIDE 20 — CTA final
# =====================================================================
def slide_cta():
    s=bg({"cx":12.8,"cy":-0.3,"r":4.0,"color":VIOLET,"alpha":38},
         {"cx":-0.3,"cy":7.7,"r":4.0,"color":BLUE,"alpha":34},
         {"cx":11.5,"cy":6.8,"r":2.2,"color":GOLD,"alpha":16})
    s+=kicker(MX,1.0,"C'EST À TOI DE JOUER")
    s+=[el("text", x=MX, y=1.5, w=11.6, h=1.2, paras=[{"runs":[
        {"t":"Passe à l'action ","font":FONT_HB,"size":48,"color":TXT},
        {"t":"maintenant","font":FONT_HB,"size":48,"grad":[(0,BLUE,100),(100,VIOLET,100)],"gangle":0}]}])]
    s+=subtitle(MX,2.7,"Tu as deux choix : continuer à publier sans résultats… ou appliquer la méthode et transformer Facebook en source de revenus.",w=10.6,size=15.5)
    # 2 cartes contact
    cw=(CW-0.4)/2; cy=3.95; ch=1.5
    contacts=[(ic("20-1"),"La boutique","formation.kevinchrisdigital.com",GR_PRIMARY),
              (ic("20-2"),"Accompagnement perso","wa.me/message/RKOEMXQRVJD7L1",GR_GREEN)]
    for i,(f,ti,link,gr) in enumerate(contacts):
        x=MX+i*(cw+0.4)
        s+=card(x,cy,cw,ch,fill=CARD2)
        s+=chip(x+0.34,cy+(ch-0.74)/2,0.74,f,grad=gr,pad=0.17)
        s+=textbox(x+1.3,cy+0.3,cw-1.5,0.5,[{"runs":[{"t":ti,"font":FONT_TB,"size":16,"color":TXT}]}])
        s+=textbox(x+1.3,cy+0.82,cw-1.5,0.4,[{"runs":[{"t":link,"font":FONT_BM,"size":12.5,"grad":[(0,gr[0],100),(100,gr[1],100)],"gangle":0}]}])
    s+=textbox(MX,cy+ch+0.4,CW,0.6,[{"runs":[{"t":"Merci d'avoir suivi cette masterclass — à toi de jouer.","font":FONT_TB,"size":17,"color":TXT}]}])
    s+=[el("text", x=W_IN-MX-3, y=6.95, w=3, h=0.3, paras=[{"align":"r","runs":[
        {"t":"© Kevin Chris Digital","font":FONT_BS,"size":9.5,"color":TXT3,"spc":1}]}])]
    return s

# =====================================================================
#  COMPOSANTS — carte feature 2x2, bandeau, avatar
def feat_card(x,y,w,h,iconf,title,desc,grad):
    out=card(x,y,w,h,fill=CARD2)
    out+=chip(x+0.3,y+0.3,0.62,iconf,grad=grad,pad=0.14)
    out+=textbox(x+1.06,y+0.32,w-1.3,0.62,[{"line":1.04,"runs":[{"t":title,"font":FONT_TB,"size":14,"color":TXT}]}],valign="middle")
    out+=textbox(x+0.32,y+1.04,w-0.64,h-1.16,[{"line":1.16,"runs":[{"t":desc,"font":FONT_B,"size":11.5,"color":TXT2}]}])
    return out

def info_banner(y,iconf,title,text,grad,h=0.84):
    out=[el("rrect", x=MX, y=y, w=CW, h=h, radius=0.16, fill=CARD2, line=grad[0], line_w=1.2,
            shadow={"blur":18,"dist":8,"alpha":32,"color":grad[0]})]
    out+=chip(MX+0.32, y+(h-0.58)/2, 0.58, iconf, grad=grad, pad=0.13)
    out+=textbox(MX+1.1, y+0.15, CW-1.4, h-0.28,[
        {"runs":[{"t":title,"font":FONT_TB,"size":13,"grad":[(0,grad[0],100),(100,grad[1],100)],"gangle":0}]},
        {"space_before":3,"line":1.12,"runs":[{"t":text,"font":FONT_B,"size":11.8,"color":TXT2}]}])
    return out

def _initials(name):
    parts=[p for p in name.replace("'"," ").replace("’"," ").split() if p]
    letters=[p[0] for p in parts if p[0].isalpha()]
    return ("".join(letters[:2]) or name[:2]).upper()

def avatar(x,y,d,name,grad,slug=None):
    photo=client_photo(slug) if slug else None
    if photo:
        cache=os.path.join(AVA_CACHE, (slug or name)+".png")
        make_circle_avatar(photo, cache)
        ring=0.05
        return [
            el("oval", x=x-ring, y=y-ring, w=d+2*ring, h=d+2*ring,
               grad=[(0,grad[0],100),(100,grad[1],100)], angle=125, shadow=True),
            el("icon", x=x, y=y, w=d, h=d, file=cache),
        ]
    return [
        el("oval", x=x, y=y, w=d, h=d, grad=[(0,grad[0],100),(100,grad[1],100)], angle=125,
           shadow=True),
        el("text", x=x, y=y, w=d, h=d, valign="middle", paras=[{"align":"c","runs":[
            {"t":_initials(name),"font":FONT_HB,"size":d*30,"color":WHITE}]}]),
    ]

# =====================================================================
#  SLIDE — Créer du contenu SANS IA
# =====================================================================
def slide_content_noia():
    s=bg({"cx":-0.2,"cy":0.2,"r":3.0,"color":ROSE,"alpha":24},
         {"cx":13.2,"cy":7.4,"r":3.4,"color":GOLD,"alpha":22})
    s+=kicker(MX,0.55,"PARTIE 2 · CRÉER DU CONTENU",grad=GR_ROSE)
    s+=heading(MX,0.94,"Créer du contenu SANS IA",size=30)
    s+=subtitle(MX,1.6,"L'authenticité brute : ton visage, ta voix, ton vécu. C'est le socle qui crée le lien — et la confiance qui vend.",size=13.5,color=TXT3)
    cards=[(ic("18-3"),"Ton authenticité = ton avantage","Montre ton visage, parle ta langue, partage ton vécu. La proximité crée la confiance qui vend.",GR_ROSE),
           (ic("17-2"),"Filme simplement","Un smartphone, une bonne lumière, un son clair. Le message compte toujours plus que le matériel.",GR_GOLD),
           (ic("7-1"),"Raconte des histoires","Pars d'un problème réel, montre ta galère, finis par la solution. L'histoire capte plus que le conseil.",GR_GREEN),
           (ic("3-3"),"Le terrain, ta mine d'idées","Tes clients, tes échecs, l'actualité locale. Note chaque question qu'on te pose : c'est ton prochain post.",GR_PRIMARY)]
    cw=(CW-0.4)/2; ch=1.7; y0=2.26
    for i,(f,ti,de,gr) in enumerate(cards):
        r,c=divmod(i,2)
        s+=feat_card(MX+c*(cw+0.4), y0+r*(ch+0.16), cw, ch, f,ti,de,gr)
    s+=info_banner(5.84,ic("11-3"),
        "À retenir","Sans authenticité, aucune technique ne tient. C'est ta personnalité qui transforme un spectateur en abonné fidèle.",GR_GOLD)
    s+=footer()
    return s

# =====================================================================
#  SLIDE — Créer du contenu AVEC l'IA
# =====================================================================
def slide_content_ia():
    s=bg({"cx":13.2,"cy":0.2,"r":3.2,"color":BLUE,"alpha":26},
         {"cx":-0.2,"cy":7.4,"r":3.4,"color":VIOLET,"alpha":24})
    s+=kicker(MX,0.55,"PARTIE 2 · CRÉER DU CONTENU",grad=GR_ROSE)
    s+=heading(MX,0.94,"Créer du contenu AVEC l'IA",size=30)
    s+=subtitle(MX,1.6,"L'IA ne te remplace pas — elle multiplie ta vitesse. Tu gardes ton authenticité, tu gagnes 10× en productivité.",size=13.5,color=TXT3)
    cards=[(ic("5-2"),"Des idées & des hooks en rafale","Demande à une IA (ChatGPT, Claude) 20 angles sur ta niche et des accroches qui stoppent le scroll.",GR_PRIMARY),
           (ic("2-2"),"Scripts & légendes","Génère un script structuré (hook → valeur → action), puis réécris-le avec TES mots pour sonner vrai.",GR_CYAN),
           (ic("10-1"),"Visuels & montage assistés","Miniatures, sous-titres, voix off, images : un rendu pro en quelques minutes (Canva, CapCut…).",GR_ROSE),
           (ic("18-2"),"Planifie & recycle","L'IA transforme 1 vidéo en 5 contenus : carrousel, citation, post texte. Publie plus sans t'épuiser.",GR_GREEN)]
    cw=(CW-0.4)/2; ch=1.7; y0=2.26
    for i,(f,ti,de,gr) in enumerate(cards):
        r,c=divmod(i,2)
        s+=feat_card(MX+c*(cw+0.4), y0+r*(ch+0.16), cw, ch, f,ti,de,gr)
    s+=info_banner(5.84,ic("6-4"),
        "Règle d'or","L'IA propose, TU valides. Un contenu 100 % IA sonne faux : garde ta voix — l'IA n'est que ton assistant.",GR_PRIMARY)
    s+=footer()
    return s

# =====================================================================
#  SLIDE — Mur des créateurs qui me font confiance
# =====================================================================
def slide_trustwall():
    s=bg({"cx":-0.2,"cy":-0.2,"r":3.2,"color":VIOLET,"alpha":26},
         {"cx":13.2,"cy":7.6,"r":3.6,"color":BLUE,"alpha":26},
         {"cx":11.0,"cy":0.4,"r":2.0,"color":CYAN,"alpha":16})
    s+=kicker(MX,0.55,"ILS ME FONT CONFIANCE")
    s+=heading(MX,0.94,"Le mur des créateurs accompagnés",size=29)
    s+=subtitle(MX,1.6,"Des créateurs, artistes et marques que j'aide à grandir et à monétiser au quotidien.",size=13.5,color=TXT3)
    creators=[("Laurisse Digital","Créatrice digitale","Monétisation","laurisse-digital"),
              ("Le MB Bandjounais","Humoriste","Gestion de page","le-mb-bandjounais"),
              ("L'étoile Kribienne","Influenceuse","Certification","letoile-kribienne"),
              ("Papy Le Jongleur","Artiste","Facebook Ads","papy-le-jongleur"),
              ("Justine Kem's","Créatrice lifestyle","Création de contenu","justine-kems"),
              ("Dilane Nofole Pro","Entrepreneur","Audit de page","dilane-nofole-pro"),
              ("Kevin Chris Digital","Coach digital","FaceHOOK Studio","kevin-chris-digital"),
              ("Mbanga Diaspora","Média","Sécurité","mbanga-diaspora"),
              ("Alain Tchamo Officiel","Artiste musique","Monétisation","alain-tchamo-officiel"),
              ("Dj Styvo Godson","DJ / Artiste","Facebook Ads","dj-styvo-godson")]
    grads=[GR_PRIMARY,GR_ROSE,GR_GOLD,GR_CYAN,GR_GREEN,GR_CYAN,GR_PRIMARY,GR_ROSE,GR_GOLD,GR_GREEN]
    gap=0.22; cw=(CW-4*gap)/5; ch=1.96; y0=2.45
    for i,(name,role,tag,slug) in enumerate(creators):
        r,c=divmod(i,5)
        x=MX+c*(cw+gap); y=y0+r*(ch+0.2); gr=grads[i]
        s+=card(x,y,cw,ch,fill=CARD)
        d=0.76
        s+=avatar(x+cw/2-d/2, y+0.2, d, name, gr, slug=slug)
        s+=textbox(x+0.12,y+1.04,cw-0.24,0.32,[{"align":"c","line":1.0,"runs":[{"t":name,"font":FONT_BS,"size":11,"color":TXT}]}])
        s+=textbox(x+0.12,y+1.34,cw-0.24,0.24,[{"align":"c","runs":[{"t":role,"font":FONT_B,"size":9,"color":TXT3}]}])
        s+=[el("rrect", x=x+0.22, y=y+1.6, w=cw-0.44, h=0.28, radius=0.14, fill=CARD_HI, line=BORDER_HI, line_w=1)]
        s+=textbox(x+0.16,y+1.6,cw-0.32,0.28,[{"align":"c","runs":[{"t":tag,"font":FONT_BS,"size":8.3,"grad":[(0,gr[0],100),(100,gr[1],100)],"gangle":0,"spc":0.2}]}],valign="middle")
    s+=footer()
    return s

# =====================================================================
ALL_SLIDES = [
    slide_cover, slide_agenda, slide_story,
    lambda: section("1","PARTIE 1","Comprendre Facebook avant de monétiser","Tu ne peux pas gagner à un jeu dont tu ignores les règles.",ic("4-1"),GR_PRIMARY,BLUE),
    slide_algo, slide_ecosystem,
    lambda: section("2","PARTIE 2","Créer du contenu qui performe","Le contenu est roi — mais seulement s'il sert l'algorithme.",ic("7-1"),GR_ROSE,VIOLET),
    slide_niche, slide_content_noia, slide_content_ia,
    lambda: section("3","PARTIE 3","Les programmes de monétisation","Comment Facebook paie réellement les créateurs en 2025.",ic("9-1"),GR_GOLD,GOLD),
    slide_cmp, slide_eligibility,
    lambda: section("4","PARTIE 4","Monétiser depuis un pays inéligible","Inéligible ne veut pas dire impossible. C'est un détour, pas une fin.",ic("12-1"),GR_CYAN,CYAN),
    slide_strategy, slide_paypal,
    lambda: section("5","PARTIE 5","Gérer les restrictions & diversifier","Sécurise ta page, puis bâtis ton propre système de revenus.",ic("15-1"),GR_GREEN,GREEN),
    slide_protect, slide_now, slide_pricing, slide_proof, slide_trustwall, slide_cta,
]

def build_all():
    slides=[fn() for fn in ALL_SLIDES]
    total=len(slides)
    for i,sp in enumerate(slides,1):
        for e in sp:
            if e.get("_pagenum"):
                e["paras"][0]["runs"][0]["t"]=f"{i:02d} / {total}"
    return slides
