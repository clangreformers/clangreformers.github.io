---
layout: default
ref: shugu
lang: 繁體中文
banvar: banner-tw.md
glossaryNpeople-banvar: glossaryNpeople-banner-tw.md
---

<div class="home-page">

  <div class="container">
    
    <div id="bannerCarousel" class="carousel slide" data-bs-ride="false" data-bs-interval="false">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <h1 class="page-heading">述 故 / 循 跡 , 現 代 漢 語 的 蒂 基 者</h1>
          <div class="home-banner">
            <img src="/assets/images/banner.png" class="d-block w-100" alt="Shugu Banner">
          </div>
        </div>
        <div class="carousel-item">
          <h1 class="page-heading">說 文 / 探 索 漢 字 的 點 滴</h1>
          <div class="home-banner">
            <img src="/assets/images/banner1.png" class="d-block w-100" alt="Shuowen Banner">
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#bannerCarousel" data-bs-slide="prev" style="width: 5%; justify-content: flex-start;">
        <span class="carousel-control-prev-icon" aria-hidden="true" style="background-color: black; border-radius: 50%;"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#bannerCarousel" data-bs-slide="next" style="width: 5%; justify-content: flex-end;">
         <span class="carousel-control-next-icon" aria-hidden="true" style="background-color: black; border-radius: 50%;"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>


    <!-- Content Sections controlled by Carousel -->
    <div id="content-shugu" class="content-section">
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
    <div id="content-shuowen" class="content-section" style="display: none;">

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

<script src="{{ site.baseurl }}/assets/js/index_slider.js"></script>
