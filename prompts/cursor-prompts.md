# Cursor-Prompts fuer TrauerOhr Kompasse

## 1. Kleine Aenderung sicher umsetzen

Bitte aendere nur die konkret genannte Stelle im TrauerOhr friedhöfe.online (friedhöfe.online). Das bestehende Erscheinungsbild soll erhalten bleiben. Arbeite ruhig, professionell und ohne unnoetige technische Komplexitaet. Erklaere mir vorher kurz, was du aenderst, warum du es aenderst und welche Auswirkung es hat.

## 2. Neuen Stadt-Kompass aus Stuttgart ableiten

Erstelle aus dem bestehenden friedhöfe.online Stuttgart eine neue Version fuer `[STADT]`.

Bitte passe an:

- Seitentitel
- sichtbare Stadtbezeichnung
- Subdomain-Hinweise
- Bestatterdaten
- Friedhoefe
- lokale Gebuehren und Kostenhinweise
- Ratgebertexte, sofern Stuttgart-spezifisch

Bitte nicht grundlos aendern:

- Grundlayout
- Markenfarben
- Navigationsstruktur
- ruhiger TrauerOhr-Stil
- Datenschutz-Grundsaetze

Wichtig: Wenn Daten unsicher sind, markiere sie als zu pruefen und erfinde keine Kontaktdaten.

## 3. Werbung weniger dominant machen

Die Werbung fuer die Digitale Bestattungsvorsorge soll ergaenzend wirken und nicht die Hauptfunktion des Kompasses ueberlagern. Bitte setze sie weiter nach unten oder reduziere ihre Dominanz, ohne das bestehende Design unruhig zu machen.

## 4. GitHub vorbereiten

Bitte pruefe, ob dieses Projekt als einfache statische Seite sauber fuer GitHub vorbereitet ist. Es soll moeglichst wenig Technik enthalten. Keine Build-Abhaengigkeiten hinzufuegen, solange `index.html` direkt funktioniert. Lege bei Bedarf nur kleine Hilfsdateien wie `README.md` oder `.gitignore` an.

## 5. Cloudflare Pages vorbereiten

Bitte bereite das Projekt fuer Cloudflare Pages vor. Ziel ist eine statische Seite ohne Build-Schritt.

Gewuenschte Einstellung:

- Framework preset: `None`
- Build command: leer
- Output directory: `/`

Bitte keine kostenpflichtigen oder komplexen Cloudflare-Funktionen einfuehren, solange sie nicht notwendig sind.

## 6. Datenschutz-Check

Bitte pruefe diese Seite auf Datenschutzrisiken. Achte besonders darauf, ob externe Dienste, Tracking, Formulare, Cookies oder personenbezogene Daten verwendet werden. Schlage nur einfache und notwendige Verbesserungen vor.

## 7. Friedhofsbilder pruefen und einbauen

Bitte pruefe die Friedhofsbilder fuer den Stuttgart-Kompass. Unterscheide klar zwischen Lageplan, Grabfeldfoto, Eingangsfoto und Symbolbild. Verwende keine Fremdbilder oeffentlich, wenn Quelle, Lizenz oder Freigabe unklar sind. Wenn ein Bild fehlt, markiere den Friedhof als `Bild fehlt / Foto oder Freigabe recherchieren` und ergaenze eine moegliche Recherchequelle in `friedhof-bildquellen-und-todos.md`.

Aktiv eingebundene Lageplaene liegen in `assets/friedhoefe/lageplaene-clean/`. Bitte verwende diesen Ordner fuer die Webseite. Die Quelle soll als lesbare Bildunterschrift im HTML stehen, nicht als abgeschnittener Text im Bild. Bei vorhandenen Lageplaenen soll die Klick-Vergroesserung erhalten bleiben.

## 8. Inhaltspruefung

Bitte pruefe alle Texte auf einen ruhigen, professionellen und vertrauensvollen TrauerOhr-Ton. Entferne werbliche Uebertreibungen, kitschige Formulierungen und alles, was fuer Angehoerige in einer belastenden Situation zu laut wirken koennte.
