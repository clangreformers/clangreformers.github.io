---
layout: page
title: National Language Movement Timeline
ref: timeline
lang: English
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
    font-family: Georgia, 'Times New Roman', 'Songti SC', serif;
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

.tl-item.left {
    margin-left: 0;
    text-align: right;
}

.tl-item.right {
    margin-left: 50%;
    text-align: left;
}

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
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--tl-accent);
    font-weight: 700;
    margin-bottom: 0.35rem;
    font-family: -apple-system, 'Helvetica Neue', sans-serif;
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

.tl-card ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.tl-card li {
    position: relative;
    padding-left: 1.1rem;
    margin-bottom: 0.7rem;
    line-height: 1.6;
    font-size: 0.97rem;
    color: var(--tl-ink);
}

.tl-card li:last-child { margin-bottom: 0; }

.tl-card li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.62rem;
    width: 5px;
    height: 5px;
    background: var(--tl-accent-soft);
    border-radius: 50%;
}

.year {
    display: inline-block;
    font-weight: 700;
    color: var(--tl-accent);
    font-family: -apple-system, 'Helvetica Neue', sans-serif;
    letter-spacing: 0.02em;
}

@media (max-width: 720px) {
    .tl-track::before {
        left: 18px;
    }
    .tl-item,
    .tl-item.left,
    .tl-item.right {
        width: 100%;
        margin-left: 0;
        padding: 0.6rem 0 0.6rem 2.5rem;
        text-align: left;
    }
    .tl-item.left::before,
    .tl-item.right::before {
        left: 10px;
        right: auto;
    }
    .tl-item.left .tl-card::before,
    .tl-item.right .tl-card::before {
        left: -10px;
        right: auto;
        border-width: 8px 10px 8px 0;
        border-color: transparent var(--tl-card-border) transparent transparent;
    }
    .tl-period { font-size: 1.05rem; }
}
</style>

<div class="tl-wrap">

<p class="tl-intro">Five eras in the modernization of the Chinese script — from late-Qing reformers to a unified phonetic standard.</p>

<div class="tl-track">

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">Era I · Late 19th c.</span>
      <div class="tl-period">Phonetic Spelling Movement</div>
      <ul>
        <li><span class="year">1892</span> — Lu Xizhang published <em>First Steps to Clarity at a Glance</em>, marking an important start for romanized phonetic schemes.</li>
        <li>Wei Xu's <em>Rapid Sound Transmission Characters</em>, Qi Baoqi's <em>Easy Character Method</em>, and Wang Zhao's <em>Pinyin Method</em> followed in close succession.</li>
        <li>The movement was civil and commercial in character, originating from the private sector.</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">Era II · 1900–1912</span>
      <div class="tl-period">Simplified Character Movement</div>
      <ul>
        <li><span class="year">1900</span> — Wang Zhao published <em>Mandarin Combined Phonetic Alphabet</em>, more developed than earlier cut-sound work, and began wide promotion.</li>
        <li>Phonetic teaching and Mandarin instruction flourished, still in a non-governmental capacity.</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">Era III · 1913–1928</span>
      <div class="tl-period">Zhuyin Alphabet Movement</div>
      <ul>
        <li><span class="year">1913</span> — The Ministry of Education convened the Pronunciation Unification Conference, fixing the standard pronunciation of 6,500 characters and creating today's Zhuyin symbols.</li>
        <li><span class="year">1916</span> — The Beiyang Government formally approved the National Alphabet; teaching and promotion began.</li>
        <li><span class="year">1918</span> — Zhuyin was officially promulgated nationwide; the National Language Dictionary was published.</li>
        <li><span class="year">1920</span> — The Chinese Character Commission was reorganized; schools began Zhuyin-based education.</li>
      </ul>
    </div>
  </div>

  <div class="tl-item right">
    <div class="tl-card">
      <span class="tl-era">Era IV · 1928–1949</span>
      <div class="tl-period">National Language Romanization</div>
      <ul>
        <li><span class="year">1928</span> — The National Academy promulgated the Official National Language Romanization, marking its formal use as an official pinyin tool.</li>
        <li><span class="year">1931</span> — The Soviet Academy of Sciences and the Chinese Language Reform Research Society issued a written standard.</li>
        <li><span class="year">1932</span> — The Ministry of Education announced the National Language Romanization (Pinyin Guoyu), establishing a unified system.</li>
        <li><span class="year">1940</span> — The four-tone edition of the National Language Dictionary was published as the everyday pinyin standard.</li>
      </ul>
    </div>
  </div>

  <div class="tl-item left">
    <div class="tl-card">
      <span class="tl-era">Era V · 1949–1960 · PRC</span>
      <div class="tl-period">Stage of Script Reform</div>
      <ul>
        <li><span class="year">1956</span> — The first pinyin scheme of the PRC was introduced, drawing the attention and cooperation of many linguists.</li>
        <li><span class="year">1958</span> — The Scheme for the Chinese Phonetic Alphabet (Hanyu Pinyin) was promulgated as the legal phonetic system for Chinese.</li>
        <li><span class="year">1960</span> — The Modern Chinese Dictionary was published, codifying character usage and laying the foundation for pinyin writing.</li>
      </ul>
    </div>
  </div>

</div>
</div>
