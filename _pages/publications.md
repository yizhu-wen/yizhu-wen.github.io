---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

You can also find my work on my <u><a href="{{ site.author.googlescholar }}">Google Scholar profile</a></u>.


Peer-reviewed
======

{% assign reviewed = site.publications | where_exp: "post", "post.pubtype != 'preprint'" | sort: "date" | reverse %}
{% for post in reviewed %}
  {% include archive-single-publication.html %}
{% endfor %}

Preprints & Under Review
======

{% assign preprints = site.publications | where: "pubtype", "preprint" | sort: "date" | reverse %}
{% for post in preprints %}
  {% include archive-single-publication.html %}
{% endfor %}
