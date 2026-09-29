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
- `config.json` décrit la source et chaque app (dépôt GitHub, nom de l'IPA attaché aux releases, métadonnées).
- `scripts/build_source.py` lit les releases GitHub de chaque app et écrit `apps.json`.
- Le workflow `Update AltStore source` le relance toutes les 6 h (et à la demande : Actions → *Run workflow*).
  Publier une release dans le dépôt d'une app suffit donc : la nouvelle version apparaît dans AltStore.

## Ajouter une app
Ajoute un objet dans `apps` de `config.json` (`repo`, `asset`, `name`, `bundleIdentifier`, …), pousse : `apps.json` est régénéré.

## Limites avec un compte Apple gratuit
7 jours de validité (AltStore rafraîchit), 3 apps actives, et une app avec widget consomme 2 identifiants d'app (10 par semaine).
