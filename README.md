# friedhöfe.online Stuttgart

Statische Startversion fuer den TrauerOhr friedhöfe.online Stuttgart.

## Dateien

- `index.html` ist die Startseite mit Einleitung und Karte.
- `regionen/index.html` ist die Regionen-Uebersicht.
- `stuttgart/index.html` ist der bestehende friedhöfe.online Stuttgart.
- `ratgeber/index.html` ist der Ratgeber als eigener Menuepunkt.
- `.cursor/rules/trauerohr-kompass.mdc` enthaelt die Grundregeln fuer Cursor.
- `CURSOR_START_HERE.md` ist die Startdatei fuer die Weiterarbeit in Cursor.
- `CLOUDFLARE_GITHUB_DEPLOYMENT.md` beschreibt den einfachen GitHub-/Cloudflare-Weg.

## Ziel

Der Stuttgart-Kompass bleibt die Vorlage fuer weitere regionale Kompasse. Das Erscheinungsbild soll ruhig, professionell und nah an TrauerOhr bleiben. Im Mittelpunkt stehen Orientierung, Friedhof TO GO und der Ratgeber.

## Aktueller Stand

- Regionen enthalten Bestatter und Friedhoefe. Der Ratgeber liegt extra im Menue unter `/ratgeber/`.
- Der Kostenrechner ist entfernt.
- Sichtbar sind Häfner & Züfle sowie eine Beispielkarte fuer weitere Bestatter-Werbung.
- Die Werbung fuer die Digitale Bestattungsvorsorge steht unten unter den Bestatter-Karten als kleiner Hinweis, nicht als Hauptbanner.
- Der Friedhofsbereich ist Friedhof TO GO: Name, Stadtteil, Adresse, Grabfelder, Lageplan wo vorhanden, Kartenlink.

## GitHub / Cloudflare Pages

Einfachste stabile Variante:

- Framework preset: `None`
- Build command: leer lassen
- Output directory: `/`
- Pages-Projekt: bestehendes Git-Projekt (ein Projekt, nicht zwei)
- Oeffentliche Adresse: `friedhöfe.online`

## Wichtige Pflege-Regeln

- Keine sensiblen Personendaten speichern.
- Bestatterdaten regelmaessig pruefen.
- Preise und Gebuehren immer mit Quellenstand und Datum dokumentieren.
- Fuer neue Staedte zuerst Inhalte austauschen, dann Design nur minimal anpassen.
- Keine komplexe Plattform einfuehren, solange eine statische Seite ausreicht.
