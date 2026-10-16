#!/usr/bin/env python3
import json
import os
import urllib.error
import urllib.request

ACCOUNT_ID = os.environ["CLOUDFLARE_ACCOUNT_ID"]
TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
PROJECT = "trauerguide"
API = "https://api.cloudflare.com/client/v4"


def request(method, path, body=None):
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            return json.loads(raw)
        except Exception:
            return {"success": False, "errors": [{"message": raw, "code": e.code}]}


print(f"Account ID length: {len(ACCOUNT_ID)}")
print(f"Token length: {len(TOKEN)}")

print("== List Pages projects ==")
projects = request("GET", f"/accounts/{ACCOUNT_ID}/pages/projects?per_page=25")
print("success", projects.get("success"))
print("errors", projects.get("errors"))
for p in projects.get("result") or []:
    cfg = ((p.get("source") or {}).get("config") or {})
    print(
        "-",
        p.get("name"),
        "domains=",
        p.get("domains"),
        "branch=",
        p.get("production_branch"),
        "repo=",
        f"{cfg.get('owner')}/{cfg.get('repo_name')}",
    )

# Unicode + Punycode (Cloudflare akzeptiert beides; IDN: xn--friedhfe-s4a.online)
for domain in (
    "xn--friedhfe-s4a.online",
    "www.xn--friedhfe-s4a.online",
    "friedhöfe.online",
    "www.friedhöfe.online",
):
    print(f"== Add domain {domain} ==")
    resp = request(
        "POST",
        f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains",
        {"name": domain},
    )
    print(json.dumps(resp, indent=2)[:4000])

print("== Current domains on project ==")
domains = request("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains")
print(json.dumps(domains, indent=2)[:6000])

print("== Zones ==")
zones = request("GET", "/zones?per_page=50")
print("success", zones.get("success"))
for z in zones.get("result") or []:
    print("-", z.get("name"), z.get("status"), z.get("id"))
