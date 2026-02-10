---
title: "Browse by Tag"
layout: single
permalink: /tags/
---

{% assign tags_raw = "" %}
{% for item in site.prints %}
  {% for t in item.tags %}
    {% assign t = t | strip %}
    {% if t != "" %}
      {% assign tags_raw = tags_raw | append: t | append: "|" %}
    {% endif %}
  {% endfor %}
{% endfor %}
{% assign tags = tags_raw | split: "|" | uniq | sort %}

<div class="notice--primary">
  <strong>Tags</strong>
  <div style="margin-top: 0.5rem;">
    {% for tag in tags %}
      {% assign tg = tag | strip %}
      {% if tg != "" %}
        <a class="btn btn--small" href="#{{ tg | slugify }}">{{ tg }}</a>
      {% endif %}
    {% endfor %}
  </div>
</div>

{% for tag in tags %}
  {% assign tg = tag | strip %}
  {% if tg != "" %}
  <section class="taxonomy__section">
    <h2 id="{{ tg | slugify }}">{{ tg }}</h2>
    <div class="entries-list">
      {% for item in site.prints %}
        {% assign has_tag = false %}
        {% for item_tag in item.tags %}
          {% assign item_tag_stripped = item_tag | strip %}
          {% if item_tag_stripped == tg %}
            {% assign has_tag = true %}
          {% endif %}
        {% endfor %}
        {% if has_tag %}
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
