demodiff: berlin
===================

Seit dem März 2021 kündigt die Polizei Berlin Demonstrationen und andere
politische Versammlungen [auf ihrer Website berlin.de](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/)
an. Dieses Repository [scrapt den JSON-Endpunkt](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/index.php/index/all.json)
und parst ihn zu JSON-Lines. Dadurch wird ein Diff im `git-log` erstellt.

## Vorwort

Die Polizei Berlin ist seit der Novelle vom 23. Februar 2021 verpflichtet,
Versammlungen und Demonstrationen zu veröffentlichen.

> Die zuständige Behörde hat Ort, Zeit und Thema
> der angezeigten Versammlung zu veröffentlichen.
> Sofern es sich um einen Aufzug handelt, hat
> sie auch den Streckenverlauf zu veröffentlichen.
> (*§ 12 Absatz 8 VersFG BE*)

Aber die Polizei ist nicht verpflichtet, Aufzeichnungen über vergangene
Ereignisse zu veröffentlichen. Dies soll durch dieses Projekt geschehen, das
allerdings nicht an eine offizielle Stelle angebunden ist.

## Links

An dieser Stelle gibt es relevante Links des Projekts.

- [Letzte Diffs](https://github.com/demodiff/berlin/commits/main/data/results.jsonl)
- [Letzte Postleitzahl-Statistiken](https://github.com/demodiff/berlin/commits/main/data/stats-zips.csv)
- [RSS-Feed für Diffs (mit Developemnt)](https://github.com/demodiff/berlin/commits.atom)
- [Twitter-Bot für Diffs (ohne development)](https://twitter.com/demodiff)

## Fokus

Da die Polizei Berlin vergangene Versammlungen auf ihrer Website
veröffentlicht, trägt dieses Projekt dazu bei, historische Daten zu bewahren
und die Polizei zur Rechenschaft zu ziehen.

Daher werden im Folgenden drei zentrale Punkte hervorgehoben:

1. *Wissenschaft*: Eine Analyse der Daten kann und soll für immer möglich sein.
2. *Aktivismus*: Die Daten können helfen, auf dem aktuellenStand zu bleiben.
3. *Politik:* Weitere Städte und Bundesländer sollten diese Daten
   veröffentlichen.
   
Dir fallen weitere Punkt ein? [Öffne gerne ein Issue.](https://github.com/demodiff/berlin/issues/new).

## Workflows

[Zwei GitHub-Workflows](https://github.com/demodiff/berlin/tree/main/.github/workflows)
halten dieses Projekt am Laufen: den Scraper und den Parser.

Der Scraper lädt die Ergebnisse des JSON-Endpunkts mit wget herunter und
überträgt sie in das Repo unter `data/results.json`.

Der Parser konvertiert den heruntergeladenen Status in JSON-Zeilen, so dass das
Diff für Menschen lesbar ist. Er übersetzt auch die Keys des JSON in die
englische Sprache und lässt Values weg, die - bisher - nicht benötigt werden
(wie z.B. die Laufende Nummer).

Ein dritter Workflow ist an den IFTTT-Dienst ausgelagert. Er twittert, wenn ein
neuer Commit vom Parser gemacht wird. [Schau Dir den Twitter-Bot hier an](https://twitter.com/demodiff).

## Kontakt & Rechtliches

Falls Sie Fragen oder Drohbriefe haben, wenden Sie sich bitte an [Lennart Mühlenmeier](https://lnrt.de).

_LICENSE wird noch hinzugefügt._
