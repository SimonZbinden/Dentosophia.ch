# Development Partnership
We build a website together. I'll handle implementation details while you guide architecture and catch complexity early.

---

## Language
The website is build written in HTML and CSS. No Javascript! We use Jinja2 as a template tool and Python to build the HTML files.

---

## Core Workflow: Research → Plan → Implement → Validate
**Start every feature with:** "Let me research the codebase and create a plan before implementing."

1. **Research** 
    - Study existing Jinja templates, routes, and CSS structure.
    - Identify reusable components (e.g., base template, macros).
2. **Plan** 
    - Sketch HTML/Jinja structure (avoid duplication).
    - Define Python route logic (keep it minimal).
3. **Implement**
    - Write Python routes + Jinja templates.
    - Add CSS after HTML structure is stable.
4. **Validate** 
    - Check rendered HTML/CSS in browser.
    - Run `pytest` for Python logic.

---

## **Code Organization**  
- **Structure**:  
  ```
  /project  
    /assets                 # figures, images, etc.
    /config                 # variables for each template
      global.yaml           # main dict for all global variables
      index.yaml            # dict for the index.html file
      about.yaml            # dict for the about.html file
      ...                   # and so on
    /css
      bulma.css             # bulma css content from bulma github
      client.css            # static css tailored for this client
    /html                   # rendered html files
      index.html
      about.html
      ...
    /python          
      __init__.py
      jinja_extensions.py   # Module handling filters, functions, etc. for jinja
      python_modules.py
    /templates              # Jinja2 files  
      /components           # reusable templates for header, navbar, etc.
        footer.html.j2
        header.html.j2
        navbar.html.j2
      base.html.j2          # Master template  
      index.html.j2         # template for index.html
      about.html.j2         # template for about.html
      ...
    build.py                # Renders Jinja templates using YAML configs
  ``` 

### **Python (Backend)**  
- **Small functions**: Split route logic into helper functions (e.g., `validate_form()`, `fetch_data()`).  
- **Single responsibility**: Separate business logic from route handlers.  

### **Jinja2 (Templates)**  
- **Modularize**: Use `{% extends %}` and `{% include %}` for reusable components (e.g. `{% extends "base.html.j2" %}`).  
- **Avoid logic in templates**: Move complex logic to Python (e.g., filtering data).  
- **Current base.html.j2 file**:  
  ```html
<!DOCTYPE html>
<html lang="{{ website.language }}">
  <head>
    {% include "components/header.html.j2" %}
  </head>

  <body>
    <!-- navbar -->
    {% include "components/navbar.html.j2" %}

    <!-- Main Content -->
    <main class="{{ this_site.main_class }}">
      {% block content %}No content found!{% endblock %}
    </main>

    <!-- Hero footer: will stick at the bottom -->
    {% include "components/footer.html.j2" %}    
  </body>
</html>
  ```
- **Current navbar.html.j2 file**:
    ```html
    <nav class="navbar is-warning has-shadow" role="navigation" aria-label="main navigation">
        <div class="hero-head container">
            
            <!-- Brand: always visible-->
            <div class="navbar-brand">
            <a class="navbar-item {% if this_site.name == 'index' %}is-active{% endif %}" href="{{ static_url(dir=links.dir, file=links.index) }}">
                <img class="py-2 px-2" style="max-height: 60px;" src="{{ static_url(dir='../assets/', file='logo_dentosophia_klein2.png') }}" alt="Logo">
            </a>
            </div>
            
            <!--
            #navbarMenu[navbar-toggle]
            This is the navbar menu.
            -->
            <input type="checkbox" id="navbar-burger-toggle" class="navbar-burger-toggle is-hidden is-warning">
            <label for="navbar-burger-toggle" class="navbar-burger">
            <span></span>
            <span></span>
            <span></span>
            </label>
            
            <!-- Menu. -->
            <div class="navbar-menu">
            <!-- start: on the left -->
            <div class="navbar-start">
                <a class="navbar-item {% if this_site.name == 'philosophie' %}is-active{% endif %}" href="{{ static_url(dir='../html', file='philosophie.html')}}">Philosophie</a>
                <a class="navbar-item {% if this_site.name == 'about' %}is-active{% endif %}" href="{{ static_url(dir='../html', file='about.html')}}">Über mich</a>
                <!-- DropDown Menu-->
                <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link {% if this_site.name == 'dentosophie' or this_site.name == 'cranio' %}is-active{% endif %}">
                    Therapien
                </a>
            
                <div class="navbar-dropdown">
                    <a class="navbar-item {% if this_site.name == 'dentosophie' %}is-active{% endif %}" href="{{ static_url(dir='../html', file='dentosophie.html')}}">
                    Dentosophie
                    </a>
                    <a class="navbar-item {% if this_site.name == 'cranio' %}is-active{% endif %}" href="{{ static_url(dir='../html', file='cranio.html')}}">
                    Kraniosakraltherapie
                    </a>
                </div>
                </div>
            </div>
            <!-- start: on the right -->
            <div class="navbar-end">
                <a class="navbar-item {% if this_site.name == 'kontakt' %}is-active{% endif %}" href="{{ static_url(dir='../html', file='kontakt.html')}}">Karte / Kontakt</a>
            </div> 
            </div>
        </div>
    </nav>
    ```


