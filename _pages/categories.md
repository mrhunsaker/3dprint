---
title: "Browse by Category"
layout: single
permalink: /categories/
---

{% assign categories_raw = "" %}
{% for item in site.prints %}
  {% for c in item.categories %}
    {% assign c = c | strip %}
    {% if c != "" %}
      {% assign categories_raw = categories_raw | append: c | append: "|" %}
    {% endif %}
  {% endfor %}
{% endfor %}
{% assign categories = categories_raw | split: "|" | uniq | sort %}

<!-- DEBUG: categories_raw = {{ categories_raw }} -->
<!-- DEBUG: categories array = {% for cat in categories %}[{{ cat }}]{% endfor %} -->

<div class="notice--primary">
  <strong>Categories</strong>
  <div style="margin-top: 0.5rem;">
    {% for category in categories %}
      {% assign cat = category | strip %}
      {% if cat != "" %}
        <a class="btn btn--small" href="#{{ cat | slugify }}">{{ cat }}</a>
      {% endif %}
    {% endfor %}
  </div>
</div>

{% for category in categories %}
  {% assign cat = category | strip %}
  {% if cat != "" %}
  <section class="taxonomy__section">
    <h2 id="{{ cat | slugify }}">{{ cat }}</h2>
    <!-- DEBUG: Looking for items with category "{{ cat }}" -->
    <div class="entries-list">
      {% for item in site.prints %}
        <!-- DEBUG: Item "{{ item.title }}" has categories: {% for ic in item.categories %}[{{ ic }}]{% endfor %} -->
        {% assign has_category = false %}
        {% for item_cat in item.categories %}
          {% assign item_cat_stripped = item_cat | strip %}
          {% if item_cat_stripped == cat %}
            {% assign has_category = true %}
          {% endif %}
        {% endfor %}
        {% if has_category %}
          <article class="archive__item">
            <h3 class="archive__item-title">
              <a href="{{ item.url | relative_url }}">{{ item.title }}</a>
            </h3>
            {% if item.description %}
              <p class="archive__item-excerpt">{{ item.description }}</p>
            {% endif %}
          </article>
        {% endif %}
      {% endfor %}
    </div>
  </section>
  {% endif %}
{% endfor %}

## Leave a Comment

Note, I use [Remarkbox](https://www.remarkbox.com/) for comments to prevent Disqus from showing ads or other methods requiring a GitHub login for participation in any discussions. Although you are asked for you email, there is no need to verify it through remarkbox in order to leave a comment. Verification is just so you can track discussions, etc. without the system treating you as a new person every time.  

<!-- Remarkbox - Your readers want to communicate with you -->
<div id="remarkbox-div">
    <noscript>
        <iframe id=remarkbox-iframe src="https://my.remarkbox.com/embed?nojs=true&mode=light" style="height:600px;width:100%;border:none!important" tabindex=0></iframe>
    </noscript>
</div>
<script src="https://my.remarkbox.com/static/js/iframe-resizer/iframeResizer.min.js"></script>
<script>
    var rb_owner_key = "9f6d3e72-e739-11f0-b88e-040140774501";
    var thread_uri = window.location.href;
    var thread_title = window.document.title;
    var thread_fragment = window.location.hash;

    // rb owner was here.
    var rb_src = "https://my.remarkbox.com/embed" +
            "?rb_owner_key=" + rb_owner_key +
            "&thread_title=" + encodeURI(thread_title) +
            "&thread_uri=" + encodeURIComponent(thread_uri) +
            "&mode=light" +
            thread_fragment;
    
    function create_remarkbox_iframe() {
        var ifrm = document.createElement("iframe");
        ifrm.setAttribute("id", "remarkbox-iframe");
        ifrm.setAttribute("scrolling", "no");
        ifrm.setAttribute("src", rb_src);
        ifrm.setAttribute("frameborder", "0");
        ifrm.setAttribute("tabindex", "0");
        ifrm.setAttribute("title", "Remarkbox");
        ifrm.style.width = "100%";
        document.getElementById("remarkbox-div").appendChild(ifrm);
    }
    create_remarkbox_iframe();
    iFrameResize(
        {
            checkOrigin: ["https://my.remarkbox.com"],
            inPageLinks: true,
            initCallback: function(e) {e.iFrameResizer.moveToAnchor(thread_fragment)}
        },
        document.getElementById("remarkbox-iframe")
    );
</script>
