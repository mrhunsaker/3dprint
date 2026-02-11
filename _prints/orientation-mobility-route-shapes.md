---
title: Orientation and Mobility Route Shapes
sku: "PRT-00027-OM-VIS"
description: Tactile route shape models for O&M instruction
categories:
  - orientation and mobility
  - visual impairments
tags:
  - orientation-mobility
  - navigation
  - tactile
  - education
header:
  teaser: /assets/images/prints/Orientation-Mobility-Route-Shapes.jpeg
---

![Orientation-Mobility-Route-Shapes.jpeg_Title](/assets/images/prints/Orientation-Mobility-Route-Shapes.jpeg){: .full style="max-width: 600px;"}

Tactile models representing common route shapes and travel patterns encountered during Orientation and Mobility (O&M) instruction. Students with visual impairments use these models to learn and practice recognizing L-shapes, U-shapes, zigzag routes, and other path configurations by touch. By internalizing these spatial patterns before real-world travel, learners build stronger navigation skills and greater confidence when moving through unfamiliar environments.

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
