---
layout: default
ref: shugu
lang: English
sidebar: sidebar
banvar: banner.md
glossaryNpeople-banvar: glossaryNpeople-banner.md
---

<div class="home-page">
  <div class="container">
    <div id="bannerCarousel" class="carousel slide" data-bs-ride="false" data-bs-interval="false">

      <div class="carousel-inner">
        <div class="carousel-item active">
          <h1 class="page-heading">Events and historical figures of modern Chinese</h1>
          <div class="home-banner">
            <img src="/assets/images/banner.png" class="d-block w-100" alt="Shugu Banner">
          </div>
        </div>
        <div class="carousel-item">
          <h1 class="page-heading">Exposition/Exploring the bits and pieces of Chinese characters</h1>
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
          Events and historical figures of modern Chinese
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

            <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}
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
              <button class="nav-link active" id="learning-tab" data-bs-toggle="tab" data-bs-target="#learning" type="button" role="tab" aria-controls="learning" aria-selected="true">Learning Chinese</button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link" id="stories-tab" data-bs-toggle="tab" data-bs-target="#stories" type="button" role="tab" aria-controls="stories" aria-selected="false">Stories of Chinese Characters</button>
            </li>
          </ul>
          <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="learning" role="tabpanel" aria-labelledby="learning-tab">
              <p>Mandarin Daily News Online Edition, Subscription Page: <a href="https://mdnereading.mdnkids.com/subscription/%E5%9C%8B%E8%AA%9E%E6%97%A5%E5%A0%B1">https://mdnereading.mdnkids.com/subscription/國語日報</a></p>
              <p>Selected Trial Reading Page: <a href="https://mdnereading.mdnkids.com/product_intro/hard_copy_paper">https://mdnereading.mdnkids.com/product_intro/hard_copy_paper</a></p>
            </div>
            <div class="tab-pane fade" id="stories" role="tabpanel" aria-labelledby="stories-tab">
              <p>Coming soon...</p>
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
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '<li><a href="{url}?query={query}" title="{desc}">{title}</a></li>',
    noResultsText: '<li>No results found.</li>',
    limit: 10,
    fuzzy: false,
    exclude: ['Welcome']
  })
</script>

<script src="{{ site.baseurl }}/assets/js/index_slider.js"></script>
