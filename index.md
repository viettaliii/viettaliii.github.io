---
author: vietzettt
layout: home
title: "💀v13t_z3ttt@mpei.ru◀️"
permalink: /
cover: /assets/img/Logo%20Team%20SeaHatVN.gif
---
{%- for post in site.posts -%}
  {%- capture current_year -%}{{ post.date | date: "%Y" }}{%- endcapture -%}
  {%- unless current_year == previous_year -%}
    <h3 align="center">{{ current_year }}</h3>
    {%- assign previous_year = current_year -%}
  {%- endunless -%}
  <article class="post-item" align="center">
    <h6 class="post-item-title">
      <a href="{{ post.url }}">{{ post.title | escape }}</a>
    </h6>
  </article>
{%- endfor -%}
