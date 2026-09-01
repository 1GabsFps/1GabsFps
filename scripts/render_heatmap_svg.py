import json

PALETTE = ["#1b1335", "#381a60", "#6b21a8", "#a855f7", "#06b6d4", "#38bdf8"]

def render_svg():
    try:
        with open("data/contributions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.sort(key=lambda x: x.get("date", ""))

    svg_header = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="180" viewBox="0 0 860 180" fill="none">
  <defs>
    <linearGradient id="hm-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0a1f" />
      <stop offset="100%" stop-color="#0a0716" />
    </linearGradient>
    <linearGradient id="hm-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ec4899" stop-opacity="0.8" />
    </linearGradient>
  </defs>

  <style>
    <![CDATA[
    .window-bg { fill: url(#hm-bg); stroke: url(#hm-border); stroke-width: 1.5px; }
    .header-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #94a3b8; font-weight: 500; }
    .day { rx: 2.5px; ry: 2.5px; opacity: 0; animation: fadeIn 0.5s forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    ]]>
  </style>

  <!-- Window Frame -->
  <rect width="860" height="180" rx="12" ry="12" class="window-bg" />

  <!-- Terminal Header / Title Bar -->
  <path d="M 0 12 C 0 5.373 5.373 0 12 0 L 848 0 C 854.627 0 860 5.373 860 12 L 860 34 L 0 34 Z" fill="#160f30" />
  <line x1="0" y1="34" x2="860" y2="34" stroke="#2e1d54" stroke-width="1" />

  <!-- Window Buttons -->
  <circle cx="20" cy="17" r="5.5" fill="#ff5f56" stroke="#e0443e" stroke-width="0.5" />
  <circle cx="36" cy="17" r="5.5" fill="#ffbd2e" stroke="#dea123" stroke-width="0.5" />
  <circle cx="52" cy="17" r="5.5" fill="#27c93f" stroke="#1aab29" stroke-width="0.5" />

  <!-- Header Title -->
  <text x="430" y="21" text-anchor="middle" class="header-text">1GabsFps@activity-log:~ (contributions-matrix)</text>

  <!-- Heatmap Rectangles -->
  <g transform="translate(30, 52)">
'''

    rects = ""
    col = 0
    row = 0
    for i, item in enumerate(data[-371:]):  # Últimas ~53 semanas
        color = PALETTE[min(item.get("level", 0), 5)]
        x = col * 15
        y = row * 15
        delay = (col + row) * 0.015
        rects += f'    <rect x="{x}" y="{y}" width="11" height="11" rx="2" ry="2" fill="{color}" class="day" style="animation-delay: {delay:.2f}s;" />\n'
        row += 1
        if row >= 7:
            row = 0
            col += 1

    svg_footer = '''  </g>
</svg>'''

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg_header + rects + svg_footer)
    print("contrib-heatmap.svg gerado com sucesso!")

if __name__ == "__main__":
    render_svg()
