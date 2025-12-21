---
layout: page
title: projects
permalink: /projects/
description: Research and Developer Project Experience
nav: true
nav_order: 3
---

## Research and Developer Projects

{% assign sorted_projects = site.projects | sort: "year" | reverse %}
{% for project in sorted_projects %}
* [{{ project.title }}]({{ project.url | relative_url }}){% if project.owner %}, **{{ project.owner }}**{% endif %}  
  {{ project.description }}
{% endfor %}
