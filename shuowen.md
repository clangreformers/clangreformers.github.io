---
layout: default
ref: shuowen
lang: English
sidebar: sidebar
banvar: banner.md
---

<div class="home-page">
  <div class="container">
    <h1 class="page-heading">Exposition/Exploring the bits and pieces of Chinese characters</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner1.png">

    </div>
    <div class="searchbar">
      <div class="left">
        Exposition/Exploring the bits and pieces of Chinese characters 
      </div>
      <div class="right">
        <div id="search-demo-container" class="search-demo-container">
          <input type="input" id="search-input" placeholder="Search...">
          <div class="icon"></div>
          <ul id="results-container" class="results-container"></ul>
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
