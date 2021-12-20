demodiff: berlin
===================

**THIS README IS STILL WIP.**

> Diffing political assemblies for Berlin, Germany.

Since March 2021, Polizei Berlin announces demonstrations and other
political assemblies [on its website
berlin.de](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/).
This repository scrapes [the JSON
endpoint](https://www.berlin.de/polizei/service/versammlungsbehoerde/versammlungen-aufzuege/index.php/index/all.json)
and parses it to JSON Lines. By this, a diff is created in the git-log.

## Usage


## Links
- [latest diffs](https://github.com/demodiff/berlin/commits/main/data/results.jsonl)
- [latest zip code statistics](https://github.com/demodiff/berlin/commits/main/data/stats-zips.csv)
- [tweet bot](https://twitter.com/demodiff)

## Politics

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

## Contact

In case you have questions or threatening letters, 
please contact [Lennart Mühlenmeier](https://lnrt.de/).

_LICENSE to be added._
