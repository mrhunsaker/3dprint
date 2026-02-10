
# Jekyll 3D Prints Starter (Minimal Mistakes)

This is a ready-to-deploy Jekyll starter for a school-district 3D print catalog:

- **Minimal Mistakes** theme
- **`prints` collection** (one Markdown file per print)
- **Gallery page** with thumbnails (grid)
- **Category and Tag archives**
- **Lunr.js search** (client-side)
- **Microsoft Forms** integration
  - Per-item: **Request this Print** button reveals an embedded form, **pre-filled** with the item name
  - Global: **Checkout** page gathers multiple items (localStorage) and pre-fills a single form field

> Replace `YOUR_FORM_ID`, `ITEM_PARAM`, and `ITEMS_PARAM` in the pages below with the values from **Microsoft Forms → … → Get Pre-filled URL**.

## Quick Start

```bash
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000 and explore:

- `/prints/` – All prints (grid)
- `/categories/` and `/tags/`
- `/request/` – Global checkout form

## Where to edit

- Add items in **`_prints/`** (copy one of the samples)
- Teaser thumbnails go in **`assets/images/prints/`**; set in front matter as `header.teaser: /assets/images/prints/<file>`
- STL or links in `stl:` front matter
- Microsoft Form settings in **`_pages/request.md`** and each item page’s script block

## Notes

- If your MS Form is restricted to organization-only, some browsers (e.g., Safari) may block sign-in in iframes. Provide the direct link fallback on the request page.
- Prefilled values may persist due to caching in some cases; a cache-buster parameter is added in the scripts.

## License
MIT for the repository scaffolding. Minimal Mistakes is MIT-licensed by Michael Rose.
# 3dprint
