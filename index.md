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
    <h1 class="page-heading">Events and historical figures of modern Chinese</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner.png">
    </div>

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
    <ul class="nav nav-tabs" id="mainTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="shugu-tab" data-bs-toggle="tab" data-bs-target="#shugu" type="button" role="tab" aria-controls="shugu" aria-selected="true">Shugu</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="shuowen-tab" data-bs-toggle="tab" data-bs-target="#shuowen" type="button" role="tab" aria-controls="shuowen" aria-selected="false">Shuowen</button>
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

            <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}
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
