def make_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="280" viewBox="0 0 490 280" fill="none">
  <style>
    .bg { fill: #0d1117; rx: 8px; stroke: #30363d; stroke-width: 1px; }
    .title { font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; }
    .label { font-family: monospace; font-size: 13px; fill: #7ee787; font-weight: bold; }
    .text { font-family: monospace; font-size: 13px; fill: #c9d1d9; }
    .line { opacity: 0; animation: slideIn 0.4s forwards; }
    @keyframes slideIn { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: translateX(0); } }
  </style>
  <rect width="490" height="280" class="bg" />
  <g transform="translate(25, 35)">
    <g class="line" style="animation-delay: 0.1s;">
      <text y="0" class="title">1GabsFps@github</text>
      <text y="15" class="text" fill="#8b949e">----------------------------------------</text>
    </g>
    <g class="line" style="animation-delay: 0.2s;" transform="translate(0, 40)">
      <text class="label">OS:</text>
      <text x="70" class="text">Ubuntu VPS / Pop!_OS / Windows</text>
    </g>
    <g class="line" style="animation-delay: 0.3s;" transform="translate(0, 70)">
      <text class="label">Role:</text>
      <text x="70" class="text">Software Engineering Student</text>
    </g>
    <g class="line" style="animation-delay: 0.4s;" transform="translate(0, 100)">
      <text class="label">Stack:</text>
      <text x="70" class="text">Python, React, Node.js, FastAPI, Docker</text>
    </g>
    <g class="line" style="animation-delay: 0.5s;" transform="translate(0, 130)">
      <text class="label">Focus:</text>
      <text x="70" class="text">Full-stack Web Dev & Automation</text>
    </g>
    <g class="line" style="animation-delay: 0.6s;" transform="translate(0, 160)">
      <text class="label">Hosting:</text>
      <text x="70" class="text">Oracle Cloud, Nginx, Docker Compose</text>
    </g>
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg gerado com sucesso!")

if __name__ == "__main__":
    make_card()
