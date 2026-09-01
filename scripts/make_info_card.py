def make_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="280" viewBox="0 0 490 280" fill="none">
  <style>
    <![CDATA[
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }
    .title { font-family: monospace, Courier, 'Courier New', sans-serif; font-size: 14px; fill: #58a6ff; font-weight: bold; }
    .divider { font-family: monospace, Courier, 'Courier New', sans-serif; font-size: 13px; fill: #8b949e; }
    .label { font-family: monospace, Courier, 'Courier New', sans-serif; font-size: 13px; fill: #7ee787; font-weight: bold; }
    .text { font-family: monospace, Courier, 'Courier New', sans-serif; font-size: 13px; fill: #c9d1d9; }
    .line { opacity: 0; animation: slideIn 0.4s forwards; }
    @keyframes slideIn {
      from { opacity: 0; transform: translateX(-10px); }
      to { opacity: 1; transform: translateX(0); }
    }
    ]]>
  </style>
  <rect width="490" height="280" rx="8" ry="8" class="bg" />
  <g transform="translate(25, 35)">
    <g class="line" style="animation-delay: 0.1s;">
      <text x="0" y="0" class="title">1GabsFps@github</text>
      <text x="0" y="16" class="divider">----------------------------------------</text>
    </g>
    <g class="line" style="animation-delay: 0.2s;">
      <text x="0" y="48" class="label">OS:</text>
      <text x="70" y="48" class="text">Ubuntu VPS / Pop!_OS / Windows</text>
    </g>
    <g class="line" style="animation-delay: 0.3s;">
      <text x="0" y="78" class="label">Role:</text>
      <text x="70" y="78" class="text">Software Engineering Student</text>
    </g>
    <g class="line" style="animation-delay: 0.4s;">
      <text x="0" y="108" class="label">Stack:</text>
      <text x="70" y="108" class="text">Python, React, Node.js, FastAPI, Docker</text>
    </g>
    <g class="line" style="animation-delay: 0.5s;">
      <text x="0" y="138" class="label">Focus:</text>
      <text x="70" y="138" class="text">Full-stack Web Dev &amp; Automation</text>
    </g>
    <g class="line" style="animation-delay: 0.6s;">
      <text x="0" y="168" class="label">Hosting:</text>
      <text x="70" y="168" class="text">Oracle Cloud, Nginx, Docker Compose</text>
    </g>
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg gerado com sucesso!")

if __name__ == "__main__":
    make_card()
