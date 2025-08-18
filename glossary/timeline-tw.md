---
layout: page
title: 國語運動時間線
ref: timeline
lang: 繁體中文
---

<style>
body {
    font-family: 'Microsoft YaHei', SimSun, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f8f9fa;
    line-height: 1.6;
}

.timeline-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.timeline-title {
    text-align: center;
    font-size: 2.5em;
    color: #2c3e50;
    margin-bottom: 40px;
    font-weight: bold;
}

.timeline-flow {
    display: flex;
    flex-direction: column;
    gap: 30px;
    padding: 20px 0;
}

.timeline-box {
    background: linear-gradient(135deg, #4a90e2, #357abd);
    color: white;
    padding: 25px;
    border-radius: 15px;
    width: 100%;
    max-width: none;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.timeline-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 35px rgba(0,0,0,0.2);
}

.period-title {
    font-size: 1.3em;
    font-weight: bold;
    text-align: left;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid rgba(255,255,255,0.3);
}

.timeline-box ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.timeline-box li {
    margin-bottom: 15px;
    font-size: 1em;
    line-height: 1.5;
    position: relative;
    padding-left: 20px;
}

.timeline-box li:before {
    content: "•";
    color: #ffd700;
    font-weight: bold;
    position: absolute;
    left: 0;
    font-size: 1.2em;
}

.year {
    font-weight: bold;
    color: #ffd700;
}

.arrow {
    position: absolute;
    bottom: -20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2em;
    color: #4a90e2;
    z-index: 10;
}

.timeline-box:last-child .arrow {
    display: none;
}

@media (max-width: 768px) {
    .timeline-box {
        padding: 20px;
    }
    
    .period-title {
        font-size: 1.1em;
    }
    
    .timeline-box li {
        font-size: 0.9em;
        padding-left: 15px;
    }
}

.jekyll-frontmatter {
    background: #2c3e50;
    color: #ecf0f1;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    white-space: pre-line;
}
</style>

<div class="timeline-flow">
    <div class="timeline-box">
        <div class="period-title">切音運動 (十九世紀末)</div>
        <ul>
            <li><span class="year">1892年</span>，盧戲章出版《一目了然初階》（什麽是切音字？），為羅馬字注音方案的重要開始。</li>
            <li>同時，魏旭等人的《傳音快字》、齊寶琦的《易字法》、王照等人提出的工況繁拼《拼音法》的有感媒助的官音方案。</li>
            <li>這一時期的官音運動帶有民商性質，民間的。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">簡字運動 (1900-1912)</div>
        <ul>
            <li><span class="year">1900年</span>，王照出版《官話合聲字母》，比先前切音運動較成熟，開始有了廣泛的宣傳和推廣；</li>
            <li>另外，注音教學及官話教學也大行其道，仍屬民間性質方式。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">注音字母運動時期 (1913-1928)</div>
        <ul>
            <li><span class="year">1913年</span>，中華民國教育部召開了"讀音統一會"，決定6500個字的標准音，並制定現在的注音符號。</li>
            <li><span class="year">1916年</span>，北洋政府會議正式確定"國定字母"教學推廣工作開始。</li>
            <li><span class="year">1918年</span>，發布由注音字母規定正式規天下，《國語字典》出版。</li>
            <li><span class="year">1920年</span>，教育部頒會改組漢字委員會，學校開始推行注音文教。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">國語羅馬字運動階段 (1928-1949)</div>
        <ul>
            <li><span class="year">1928年</span>，"中國大學院"頒布"中正式國語羅馬字"，作為正式拼音工具自此開始。</li>
            <li><span class="year">1932年</span>，中華民國教育部公告《國語羅馬字》（拼音國語），作定羅馬拼音符號的統制度。</li>
            <li><span class="year">1931年</span>，蘇聯科學院東方研究所和中國文字改革研究會的書面標准。</li>
            <li><span class="year">1940年</span>，《國語辭典》（四聲版）正式出版，成為日用國語習中國語言標准的拼音。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">文字改革化階段<br>(中華人民共和國)<br>(1949-1960)</div>
        <ul>
            <li><span class="year">1956年</span>，中華人民共和國成立60年來的第一段拼音方案，吸引大批文字學者的注意協作合作。</li>
            <li><span class="year">1958年</span>，中華人民共和國頒布"中華人民共和國漢語拼音方案"，稱為拼音符號，成為法定的漢語注音方案。</li>
            <li><span class="year">1960年</span>，《現代漢語詞典》出版，確定漢語用字規範，為拼音文字的推廣奠定基礎。</li>
        </ul>
    </div>
</div>
