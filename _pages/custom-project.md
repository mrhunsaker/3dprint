---
title: "Custom Project"
layout: single
permalink: /custom-project/
classes: wide
---

Have an idea for a custom 3D print that isn't in our catalog? Use this form to describe your project and we'll work with you to bring it to life.

<p>
  <a id="open-direct" class="btn btn--primary" target="_blank" rel="noopener">Open Form in New Tab</a>
</p>

<!-- Replace FORM_BASE with your actual Custom Project Microsoft Form URL -->
<script>
  const FORM_BASE = "https://forms.office.com/Pages/ResponsePage.aspx?id=dPKcPX5U9UqN3gGmNuC2B9BUqS29h4FEq3EuP1SejDdUOEdOVUZWUk9FN1NZVlNWNjNFRVpXWkxJQy4u&embed=true";

  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("msform").src = FORM_BASE;
    document.getElementById("open-direct").href = FORM_BASE.replace("&embed=true", "");
  });
</script>

<noscript>
  <p><strong>JavaScript is required to load the embedded form.</strong> Please <a id="open-direct-noscript">open the form directly</a>.</p>
</noscript>

<div id="iframe-fallback" style="display:none; padding:1.5rem; background:#fff3cd; border:1px solid #ffc107; border-radius:6px; margin-bottom:1rem;">
  <p style="margin:0;">⚠️ <strong>Form not loading?</strong> Your browser may be blocking the embedded form. Please click <a id="open-direct-fallback" class="btn btn--primary" target="_blank" rel="noopener">Open Form in New Tab</a> instead, or add this site to your browser's exceptions for Enhanced Tracking Protection.</p>
</div>

<iframe id="msform"
        width="100%" height="900"
        frameborder="0" marginwidth="0" marginheight="0"
        style="border:none; max-width:100%;"
        allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen>
</iframe>
