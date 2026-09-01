def make_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="490" height="280" viewBox="0 0 490 280" fill="none">
  <style>
    <![CDATA[
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }
    .title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 14px; fill: #58a6ff; font-weight: 700; }
    .divider { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 13px; fill: #8b949e; }
    .label { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 13px; fill: #7ee787; font-weight: 600; }
    .text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 13px; fill: #c9d1d9; }
    .line { opacity: 0; animation: fadeIn 0.4s ease-in-out forwards; }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    ]]>
  </style>
  <rect width="490" height="280" rx="8" ry="8" class="bg" />
  <g transform="translate(25, 35)">
    <g class="line" style="animation-delay: 0.05s;">
      <text x="0" y="5" class="title">1GabsFps@github</text>
      <text x="0" y="24" class="divider">----------------------------------------</text>
    </g>
    <g class="line" style="animation-delay: 0.15s;">
      <text x="0" y="58" class="label">OS:</text>
      <text x="75" y="58" class="text">Ubuntu VPS / Pop!_OS / Windows</text>
    </g>
    <g class="line" style="animation-delay: 0.25s;">
      <text x="0" y="88" class="label">Role:</text>
      <text x="75" y="88" class="text">Software Engineering Student</text>
    </g>
    <g class="line" style="animation-delay: 0.35s;">
      <text x="0" y="118" class="label">Stack:</text>
      <text x="75" y="118" class="text">Python, React, Node.js, FastAPI, Docker</text>
    </g>
    <g class="line" style="animation-delay: 0.45s;">
      <text x="0" y="148" class="label">Focus:</text>
      <text x="75" y="148" class="text">Full-stack Web Dev &amp; Automation</text>
    </g>
    <g class="line" style="animation-delay: 0.55s;">
      <text x="0" y="178" class="label">Hosting:</text>
      <text x="75" y="178" class="text">Oracle Cloud, Nginx, Docker Compose</text>
    </g>
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg gerado com sucesso!")

if __name__ == "__main__":
    make_card()
