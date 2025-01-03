---
permalink: /
layout: single
title: "About Me"
author_profile: true
redirect_from: 
  - /home/
  - /home.html
copyright: false
---

> Hi, I'm Hsuan Han Lai, a Product Engineer Lead.

With **5 years of expertise** in product engineering and development processes, I've helped **Vibe Inc.** deliver over **10 complex smart products** from concept to mass production.

I possess multidisciplinary knowledge in **software development**, **electrical engineering**, and **mechanical engineering**, with hands-on experience solving challenging cross-domain problems. I enjoy building quality products that not only feel good in hand but also spark creativity.
  
--- 

# Projects 
- ### [What I Built at Work 🏢 -->](/work_projects.md)
- ### [What I Built at Home 🏠 -->](/projects)

---

# Skill Keywords
{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
