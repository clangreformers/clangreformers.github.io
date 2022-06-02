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
              <p> People </p>
            </div>
            <div class="right">
              <div class="right-scroll">


                <p>
                     
                  [Yilin Zhang](https://zh.wikipedia.org/wiki/張一麐)

                  [Xitao Yuan](https://zh.wikipedia.org/wiki/袁希濤)、[Jingheng Wu](https://zh.wikipedia.org/wiki/吳敬恆)

                  [Jinxi Li](https://zh.wikipedia.org/wiki/黎錦熙)、[Maozhi Chen](https://zh.wikipedia.org/wiki/陳懋治)、Yi Shen、Buqing Li、Ji Lu、[Wenxiong zhu](https://zh.wikipedia.org/wiki/朱文熊)、[Daosun Qian](https://zh.wikipedia.org/wiki/錢稻孫)、[Xuantong Qian](https://zh.wikipedia.org/wiki/錢玄同)、[Shi Hu](https://zh.wikipedia.org/wiki/胡適)、[Fu Liu](https://zh.wikipedia.org/wiki/劉半農)、[Zuoren Zhou](https://zh.wikipedia.org/wiki/周作人)、[Yuzhao Ma](https://zh.wikipedia.org/wiki/馬裕藻)、[Yuen Ren Chao](https://zh.wikipedia.org/wiki/趙元任)、[Yi Wang]({{ site.baseurl }}{% link people/wangyi.md %})、[Yuanpei Cai](https://zh.wikipedia.org/wiki/蔡元培)、Zhenying Bai、[Jialin Xiao]({{ site.baseurl }}{% link people/xiaojialin-tw.md %})、Lijin Zeng、[Shiqing Sun]({{ site.baseurl }}{% link people/sunshiqing-tw.md %})、Yi Fang、[Jianshi Shen](https://zh.wikipedia.org/wiki/沈兼士)、[Jinhui Li](https://zh.wikipedia.org/wiki/黎錦暉)、[Dishan Xuu](https://zh.wikipedia.org/wiki/許地山)、[Yuutang Lin](https://zh.wikipedia.org/wiki/林語堂)、Pu Wang

                  [Jingheng Wu](https://zh.wikipedia.org/wiki/吳敬恆)

                  [Xuantong Qian](https://zh.wikipedia.org/wiki/錢玄同)、[Jinxi Li](https://zh.wikipedia.org/wiki/黎錦熙)、[Maozhi Chen](https://zh.wikipedia.org/wiki/陳懋治)、[Yi Wang]({{ site.baseurl }}{% link people/wangyi-tw.md %})、Yi Sheng、Zhenying Bai、[Jiangong Wei](https://zh.wikipedia.org/wiki/魏建功)

                  [Yuanpei Cai](https://zh.wikipedia.org/wiki/蔡元培)、[Yilin Zhang](https://zh.wikipedia.org/wiki/張一麐)、[Shizeng Li](https://zh.wikipedia.org/wiki/李石曾)、[Shuhua Li](https://zh.wikipedia.org/wiki/李書華)、Buqing Li、[Shi Hu](https://zh.wikipedia.org/wiki/胡適)、[Fu Liu](https://zh.wikipedia.org/wiki/劉半農)、[Zuoren Zhou](https://zh.wikipedia.org/wiki/周作人)、Ji Lu、[Wenxiong Zhu](https://zh.wikipedia.org/wiki/朱文熊)、[Lijin Zeng](https://zh.wikipedia.org/wiki/曾彝進)、[Shiqing Sun]]({{ site.baseurl }}{% link people/sunshiqing.md %})、Yi Fang、[Jianshi Shen](https://zh.wikipedia.org/wiki/沈兼士)、[Dishan Xuu](https://zh.wikipedia.org/wiki/許地山)、[Yuutang Lin](https://zh.wikipedia.org/wiki/林語堂)、[Hongjun Ren](https://zh.wikipedia.org/wiki/任鴻雋)、Tigan Ma、[Daosun Qian](https://zh.wikipedia.org/wiki/錢稻孫)、[Yuzao Ma](https://zh.wikipedia.org/wiki/馬裕藻)、[Jialin Xiao]({{ site.baseurl }}{% link people/xiaojialin.md %})



                  [Lian Ma](https://zh.wikipedia.org/wiki/馬廉)

                  [Jinxi Li](https://zh.wikipedia.org/wiki/黎錦熙)

                  [Fu Liu](https://zh.wikipedia.org/wiki/劉半農)

                  [Xuantong Qian](https://zh.wikipedia.org/wiki/錢玄同)

                  [Yu Xiao](https://zh.wikipedia.org/wiki/蕭瑜)

                  [Yuan Ren Chao](https://zh.wikipedia.org/wiki/趙元任)

                  [Yi Wang]({{ site.baseurl }}{% link people/wangyi.md %})

                  [Tongli Yuan](https://zh.wikipedia.org/wiki/袁同禮)


                  [Jinxi Li](https://zh.wikipedia.org/wiki/黎錦熙)

                  [Xuantong Qian](https://zh.wikipedia.org/wiki/錢玄同) 

                  [Fu Liu](https://zh.wikipedia.org/wiki/劉半農) 

                  [Yi Wang]({{ site.baseurl }}{% link people/wangyi-tw.md %}) 

                  [Jialin Xiao]({{ site.baseurl }}{% link people/xiaojialin.md %}) 

                  Yi Liu 

                  Dizhou Bai

                  [Kaidi Sun](https://zh.wikipedia.org/wiki/孫楷第) 

                  [Jiangong Wei](https://zh.wikipedia.org/wiki/魏建功)

                  [Zhongmin Wang](https://zh.wikipedia.org/wiki/王重民) 

                  [LIan Ma](https://zh.wikipedia.org/wiki/馬廉) 

                  Weiyuu Zhang 

                  [Shuda Wang]({{ site.baseurl }}{% link people/wangshuda.md %})  

                  Ji Cui 

                  Zongjian Wang 

                  [Yishi Xuu](https://zh.wikipedia.org/wiki/徐一士) 

                  Shaohua Yuan

                  Wangqun Peng 

                  Linzhang Luo 

                  Fanjun Kong 

                  [Shoukang Wang]({{ site.baseurl }}{% link people/wangshoukang.md %}) 

                  Jiewu Xiao 

                  Kun Xiao 

                  Shoupeng Li 

                  Ruidi Sun 

                  Binyi Weng 

                  Jiabin Shang 

                  Yizheng Zhao 

                  Xueming Qiu 

                  [Xunru Zhang]({{ site.baseurl }}{% link people/zhangxunru-tw.md %}) 

                  Sikun Suo 


                  Yintang Zhao

                  Pansui Liu

                  Zhuangyou Fang

                  [Rulin Liu](https://zh.wikipedia.org/wiki/劉汝霖)

                  Shiji He

                  [Dingyi Fu](https://zh.wikipedia.org/wiki/符定一) 

                  Shoulin Zhang

                  Shiying Ao

                  Rujun Diao

                  Qifang Shen 

                  Deyun Wu

                  Wenguang Li 


                  Meicen He、Jichang Niu、Jieshi Fu（relative）、Jincheng Gao、Shirong Xuu、Chongyi Sun、Wenzhuo An


                  [Shengshu Ding](https://zh.wikipedia.org/wiki/丁聲樹)、[Jinxi Li](https://zh.wikipedia.org/wiki/黎錦熙)、[Rong Li](https://zh.wikipedia.org/wiki/李榮_(語言學家))、[Zhiwei Lu](https://zh.wikipedia.org/wiki/陸志韋)、[Zongda Lu](https://zh.wikipedia.org/wiki/陸宗達)、[Shuxiang Luu](https://zh.wikipedia.org/wiki/呂叔湘)、Mingda Shi、[Li Wang](https://zh.wikipedia.org/wiki/王力_(语言学家))、[JIangong Wei](https://zh.wikipedia.org/wiki/魏建功)、[Laishi Ye](https://zh.wikipedia.org/wiki/葉籟士)、[Shengtao Ye](https://zh.wikipedia.org/wiki/葉聖陶)、[Dingyi Zhou](https://zh.wikipedia.org/wiki/周定一)、Haoran Zhou、[Xumo Zhao](https://zh.wikipedia.org/wiki/周祖謨)、Wenshu Zhu

                  Dexuan Kong、Chongyi Sun、Meicen He、Bochun Li、[Jialin Xiao]({{ site.baseurl }}{% link people/xiaojialin-tw.md %})、Fanjun Kong、[Shuda Wang]({{ site.baseurl }}{% link people/wangshuda.md %})、Qinglong Liu、Di Guo、Wensheng Li、Jiexiu Liu、Heng Mo、Chongkang Wu、Guoyan Li、Xuanmu Zheng、Yaohai Shan、Tiankun Luu、Xiaofu Xuu、Jiyan Fan、Fanglian Fan、Jing Fu、Da Jiang、Lida Wang

                  Shilu Xuu、[Danjiang He]({{ site.baseurl }}{% link people/hedanjiang-tw.md %})、Zejun Gao、Huanzhen Wang、Guijun Zhao、Yunming Zhao、Xuantian Yao

                  

                </p>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
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