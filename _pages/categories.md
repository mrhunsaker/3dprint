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
