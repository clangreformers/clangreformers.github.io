---
layout: default
ref: index
lang: 繁體中文
---

<div class="home-page">

  <div class="container">
    <h1 class="page-heading">文章</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner.png">

    </div>
    <ul class="post-list">
      {% assign posts=site.posts | where:"lang", page.lang %}
      {% for post in posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>

        <a href="{{ post.url | prepend: site.baseurl }}" class="more">More</a>
      </li>
      {% endfor %}
    </ul>
    <!--
  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p> -->


    <div class="bottom">
      <div class="row">
        <div class="col-lg-6 col-md-12 col-12">
          <div class="bottom-box">
            <div class="left">
              <p>中 <br>晓 <br>十 <br>奥<br>史</p>
            </div>
            <div class="right">
              <p>
                ( 途 文 解 学 》、( 神 雅 》、《 頼 年 使 者 委 代 通 輻 初 国 方 言 》 ( 筒 称 《 方 託 )) 、 ( 税 名 》 、 艸 雇 》 、 ( 玉 肯 》、( 康 照 字
                奏 》、《 辞 源 》、( 辞 海 》 、《 新 平 学 典 》、( 現 代 沓 通 辺 典 》、《 中 文 大 辞 典 》、《 現 代 汲 逢 反 序 司 典 》、( 現 代 河 通 双
                序 大 砲 典 》、《 同 又 週 述 典 》、《 反 又 週 彼 典 》、《 治 逢 大 字 典 、《 現 代 汲 逢 方 目 大 述 典 》、《 況 通 方 目 大 司 典 、
                ( 吉 汲 途 常 用 学 字 典 》、《 向 治 逢 学 典 》、《 吉 代 汲 逢 汁 典 》、《 古 汲 通 大 砲 典 》、( 向 況 逢 知 返 律 解 典 》
                《 说 文 解 字 》、《 尔 雅 》、《 辅 轩 使 者 绝 代 语 释 别 国 方 言 》( 简 称 ( 方 言 》) 、《 释 名 )、《 广 雅 》、《 玉 篓 》、《 康 熊 字
                、《 古 汉 语 字 词 典 》、《 古 代 汉 语 词 典 》、《 古 汉 语

              </p>
            </div>
          </div>
        </div>
        <div class="col-lg-6 col-md-12 col-12">
          <div class="bottom-box">
            <div class="left">
              <p>人

                <br>物 <br>表
              </p>
            </div>
            <div class="right">
              <div class="right-scroll">
                <p>
                  ( 途 文 解 学 》、( 神 雅 》、《 頼 年 使 者 委 代 通 輻 初 国 方 言 》 ( 筒 称 《 方 託 )) 、 ( 税 名 》 、 艸 雇 》 、 ( 玉 肯 》、( 康 照 字
                  奏 》、《 辞 源 》、( 辞 海 》 、《 新 平 学 典 》、( 現 代 沓 通 辺 典 》、《 中 文 大 辞 典 》、《 現 代 汲 逢 反 序 司 典 》、( 現 代 河 通 双
                  序 大 砲 典 》、《 同 又 週 述 典 》、《 反 又 週 彼 典 》、《 治 逢 大 字 典 、《 現 代 汲 逢 方 目 大 述 典 》、《 況 通 方 目 大 司 典 、
                  ( 吉 汲 途 常 用 学 字 典 》、《 向 治 逢 学 典 》、《 吉 代 汲 逢 汁 典 》、《 古 汲 通 大 砲 典 》、( 向 況 逢 知 返 律 解 典 》
                  《 说 文 解 字 》、《 尔 雅 》、《 辅 轩 使 者 绝 代 语 释 别 国 方 言 》( 简 称 ( 方 言 》) 、《 释 名 )、《 广 雅 》、《 玉 篓 》、《 康 熊 字
                  典 》 《 辞 源 》、《 辞 海 》、《 新 华 字 典 》、《 现 代 汉 语 词 典 》、《 中 文 大 辞 奎 )、《 现 代 汉 语 反 序 词 典 》、《 现 代 汉 语 双
                  序 大 词 典 》、《 同 义 词 词 典 》、《 反 义 词 词 典 》、《 汉 语 大 字 典 》、《 现 代 汉 语 方 言 大 词 典 )、《 汉 语 方 言 大 词 典 》 、
                  《 古 汉 语 常 用 字 字 典 》 、《 古 汉 语 字 词 典 》、《 古 代 汉 语 词 典 》、《 古 汉 语 大 词 典 》、《 古 汉 语 知 识 详 解 词 奎 》
                  ( 途 文 解 学 》、( 神 雅 》、《 頼 年 使 者 委 代 通 輻 初 国 方 言 》 ( 筒 称 《 方 託 )) 、 ( 税 名 》 、 艸 雇 》 、 ( 玉 肯 》、( 康 照 字
                  奏 》、《 辞 源 》、( 辞 海 》 、《 新 平 学 典 》、( 現 代 沓 通 辺 典 》、《 中 文 大 辞 典 》、《 現 代 汲 逢 反 序 司 典 》、( 現 代 河 通 双
                  序 大 砲 典 》、《 同 又 週 述 典 》、《 反 又 週 彼 典 》、《 治 逢 大 字 典 、《 現 代 汲 逢 方 目 大 述 典 》、《 況 通 方 目 大 司 典 、
                  ( 吉 汲 途 常 用 学 字 典 》、《 向 治 逢 学 典 》、《 吉 代 汲 逢 汁 典 》、《 古 汲 通 大 砲 典 》、( 向 況 逢 知 返 律 解 典 》
                  《 说 文 解 字 》、《 尔 雅 》、《 辅 轩 使 者 绝 代 语 释 别 国 方 言 》( 简 称 ( 方 言 》) 、《 释 名 )、《 广 雅 》、《 玉 篓 》、《 康 熊 字
                  典 》 《 辞 源 》、《 辞 海 》、《 新 华 字 典 》、《 现 代 汉 语 词 典 》、《 中 文 大 辞 奎 )、《 现 代 汉 语 反 序 词 典 》、《 现 代 汉 语 双
                  序 大 词 典 》、《 同 义 词 词 典 》、《 反 义 词 词 典 》、《 汉 语 大 字 典 》、《 现 代 汉 语 方 言 大 词 典 )、《 汉 语 方 言 大 词 典 》 、
                  《 古 汉 语 常 用 字 字 典 》 、《 古 汉 语 字 词 典 》、《 古 代 汉 语 词 典 》、《 古 汉 语 大 词 典 》、《 古 汉 语 知 识 详 解 词 奎 》

                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>