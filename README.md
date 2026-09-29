# Nozo Apps — source AltStore

Source [AltStore](https://altstore.io) / [SideStore](https://sidestore.io) de mes apps.

## Ajouter la source
Dans AltStore → **Sources** → **+**, colle :

```
https://raw.githubusercontent.com/Nozomagarion/altstore-source/main/apps.json
```

## Apps
| App | Description | Code |
|---|---|---|
| **Quotas IA** | Widget des quotas Claude / Codex / OpenCode Go | [quotas-ia-widget](https://github.com/Nozomagarion/quotas-ia-widget) |

## Comment ça marche
- Ce dépôt est **public** et ne contient aucun code d'app : uniquement la source, l'icône et les IPA publiés en releases (tag `quotas-ia-vX.Y.Z`).
- `config.json` décrit la source et chaque app (nom de l'IPA, préfixe de tag, métadonnées).
- `scripts/build_source.py` lit les releases de ce dépôt et écrit `apps.json`.
- Le workflow `Update AltStore source` le relance toutes les 6 h (et à la demande : Actions → *Run workflow*).
  Publier une release ici suffit donc : la nouvelle version apparaît dans AltStore.

## Ajouter une app
Ajoute un objet dans `apps` de `config.json` (`repo`, `tagPrefix`, `asset`, `name`, `bundleIdentifier`, …), pousse : `apps.json` est régénéré.

## Limites avec un compte Apple gratuit
7 jours de validité (AltStore rafraîchit), 3 apps actives, et une app avec widget consomme 2 identifiants d'app (10 par semaine).
