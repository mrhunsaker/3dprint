---
title: "All Prints"
layout: home
permalink: /prints/
entries_layout: grid
classes: wide
---

<style>
.grid__wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 200px));
  gap: 1.5rem;
  margin-top: 1rem;
  justify-content: center;
}

.grid__item .archive__item-teaser {
  width: 200px;
  height: 200px;
  overflow: hidden;
  border-radius: 4px;
  margin-bottom: 0.5rem;
}

.grid__item .archive__item-teaser img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  display: block;
}

.grid__item .archive__item-title {
  font-size: 1rem;
  margin-top: 0.5rem;
  margin-bottom: 0.25rem;
}

.grid__item .archive__item-excerpt {
  font-size: 0.875rem;
  margin-bottom: 0;
}
</style>

<div style="text-align: center; margin-bottom: 2rem;">
  <p style="font-size: 1.2rem;">Browse our complete collection of accessible 3D prints</p>
  <a href="/request/" class="btn btn--primary btn--large">View Checkout</a>
  <a href="/categories/" class="btn btn--info">Browse by Category</a>
  <a href="/tags/" class="btn btn--info">Browse by Tag</a>
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
