# Masterclass — Création de contenu & monétisation Facebook

Refonte complète du design de la présentation de masterclass de **Kevin Chris Digital**.

## Livrable

**`Masterclass_Facebook_KevinChris_REDESIGN.pptx`** — 20 slides, format 16:9, **polices intégrées** (le fichier reste identique sur n'importe quel ordinateur, même sans les polices installées). Les notes du présentateur de la version originale ont été conservées.

## Direction artistique — « Aurora Dark Premium »

Le deck original était classique (fond blanc, polices Calibri/Cambria, cartes plates). La nouvelle version adopte un style sombre premium, moderne et impactant :

- **Fond** : dégradé bleu-nuit profond + halos lumineux (glow) dégradés dans les angles pour la profondeur.
- **Typographie** : **Montserrat** (ExtraBold / Black) pour les titres, **Inter** pour le corps de texte.
- **Couleurs d'accent** : dégradés bleu → violet (marque), or (monétisation & prix), cyan / rose / vert pour le codage des sections.
- **Composants** : cartes « verre dépoli » avec bordures subtiles et ombres portées, pastilles d'icônes en dégradé, chiffres géants en dégradé, badges numérotés.
- **Codage couleur par partie** : chaque section (Parties 1 à 5) a sa teinte dominante pour le rythme visuel.

## Sources & reproductibilité

Le dossier `source/` contient tout le nécessaire pour régénérer le fichier :

| Fichier | Rôle |
|---|---|
| `deck.py` | Moteur de rendu (génère le PPTX **et** des aperçus PNG à partir d'un même « spec » de slide) |
| `content.py` | Définition des 20 slides et des composants réutilisables |
| `build_final.py` | Assemblage final : génération, report des notes, intégration des polices |
| `fonts/` | Polices Montserrat & Inter (graisses statiques, licence OFL) |
| `icons/` | Jeu d'icônes (réutilisées de l'original, blanches sur fond transparent) |

> Note : les chemins d'accès dans les scripts pointent vers l'environnement de build d'origine (polices dans `/usr/share/fonts/truetype/custom`, icônes dans `extract/ppt/media`). Adaptez `FONTDIR` (deck.py) et `MED` (content.py) si vous régénérez ailleurs.
