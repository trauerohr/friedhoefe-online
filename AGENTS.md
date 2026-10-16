# TrauerOhr KI-Arbeitsregel
Version 1.0 · 16. Oktober 2026 · Verbindlich für alle KI-Modelle und Entwicklungsagenten

Diese Arbeitsregel gilt für Codex, Cursor, Windsurf und jedes künftig verwendete KI-Modell. Sie dient dazu, Aufgaben zielgerichtet, zeitsparend und ohne unnötige Kosten oder Schleifen abzuschließen.

## 1. Einmalige Übergabe pro Modell

- Zu Beginn einer neuen Zusammenarbeit erhält das KI-Modell diese vollständige Regel genau einmal.
- In derselben Unterhaltung und beim selben Modell bleibt sie verbindlich. Nicht bei jedem neuen Prompt erneut lesen, zitieren, anfordern oder als neuen Auftrag ausgeben.
- Wechselt der Agent oder das Modell, wird diese Regel dem neuen Agenten einmalig zusammen mit einer knappen Übergabe übermittelt: Ziel, bestätigter Ist-Stand, bereits erledigte Schritte, offene Punkte und Abnahmekriterium.
- Automatisch geladene Projektregeln gelten als bereits übermittelt. Sie werden nicht zusätzlich nochmals vollständig eingefügt.
- Erneut lesen oder übermitteln ist nur nötig, wenn die Datei geändert wurde, ein neuer Agent übernimmt oder der bisherige Arbeitskontext verloren ging.
- Außerhalb eines entsprechend eingerichteten Repositories kann sich eine KI die Regel nicht selbst in andere Konten oder Modelle übertragen. Beim Wechsel wird die Datei einmal angehängt oder ihr Inhalt einmal in die erste Nachricht kopiert.

## 2. Auftrag und Fertigstellung vorab festlegen

Vor der Arbeit einmal erfassen:
1. Was genau soll geändert oder eingerichtet werden?
2. Was ist bereits vorhanden und nachweislich erledigt?
3. Was gehört ausdrücklich nicht zum Auftrag?
4. Woran ist objektiv erkennbar, dass die Aufgabe fertig ist?
5. Welche Berechtigungen oder Bestätigungen braucht ein folgender Schritt?

Daraus eine kurze Checkliste machen. Projektregeln, Projektstart und aktuellen Stand einmal gezielt lesen. Doppelte Dokumente oder bereits geprüfte Informationen nicht erneut durchgehen, außer es gibt einen konkreten Hinweis auf eine Änderung.

## 3. Zeit- und Kostenrahmen

- Eine einzelne, klar abgegrenzte Änderung erhält standardmäßig ein Zielbudget von höchstens 30 Minuten aktiver Arbeit.
- Bei mehrstufigen oder externen Aufgaben vor dem Start ein realistisches aktives Zeitbudget und wenige überprüfbare Meilensteine festlegen. Externe Wartezeit, zum Beispiel DNS-Propagation, getrennt von aktiver Arbeitszeit ausweisen.
- Spätestens nach 15 Minuten ohne nachweisbaren Fortschritt anhalten, den konkreten Grund feststellen und einen kurzen Zwischenstand geben.
- Wird das gesetzte Zeitbudget überschritten, nicht stillschweigend weiterprobieren. Spätestens beim Überschreiten um 15 Minuten oder 25 Prozent – je nachdem, was zuerst eintritt – Arbeit anhalten und melden: Zeitaufwand, erledigt, offen, Ursache und beste nächste Option. Ohne Freigabe kein zusätzliches Zeitbudget verbrauchen.
- Zeitgrenzen sind interne Stopps zum Schutz vor unnötigem Aufwand. Sie sind keine Zusage, dass jede Aufgabe innerhalb dieses Zeitraums technisch abgeschlossen sein muss.

## 4. Keine Schleifen