### **CSS**  
- **BEM naming**: Use `.block__element--modifier` for clarity.  
- **Bulma**: We use Bulma CSS Framework as our main source. Personalized CSS Code belongs into client.css.

### **Config Files**
**Current global.yaml file:**
  ```yaml
  personal:
    first_name: "Maria"
    last_name: "Mustermann"
    adress: "Strasse 1a"
    zip: "1234"
    city: "Ortschaft"
    city_nearby: "Umgebung"
    canton: "Kanton"
    country: "Schweiz"
    email: "info@email.ch"
    jobs: ["job1", "job2", "job3"]

  links:
    dir: "../html"
    impressum: "impressum.html"
    dsb: "dsb.html"
    index: "index.html"

  background_img:
    alt: "Hintergrundbild"
    class: "hero-background is-transparent"
    dir: "../assets"
    file: "flower-of-life.svg"

  website:
    title: "Arbeitstitel"
    language: "de-CH"
    developer:
      name: "Schweizer"
      prename: "Hans"
      email: "none"

  this_site:
    name: "none"
    title: "No Title"
    main_class: "section"
    content_class: "hero-body is-fullheight has-background"
```
**Current about.yaml file:**
  ```yaml
  this_site:
    name: "about"   # overwrites this_site.name in global.yaml (deep merge logic in Python)
    title: "Ein wenig über mich"
    tab_title: "Über mich" 
  ```
---

## **Architecture Principles**  
1. **Jinja2 Best Practices**:  
   - Prefer `{% macro %}` over copy-pasting HTML.  
   - Use `{% set %}` sparingly (logic belongs in Python).  
2. **Python Backend**:  
   - **Explicit routes**: 
      - Name routes clearly (e.g., `/blog/post/<id>`).
      - Obvious data flow over hidden magic.
   - **Minimal templates**: 
      - Pass *only* needed data from Python to Jinja.  
      - Focus on maintainable solutions over clever abstractions.
3. **JavaScript Ban ❌**:  
   - **No JavaScript under any circumstances**.  
   - Dynamic features must use Jinja2 or CSS-only solutions.  
   - Violations trigger immediate architectural review.  

---

## **Testing Strategy**  
- **Python**: Pytest for routes and helpers (mock external dependencies).  
- **Templates**: Manually check rendered output (no JS = simpler testing).  
- **CSS**: Validate with browser dev tools.  

---

## **Problem Solving**  
**When stuck:** 
  - Stop. The simple solution is usually correct.
  - *"Should this logic be in Python or Jinja?"* → Default to Python.  
  - *"Is this CSS getting too complex?"* → Simplify with BEM or split files.  

**When uncertain:** "Let me ultrathink about this architecture."

**When choosing:** *"I see two approaches: A (simple Jinja) vs B (Python-heavy). Which do you prefer?"*

---

## **User Interaction**  
- Keep your answers as short as possible and as long as needed.
- Do not explain why your code works, what you changed, etc.
**When LLM suggests JavaScript**:  
- Reject the solution outright.  
- Respond with: "Architecture violation: JS ban. Propose a Jinja2/CSS alternative."

---

Let me know when you are ready for my instructions.