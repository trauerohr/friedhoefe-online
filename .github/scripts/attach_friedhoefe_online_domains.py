#!/usr/bin/env python3
import json
import os
import urllib.error
import urllib.request

ACCOUNT_ID = os.environ["CLOUDFLARE_ACCOUNT_ID"]
TOKEN = os.environ["CLOUDFLARE_API_TOKEN"]
PROJECT = "trauerguide"
API = "https://api.cloudflare.com/client/v4"

# IDN friedhöfe.online
ROOT = "xn--friedhfe-s4a.online"
WWW = "www.xn--friedhfe-s4a.online"


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

for domain in (ROOT, WWW):
    print(f"== Add domain {domain} ==")
    resp = request(
        "POST",
        f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains",
        {"name": domain},
    )
    print(json.dumps(resp, indent=2)[:4000])

print("== Current domains on project ==")
domains = request("GET", f"/accounts/{ACCOUNT_ID}/pages/projects/{PROJECT}/domains")
print(json.dumps(domains, indent=2)[:8000])

print("== Ensure zone for IDN root ==")
zones = request("GET", f"/zones?name={ROOT}")
print(json.dumps(zones, indent=2)[:3000])
if not (zones.get("result") or []):
    created = request(
        "POST",
        "/zones",
        {"name": ROOT, "account": {"id": ACCOUNT_ID}, "jump_start": True},
    )
    print("== Create zone ==")
    print(json.dumps(created, indent=2)[:4000])
    zone = (created.get("result") or {})
else:
    zone = zones["result"][0]
    print("Zone exists:", zone.get("id"), zone.get("status"), zone.get("name_servers"))

zone_id = zone.get("id")
if zone_id:
    detail = request("GET", f"/zones/{zone_id}")
    print("== Zone detail ==")
    print(json.dumps(detail, indent=2)[:4000])
    ns = (detail.get("result") or {}).get("name_servers") or zone.get("name_servers")
    print("REQUIRED_NAMESERVERS:", ns)

    # Apex CNAME to Pages (CNAME flattening) + www CNAME
    for name, content in ((ROOT, "trauerguide.pages.dev"), (WWW, "trauerguide.pages.dev")):
        existing = request(
            "GET",
            f"/zones/{zone_id}/dns_records?type=CNAME&name={name}",
        )
        print(f"== Existing CNAME {name} ==")
        print(json.dumps(existing, indent=2)[:2000])
        if not (existing.get("result") or []):
            added = request(
                "POST",
                f"/zones/{zone_id}/dns_records",
                {
                    "type": "CNAME",
                    "name": name,
                    "content": content,
                    "proxied": True,
                    "ttl": 1,
                },
            )
            print(f"== Add CNAME {name} ==")
            print(json.dumps(added, indent=2)[:2000])

print("== Zones ==")
zones_all = request("GET", "/zones?per_page=50")
print("success", zones_all.get("success"))
for z in zones_all.get("result") or []:
    print("-", z.get("name"), z.get("status"), z.get("id"), z.get("name_servers"))
