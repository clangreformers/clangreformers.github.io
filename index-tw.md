---
layout: default
ref: index
lang: 繁體中文
banvar: banner-tw.md
---

<div class="home-page">

  <div class="container">
    <h1 class="page-heading">述 故 / 循 跡 , 現 代 漢 語 的 蒂 基 者
</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner.png">

    </div>
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