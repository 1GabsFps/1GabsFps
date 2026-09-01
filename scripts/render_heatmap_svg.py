import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_svg():
    try:
        with open("data/contributions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.sort(key=lambda x: x.get("date", ""))

    svg_header = '''<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150" viewBox="0 0 860 150" fill="none">
  <style>
    <![CDATA[
    .day { opacity: 0; animation: fadeIn 0.5s forwards; }
    @keyframes fadeIn { to { opacity: 1; } }
    ]]>
  </style>
  <rect width="860" height="150" rx="8" ry="8" fill="#0d1117" />
  <g transform="translate(20, 20)">
'''
    
    rects = ""
    col = 0
    row = 0
    for i, item in enumerate(data[-371:]):  # Últimas ~53 semanas
        color = PALETTE[min(item.get("level", 0), 5)]
        x = col * 15
        y = row * 15
        delay = (col + row) * 0.02
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
