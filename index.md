---
layout: home
title: "3D Prints Catalog"
permalink: /
entries_layout: grid
classes: wide
author_profile: true
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
  <p style="font-size: 1.2rem;">Browse our collection of accessible 3D prints</p>
  <a href="/request/" class="btn btn--primary btn--large">View Checkout</a>
  <a href="/custom-project/" class="btn btn--success btn--large">Custom Project</a>
  <a href="/categories/" class="btn btn--info">Browse by Category</a>
  <a href="/tags/" class="btn btn--info">Browse by Tag</a>
</div>

<h2 class="archive__subtitle">Available Prints</h2>

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
