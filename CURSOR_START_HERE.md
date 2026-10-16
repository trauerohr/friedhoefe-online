# Cursor Start Here - friedhöfe.online Stuttgart

Dies ist die Uebergabe fuer Cursor.

## Ziel

Der aktuelle Leitfaden ist der friedhöfe.online Stuttgart. Er soll sauber weitergefuehrt werden und spaeter als Vorlage fuer weitere regionale TrauerOhr-friedhöfe.onlines dienen.

## Wichtigste Dateien

- `index.html` ist die Startseite mit Einleitung und Karte zum Regierungsbezirk Stuttgart.
- `regionen/index.html` ist die Regionen-Uebersicht.
- `stuttgart/index.html` ist der bestehende friedhöfe.online Stuttgart.
- `ratgeber/index.html` ist der eigene Ratgeber, nicht als Reiter in den Regionen.

## Wichtige Unterlagen

- `AGENTS.md` - verbindliche KI-Arbeitsregel; je neuer Agent einmal lesen, nicht pro Prompt wiederholen
- `.cursor/rules/trauerohr-kompass.mdc` - feste Projektregeln
- `CLOUDFLARE_GITHUB_DEPLOYMENT.md` - einfache GitHub-/Cloudflare-Schritte

## Verbindliche KI-Arbeitsregel

`AGENTS.md` ist die verbindliche Regel für alle KI-Modelle. Ein neuer Agent liest sie und diese Übergabe einmal zu Beginn, übernimmt den bestätigten Stand und liest sie nicht bei jedem Folgeprompt erneut. Für jede Aufgabe: Ziel, Ist-Stand, Nicht-Ziel und prüfbares Fertig-Kriterium festhalten; höchstens fünf Schritte. Für eine klar abgegrenzte Änderung gelten höchstens 30 Minuten aktive Zielzeit. Bei 15 Minuten ohne Fortschritt oder bei drohender Budgetüberschreitung anhalten und berichten. Höchstens zwei Lösungsversuche insgesamt; danach mit dem konkreten Blocker stoppen. Abschluss nach dem Format in `AGENTS.md`.

## Aktueller Stand

- Die Startseite heisst **friedhöfe.online** und steht extra im Menue als **Start**.
- Das Menue lautet **Start**, **Regionen BW**, **Ratgeber**. In einer Region kommen **Bestatter** und **Friedhöfe** dazu.
- Der Menuepunkt heisst **Regionen BW**, damit spaeter weitere Regionen in Baden-Wuerttemberg dazukommen koennen.
- Die Startseite zeigt den friedhöfe.online-Text und eine vereinfachte eigene Karte des Regierungsbezirks Stuttgart. Fremde Kartenbilder werden nicht verwendet.
- Stuttgart liegt in der Rubrik Regionen und ist unter `/stuttgart/` erreichbar. Der volle Friedhof TO GO bleibt dort.
- Weitere Regionen im Regierungsbezirk Stuttgart haben vorbereitete Seiten mit Häfner & Züfle, Beispielkarte und Friedhöfen. In den Regionen gibt es nur die Reiter Bestatter und Friedhöfe.
- Der Ratgeber steht extra im Menue und unter `/ratgeber/`.
- Bestatter stehen nicht auf der Startseite, sondern in der jeweiligen Region.
- Standard-Ueberschrift ist **friedhöfe.online**, darunter klein **von TrauerOhr**. Die Region steht im Menue, nicht im Produktnamen.
- Bestatter: nur Häfner & Züfle plus eine Beispielkarte Mustermann Bestattungen (Werbung moeglich).
- Kein Kostenrechner, keine Preise, keine Gebuehrentabelle.
- Friedhof TO GO: Klick oeffnet Grabfelder; Karte bleibt erreichbar.
- 19 zugeschnittene Lageplaene aus der TrauerOhr-PDF liegen in `assets/friedhoefe/lageplaene-clean/` und sind den jeweiligen Friedhoefen zugeordnet.
- Juedische Sonderbereiche bleiben ohne eigenes Bild.
- Wikimedia-Grabfeldfotos bleiben zusaetzlich bei Hauptfriedhof und Waldfriedhof.
- Vorsorge-Hinweis bleibt unten, klein und ruhig, mit dezentem blauen Rahmen `#1C00CC`. Er steht auf der Startseite, Regionen, Ratgeber und allen Regionsseiten. Button: Zur Vorsorge-App, Link `https://digitale-bestattungsvorsorge.de`.
- Oeffentliche Adresse: `friedhöfe.online`
- Fusszeile: Domain `friedhöfe.online` und `© 2026 friedhöfe.online. Ein Projekt von TrauerOhr.`
- Keine Kosten-, Preis- oder Satzungssaetze auf der oeffentlichen Seite.
- Wenn eine Funktion entfaellt, immer auch Footer, Tabellen, Hinweise und verwandte Saetze mitpruefen.

## Arbeitsweise

1. Bestehendes Erscheinungsbild erhalten.
2. Nur kleine, nachvollziehbare Aenderungen machen.
3. Fuer neue Staedte die Struktur uebernehmen, aber Daten neu recherchieren.
