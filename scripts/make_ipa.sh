#!/usr/bin/env bash
# Construit un IPA non signé (AltStore / SideStore le re-signent avec ton Apple ID) depuis un projet XcodeGen.
# Usage : scripts/make_ipa.sh <dossier-projet> <scheme> <NomApp.app> <version> <sortie.ipa>
set -euo pipefail
DIR="$1"; SCHEME="$2"; APPNAME="$3"; VERSION="$4"; OUT="$(cd "$(dirname "$5")" && pwd)/$(basename "$5")"
cd "$DIR"
WORK="$(mktemp -d)"
xcodegen generate >/dev/null
xcodebuild archive -project "$(ls -d *.xcodeproj | head -1)" -scheme "$SCHEME" -configuration Release \
  -destination 'generic/platform=iOS' -archivePath "$WORK/App.xcarchive" \
  CODE_SIGNING_ALLOWED=NO CODE_SIGNING_REQUIRED=NO DEVELOPMENT_TEAM="" \
  MARKETING_VERSION="$VERSION" CURRENT_PROJECT_VERSION="$VERSION" | tail -3
mkdir -p "$WORK/Payload"
cp -R "$WORK/App.xcarchive/Products/Applications/$APPNAME" "$WORK/Payload/"
(cd "$WORK" && zip -qry "$OUT" Payload)
rm -rf "$WORK"
echo "OK  $OUT ($(du -h "$OUT" | cut -f1)) version $VERSION"
