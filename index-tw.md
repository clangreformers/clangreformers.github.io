---
layout: default
ref: shugu
lang: 繁體中文
banvar: banner-tw.md
glossaryNpeople-banvar: glossaryNpeople-banner-tw.md
---

<div class="home-page">

  <div class="container">
    <h1 class="page-heading">述 故 / 循 跡 , 現 代 漢 語 的 蒂 基 者
</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner.png">
    </div>
{% include {{ page.glossaryNpeople-banvar }} %}
    <div class="searchbar">
      <div class="left">
        述 故 / 循 跡 , 現 代 漢 語 的 蒂 基 者
      </div>
      <div class="right">
        <div id="search-demo-container" class="search-demo-container">
          <input type="input" id="search-input" placeholder="Search...">
          <div class="icon"></div>
          <ul id="results-container" class="results-container"></ul>
        </div>
      </div>
    </div>

    <ul class="nav nav-tabs" id="mainTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="shugu-tab" data-bs-toggle="tab" data-bs-target="#shugu" type="button" role="tab" aria-controls="shugu" aria-selected="true">述古</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="shuowen-tab" data-bs-toggle="tab" data-bs-target="#shuowen" type="button" role="tab" aria-controls="shuowen" aria-selected="false">說文</button>
      </li>
    </ul>
    <div class="tab-content" id="mainTabContent">
      <div class="tab-pane fade show active" id="shugu" role="tabpanel" aria-labelledby="shugu-tab">
        <ul class="post-list">
          {% assign posts=site.posts | where:"lang", page.lang %}
          {% for post in posts %}
          <li>
            <h2>
              <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
            </h2>

            <span class="post-meta">{{ post.date | date: "%Y年%m月%d日" }}
              {% if post.author %} • {{ post.author }}{% endif %}
            </span>

            <a href="{{ post.url | prepend: site.baseurl }}" class="more">More</a>
          </li>
          {% endfor %}
        </ul>
      </div>
      <div class="tab-pane fade" id="shuowen" role="tabpanel" aria-labelledby="shuowen-tab">
        <div>
          <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link active" id="learning-tab" data-bs-toggle="tab" data-bs-target="#learning" type="button" role="tab" aria-controls="learning" aria-selected="true">國語學習園地</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="stories-tab" data-bs-toggle="tab" data-bs-target="#stories" type="button" role="tab" aria-controls="stories" aria-selected="false">字的故事</button>
            </li>
          </ul>
          <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="learning" role="tabpanel" aria-labelledby="learning-tab">
              <p>國語日報的網路版，訂閱頁面: <a href="https://mdnereading.mdnkids.com/subscription/%E5%9C%8B%E8%AA%9E%E6%97%A5%E5%A0%B1">https://mdnereading.mdnkids.com/subscription/國語日報</a></p>
              <p>精選試讀的頁面: <a href="https://mdnereading.mdnkids.com/product_intro/hard_copy_paper">https://mdnereading.mdnkids.com/product_intro/hard_copy_paper</a></p>
            </div>
            <div class="tab-pane fade" id="stories" role="tabpanel" aria-labelledby="stories-tab">
              <p>敬請期待...</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--
  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p> -->


{% include {{ page.banvar }} %}

  </div>
</div>

<script src="{{ site.baseurl }}/assets/js/simple-jekyll-search.js"></script>

<script>
  window.simpleJekyllSearch = new SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search-tw.json',
    searchResultTemplate: '<li><a href="{url}?query={query}" title="{desc}">{title}</a></li>',
    noResultsText: '<li>No results found.</li>',
    limit: 10,
    fuzzy: false,
    exclude: ['Welcome']
  })
</script>
