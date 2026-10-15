# MADT 7202 Mid-Term: Steam tag network
Narongrit Bureeruk · 6810424013

**Question:** Which tag should a Thai 2D indie studio pair with its next Steam game?

## Files
| File | What it is |
|---|---|
| `6810424013_Narongrit_Bureeruk.pdf` | The one-page A4 submission |
| `steam_tag_network.ipynb` | Full pipeline: data collection, cleaning, graph, NPMI vs raw count, robustness (run top to bottom in Google Colab) |
| `results.json` | All numbers used on the one-page report |
| `structure.json` | Betweenness and participation coefficient for 2D and its 22 partners (notebook cell 14) |
| `tagcheck.json` | Tag triangulation: SteamSpy vs Steam store pages, 29 random games (notebook cell 15) |
| `ego_fig.py` | Draws the report figure from `results.json` |
| `figure_ego.png` | The figure on the page (2D's ego network) |
| `figure.png` | Wider tag-network figure from the notebook |

## Data
- **Source:** SteamSpy public API (`request=tag`, `request=appdetails`). Review totals were cross-checked against Steam's public `appreviews` endpoint for 30 games (Spearman ρ 0.99). Tags were cross-checked against Steam store pages for 29 games.
- **Access:** Public APIs, no key, no login. SteamSpy robots.txt is `Allow: /`, and the Steam store robots.txt does not disallow `/app/`. Requests are paced at 1 to 1.5 seconds. Only game-level aggregates are kept, so there is no personal data, and raw pulls are not redistributed.
- **Sample:** 15 Oct 2026. A random 600 games (seed 7202) from 6,287 Indie-tagged games with at least 500 reviews; 592 kept.

## Rules fixed before results
1. The seed tag `Indie` is excluded from all rankings.
2. Generic tags, present in at least 40% of games' top-15 tags, are dropped.
3. Partner rule: among the core tag's neighbours with NPMI ≥ 0.10 and at least 10 shared games, rank by lift in median positive-review share against core-only games.
4. A partner is recommended only if it stays #1 in at least 60% of 500 bootstrap resamples.

**Note:** The notebook's default core `Roguelike` is not a Steam tag name, so the notebook fell back to the most common non-generic tag, `2D` (198 games).

**Added after the first results (descriptive only, the rule above was not changed):**
- Cell 14 computes betweenness and participation to describe whether candidate partners bridge communities.
- Cell 15 cross-checks tags against Steam store pages: 84% of top-15 and 83% of top-5 tags match. This is a lower bound, since 4 store pages show fewer than 15 tags.

## Reproduce
1. Open the notebook in Google Colab and choose **Runtime → Run all** (about 15 minutes).
2. Then run `python ego_fig.py` to redraw the report figure.
