<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>DieselDeck — README</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&family=Barlow:wght@300;400;600;700&display=swap" rel="stylesheet"/>
<style>
  :root {
    --amber: #F5A623;
    --amber-dim: #C17D10;
    --orange: #FF6B2B;
    --bg: #0D0D0D;
    --surface: #141414;
    --surface2: #1C1C1C;
    --border: #2A2A2A;
    --text: #E8E0D0;
    --muted: #7A7060;
    --green: #39D98A;
    --red: #FF4560;
    --blue: #00B4FF;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Barlow', sans-serif;
    font-weight: 400;
    line-height: 1.6;
    overflow-x: hidden;
  }
  .road-strip {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 3px;
    background: repeating-linear-gradient(90deg,
      var(--amber) 0px, var(--amber) 30px,
      transparent 30px, transparent 60px);
    animation: roadMove 1.2s linear infinite;
    z-index: 100;
    opacity: 0.4;
  }
  @keyframes roadMove {
    from { background-position: 0 0; }
    to   { background-position: 60px 0; }
  }
  .hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    padding: 60px 24px;
    overflow: hidden;
    background:
      radial-gradient(ellipse 80% 60% at 50% 100%, rgba(245,166,35,0.06) 0%, transparent 70%),
      repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(255,255,255,0.018) 40px),
      repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(255,255,255,0.018) 40px),
      var(--bg);
  }
  .truck-lane {
    position: absolute;
    bottom: 80px;
    left: -200px;
    animation: truckDrive 8s linear infinite;
  }
  .truck-lane svg { opacity: 0.18; }
  @keyframes truckDrive {
    from { left: -200px; }
    to   { left: calc(100% + 200px); }
  }
  .gauge-ring {
    position: absolute;
    top: 40px; right: 60px;
    width: 90px; height: 90px;
    border-radius: 50%;
    border: 2px solid var(--border);
    display: flex; align-items: center; justify-content: center;
    animation: gaugePulse 3s ease-in-out infinite;
    opacity: 0.3;
  }
  .gauge-ring::after {
    content: '⛽';
    font-size: 28px;
  }
  @keyframes gaugePulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(245,166,35,0.4); }
    50%      { box-shadow: 0 0 0 14px rgba(245,166,35,0); }
  }
  .badge-row {
    display: flex; gap: 10px; flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 28px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.3s forwards;
  }
  .badge {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 2px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .badge-live  { background: rgba(57,217,138,0.12); color: var(--green); border: 1px solid rgba(57,217,138,0.3); }
  .badge-python{ background: rgba(0,180,255,0.1);   color: var(--blue);  border: 1px solid rgba(0,180,255,0.25); }
  .badge-stream{ background: rgba(255,75,96,0.1);   color: var(--red);   border: 1px solid rgba(255,75,96,0.25); }
  .hero-eyebrow {
    font-family: 'Share Tech Mono', monospace;
    color: var(--amber);
    font-size: 13px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 16px;
    opacity: 0;
    animation: fadeUp 0.6s ease 0.5s forwards;
  }
  .hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(72px, 14vw, 160px);
    line-height: 0.9;
    text-align: center;
    letter-spacing: 2px;
    color: var(--text);
    opacity: 0;
    animation: fadeUp 0.8s ease 0.7s forwards;
  }
  .hero-title span { color: var(--amber); text-shadow: 0 0 40px rgba(245,166,35,0.5); }
  .hero-sub {
    font-size: 16px;
    font-weight: 300;
    color: var(--muted);
    text-align: center;
    max-width: 540px;
    margin: 20px auto 0;
    opacity: 0;
    animation: fadeUp 0.6s ease 1s forwards;
  }
  .hero-sub::after {
    content: '|';
    color: var(--amber);
    animation: blink 0.8s step-end infinite;
  }
  .hero-cta {
    display: flex; gap: 16px; flex-wrap: wrap;
    justify-content: center;
    margin-top: 40px;
    opacity: 0;
    animation: fadeUp 0.6s ease 1.2s forwards;
  }
  .btn {
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 12px 28px;
    border-radius: 2px;
    text-decoration: none;
    transition: all 0.2s;
    cursor: pointer;
    display: inline-block;
  }
  .btn-primary { background: var(--amber); color: #000; border: 2px solid var(--amber); font-weight: 700; }
  .btn-primary:hover { background: transparent; color: var(--amber); box-shadow: 0 0 20px rgba(245,166,35,0.3); }
  .btn-ghost { background: transparent; color: var(--text); border: 2px solid var(--border); }
  .btn-ghost:hover { border-color: var(--amber); color: var(--amber); }
  .stat-bar {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    background: var(--surface);
  }
  .stat-item {
    flex: 1; min-width: 160px;
    padding: 24px 32px;
    border-right: 1px solid var(--border);
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease;
  }
  .stat-item:last-child { border-right: none; }
  .stat-item.visible { opacity: 1; transform: translateY(0); }
  .stat-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 42px;
    color: var(--amber);
    line-height: 1;
  }
  .stat-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 4px;
  }
  section { max-width: 1100px; margin: 0 auto; padding: 80px 24px; }
  .section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: var(--amber);
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(36px, 5vw, 56px);
    line-height: 1;
    margin-bottom: 40px;
  }
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2px;
    background: var(--border);
    border: 1px solid var(--border);
  }
  .feat-card {
    background: var(--surface);
    padding: 32px;
    position: relative;
    overflow: hidden;
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.5s ease;
  }
  .feat-card.visible { opacity: 1; transform: translateY(0); }
  .feat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 0;
    background: var(--amber);
    transition: height 0.4s ease;
  }
  .feat-card:hover::before { height: 100%; }
  .feat-card:hover { background: var(--surface2); }
  .feat-icon { font-size: 28px; margin-bottom: 16px; display: block; }
  .feat-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    color: var(--text);
    letter-spacing: 1px;
    margin-bottom: 8px;
  }
  .feat-desc { font-size: 14px; color: var(--muted); line-height: 1.7; }
  .feat-tag {
    display: inline-block;
    margin-top: 14px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    padding: 3px 8px;
    background: rgba(245,166,35,0.1);
    color: var(--amber);
    border-radius: 2px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .stack-row { display: flex; gap: 12px; flex-wrap: wrap; }
  .stack-pill {
    display: flex; align-items: center; gap: 8px;
    padding: 10px 20px;
    border: 1px solid var(--border);
    border-radius: 2px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    color: var(--text);
    background: var(--surface);
    opacity: 0;
    transform: scale(0.9);
    transition: all 0.4s ease;
  }
  .stack-pill.visible { opacity: 1; transform: scale(1); }
  .stack-pill:hover { border-color: var(--amber); color: var(--amber); }
  .stack-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .terminal {
    background: #0A0A0A;
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    font-family: 'Share Tech Mono', monospace;
    font-size: 14px;
    line-height: 1.8;
  }
  .terminal-bar {
    background: var(--surface2);
    padding: 10px 16px;
    display: flex; align-items: center; gap: 8px;
    border-bottom: 1px solid var(--border);
  }
  .dot { width: 10px; height: 10px; border-radius: 50%; }
  .dot-r { background: #FF5F56; }
  .dot-y { background: #FFBD2E; }
  .dot-g { background: #27C93F; }
  .terminal-title { font-size: 11px; color: var(--muted); margin-left: 8px; letter-spacing: 2px; text-transform: uppercase; }
  .terminal-body { padding: 24px; }
  .t-line { display: block; margin-bottom: 6px; opacity: 0; animation: fadeIn 0.3s ease forwards; }
  .t-line:nth-child(1) { animation-delay: 0.4s; }
  .t-line:nth-child(2) { animation-delay: 1.1s; }
  .t-line:nth-child(3) { animation-delay: 1.8s; }
  .t-line:nth-child(4) { animation-delay: 2.5s; }
  @keyframes fadeIn { to { opacity: 1; } }
  .prompt { color: var(--amber); }
  .cmd { color: #a8d8a8; }
  .comment { color: var(--muted); }
  .tree {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 28px 32px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    line-height: 2;
    color: var(--muted);
  }
  .tree .folder { color: var(--amber); }
  .tree .file { color: var(--text); }
  .tree .arrow { color: var(--border); }
  footer {
    border-top: 1px solid var(--border);
    background: var(--surface);
    padding: 40px 24px;
    text-align: center;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    letter-spacing: 2px;
  }
  footer a { color: var(--amber); text-decoration: none; }
  footer a:hover { text-decoration: underline; }
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
    margin: 0 24px;
    opacity: 0.3;
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  @keyframes blink {
    0%,100% { opacity: 1; }
    50%      { opacity: 0; }
  }
  .ticker-wrap {
    overflow: hidden;
    background: var(--amber);
    padding: 8px 0;
    white-space: nowrap;
  }
  .ticker {
    display: inline-block;
    animation: ticker 22s linear infinite;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: #000;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  @keyframes ticker {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
  }
</style>
</head>
<body>

<div class="road-strip"></div>

<!-- HERO -->
<div class="hero">
  <div class="gauge-ring"></div>
  <div class="truck-lane">
    <svg width="180" height="65" viewBox="0 0 180 65" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect x="55" y="20" width="105" height="32" rx="3" fill="#F5A623"/>
      <rect x="8" y="28" width="52" height="24" rx="3" fill="#F5A623"/>
      <rect x="13" y="33" width="20" height="13" rx="1" fill="#0D0D0D" opacity="0.6"/>
      <rect x="36" y="33" width="14" height="13" rx="1" fill="#0D0D0D" opacity="0.4"/>
      <circle cx="32" cy="58" r="8" fill="#222"/><circle cx="32" cy="58" r="3.5" fill="#666"/>
      <circle cx="120" cy="58" r="8" fill="#222"/><circle cx="120" cy="58" r="3.5" fill="#666"/>
      <circle cx="152" cy="58" r="8" fill="#222"/><circle cx="152" cy="58" r="3.5" fill="#666"/>
      <rect x="155" y="30" width="18" height="10" rx="1" fill="#FF6B2B" opacity="0.7"/>
    </svg>
  </div>

  <div class="badge-row">
    <span class="badge badge-live">🟢 Live App</span>
    <span class="badge badge-python">Python 3.10+</span>
    <span class="badge badge-stream">Streamlit</span>
  </div>
  <p class="hero-eyebrow">Fleet Intelligence Dashboard</p>
  <h1 class="hero-title">Diesel<span>Deck</span></h1>
  <p class="hero-sub">Fleet management built for the road, not the boardroom. Upload your Excel trip sheet and instantly see every truck, every cost, every rupee — intelligence at a glance.</p>
  <div class="hero-cta">
    <a href="https://gerryhpmd8gnoobk3lfzds.streamlit.app/" class="btn btn-primary" target="_blank">🚛 Launch Live App</a>
    <a href="#features" class="btn btn-ghost">Explore Features ↓</a>
  </div>
</div>

<!-- TICKER -->
<div class="ticker-wrap">
  <span class="ticker">🚛 LIVE TRUCK STATUS &nbsp;•&nbsp; ⛽ FUEL ANOMALY DETECTION &nbsp;•&nbsp; 📊 PER-KM COST BREAKDOWN &nbsp;•&nbsp; 🏆 DRIVER LEADERBOARD &nbsp;•&nbsp; 💬 WHATSAPP SUMMARY &nbsp;•&nbsp; 📋 DAILY ACTION LIST &nbsp;•&nbsp; ₹ PROFIT/LOSS PREVIEW &nbsp;•&nbsp; 🛣️ ROUTE PROGRESS TRACKER &nbsp;•&nbsp; 📂 EXCEL TRIP SHEET INPUT &nbsp;•&nbsp; 🚛 LIVE TRUCK STATUS &nbsp;•&nbsp; ⛽ FUEL ANOMALY DETECTION &nbsp;•&nbsp; 📊 PER-KM COST BREAKDOWN &nbsp;•&nbsp; 🏆 DRIVER LEADERBOARD &nbsp;•&nbsp; 💬 WHATSAPP SUMMARY &nbsp;•&nbsp; 📋 DAILY ACTION LIST &nbsp;•&nbsp; ₹ PROFIT/LOSS PREVIEW &nbsp;•&nbsp; 🛣️ ROUTE PROGRESS TRACKER &nbsp;•&nbsp; 📂 EXCEL TRIP SHEET INPUT &nbsp;•&nbsp;</span>
</div>

<!-- STATS -->
<div class="stat-bar">
  <div class="stat-item" data-delay="0">
    <div class="stat-num" id="s1">0</div>
    <div class="stat-label">% Excel Compatible</div>
  </div>
  <div class="stat-item" data-delay="120">
    <div class="stat-num" id="s2">0</div>
    <div class="stat-label">Core Modules</div>
  </div>
  <div class="stat-item" data-delay="240">
    <div class="stat-num" id="s3">₹0</div>
    <div class="stat-label">Fuel Theft Missed</div>
  </div>
  <div class="stat-item" data-delay="360">
    <div class="stat-num" id="s4">0</div>
    <div class="stat-label">Click WhatsApp Export</div>
  </div>
</div>

<!-- FEATURES -->
<section id="features">
  <p class="section-label">// What it does</p>
  <h2 class="section-title">Six Modules.<br>Zero Guesswork.</h2>
  <div class="features-grid">
    <div class="feat-card" data-delay="0">
      <span class="feat-icon">🛣️</span>
      <div class="feat-title">Live Truck Status Board</div>
      <p class="feat-desc">Real-time per-truck status with per-KM cost breakdown and route progress at a glance. Know exactly where every vehicle stands — always.</p>
      <span class="feat-tag">Live</span>
    </div>
    <div class="feat-card" data-delay="100">
      <span class="feat-icon">⛽</span>
      <div class="feat-title">Fuel Anomaly Detection</div>
      <p class="feat-desc">Automatically spots theft and wastage. Shows ₹ loss estimates so you can act before money disappears — not after the month ends.</p>
      <span class="feat-tag">Auto-detect</span>
    </div>
    <div class="feat-card" data-delay="200">
      <span class="feat-icon">🏆</span>
      <div class="feat-title">Driver Leaderboard</div>
      <p class="feat-desc">Rank every driver by efficiency and cost control. Reward the best, coach the rest — backed by data, not gut feeling.</p>
      <span class="feat-tag">Scoring</span>
    </div>
    <div class="feat-card" data-delay="300">
      <span class="feat-icon">📋</span>
      <div class="feat-title">Daily Action List</div>
      <p class="feat-desc">Auto-generated priority list every morning. One-click WhatsApp summary designed for Monday reports — fleet owners actually read it.</p>
      <span class="feat-tag">Automation</span>
    </div>
    <div class="feat-card" data-delay="400">
      <span class="feat-icon">📊</span>
      <div class="feat-title">Trip Profit/Loss Preview</div>
      <p class="feat-desc">Add or edit trips and see the live profit/loss impact before saving. Stop guessing on margins; confirm before committing.</p>
      <span class="feat-tag">Real-time</span>
    </div>
    <div class="feat-card" data-delay="500">
      <span class="feat-icon">📁</span>
      <div class="feat-title">Excel Trip Sheet Upload</div>
      <p class="feat-desc">Your existing Excel sheet is the input — drop it in and DieselDeck parses it instantly. No reformatting, no new tools to learn, no data entry from scratch.</p>
      <span class="feat-tag">Excel-powered</span>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- TECH STACK -->
<section>
  <p class="section-label">// Built with</p>
  <h2 class="section-title">Tech Stack</h2>
  <div class="stack-row">
    <div class="stack-pill" data-delay="0"><span class="stack-dot" style="background:#3776AB"></span>Python 3.10+</div>
    <div class="stack-pill" data-delay="80"><span class="stack-dot" style="background:#FF4B4B"></span>Streamlit</div>
    <div class="stack-pill" data-delay="160"><span class="stack-dot" style="background:#150458"></span>Pandas</div>
    <div class="stack-pill" data-delay="240"><span class="stack-dot" style="background:#4DABCF"></span>NumPy</div>
    <div class="stack-pill" data-delay="320"><span class="stack-dot" style="background:#3F4F75"></span>Plotly</div>
    <div class="stack-pill" data-delay="400"><span class="stack-dot" style="background:#1D6F42"></span>Excel / openpyxl</div>
    <div class="stack-pill" data-delay="480"><span class="stack-dot" style="background:#25D366"></span>WhatsApp Export</div>
  </div>
</section>

<div class="divider"></div>

<!-- INSTALL -->
<section>
  <p class="section-label">// Get running</p>
  <h2 class="section-title">Quick Start</h2>
  <div class="terminal">
    <div class="terminal-bar">
      <span class="dot dot-r"></span><span class="dot dot-y"></span><span class="dot dot-g"></span>
      <span class="terminal-title">bash — DieselDeck</span>
    </div>
    <div class="terminal-body">
      <span class="t-line"><span class="comment"># Clone the repository</span></span>
      <span class="t-line"><span class="prompt">$ </span><span class="cmd">git clone https://github.com/your-username/DieselDeck.git && cd DieselDeck</span></span>
      <span class="t-line"><span class="prompt">$ </span><span class="cmd">pip install -r requirements.txt</span></span>
      <span class="t-line"><span class="prompt">$ </span><span class="cmd">streamlit run app.py</span></span>
    </div>
  </div>
</section>

<!-- STRUCTURE -->
<section>
  <p class="section-label">// Project layout</p>
  <h2 class="section-title">Folder Structure</h2>
  <div class="tree">
    <div><span class="folder">DieselDeck/</span></div>
    <div><span class="arrow">├── </span><span class="folder">modules/</span></div>
    <div><span class="arrow">│&nbsp;&nbsp; ├── </span><span class="file">truck_status.py</span><span class="comment">&nbsp;&nbsp;&nbsp;# Live board + per-KM costs</span></div>
    <div><span class="arrow">│&nbsp;&nbsp; ├── </span><span class="file">fuel_anomaly.py</span><span class="comment">&nbsp;&nbsp;# Theft detection engine</span></div>
    <div><span class="arrow">│&nbsp;&nbsp; ├── </span><span class="file">driver_board.py</span><span class="comment">&nbsp;&nbsp;# Leaderboard scoring</span></div>
    <div><span class="arrow">│&nbsp;&nbsp; ├── </span><span class="file">action_list.py</span><span class="comment">&nbsp;&nbsp;&nbsp;# Daily priorities + WhatsApp</span></div>
    <div><span class="arrow">│&nbsp;&nbsp; └── </span><span class="file">trip_editor.py</span><span class="comment">&nbsp;&nbsp;&nbsp;# Add/edit with P&L preview</span></div>
    <div><span class="arrow">├── </span><span class="file">app.py</span><span class="comment">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Streamlit entry point</span></div>
    <div><span class="arrow">├── </span><span class="file">sample_trip_sheet.xlsx</span><span class="comment">&nbsp;# Example Excel input</span></div>
    <div><span class="arrow">├── </span><span class="file">requirements.txt</span></div>
    <div><span class="arrow">└── </span><span class="file">README.html</span></div>
  </div>
</section>

<div class="divider"></div>

<footer>
  <p style="font-size:22px;margin-bottom:12px;">🚛</p>
  <p>DIESELDECK &nbsp;•&nbsp; FLEET INTELLIGENCE FOR INDIAN TRUCK OWNERS</p>
  <p style="margin-top:10px;">
    <a href="https://gerryhpmd8gnoobk3lfzds.streamlit.app/" target="_blank">LIVE APP</a>
    &nbsp;|&nbsp; Built with Python &amp; Streamlit &nbsp;|&nbsp; Apache 2.0 License
  </p>
  <p style="margin-top:16px;opacity:0.35;font-size:10px;">EVERY RUPEE TRACKED. EVERY ROUTE OPTIMISED. EVERY DRIVER ACCOUNTABLE.</p>
</footer>

<script>
  // Intersection observer for scroll reveals
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const delay = parseInt(e.target.dataset.delay || 0);
      setTimeout(() => e.target.classList.add('visible'), delay);
      io.unobserve(e.target);
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.feat-card, .stat-item, .stack-pill').forEach(el => io.observe(el));

  // Animated counters
  const targets = [
    { id: 's1', target: 100, prefix: '', suffix: '%' },
    { id: 's2', target: 6,   prefix: '', suffix: '' },
    { id: 's3', target: 0,   prefix: '₹', suffix: '' },
    { id: 's4', target: 1,   prefix: '', suffix: '' },
  ];
  const countObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      countObs.unobserve(e.target);
      const idx = parseInt(e.target.dataset.idx);
      const { id, target, prefix, suffix } = targets[idx];
      const el = document.getElementById(id);
      let cur = 0;
      const step = Math.max(1, Math.ceil(target / 40));
      const t = setInterval(() => {
        cur = Math.min(cur + step, target);
        el.textContent = prefix + cur + suffix;
        if (cur >= target) clearInterval(t);
      }, 30);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.stat-item').forEach((el, i) => {
    el.dataset.idx = i;
    countObs.observe(el);
  });
</script>
</body>
</html>
