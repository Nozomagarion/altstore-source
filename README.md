# Nozo Apps — source AltStore

Source [AltStore](https://altstore.io) / [SideStore](https://sidestore.io) de mes apps.

## Installer (AltStore Classic)
À faire une seule fois, avec un ordinateur (Mac ou Windows) et un compte Apple gratuit :

1. Installe **AltServer** depuis [altstore.io](https://altstore.io) sur ton ordinateur, puis **AltStore Classic** sur ton iPhone via AltServer (iPhone branché en USB la première fois).
   > Utilise **AltStore Classic**, pas *AltStore PAL* (la version de l'App Store européen) : PAL n'accepte que des apps notarisées par Apple.
2. Sur l'iPhone : Réglages → Général → VPN et gestion de l'appareil → fais confiance à ton profil, et active le **Mode développeur** (Réglages → Confidentialité et sécurité).
3. Dans AltStore → **Sources** → **+**, colle le lien ci-dessous.
4. Ouvre la source, appuie sur **Free** à côté de l'app.
5. Ajoute ensuite le widget depuis l'écran d'accueil (appui long → +).

**Renouvellement** : l'app expire au bout de 7 jours. AltStore la renouvelle tout seul tant que l'ordinateur avec AltServer est allumé et sur le même Wi-Fi que l'iPhone.

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
