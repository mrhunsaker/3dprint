---
title: "Screen Reader Tactile Screen"
sku: "PRT-00037-VIS"
description: "Tactile screen reader display with multiple configurations"
categories:
  - visual impairments
tags:
  - braille
  - screen-reader
  - assistive-technology
header:
  teaser: /assets/images/prints/ScreenreaderScreen1.jpeg
stl: /assets/files/LINK TO 3D PRINT FILE(s).stl
---

![Screen Reader Screen - View 1](/assets/images/prints/ScreenreaderScreen1.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 2](/assets/images/prints/ScreenreaderScreen2.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 3](/assets/images/prints/ScreenreaderScreen3.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 4](/assets/images/prints/ScreenreaderScreen4.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 5](/assets/images/prints/ScreenreaderScreen5.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 6](/assets/images/prints/ScreenreaderScreen6.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 7](/assets/images/prints/ScreenreaderScreen7.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 8](/assets/images/prints/ScreenreaderScreen8.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 9](/assets/images/prints/ScreenreaderScreen9.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 10](/assets/images/prints/ScreenreaderScreen10.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 11](/assets/images/prints/ScreenreaderScreen11.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 13](/assets/images/prints/ScreenreaderScreen13.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen - View 14](/assets/images/prints/ScreenreaderScreen14.jpeg){: .full style="max-width: 600px;"}

![Screen Reader Screen Case](/assets/images/prints/ScreenReaderScreenCase.jpeg){: .full style="max-width: 600px;"}

A tactile teaching model that replicates the layout and interface of a screen reader display. Featuring multiple configurations and interchangeable components, this tool helps students with visual impairments learn how screen readers organize and present information. The accompanying case provides storage and portability for classroom and individual instruction settings.

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
