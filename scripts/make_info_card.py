def make_card():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="580" height="340" viewBox="0 0 580 340" fill="none">
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
  <rect width="580" height="340" rx="8" ry="8" class="bg" />
  <g transform="translate(25, 30)">
    <g class="line" style="animation-delay: 0.05s;">
      <text x="0" y="5" class="title">1GabsFps@github</text>
      <text x="0" y="24" class="divider">-------------------------------------------------------------</text>
    </g>
    <g class="line" style="animation-delay: 0.12s;">
      <text x="0" y="56" class="label">Role:</text>
      <text x="95" y="56" class="text">Fullstack Developer (Python | React)</text>
    </g>
    <g class="line" style="animation-delay: 0.18s;">
      <text x="0" y="84" class="label">Backend:</text>
      <text x="95" y="84" class="text">Python (Django, Flask, FastAPI), REST APIs, MVC</text>
    </g>
    <g class="line" style="animation-delay: 0.24s;">
      <text x="0" y="112" class="label">Frontend:</text>
      <text x="95" y="112" class="text">React, React Native (Expo), Vue.js, JS (ES6+)</text>
    </g>
    <g class="line" style="animation-delay: 0.30s;">
      <text x="0" y="140" class="label">Data &amp; Cloud:</text>
      <text x="95" y="140" class="text">SQL, Firebase, Azure (DP-900 &amp; AI-900)</text>
    </g>
    <g class="line" style="animation-delay: 0.36s;">
      <text x="0" y="168" class="label">DevOps &amp; OS:</text>
      <text x="95" y="168" class="text">Linux, Git/GitHub, Docker, Nginx</text>
    </g>
    <g class="line" style="animation-delay: 0.42s;">
      <text x="0" y="196" class="label">IoT &amp; AI:</text>
      <text x="95" y="196" class="text">NFC / Hardware, WEGnology, Google Gemini API</text>
    </g>
    <g class="line" style="animation-delay: 0.48s;">
      <text x="0" y="224" class="label">Education:</text>
      <text x="95" y="224" class="text">Análise e Desenv. de Sistemas (SENAI)</text>
    </g>
    <g class="line" style="animation-delay: 0.54s;">
      <text x="0" y="252" class="label">Languages:</text>
      <text x="95" y="252" class="text">Inglês (Avançado) | Português (Nativo)</text>
    </g>
    <g class="line" style="animation-delay: 0.60s;">
      <text x="0" y="280" class="label">LinkedIn:</text>
      <text x="95" y="280" class="text" fill="#58a6ff">linkedin.com/in/gabrielneco</text>
    </g>
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg gerado com sucesso!")

if __name__ == "__main__":
    make_card()
