# GitHub und Cloudflare Pages

## Aktueller technischer Stand

Das Projekt ist eine einfache statische Webseite. Es braucht keinen Build-Schritt.

## GitHub

Empfohlene Struktur im Repository:

```text
/
  index.html
  README.md
  CURSOR_START_HERE.md
  CLOUDFLARE_GITHUB_DEPLOYMENT.md
  friedhof-bildquellen-und-todos.md
  friedhof-bildrecherche-stuttgart.md
  assets/
  prompts/
  .cursor/
```

## Cloudflare Pages

Einstellungen:

- Pages-Projektname: bestehendes Git-Projekt, oeffentliche Domain `friedhöfe.online`
- Framework preset: `None`
- Build command: leer lassen
- Output directory: `/`

GitHub ist direkt mit Cloudflare Pages verbunden. Die Seite wird bei Push auf `main` ohne Build-Schritt veroeffentlicht.

## Subdomain

Oeffentliche Adresse:

`friedhöfe.online`

Aeltere Testadressen werden nicht weiter genutzt. Es bleibt ein Cloudflare-Pages-Projekt; oeffentlich ist nur `friedhöfe.online`.

Wenn Cloudflare Pages verbunden ist:

1. GitHub-Repository verbinden.
2. Projekt deployen.
3. Custom Domain in Cloudflare Pages hinzufuegen.
4. DNS/Validierung nach Cloudflare-Anweisung setzen.

## Wichtige Veroeffentlichungsregel

Vor dem Livegang pruefen:

- Funktioniert `index.html` als statische Seite?
- Ist die Vorsorge-Werbung unten und nicht dominant?
- Stimmen Impressum-/Hauptseitenlinks?
