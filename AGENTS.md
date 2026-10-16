# TrauerOhr KI-Arbeitsregel
Version 1.1 · 16. Oktober 2026 · Verbindlich für alle KI-Modelle und Entwicklungsagenten

Gilt für Codex, Cursor, Windsurf und jedes künftig verwendete Modell. Ziel: Änderungen mit klarem Umfang, überprüfbarem Fortschritt und begrenztem Zeit- und Kreditaufwand abschließen.

## 1. Einmaliger Start und Agentenwechsel

- Ein Modell liest diese Regel zu Beginn der Zusammenarbeit einmal vollständig. Im selben Arbeitskontext bleibt sie verbindlich; nicht bei jedem Prompt erneut lesen, anfordern, wiederholen oder vollständig zitieren.
- Automatisch geladene Regeln gelten als einmal übermittelt. Bei einem Agenten- oder Modellwechsel erhält nur das neue Modell die Regel einmal sowie eine knappe Übergabe: Auftrag, bestätigter Ist-Stand, erledigt, offen, Abnahmekriterium.
- Bereits geprüfte Informationen und erledigte Schritte werden übernommen, nicht erneut ausgeführt. Noch einmal lesen ist nur nötig, wenn die Regel geändert wurde oder der Arbeitskontext verloren ging.
- Außerhalb eines entsprechend eingerichteten Repositories kann ein Modell die Regel nicht selbst an andere Konten übertragen. Beim Wechsel wird die Datei einmal angehängt oder ihr Link einmal mit der Übergabe gesendet.

## 2. Auftrag vor dem Start festlegen

Einmal kurz festhalten:
1. Gewünschte konkrete Änderung.
2. Bestätigter aktueller Stand.
3. Was ausdrücklich nicht zum Auftrag gehört.
4. Objektiv prüfbares Fertig-Kriterium.
5. Blocker, Berechtigung oder Freigabe, die tatsächlich erforderlich ist.

Daraus eine Checkliste mit höchstens fünf Schritten erstellen und den kürzesten sicheren Weg wählen. Projektregeln und relevante Dateien gezielt einmal lesen. Keine bereits beantworteten Fragen stellen. Nur wenn ein fehlendes Detail die Arbeit blockiert: höchstens eine kurze Rückfrage mit Antwortoptionen. Keine ungefragten Zusatzideen, Umbauten oder Werkzeuge.

## 3. Zeit- und Kreditrahmen

- Für eine einzelne, klar abgegrenzte Änderung gilt standardmäßig ein Zielbudget von höchstens 30 Minuten aktiver Arbeit. Das ist ein interner Stoppwert, keine Fertigstellungsgarantie.
- Für mehrstufige Aufgaben vor Beginn ein realistisches aktives Zeitbudget und wenige prüfbare Meilensteine nennen. Externe Wartezeit, etwa DNS-Propagation, separat führen.
- Ohne nachweisbaren Fortschritt spätestens nach 15 Minuten anhalten und knapp Ursache, erledigt, offen und nächsten sinnvollen Schritt melden.
- Wird das vereinbarte Zeitbudget überschritten, spätestens bei zusätzlich 15 Minuten oder 25 Prozent Überschreitung – je nachdem, was zuerst eintritt – anhalten. Keine stillschweigende Verlängerung und keine weitere Schleife. Nur mit ausdrücklicher Freigabe zusätzliche aktive Zeit einsetzen.
- Aktive Arbeit, externe Wartezeit und durch KI- oder Tool-Fehler verursachte Wiederholungen getrennt dokumentieren. Zeiten nicht schätzen oder erfinden. Diese Regel gibt keine Empfehlung zur Kundenabrechnung.

## 4. Ausführung und Fehlerbehandlung

- Den besten passenden Ansatz wählen, nur die beauftragte Änderung umsetzen und bereits erledigte Schritte nicht wiederholen.
- Höchstens zwei Lösungsversuche insgesamt: ein erster Ansatz und, nach Prüfung der konkreten Ursache, eine gezielte Korrektur.
- Scheitert der zweite Versuch oder ist ein echter Blocker erreicht, sofort stoppen. Keine weiteren Varianten, Umwege, Agentenwechsel oder Vermutungen starten. Den Fehler, bereits geprüfte Punkte und genau fehlende Voraussetzung melden.
- Vor Änderungen an Live-Systemen, DNS, E-Mail oder Konten den aktuellen Zustand und mögliche Folgen gezielt prüfen und festhalten. Keine destruktive Änderung ohne erforderliche Freigabe.

## 5. Fortschritt und Abnahme

- Bei längerer Arbeit spätestens nach 15 Minuten aktiver Arbeit, an jedem wesentlichen Meilenstein und sofort bei einem Blocker kurz berichten: erledigt, offen, nächster Schritt.
- Jeden Punkt des Fertig-Kriteriums gezielt prüfen. Nur aussagekräftige, notwendige Tests ausführen.
- Einen begonnenen Schritt, Entwurf, Build oder eine Vorschau nicht als fertig melden. Nicht geprüfte oder blockierte Punkte klar als offen kennzeichnen.
- Vor Commit, Push, Veröffentlichung oder Live-Änderung die Projektfreigaben beachten. Keine Aktion als erfolgt bezeichnen, wenn sie nicht nachweislich ausgeführt wurde.

## 6. Übergabe und Abschluss

Bei Agentenwechseln einmal diese kompakte Übergabe verwenden:

> **Auftrag:** [konkretes Ziel]  
> **Erledigt/geprüft:** [bestätigter Stand]  
> **Offen/Blocker:** [konkrete Punkte]  
> **Fertig, wenn:** [prüfbares Abnahmekriterium]  
> **Zeit:** [aktive Arbeit / externe Wartezeit, falls erfasst]

Abschluss kurz und immer in diesem Format:

- ✅ **Erledigt:** Ergebnis
- 🔍 **Geprüft:** tatsächlich ausgeführte Prüfungen
- ⚠️ **Offen:** verbleibende Punkte oder „nichts“
- ▶️ **Nächster Schritt:** nur falls erforderlich

Beim ersten Kontakt einmalig mitgeben: „Lies die beigefügte TrauerOhr KI-Arbeitsregel jetzt vollständig und halte sie für diese Zusammenarbeit verbindlich ein. Lies oder wiederhole sie bei weiteren Prompts nicht erneut. Bei einer Agentenübergabe erhält das neue Modell sie einmal zusammen mit dem aktuellen Stand.“
