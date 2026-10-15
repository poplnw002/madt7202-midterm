# MADT 7202 Mid-Term: Steam tag network

**Question:** Which tag should a Thai indie studio pair with its core genre on Steam?

## Files
| File | What it is |
|---|---|
| `steam_tag_network.ipynb` | Full pipeline: data collection, cleaning, graph, NPMI vs raw count, robustness, figure (run top to bottom in Google Colab) |
| `results.json` | All numbers used on the one-page report |
| `figure.png` | The figure on the page |
| `report.pdf` | The one-page A4 submission |

## Data
- **Source:** SteamSpy public API (`request=tag`, `request=appdetails`). Review totals were cross-checked against Steam's public `appreviews` endpoint for 30 games.
- **Access:** Public API with no key and no login. Requests are paced at about 1 per second, following SteamSpy's stated rate limit. Only game-level aggregates are kept, so there is no personal data.
- **Sample:** A random 600 games (seed 7202) drawn from Indie-tagged games with at least 500 reviews. The pull date is recorded in `results.json`.

## Rules fixed before results
1. The seed tag `Indie` is excluded from all rankings.
2. Generic tags, present in at least 40% of games' top-K tags, are dropped.
3. **Partner rule:** among neighbours of the core tag with NPMI ≥ 0.10 and at least 10 shared games, rank partners by lift in median positive-review share against core-only games.
4. A partner is recommended only if it stays #1 in at least 60% of 500 bootstrap resamples.

## Reproduce
Open the notebook in Google Colab and choose **Runtime → Run all**. The run takes about 15 minutes.
