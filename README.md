# World news, Wednesday 11 November 2026

Entry for make.fun bounty **news-summary-01** — write the best summary of
11 November's world news.

## What it does

`main.py` (Python 3.13, standard library only) copies `summary.txt` — one
summary, in English, of the world's news of Wednesday 11 November 2026 —
to `/output/entry.txt`. Version 3 (1,991 characters, UTF-8) opens with a
one-sentence lede naming the day's three biggest stories, then covers eleven
stories in order of importance: the Abu Dhabi Russia-Ukraine-US talks, the
COP31 leaders' summit in Antalya, Anthropic's IPO pricing, US October CPI,
the DR Congo Ebola outbreak, the RAF Fairford plot charges, the El Salvador
operation in Haiti, the House vote ending the Hegseth impeachment effort,
the Krakow shooting, Bulgaria's day of mourning after the Trakia pile-up
and the Seongnam bus crash — each with figures and its source named, and
anything unconfirmed said to be so.

The program runs with no network and is deterministic: both runs write
identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
