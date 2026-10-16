# Cursor-Masterprompt fuer TrauerOhr Kompasse

Du arbeitest am TrauerOhr friedhöfe.online (oeffentlich friedhöfe.online).

## Grundhaltung

Arbeite ruhig, sauber und langfristig wartbar. Stephanie ist keine professionelle Programmiererin. Erklaere Aenderungen verstaendlich und vermeide unnoetige technische Komplexitaet.

## Design

- Gruen: `#79A83B`
- Blau: `#1C00CC`
- Text: `#3F3F3F`
- Stil: ruhig, professionell, vertrauensvoll, modern
- Keine kitschigen oder ueberladenen Designs
- Bestehendes Erscheinungsbild erhalten

## Technik

- Statische Loesung bevorzugen
- Keine Plattform, kein Backend, keine laufenden Kosten einfuehren, solange es nicht notwendig ist
- Keine Build-Abhaengigkeiten hinzufuegen, solange `index.html` direkt funktioniert
- Kleine nachvollziehbare Schritte statt grosser Umbauten

## Datenschutz

- Keine sensiblen Daten unnoetig sammeln
- Keine Trackingdienste einbauen
- Keine personenbezogenen Daten von Besuchern speichern
- Bei spaeteren Formularen: Loeschbarkeit, Export und Backup von Anfang an bedenken

## Friedhofsbilder

Nutze die Regeln aus `.cursor/rules/bildrechte-friedhoefe.mdc`.

Wichtig:

- Keine Fremdbilder ohne klare Lizenz/Freigabe einbauen
- Quelle/Freigabe als lesbare Bildunterschrift oder Quellenliste dokumentieren
- Bilddatei selbst sauber halten: keine PDF-Raender, keine Seitenzahlen, keine abgeschnittenen Quellen
- Lageplan, Grabfeldfoto, Eingangsfoto und Symbolbild klar unterscheiden
- Fehlende Bilder offen markieren, nicht ersetzen durch ungeprueftes Material

## Stuttgart aktueller Stand

- `index.html` ist die Hauptdatei
- 51 Friedhofs-/Sondereintraege
- 19 bereinigte Lageplaene in `assets/friedhoefe/lageplaene-clean/`
- Bildvergroesserung ist eingebaut
- Bildrecherche steht in `friedhof-bildrecherche-stuttgart.md`

## Neue Stadt-Kompasse

Wenn aus Stuttgart ein neuer Kompass entsteht:

1. Stadtname, Subdomain und sichtbare Texte anpassen.
2. Bestatterdaten neu recherchieren.
3. Friedhoefe neu recherchieren.
4. Gebuehren nur mit Quellenstand uebernehmen.
5. Bilder nur mit sauberer Quelle/Freigabe verwenden.
6. Struktur und ruhiges TrauerOhr-Design beibehalten.
7. README und Bildrecherche-Datei fuer die neue Stadt aktualisieren.

## Nicht tun

- Keine erfundenen Kontaktdaten
- Keine unsicheren Gebuehren als Fakt darstellen
- Keine Bildrechte ignorieren
- Keine dominante Werbung oben einfuegen
- Keine Loeschungen ohne Rueckfrage
