---
layout: default
title: 国语运动时间线
ref: timeline
lang: 简体中文
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

</style>

<div class="timeline-flow">
    <div class="timeline-box">
        <div class="period-title">切音运动 (十九世纪末)</div>
        <ul>
            <li><span class="year">1892年</span>，卢戏章出版《一目了然初阶》（什么是切音字？），为罗马字注音方案的重要开始。</li>
            <li>同时，魏旭等人的《传音快字》、齐宝琦的《易字法》、王照等人提出的工况繁拼《拼音法》的有感媒助的官音方案。</li>
            <li>这一时期的官音运动带有民商性质，民间的。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">简字运动 (1900-1912)</div>
        <ul>
            <li><span class="year">1900年</span>，王照出版《官话合声字母》，比先前切音运动较成熟，开始有了广泛的宣传和推广；</li>
            <li>另外，注音教学及官话教学也大行其道，仍属民间性质方式。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">注音字母运动时期 (1913-1928)</div>
        <ul>
            <li><span class="year">1913年</span>，中华民国教育部召开了"读音统一会"，决定6500个字的标准音，并制定现在的注音符号。</li>
            <li><span class="year">1916年</span>，北洋政府会议正式确定"国定字母"教学推广工作开始。</li>
            <li><span class="year">1918年</span>，发布由注音字母规定正式规天下，《国语字典》出版。</li>
            <li><span class="year">1920年</span>，教育部颁会改组汉字委员会，学校开始推行注音文教。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">国语罗马字运动阶段 (1928-1949)</div>
        <ul>
            <li><span class="year">1928年</span>，"中国大学院"颁布"中正式国语罗马字"，作为正式拼音工具自此开始。</li>
            <li><span class="year">1932年</span>，中华民国教育部公告《国语罗马字》（拼音国语），作定罗马拼音符号的统制度。</li>
            <li><span class="year">1931年</span>，苏联科学院东方研究所和中国文字改革研究会的书面标准。</li>
            <li><span class="year">1940年</span>，《国语辞典》（四声版）正式出版，成为日用国语习中国语言标准的拼音。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">文字改革化阶段<br>(中华人民共和国)<br>(1949-1960)</div>
        <ul>
            <li><span class="year">1956年</span>，中华人民共和国成立60年来的第一段拼音方案，吸引大批文字学者的注意协作合作。</li>
            <li><span class="year">1958年</span>，中华人民共和国颁布"中华人民共和国汉语拼音方案"，称为拼音符号，成为法定的汉语注音方案。</li>
            <li><span class="year">1960年</span>，《现代汉语词典》出版，确定汉语用字规范，为拼音文字的推广奠定基础。</li>
        </ul>
    </div>
</div>



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

</style>

<div class="timeline-flow">
    <div class="timeline-box">
        <div class="period-title">切音运动 (十九世纪末)</div>
        <ul>
            <li><span class="year">1892年</span>，卢戏章出版《一目了然初阶》（什么是切音字？），为罗马字注音方案的重要开始。</li>
            <li>同时，魏旭等人的《传音快字》、齐宝琦的《易字法》、王照等人提出的工况繁拼《拼音法》的有感媒助的官音方案。</li>
            <li>这一时期的官音运动带有民商性质，民间的。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">简字运动 (1900-1912)</div>
        <ul>
            <li><span class="year">1900年</span>，王照出版《官话合声字母》，比先前切音运动较成熟，开始有了广泛的宣传和推广；</li>
            <li>另外，注音教学及官话教学也大行其道，仍属民间性质方式。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">注音字母运动时期 (1913-1928)</div>
        <ul>
            <li><span class="year">1913年</span>，中华民国教育部召开了"读音统一会"，决定6500个字的标准音，并制定现在的注音符号。</li>
            <li><span class="year">1916年</span>，北洋政府会议正式确定"国定字母"教学推广工作开始。</li>
            <li><span class="year">1918年</span>，发布由注音字母规定正式规天下，《国语字典》出版。</li>
            <li><span class="year">1920年</span>，教育部颁会改组汉字委员会，学校开始推行注音文教。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">国语罗马字运动阶段 (1928-1949)</div>
        <ul>
            <li><span class="year">1928年</span>，"中国大学院"颁布"中正式国语罗马字"，作为正式拼音工具自此开始。</li>
            <li><span class="year">1932年</span>，中华民国教育部公告《国语罗马字》（拼音国语），作定罗马拼音符号的统制度。</li>
            <li><span class="year">1931年</span>，苏联科学院东方研究所和中国文字改革研究会的书面标准。</li>
            <li><span class="year">1940年</span>，《国语辞典》（四声版）正式出版，成为日用国语习中国语言标准的拼音。</li>
        </ul>
        <div class="arrow">↓</div>
    </div>
    
    <div class="timeline-box">
        <div class="period-title">文字改革化阶段<br>(中华人民共和国)<br>(1949-1960)</div>
        <ul>
            <li><span class="year">1956年</span>，中华人民共和国成立60年来的第一段拼音方案，吸引大批文字学者的注意协作合作。</li>
            <li><span class="year">1958年</span>，中华人民共和国颁布"中华人民共和国汉语拼音方案"，称为拼音符号，成为法定的汉语注音方案。</li>
            <li><span class="year">1960年</span>，《现代汉语词典》出版，确定汉语用字规范，为拼音文字的推广奠定基础。</li>
        </ul>
    </div>
</div>


