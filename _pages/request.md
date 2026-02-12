---
title: "Request (Checkout)"
layout: single
permalink: /request/
classes: wide
---

This page collects all items you've added and pre-fills them into the district Microsoft Form.

<p><strong>Items in your request:</strong> <span id="cart-list">(none)</span></p>

<p>
  <button id="clear-cart" class="btn">Clear</button>
  <a id="open-direct" class="btn btn--primary" target="_blank" rel="noopener">Open Form in New Tab</a>
</p>

<!-- Replace with your base (non-prefilled) Microsoft Form URL: -->
<script>
  const FORM_BASE = "https://forms.office.com/Pages/ResponsePage.aspx?id=dPKcPX5U9UqN3gGmNuC2B9BUqS29h4FEq3EuP1SejDdUMEZYSDZSWUNOQ1I0MzRVV0g0OVhRWEpJWC4u&embed=true";
  // Parameter name for your long-text question that will hold the list of items
  const ITEMS_PARAM = "rf3339a6f9c3c442c979ac041381e732b"; // <— change to match Forms' generated prefill param name

  // Map of print title -> SKU (generated from site.prints sorted by title)
  const PRINT_SKU = {
  {% assign prints = site.prints | sort: 'title' %}
  {% for p in prints %}
    "{{ p.title | escape }}": "{{ p.sku | default: '' }}"{% unless forloop.last %},{% endunless %}
  {% endfor %}
  };

  function getCart() {
    try { return JSON.parse(localStorage.getItem("print_cart") || "[]"); }
    catch { return []; }
  }

  function updatePage() {
    const cart = getCart();
    // show SKU + title for clarity
    const numbered = cart.map(name => {
      const sku = PRINT_SKU[name];
      return sku && sku.length ? `${sku} - ${name}` : name;
    });
    const listSpan = document.getElementById("cart-list");
    listSpan.textContent = numbered.length ? numbered.join(", ") : "(none)";

    const params = new URLSearchParams();
    params.set(ITEMS_PARAM, numbered.join(", "));
    params.set("_", Date.now().toString()); // cache-buster
    
    const url = FORM_BASE + "&" + params.toString();
    document.getElementById("msform").src = url;
    document.getElementById("open-direct").href = url.replace("&embed=true", "");
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("clear-cart").addEventListener("click", () => {
      localStorage.removeItem("print_cart");
      updatePage();
    });
    updatePage();

    // Detect blocked iframe after a timeout
    const iframe = document.getElementById("msform");
    const fallback = document.getElementById("iframe-fallback");
    if (iframe && fallback) {
      setTimeout(() => {
        try {
          const doc = iframe.contentDocument || iframe.contentWindow.document;
          if (!doc || !doc.body || doc.body.innerHTML.trim() === "") {
            fallback.style.display = "block";
          }
        } catch (e) { /* cross-origin = loaded OK */ }
      }, 4000);
      iframe.addEventListener("error", () => { fallback.style.display = "block"; });
    }
  });
</script>

<div id="iframe-fallback" style="display:none; padding:1.5rem; background:#fff3cd; border:1px solid #ffc107; border-radius:6px; margin-bottom:1rem;">
  <p style="margin:0;">⚠️ <strong>Form not loading?</strong> Your browser may be blocking the embedded form. Click <strong>Open Form in New Tab</strong> above, or add this site to your browser's exceptions for Enhanced Tracking Protection.</p>
</div>

<iframe id="msform"
        width="100%" height="900"
        frameborder="0" marginwidth="0" marginheight="0"
        style="border:none; max-width:100%;"
        allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen>
</iframe>

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

