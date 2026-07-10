---
layout: page
title: projects
permalink: /projects/
description: Research and Developer Project Experience
nav: true
nav_order: 3
---

## Capstone Projects

{% assign capstones = site.projects | where: "category", "capstone" | sort: "year" | reverse %}
{% for project in capstones %}

<div class="card hoverable mb-4">
  <div class="card-body">
    <div class="row">
      <div class="{% if project.img %}col-md-8{% else %}col-12{% endif %}">
        <h3 class="card-title" style="margin-top: 0; margin-bottom: 10px; white-space: normal; word-wrap: break-word;">{{ project.title }} <span style="font-size: 0.7em; color: #6c757d;">(AY{{ project.year }})</span></h3>
        <h6 class="card-subtitle mb-3 text-muted"><strong>Team:</strong> {{ project.team }} <br> <strong>Advisor:</strong> {{ project.advisor }}</h6>
        <p class="card-text">{{ project.description }}</p>
        <div class="row" style="font-size: 0.95rem;">
          <div class="col-sm-6">
            <ul class="list-unstyled" style="margin-bottom: 0;">
              <li><strong>🧠 Brain:</strong> {{ project.brain }}</li>
              <li><strong>🗺️ Navigation:</strong> {{ project.navigation }}</li>
              {% if project.database %}<li><strong>💾 Database:</strong> {{ project.database }}</li>{% endif %}
            </ul>
          </div>
          <div class="col-sm-6">
            <ul class="list-unstyled" style="margin-bottom: 0;">
              <li><strong>🗣️ Speech:</strong> {{ project.speech }}</li>
              <li><strong>👀 Vision:</strong> {{ project.vision }}</li>
            </ul>
          </div>
        </div>
        <div class="mt-3">
          <span class="badge badge-success" style="font-size: 0.85em; margin-right: 5px; background-color: #28a745;">⚡ Response: {{ project.performance }}</span>
          <span class="badge badge-info" style="font-size: 0.85em; background-color: #17a2b8;">🛡️ Safety: {{ project.safety }}</span>
          {% if project.tiktok_url %}
          <a href="{{ project.tiktok_url }}" target="_blank" class="badge badge-danger" style="font-size: 0.85em; margin-left: 5px; background-color: #fe2c55; text-decoration: none; color: white;">▶️ TikTok Demo</a>
          {% endif %}
        </div>
      </div>
      {% if project.img %}
      <div class="col-md-4 d-flex align-items-center justify-content-center mt-3 mt-md-0">
        <img src="{{ project.img | relative_url }}" class="img-fluid rounded" alt="{{ project.title }}" style="width: 100%; object-fit: contain;">
      </div>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

## Research and Developer Projects

{% assign work_projects = site.projects | where_exp: "item", "item.category != 'capstone'" | sort: "year" | reverse %}
{% for project in work_projects %}

- [{{ project.title }}]({{ project.url | relative_url }}){% if project.owner %}, **{{ project.owner }}**{% endif %}  
   {{ project.description }}
  {% endfor %}
