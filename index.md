---
layout: default
ref: index
lang: English
sidebar: sidebar
---

<div class="home-page">

  <div class="container">
    <h1 class="page-heading">Events and historical figures of modern Chinese</h1>
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
              <p>History <br>of <br>Chinese <br>Dictionaries</p>
            </div>
            <div class="right">
              <p>
                (Tuwen Xue Xue, (Shen Ya), "Dian Nian Messengers Delegate Tongfu Dialects of the Early Kingdom" (tube
                name
                "Fangtuo"), (Tax Name", Shu hire", (Yuken", (Kang Zhaozi)
                "Sounds", "Ciyuan", (Cihai", "Xinping Xuedian", (Modern Tatong Dictionary), "Chinese Dictionary",
                "Modern
                Jifeng Reverse Preface Sidian", (Modern Hetong Shuang
                Preface Cannon Dictionary, Tong You Zhou Shu Dian, Anti-You Zhou Bi Dian, Zhi Feng Da Dictionary, Modern
                Ji


              </p>
            </div>
          </div>
        </div>
        <div class="col-lg-6 col-md-12 col-12">
          <div class="bottom-box">
            <div class="left">
              <p>History <br>figures</p>
            </div>
            <div class="right">
              <div class="right-scroll">


                <p>
                  (Tuwen Xue Xue, (Shen Ya), "Dian Nian Messengers Delegate Tongfu Dialects of the Early Kingdom" (tube
                  name
                  "Fangtuo"), (Tax Name", Shu hire", (Yuken", (Kang Zhaozi)
                  "Sounds", "Ciyuan", (Cihai", "Xinping Xuedian", (Modern Tatong Dictionary), "Chinese Dictionary",
                  "Modern
                  Jifeng Reverse Preface Sidian", (Modern Hetong Shuang
                  Preface Cannon Dictionary, Tong You Zhou Shu Dian, Anti-You Zhou Bi Dian, Zhi Feng Da Dictionary,
                  Modern
                  Ji
                  (Tuwen Xue Xue, (Shen Ya), "Dian Nian Messengers Delegate Tongfu Dialects of the Early Kingdom" (tube
                  name
                  "Fangtuo"), (Tax Name", Shu hire", (Yuken", (Kang Zhaozi)
                  "Sounds", "Ciyuan", (Cihai", "Xinping Xuedian", (Modern Tatong Dictionary), "Chinese Dictionary",
                  "Modern
                  Jifeng Reverse Preface Sidian", (Modern Hetong Shuang
                  Preface Cannon Dictionary, Tong You Zhou Shu Dian, Anti-You Zhou Bi Dian, Zhi Feng Da Dictionary,
                  Modern
                  Ji


                </p>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
</div>