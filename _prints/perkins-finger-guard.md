---
title: "Perkins Finger Guard"
sku: "PRT-00032-OT-VIS"
description: "Finger guard for Perkins Brailler to improve typing accuracy"
categories:
  - occupational therapy
  - visual impairments
tags:
  - braille
  - writing
  - adaptive-tools
header:
  teaser: /assets/images/prints/PerkinsFingerGuard.jpeg
stl: /assets/files/LINK TO 3D PRINT FILE(s).stl
---

![Perkins Finger Guard - View 1](/assets/images/prints/PerkinsFingerGuard.jpeg){: .full style="max-width: 600px;"}

![Perkins Finger Guard - View 2](/assets/images/prints/PerkinsFingerGuard2.jpeg){: .full style="max-width: 600px;"}

A 3D-printed finger guard that attaches to the Perkins Brailler to help students develop proper finger placement and key isolation when learning to write braille. By guiding fingers to the correct keys and preventing accidental presses, this tool improves typing accuracy and builds confidence during braille instruction.

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
