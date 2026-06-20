---
layout: page
title: 国语运动时间线
ref: timeline
lang: 简体中文
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
    font-family: 'Songti SC', 'STSong', Georgia, serif;
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
    font-family: -apple-system, 'PingFang SC', sans-serif;
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
    font-family: -apple-system, 'PingFang SC', sans-serif;
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

<p class="tl-intro">汉语文字现代化的五个阶段——从清末改良者到统一的拼音方案。</p>

<div class="tl-track">

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第一阶段 · 十九世纪末</span>
      <div class="tl-period">切音运动</div>
      <ul>
        <li><span class="year">1892年</span>，卢戆章出版《一目了然初阶》，为罗马字注音方案的重要开端。</li>
        <li>同时，魏旭等人的《传音快字》、齐宝琦的《易字法》、王照等人的《拼音法》相继问世。</li>
        <li>这一时期的注音运动带有民商性质，源于民间。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">第二阶段 · 1900–1912</span>
      <div class="tl-period">简字运动</div>
      <ul>
        <li><span class="year">1900年</span>，王照出版《官话合声字母》，比此前切音运动更为成熟，开始有了广泛的宣传与推广。</li>
        <li>此外，注音教学及官话教学也大行其道，仍属民间性质。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第三阶段 · 1913–1928</span>
      <div class="tl-period">注音字母运动时期</div>
      <ul>
        <li><span class="year">1913年</span>，中华民国教育部召开"读音统一会"，确定6500字的标准音，并制定现行的注音符号。</li>
        <li><span class="year">1916年</span>，北洋政府正式确定"国定字母"，教学推广工作开始。</li>
        <li><span class="year">1918年</span>，注音字母正式颁行天下，《国语字典》出版。</li>
        <li><span class="year">1920年</span>，教育部改组汉字委员会，学校开始推行注音教学。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">第四阶段 · 1928–1949</span>
      <div class="tl-period">国语罗马字运动阶段</div>
      <ul>
        <li><span class="year">1928年</span>，"中国大学院"颁布《国语罗马字》，作为正式拼音工具自此开始。</li>
        <li><span class="year">1931年</span>，苏联科学院东方研究所与中国文字改革研究会颁布书面标准。</li>
        <li><span class="year">1932年</span>，中华民国教育部公告《国语罗马字》（拼音国语），确定罗马拼音符号的统一制度。</li>
        <li><span class="year">1940年</span>，《国语辞典》（四声版）正式出版，成为日用国语与汉语标准的拼音依据。</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">第五阶段 · 1949–1960 · 中华人民共和国</span>
      <div class="tl-period">文字改革阶段</div>
      <ul>
        <li><span class="year">1956年</span>，中华人民共和国推出第一套拼音方案，吸引大批文字学者关注与协作。</li>
        <li><span class="year">1958年</span>，《中华人民共和国汉语拼音方案》正式颁布，成为法定的汉语注音方案。</li>
        <li><span class="year">1960年</span>，《现代汉语词典》出版，确立汉字规范，为拼音文字的推广奠定基础。</li>
      </ul>
    </div>
  </div>

</div>
</div>
