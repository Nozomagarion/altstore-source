#!/usr/bin/env python3
"""Génère apps.json (source AltStore) à partir de config.json et des releases GitHub de chaque app."""
import json, os, sys, urllib.request

def gh(path):
    req = urllib.request.Request(f"https://api.github.com/{path}", headers={"Accept": "application/vnd.github+json"})
    if token := os.environ.get("GITHUB_TOKEN"):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def versions_for(app):
    out = []
    for rel in gh(f"repos/{app['repo']}/releases?per_page=20"):
        if rel.get("draft") or rel.get("prerelease"):
            continue
        asset = next((a for a in rel.get("assets", []) if a["name"] == app["asset"]), None)
        if not asset:
            continue
        v = rel["tag_name"].lstrip("v")
        out.append({
            "version": v,
            "buildVersion": v,
            "date": rel["published_at"],
            "localizedDescription": (rel.get("body") or "").strip() or f"Version {v}",
            "downloadURL": asset["browser_download_url"],
            "size": asset["size"],
            "minOSVersion": app.get("minOSVersion", "17.0"),
        })
    return out  # les plus récentes d'abord

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cfg = json.load(open(os.path.join(root, "config.json")))
    apps = []
    for app in cfg["apps"]:
        try:
            versions = versions_for(app)
        except Exception as e:  # dépôt introuvable / pas encore de release
            print(f"skip {app['repo']}: {e}", file=sys.stderr)
            continue
        if not versions:
            print(f"skip {app['repo']}: aucune release avec {app['asset']}", file=sys.stderr)
            continue
        latest = versions[0]
        entry = {k: v for k, v in app.items() if k not in ("repo", "asset", "minOSVersion")}
        entry.update({
            "versions": versions,
            # champs « legacy » lus par les anciennes versions d'AltStore
            "version": latest["version"],
            "versionDate": latest["date"],
            "versionDescription": latest["localizedDescription"],
            "downloadURL": latest["downloadURL"],
            "size": latest["size"],
            "screenshots": app.get("screenshots", []),
        })
        apps.append(entry)
    source = {k: cfg[k] for k in ("name", "identifier", "subtitle", "description", "iconURL", "website", "tintColor") if k in cfg}
    source.update({"apps": apps, "news": []})
    with open(os.path.join(root, "apps.json"), "w") as f:
        json.dump(source, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"apps.json : {len(apps)} app(s)")

if __name__ == "__main__":
    main()
