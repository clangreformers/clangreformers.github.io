---
layout: page
title: 國語運動時間線
ref: timeline
lang: 繁體中文
---

<style>
.tl-wrap {
    --tl-accent: #b8860b;
    --tl-accent-soft: #d4af37;
    --tl-ink: #2c2418;
    --tl-muted: #6b5d4f;
    --tl-spine: #d9cfbf;
    --tl-card: #fffdf8;
    --tl-card-border: #e8dfcc;
    max-width: 980px;
    margin: 0 auto;
    padding: 1rem 1rem 3rem;
    color: var(--tl-ink);
    font-family: 'Songti TC', 'Songti SC', 'STSong', Georgia, serif;
}

.tl-intro {
    text-align: center;
    color: var(--tl-muted);
    font-style: italic;
    margin-bottom: 3rem;
    font-size: 1.05rem;
}

.tl-track {
    position: relative;
    padding: 1rem 0;
}

.tl-track::before {
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    width: 2px;
    background: linear-gradient(to bottom,
        transparent 0,
        var(--tl-spine) 40px,
        var(--tl-spine) calc(100% - 40px),
        transparent 100%);
    transform: translateX(-50%);
}

.tl-item {
    position: relative;
    width: 50%;
    padding: 1rem 2.5rem;
    box-sizing: border-box;
}

.tl-item.left { margin-left: 0; text-align: right; }
.tl-item.right { margin-left: 50%; text-align: left; }

.tl-item::before {
    content: "";
    position: absolute;
    top: 2.2rem;
    width: 16px;
    height: 16px;
    background: var(--tl-card);
    border: 3px solid var(--tl-accent);
    border-radius: 50%;
    z-index: 2;
    box-shadow: 0 0 0 4px var(--tl-card);
}

.tl-item.left::before { right: -8px; }
.tl-item.right::before { left: -8px; }

.tl-card {
    background: var(--tl-card);
    border: 1px solid var(--tl-card-border);
    border-radius: 6px;
    padding: 1.25rem 1.5rem 1.4rem;
    box-shadow: 0 2px 8px rgba(40, 30, 15, 0.05);
    text-align: left;
    position: relative;
}

.tl-card::before {
    content: "";
    position: absolute;
    top: 1.5rem;
    width: 0;
    height: 0;
    border-style: solid;
}

.tl-item.left .tl-card::before {
    right: -10px;
    border-width: 8px 0 8px 10px;
    border-color: transparent transparent transparent var(--tl-card-border);
}

.tl-item.right .tl-card::before {
    left: -10px;
    border-width: 8px 10px 8px 0;
    border-color: transparent var(--tl-card-border) transparent transparent;
}

.tl-era {
    display: inline-block;
    font-size: 0.78rem;
    letter-spacing: 0.15em;
    color: var(--tl-accent);
    font-weight: 700;
    margin-bottom: 0.35rem;
    font-family: -apple-system, 'PingFang TC', sans-serif;
}

.tl-period {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--tl-ink);
    line-height: 1.3;
    margin-bottom: 0.9rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--tl-card-border);
}

.tl-card ul { list-style: none; padding: 0; margin: 0; }

.tl-card li {
    position: relative;
    padding-left: 1.1rem;
    margin-bottom: 0.7rem;
    line-height: 1.7;
    font-size: 0.97rem;
    color: var(--tl-ink);
}

.tl-card li:last-child { margin-bottom: 0; }

.tl-card li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.7rem;
    width: 5px;
    height: 5px;
    background: var(--tl-accent-soft);
    border-radius: 50%;
}

.year {
    display: inline-block;
    font-weight: 700;
    color: var(--tl-accent);
    font-family: -apple-system, 'PingFang TC', sans-serif;
}

@media (max-width: 720px) {
    .tl-track::before { left: 18px; }
    .tl-item, .tl-item.left, .tl-item.right {
        width: 100%;
        margin-left: 0;
        padding: 0.6rem 0 0.6rem 2.5rem;
        text-align: left;
    }
    .tl-item.left::before, .tl-item.right::before {
        left: 10px; right: auto;
    }
    .tl-item.left .tl-card::before, .tl-item.right .tl-card::before {
        left: -10px; right: auto;
        border-width: 8px 10px 8px 0;
        border-color: transparent var(--tl-card-border) transparent transparent;
    }
    .tl-period { font-size: 1.05rem; }
}
</style>

<div class="tl-wrap">

<p class="tl-intro">漢語文字現代化的五個階段——從清末改良者到統一的拼音方案。</p>

<div class="tl-track">

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第一階段 · 十九世紀末</span>
      <div class="tl-period">切音運動</div>
      <ul>
        <li><span class="year">1892年</span>，盧戇章出版《一目了然初階》，為羅馬字注音方案的重要開端。</li>
        <li>同時，魏旭等人的《傳音快字》、齊寶琦的《易字法》、王照等人的《拼音法》相繼問世。</li>
        <li>這一時期的注音運動帶有民商性質，源於民間。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">第二階段 · 1900–1912</span>
      <div class="tl-period">簡字運動</div>
      <ul>
        <li><span class="year">1900年</span>，王照出版《官話合聲字母》，比此前切音運動更為成熟，開始有了廣泛的宣傳與推廣。</li>
        <li>此外，注音教學及官話教學也大行其道，仍屬民間性質。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第三階段 · 1913–1928</span>
      <div class="tl-period">注音字母運動時期</div>
      <ul>
        <li><span class="year">1913年</span>，中華民國教育部召開「讀音統一會」，確定6500字的標準音，並制定現行的注音符號。</li>
        <li><span class="year">1916年</span>，北洋政府正式確定「國定字母」，教學推廣工作開始。</li>
        <li><span class="year">1918年</span>，注音字母正式頒行天下，《國語字典》出版。</li>
        <li><span class="year">1920年</span>，教育部改組漢字委員會，學校開始推行注音教學。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">第四階段 · 1928–1949</span>
      <div class="tl-period">國語羅馬字運動階段</div>
      <ul>
        <li><span class="year">1928年</span>，「中國大學院」頒布《國語羅馬字》，作為正式拼音工具自此開始。</li>
        <li><span class="year">1931年</span>，蘇聯科學院東方研究所與中國文字改革研究會頒布書面標準。</li>
        <li><span class="year">1932年</span>，中華民國教育部公告《國語羅馬字》（拼音國語），確定羅馬拼音符號的統一制度。</li>
        <li><span class="year">1940年</span>，《國語辭典》（四聲版）正式出版，成為日用國語與漢語標準的拼音依據。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第五階段 · 1949–1960 · 中華人民共和國</span>
      <div class="tl-period">文字改革階段</div>
      <ul>
        <li><span class="year">1956年</span>，中華人民共和國推出第一套拼音方案，吸引大批文字學者關注與協作。</li>
        <li><span class="year">1958年</span>，《中華人民共和國漢語拼音方案》正式頒布，成為法定的漢語注音方案。</li>
        <li><span class="year">1960年</span>，《現代漢語詞典》出版，確立漢字規範，為拼音文字的推廣奠定基礎。</li>
      </ul>
    </div>
  </div>

</div>
</div>
