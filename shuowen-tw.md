---
layout: default
ref: shuowen
lang: 繁體中文
banvar: banner-tw.md
---

<div class="home-page">
  <div class="container">
    <h1 class="page-heading">說文 / 探索中國文字的點點滴滴</h1>
    <div class="home-banner">
      <img alt="" src="/assets/images/banner1.png">

    </div>
    <div>
      <ul class="nav nav-tabs" id="myTab" role="tablist">
        <li class="nav-item" role="presentation">
          <button class="nav-link active" id="stories-tab" data-bs-toggle="tab" data-bs-target="#stories" type="button" role="tab" aria-controls="stories" aria-selected="true">字的故事</button>
        </li>
        <li class="nav-item" role="presentation">
          <button class="nav-link" id="learning-tab" data-bs-toggle="tab" data-bs-target="#learning" type="button" role="tab" aria-controls="learning" aria-selected="false">國語學習園地</button>
        </li>
      </ul>
      <div class="tab-content" id="myTabContent">
        <div class="tab-pane fade show active" id="stories" role="tabpanel" aria-labelledby="stories-tab">
          <div style="margin-top: 20px;">
            <ul class="nav nav-pills mb-3" id="storiesSubTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="random-subtab" data-bs-toggle="pill" data-bs-target="#random-content" type="button" role="tab" aria-controls="random-content" aria-selected="true">每日一字</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="list-subtab" data-bs-toggle="pill" data-bs-target="#list-content" type="button" role="tab" aria-controls="list-content" aria-selected="false">六百常用字真解</button>
              </li>
            </ul>
            <div class="tab-content" id="storiesSubTabContent">
              <div class="tab-pane fade show active" id="random-content" role="tabpanel" aria-labelledby="random-subtab">
                {% include shuowen-random.html %}
              </div>
              <div class="tab-pane fade" id="list-content" role="tabpanel" aria-labelledby="list-subtab">
                {% include shuowen-600-list.html %}
              </div>
            </div>
          </div>
        </div>
        <div class="tab-pane fade" id="learning" role="tabpanel" aria-labelledby="learning-tab">
          <p>國語日報的網路版，訂閱頁面: <a href="https://mdnereading.mdnkids.com/subscription/%E5%9C%8B%E8%AA%9E%E6%97%A5%E5%A0%B1">https://mdnereading.mdnkids.com/subscription/國語日報</a></p>
          <p>精選試讀的頁面: <a href="https://mdnereading.mdnkids.com/product_intro/hard_copy_paper">https://mdnereading.mdnkids.com/product_intro/hard_copy_paper</a></p>
          {% include pinyin-zhuyin-table.html %}
        </div>
      </div>
    </div> 

{% include {{ page.banvar }} %}

  </div>
</div>

