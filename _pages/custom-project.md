---
title: "Custom Project"
layout: single
permalink: /custom-project/
classes: wide
show_in_prints: true
---

Have an idea for a custom 3D print that isn't in our catalog? Use this form to describe your project and we'll work with you to bring it to life.

<p>
  <a id="open-direct" class="btn btn--primary" target="_blank" rel="noopener">Open Form in New Tab</a>
</p>

<!-- Replace FORM_BASE with your actual Custom Project Microsoft Form URL -->
<script>
  const FORM_BASE = "https://forms.office.com/Pages/ResponsePage.aspx?id=dPKcPX5U9UqN3gGmNuC2B9BUqS29h4FEq3EuP1SejDdUOEdOVUZWUk9FN1NZVlNWNjNFRVpXWkxJQy4u&embed=true";
  const FORM_DIRECT = FORM_BASE.replace("&embed=true", "");

  document.addEventListener("DOMContentLoaded", () => {
    const iframe = document.getElementById("msform");
    const fallback = document.getElementById("iframe-fallback");

    // Set all "open direct" links
    document.getElementById("open-direct").href = FORM_DIRECT;
    const fb = document.getElementById("open-direct-fallback");
    if (fb) { fb.href = FORM_DIRECT; fb.target = "_blank"; }
    const ns = document.getElementById("open-direct-noscript");
    if (ns) ns.href = FORM_DIRECT;

    // Try to detect blocked iframe after a timeout
    iframe.src = FORM_BASE;
    setTimeout(() => {
      try {
        // If cross-origin, accessing contentDocument throws; that's expected.
        // But if the iframe body is completely empty or the iframe didn't load,
        // show the fallback.
        const doc = iframe.contentDocument || iframe.contentWindow.document;
        if (!doc || !doc.body || doc.body.innerHTML.trim() === "") {
          fallback.style.display = "block";
        }
      } catch (e) {
        // Cross-origin = form loaded successfully (normal); do nothing
      }
    }, 4000);

    // Also show fallback if iframe fires an error
    iframe.addEventListener("error", () => {
      fallback.style.display = "block";
    });
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
