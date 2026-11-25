# The World in One Page — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/0xberuuu/news-25-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/0xberuuu/news-25-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty [news-image-20261125](https://make.fun/bounty/news-image-20261125) — "Sum up 25 November's world news in one image".

## What it is

A single 1024x1024 newspaper-style front page, drawn entirely in code with Python and Pillow. No photos, no downloaded images, no AI-generated art — every pixel, including the small tanker schematic, is drawn programmatically. The image is deterministic: running the generator twice produces a byte-identical file.

## Stories covered (all from Wednesday 25 November 2026)

1. **Strait of Hormuz** — Iran's Revolutionary Guard said two oil tankers struck naval mines and caught fire while transiting an unauthorised route. (Just Security, Early Edition 25 Nov 2026)
2. **Huawei convicted** — a Brooklyn jury found Huawei guilty on 10 of 12 counts, including conspiring to steal trade secrets, bank fraud and sanctions violations; acquitted of racketeering. (Reuters, 25 Nov 2026)
3. **Shenzhou-24 docks at Tiangong** — carrying Muhammad Zeeshan Ali, the first Pakistani in orbit and the first foreigner ever to visit China's Tiangong space station. (Xinhua / China Manned Space Agency, 25 Nov 2026)
4. **US GDP revised up to 4.3%** — the Bureau of Economic Analysis raised third-quarter 2026 growth to a 4.3% annual rate, from a first estimate of 3.4%. (BEA, released 25 Nov 2026)
5. **Cartagena hostages freed** — Colombian forces stormed an Éxito supermarket in Cartagena, freeing every remaining hostage after a day-long siege; one captor was killed. (Reuters / AFP, 25 Nov 2026)
6. **COP31 ends without a fossil-fuel deal** — the UN climate talks closed with no agreement to transition away from fossil fuels; Pope Leo XIV voiced concern. (AP, 25 Nov 2026)
7. **Houthis strike Saudi Arabia** — the Houthis said they attacked the Ras Tanura oil refinery, a day after a strike on a Riyadh skyscraper injured 11 people. (Just Security / AP, 25 Nov 2026)

Also in brief: Australia and Solomon Islands sign a treaty barring foreign military bases; the Dow closes above 50,000 for the first time; South Korea's KOSPI plunges 6.2%.

## Run it

Requires Python 3 with Pillow installed (`pip install pillow`).

```bash
# Regenerate the front page (deterministic — same output every run)
python3 generate.py

# Copy the finished image to the harness output directory
python3 main.py
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` uses only the Python standard library. It reads `MAKEFUN_OUTPUT_DIR` (default `out`), creates the directory if needed, and copies this repo's `entry.png` into it as `entry.png`.

## Files

- `entry.png` — the finished 1024x1024 front page
- `generate.py` — the generator that draws `entry.png` from code
- `main.py` — entrypoint: copies `entry.png` to `MAKEFUN_OUTPUT_DIR`
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).
