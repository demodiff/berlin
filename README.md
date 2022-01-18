demodiff: berlin
===================

> Diffing political assemblies for Berlin, Germany.

Since March 2021, Polizei Berlin announces demonstrations and other
political assemblies [on its website
berlin.de](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/).
This repository scrapes [the JSON
endpoint](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/index.php/index/all.json)
and parses it to JSON Lines. By this, a diff is created in the git-log.

## Preface

Polizei Berlin is obliged to publish assemblies
and demonstrations since the amendment of February
23rd 2021.

> Die zuständige Behörde hat Ort, Zeit und Thema
> der angezeigten Versammlung zu veröffentlichen.
> Sofern es sich um einen Aufzug handelt, hat
> sie auch den Streckenverlauf zu veröffentlichen.
> (*§ 12 Absatz 8 VersFG BE*)

But the police is not obliged to keep records of
past events. This shall be done by this project,
that is not connected to any official entitiy though.

## Links

Please see below for relevant links regarding this
project.

- [Latest diffs](https://github.com/demodiff/berlin/commits/main/data/results.jsonl)
- [Latest zip code statistics](https://github.com/demodiff/berlin/commits/main/data/stats-zips.csv)
- [RSS feed for diffs (and development)](https://github.com/demodiff/berlin/commits.atom)
- [tweet bot for diffs (excluding development)](https://twitter.com/demodiff)

## Focus

Since Polizei Berlin depublishes past assemblies from
their website, this project contributes to conserving
historical data and keeping the police accountable.

Thus three key focus points are highlighted below:

1. *Scientific work*: Analysing the data can and shall
   always be possible. 
2. *Activism*: If you want to stay up-to-date or
   analyse past assemblies, the data may help.
3. *Politics:* Further cities and states should
   implement, that assembly authorities shall keep
   records of demonstrations.
   
You got further points? [Please feel free to open an
issue](https://github.com/demodiff/berlin/issues/new).

## Workflows
[Two GitHub workflows](https://github.com/demodiff/berlin/tree/main/.github/workflows)
keep this repo working: the scraper and the parser.

The scraper downloads the results of the JSON endpoint
with `wget` and commits it to the repo under
`data/results.json`.

The parser converts the downloaded state to JSON Lines,
so the diff is human readable. It also translates the keys
of the JSON into the English language and omits values that
– so far – are not needed (such as the Laufende Nummer).

A third workflow is outsourced to the IFTTT service. It
tweets when a new commit is made by the parser. [Have a look
at the twitter account here](https://twitter.com/demodiff).

## Contact & Legal

In case you have questions or threatening letters, 
please contact [Lennart Mühlenmeier](https://lnrt.de/).

_LICENSE to be added._
