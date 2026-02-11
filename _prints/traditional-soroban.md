---
title: Traditional Soroban
sku: "PRT-00049-VIS"
description: Japanese abacus for mathematical calculations
categories:
  - visual impairments
tags:
  - braille
  - math
  - abacus
  - arithmetic
header:
  teaser: /assets/images/prints/IMG_0044.jpeg
---

![IMG_0044.jpeg_Title](/assets/images/prints/IMG_0044.jpeg){: .full style="max-width: 600px;"}

A 3D-printed traditional Japanese soroban abacus adapted for tactile use by students with visual impairments. Featuring the classic 1-bead-above / 4-beads-below configuration per column, this soroban supports all four basic arithmetic operations as well as more advanced calculations. The tactile bead positions allow students to learn and apply the standard soroban methods used worldwide, making it a powerful tool for math instruction from elementary through advanced levels.

<div class="notice--primary">
  <strong>Request this Print</strong><br>
  <button class="btn btn--success" id="show-item-form">Request this Print</button>
  <button class="btn" id="add-to-cart">Add to Checkout</button>
</div>

<div id="item-form-wrap" style="display:none; margin-top:1rem;">
  <iframe id="item-form"
          width="100%" height="900"
          frameborder="0" marginwidth="0" marginheight="0"
          style="border:none; max-width:100%;"
          allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen></iframe>
</div>
<script>
const FORM_BASE = "https://forms.office.com/Pages/ResponsePage.aspx?id=dPKcPX5U9UqN3gGmNuC2B9BUqS29h4FEq3EuP1SejDdUMEZYSDZSWUNOQ1I0MzRVV0g0OVhRWEpJWC4u&embed=true";
const ITEM_PARAM = "r9a5938ee7a304e89b8565f45b75aa5d8";
const itemName = "{{ page.title | uri_escape }}";

  document.getElementById("show-item-form").addEventListener("click", () => {
    const params = new URLSearchParams();
    params.set(ITEM_PARAM, itemName);
    params.set("_", Date.now().toString());
    document.getElementById("item-form").src = FORM_BASE + "&" + params.toString();
    document.getElementById("item-form-wrap").style.display = "block";
    document.getElementById("item-form-wrap").scrollIntoView({ behavior: "smooth" });
  });

  document.getElementById("add-to-cart").addEventListener("click", () => {
    const cart = JSON.parse(localStorage.getItem("print_cart") || "[]");
    const name = "{{ page.title | escape }}";
    if (!cart.includes(name)) cart.push(name);
    localStorage.setItem("print_cart", JSON.stringify(cart));
    window.location.href = "{{ '/request/' | relative_url }}";
  });
</script>