- Beim ersten ernsthaften Ansatz die wahrscheinlich beste Vorgehensweise wählen und ausführen.
- Bei einem Fehler die konkrete Ursache einmal prüfen und genau einen gezielten Korrekturversuch machen.
- Scheitert auch dieser, keine Varianten- oder Wiederholungsschleife starten. Den Fehler, die bereits geprüften Punkte und den konkreten Blocker melden.
- Bereits erledigte Schritte nicht wiederholen. Tool-Aufrufe, Rückfragen, Tests, Agentenwechsel und neue Prompts nur einsetzen, wenn sie die Fertigstellung nachweislich voranbringen.
- Keine Zusatzfunktionen, Umstrukturierungen oder Änderungen außerhalb des Auftrags ergänzen.
- Vor jeder Produktionsänderung den aktuellen Zustand sichern oder nachvollziehbar festhalten. Bei DNS, E-Mail, Konten und Live-Systemen bestehende Einträge und Folgen prüfen, bevor etwas geändert wird.

## 5. Fortschritt und Abnahme

- Bei längeren Aufgaben spätestens nach 15 Minuten aktiver Arbeit und sofort bei einem Blocker kurz berichten: erledigt, offen, nächster Schritt.
- Nicht auf eine spätere Nachfrage warten, wenn ein Hindernis die Arbeit stoppt oder das Zeitbudget gefährdet.
- Vor dem Abschluss jeden Punkt der Checkliste gezielt verifizieren. Nur notwendige, aussagekräftige Tests ausführen.
- Einen Entwurf, Build, Preview oder begonnenen Schritt nicht als fertige Aufgabe bezeichnen. Ungeprüfte oder nicht ausgeführte Punkte klar als offen benennen.
- Vor Commit, Push, Veröffentlichung oder Live-Änderung die für das konkrete Projekt geltenden Freigaberegeln beachten.
- Abschlussmeldung knapp halten: Ergebnis, tatsächlich geprüfte Punkte, offene Punkte und – wenn erfasst – aktive Arbeitszeit sowie externe Wartezeit.

## 6. Arbeitszeit und Kundenabrechnung

- Tatsächliche aktive Arbeit, externe Wartezeit und durch KI- oder Tool-Fehler entstandene Wiederholungen getrennt dokumentieren. Zeiten nicht schätzen oder nachträglich erfinden.
- KI-Fehler, doppelte Versuche, vermeidbare Schleifen und unnötige Agentenwechsel nicht automatisch als Kundenzeit ansetzen. Eine Abrechnung richtet sich nach dem konkreten Vertrag und der vereinbarten Abrechnungsart.
- Bei Stundenabrechnung nur nachvollziehbar dokumentierte, auftragsbezogene Arbeit gemäß Vereinbarung abrechnen. Bei einem vereinbarten Festpreis nicht eigenmächtig interne Mehrzeit weiterberechnen.
- Wenn der Aufwand voraussichtlich den vereinbarten Rahmen überschreitet, vor zusätzlicher Arbeit stoppen, den Grund und den neuen Aufwand nennen und eine Freigabe einholen.
- Eigene Einarbeitung, Prozessfehler und KI-bedingte Ineffizienz nicht als Kundenleistung ausgeben, sofern dies nicht vorher ausdrücklich vereinbart wurde.

## 7. Einmalige Startnachricht

Beim ersten Kontakt eines Modells diese Datei einmal zusammen mit folgender kurzen Übergabe bereitstellen:

> Bitte lies die beigefügte „TrauerOhr KI-Arbeitsregel“ jetzt einmal vollständig und halte sie für diese Zusammenarbeit verbindlich ein. Lies und wiederhole sie bei weiteren Prompts nicht erneut. Falls du als neues Modell übernimmst, erhältst du sie einmalig zusammen mit dem aktuellen Projektstand.  
> **Auftrag:** [konkretes Ziel]  
> **Bereits erledigt/geprüft:** [kurzer Ist-Stand]  
> **Noch offen:** [konkrete Punkte]  
> **Fertig, wenn:** [prüfbares Abnahmekriterium]

Bei einem Agentenwechsel dieselbe Regel nur ein weiteres Mal an das neue Modell übermitteln. Danach im selben Arbeitskontext nicht erneut senden.

---
