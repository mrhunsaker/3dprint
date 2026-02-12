---
title: "All Prints"
layout: home
permalink: /prints/
entries_layout: grid
classes: wide
---

<style>
.grid__wrapper {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)) !important;
  gap: 1.5rem !important;
  margin-top: 1rem !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  justify-content: center !important;
  max-width: 100% !important;
}

.grid__item {
  width: 200px !important;
  max-width: 200px !important;
  float: none !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  clear: none !important;
}

.grid__item .archive__item-teaser {
  width: 200px !important;
  height: 200px !important;
  min-width: 200px !important;
  min-height: 200px !important;
  max-width: 200px !important;
  max-height: 200px !important;
  overflow: hidden;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.grid__item .archive__item-teaser img {
  width: 200px !important;
  height: 200px !important;
  min-width: 200px !important;
  min-height: 200px !important;
  max-width: 200px !important;
  max-height: 200px !important;
  object-fit: cover !important;
  display: block !important;
}

.grid__item .archive__item-title {
  font-size: 1rem;
  margin-top: 0.5rem;
  margin-bottom: 0.25rem;
  max-width: 200px;
  word-wrap: break-word;
}

.grid__item .archive__item-excerpt {
  font-size: 0.875rem;
  margin-bottom: 0;
  max-width: 200px;
  word-wrap: break-word;
}
</style>

<div style="text-align: center; margin-bottom: 2rem;">
  <p style="font-size: 1.2rem;">Browse our complete collection of accessible 3D prints</p>
  <a href="{{ '/request/' | relative_url }}" class="btn btn--primary btn--large">View Checkout</a>
  <a href="{{ '/custom-project/' | relative_url }}" class="btn btn--success btn--large">Custom Project</a>
  <a href="{{ '/puppets/' | relative_url }}" class="btn btn--warning btn--large">Puppets</a>
  <a href="{{ '/categories/' | relative_url }}" class="btn btn--info">Browse by Category</a>
  <a href="{{ '/tags/' | relative_url }}" class="btn btn--info">Browse by Tag</a>
</div>

{% assign prints = site.prints | sort: 'title' %}
<div class="grid__wrapper">
  {% for print in prints %}
    <div class="grid__item">
      <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
        {% if print.header.teaser %}
          <div class="archive__item-teaser">
            <img src="{{ print.header.teaser | relative_url }}" alt="{{ print.title }}">
          </div>
        {% endif %}
        <h2 class="archive__item-title" itemprop="headline">
          <a href="{{ print.url | relative_url }}" rel="permalink">{{ print.title }}</a>
        </h2>
        {% if print.description %}
          <p class="archive__item-excerpt" itemprop="description">{{ print.description }}</p>
        {% endif %}
      </article>
    </div>
  {% endfor %}
</div>

{%- comment -%}
Also include any documents in the `pages` collection that opt-in via `show_in_prints: true`.
This renders `_pages/*.md` items marked for inclusion alongside the `prints` collection.
{%- endcomment -%}

{% if site.collections.pages %}
  {% assign page_docs = site.collections.pages.docs | sort: 'title' %}
  <div class="grid__wrapper" style="margin-top:1.5rem;">
    {% for page in page_docs %}
      {% if page.show_in_prints %}
        <div class="grid__item">
          <article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">
            {% if page.header and page.header.teaser %}
              <div class="archive__item-teaser">
                <img src="{{ page.header.teaser | relative_url }}" alt="{{ page.title }}">
              </div>
            {% endif %}
            <h2 class="archive__item-title" itemprop="headline">
              <a href="{{ page.url | relative_url }}" rel="permalink">{{ page.title }}</a>
            </h2>
            {% if page.description %}
              <p class="archive__item-excerpt" itemprop="description">{{ page.description }}</p>
            {% else %}
              {% assign excerpt = page.content | strip_html | strip_newlines | truncate: 140 %}
              <p class="archive__item-excerpt" itemprop="description">{{ excerpt }}</p>
            {% endif %}
          </article>
        </div>
      {% endif %}
    {% endfor %}
  </div>
{% endif %}

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
