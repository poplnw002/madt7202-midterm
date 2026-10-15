import json, math, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager
R = json.load(open('results.json'))
P = R['partners']; core = R['core']
same = sorted([p for p in P if not p['cross']], key=lambda p: -p['lift_pp'])
cross = sorted([p for p in P if p['cross']], key=lambda p: -p['lift_pp'])
pos = {}
def place(group, side):
    n = len(group)
    for i, p in enumerate(group):
        y = 1.7 - 3.4 * i / max(1, n - 1)
        x = side * (0.9 + 2.0 * (0.45 - min(p['npmi'], 0.45)) / 0.35)
        pos[p['partner']] = (x, y)
place(same, -1)
place(cross, 1)
ORANGE, NAVY, GREY = '#E8692C', '#2E5AAC', '#9AA0AE'
fig, ax = plt.subplots(figsize=(6.9, 1.95), dpi=300)
for p in P:
    x, y = pos[p['partner']]
    hl = p['partner'] in ('Arcade', 'Mystery'); cr = p['partner'] == R['crowded']
    ax.plot([0, x], [0, y], color=ORANGE if hl else ('#444' if cr else '#CCCCCC'),
            lw=0.3 + p['n_pair'] / 14, ls='--' if cr else '-', zorder=1, solid_capstyle='round')
for p in P:
    x, y = pos[p['partner']]; L = p['lift_pp']
    c = ORANGE if L >= 2 else (NAVY if L >= 0 else GREY)
    ax.scatter(x, y, s=12 + 2.6 * p['n_pair'], color=c, edgecolor='black' if p['partner'] in ('Arcade', 'Mystery', R['crowded']) else 'white', lw=1, zorder=2)
    lbl = f"{p['partner']}  {L:+.1f} pp ({p['n_pair']})"
    flip = False
    ha = 'right' if (x < 0) != flip else 'left'; dx = (-1 if (x < 0) != flip else 1) * (0.12 + 0.004 * p['n_pair']) 
    ax.text(x + dx, y, lbl, fontsize=6.3, ha=ha, va='center', zorder=3,
            fontweight='bold' if p['partner'] in ('Arcade', 'Mystery', R['crowded']) else 'normal')
ax.scatter(0, 0, s=520, color='#23306B', zorder=4); ax.text(0, 0, f"{core}\n{R['core_games']} games", color='white', fontsize=6.5, ha='center', va='center', fontweight='bold', zorder=5)
ax.text(-4.6, 2.25, 'Same community as 2D (pixel / platformer), sorted by lift', fontsize=6.5, color='#555', ha='left', va='top')
ax.text(4.6, 2.25, 'Other communities (second audience), sorted by lift', fontsize=6.5, color='#555', ha='right', va='top')
ax.set_xlim(-4.7, 4.7); ax.set_ylim(-1.9, 2.3); ax.axis('off')
plt.tight_layout(pad=0.1); plt.savefig('figure_ego.png', dpi=300, bbox_inches='tight')
