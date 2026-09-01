def make_card():
    svg_content = r'''<svg xmlns="http://www.w3.org/2000/svg" width="700" height="420" viewBox="0 0 700 420" fill="none">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e0a1f" />
      <stop offset="50%" stop-color="#120d28" />
      <stop offset="100%" stop-color="#0a0716" />
    </linearGradient>

    <!-- Border Glow Gradient -->
    <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#06b6d4" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ec4899" stop-opacity="0.8" />
    </linearGradient>

    <!-- Divider Gradient -->
    <linearGradient id="divider-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#c084fc" />
      <stop offset="50%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#f472b6" />
    </linearGradient>
  </defs>

  <style>
    <![CDATA[
    .window-bg { fill: url(#bg-grad); stroke: url(#border-grad); stroke-width: 1.5px; rx: 12px; }
    .header-bar { fill: #181135; rx: 12px; }
    .header-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #94a3b8; font-weight: 500; }
    
    .ascii { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #38bdf8; font-weight: bold; line-height: 1.2; }
    .ascii-sub { fill: #c084fc; font-weight: bold; }
    
    .user-title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 15px; font-weight: bold; }
    .label { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12px; fill: #38bdf8; font-weight: 700; }
    .val { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12px; fill: #e2e8f0; }
    .val-accent { fill: #f472b6; font-weight: 600; }
    .val-dim { fill: #94a3b8; }
    
    .line { opacity: 0; animation: fadeIn 0.4s ease-in-out forwards; }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    ]]>
  </style>

  <!-- Main Terminal Window Background -->
  <rect width="700" height="420" rx="12" ry="12" class="window-bg" />

  <!-- Terminal Header / Title Bar -->
  <path d="M 0 12 C 0 5.373 5.373 0 12 0 L 688 0 C 694.627 0 700 5.373 700 12 L 700 34 L 0 34 Z" fill="#160f30" />
  <line x1="0" y1="34" x2="700" y2="34" stroke="#2e1d54" stroke-width="1" />

  <!-- Window Buttons (MacOS traffic lights) -->
  <circle cx="20" cy="17" r="5.5" fill="#ff5f56" stroke="#e0443e" stroke-width="0.5" />
  <circle cx="36" cy="17" r="5.5" fill="#ffbd2e" stroke="#dea123" stroke-width="0.5" />
  <circle cx="52" cy="17" r="5.5" fill="#27c93f" stroke="#1aab29" stroke-width="0.5" />

  <!-- Header Title -->
  <text x="350" y="21" text-anchor="middle" class="header-text">1GabsFps@cyber-deck:~ (zsh)</text>

  <!-- Left Column: Cyberpunk ASCII Art -->
  <g transform="translate(25, 65)">
    <!-- Neon Cyber Icon Box -->
    <rect x="0" y="0" width="130" height="270" rx="8" ry="8" fill="#130c2a" stroke="#4c1d95" stroke-width="1" />
    
    <!-- ASCII Art / Cyber Graphics -->
    <text x="65" y="32" text-anchor="middle" class="ascii">   /\_/\   </text>
    <text x="65" y="48" text-anchor="middle" class="ascii">  ( o.o )  </text>
    <text x="65" y="64" text-anchor="middle" class="ascii">   &gt; ^ &lt;   </text>
    <text x="65" y="80" text-anchor="middle" class="ascii-sub"> [CYBER]  </text>
    
    <text x="65" y="110" text-anchor="middle" font-family="monospace" font-size="10" fill="#a855f7">════════════</text>
    <text x="65" y="130" text-anchor="middle" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">🐍 PYTHON</text>
    <text x="65" y="150" text-anchor="middle" font-family="monospace" font-size="11" fill="#c084fc" font-weight="bold">⚛️ REACT</text>
    <text x="65" y="170" text-anchor="middle" font-family="monospace" font-size="11" fill="#38bdf8" font-weight="bold">☁️ AZURE</text>
    <text x="65" y="190" text-anchor="middle" font-family="monospace" font-size="11" fill="#f472b6" font-weight="bold">📡 IOT/NFC</text>
    <text x="65" y="210" text-anchor="middle" font-family="monospace" font-size="10" fill="#a855f7">════════════</text>
    
    <text x="65" y="235" text-anchor="middle" font-family="monospace" font-size="9" fill="#94a3b8">v2.4.0-neon</text>
    <text x="65" y="252" text-anchor="middle" font-family="monospace" font-size="9" fill="#64748b">x86_64 Linux</text>
  </g>

  <!-- Right Column: Fastfetch Specs & Information -->
  <g transform="translate(175, 60)">
    
    <!-- User Title Header -->
    <g class="line" style="animation-delay: 0.05s;">
      <text x="0" y="12" class="user-title">
        <tspan fill="#38bdf8">1GabsFps</tspan><tspan fill="#a855f7">@</tspan><tspan fill="#c084fc">mainframe</tspan>
      </text>
      <!-- Neon Underline -->
      <rect x="0" y="22" width="490" height="2" fill="url(#divider-grad)" rx="1" />
    </g>

    <!-- Data Rows -->
    <g class="line" style="animation-delay: 0.10s;">
      <text x="0" y="46" class="label">OS</text>
      <text x="15" y="46" class="val-dim">➜</text>
      <text x="30" y="46" class="val">Pop!_OS / Ubuntu VPS / Windows 11</text>
    </g>

    <g class="line" style="animation-delay: 0.15s;">
      <text x="0" y="70" class="label">Role</text>
      <text x="35" y="70" class="val-dim">➜</text>
      <text x="50" y="70" class="val"><tspan fill="#f472b6" font-weight="bold">Fullstack Dev</tspan> (Python &amp; React Ecosystem)</text>
    </g>

    <g class="line" style="animation-delay: 0.20s;">
      <text x="0" y="94" class="label">Backend</text>
      <text x="56" y="94" class="val-dim">➜</text>
      <text x="70" y="94" class="val">Python 3, Django, Flask, FastAPI, REST APIs, MVC</text>
    </g>

    <g class="line" style="animation-delay: 0.25s;">
      <text x="0" y="118" class="label">Frontend</text>
      <text x="60" y="118" class="val-dim">➜</text>
      <text x="75" y="118" class="val">React, React Native (Expo), Vue.js, JS (ES6+)</text>
    </g>

    <g class="line" style="animation-delay: 0.30s;">
      <text x="0" y="142" class="label">Data/Cloud</text>
      <text x="75" y="142" class="val-dim">➜</text>
      <text x="90" y="142" class="val">Azure (<tspan fill="#c084fc">DP-900</tspan> &amp; <tspan fill="#c084fc">AI-900</tspan>), SQL, Firebase</text>
    </g>

    <g class="line" style="animation-delay: 0.35s;">
      <text x="0" y="166" class="label">DevOps</text>
      <text x="50" y="166" class="val-dim">➜</text>
      <text x="65" y="166" class="val">Linux, Docker, Git/GitHub, Nginx, Oracle Cloud</text>
    </g>

    <g class="line" style="animation-delay: 0.40s;">
      <text x="0" y="190" class="label">IoT &amp; AI</text>
      <text x="55" y="190" class="val-dim">➜</text>
      <text x="70" y="190" class="val">NFC / Hardware, WEGnology, Google Gemini API</text>
    </g>

    <g class="line" style="animation-delay: 0.45s;">
      <text x="0" y="214" class="label">Education</text>
      <text x="68" y="214" class="val-dim">➜</text>
      <text x="82" y="214" class="val">Análise e Desenv. de Sistemas (SENAI 2024)</text>
    </g>

    <g class="line" style="animation-delay: 0.50s;">
      <text x="0" y="238" class="label">Languages</text>
      <text x="70" y="238" class="val-dim">➜</text>
      <text x="85" y="238" class="val"><tspan fill="#38bdf8">Inglês</tspan> (Avançado/C1) | <tspan fill="#38bdf8">Português</tspan> (Nativo)</text>
    </g>

    <g class="line" style="animation-delay: 0.55s;">
      <text x="0" y="262" class="label">Contact</text>
      <text x="52" y="262" class="val-dim">➜</text>
      <text x="67" y="262" class="val" fill="#c084fc">linkedin.com/in/gabrielneco</text>
    </g>

    <!-- Terminal Color Palette Circles (Neofetch signature) -->
    <g class="line" style="animation-delay: 0.60s;" transform="translate(0, 290)">
      <circle cx="6" cy="0" r="5.5" fill="#0f172a" />
      <circle cx="22" cy="0" r="5.5" fill="#ef4444" />
      <circle cx="38" cy="0" r="5.5" fill="#22c55e" />
      <circle cx="54" cy="0" r="5.5" fill="#eab308" />
      <circle cx="70" cy="0" r="5.5" fill="#3b82f6" />
      <circle cx="86" cy="0" r="5.5" fill="#a855f7" />
      <circle cx="102" cy="0" r="5.5" fill="#06b6d4" />
      <circle cx="118" cy="0" r="5.5" fill="#f43f5e" />
      
      <!-- Bright variants -->
      <circle cx="140" cy="0" r="5.5" fill="#475569" />
      <circle cx="156" cy="0" r="5.5" fill="#f87171" />
      <circle cx="172" cy="0" r="5.5" fill="#4ade80" />
      <circle cx="188" cy="0" r="5.5" fill="#fde047" />
      <circle cx="204" cy="0" r="5.5" fill="#60a5fa" />
      <circle cx="220" cy="0" r="5.5" fill="#c084fc" />
      <circle cx="236" cy="0" r="5.5" fill="#38bdf8" />
      <circle cx="252" cy="0" r="5.5" fill="#fb7185" />
    </g>
  </g>
</svg>'''

    with open("info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg gerado com sucesso!")

if __name__ == "__main__":
    make_card()
