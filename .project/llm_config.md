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
        {%- filter indent(width=2) %}
        {% include "components/header.html.j2" %}
        {%- endfilter %}
      </head>
      <body>
        {%- if background_img %}
        <img {%- for attr, val in background_img.items() %} {{ attr }}="{{ val }}" {%- endfor %} />
        {%- endif -%}
        <section class="hero is-fullheight">
          <div class="hero-head">
            {%- filter indent(width=6) %}
            {% include "components/navbar.html.j2" %}
            {%- endfilter %}
          </div>
          <main class="hero-body">
            {%- filter indent(width=6) %}
            {% block content %}No content found!{% endblock %}
            {%- endfilter %}
          </main>
          <div class="hero-foot">
            {%- filter indent(width=6) %}
            {% include "components/footer.html.j2" %}
            {%- endfilter %}
          </div>
        </section>
      </body>
    </html>
    ```
- **Current navbar.html.j2 file**:
    ```html
    <nav class="navbar has-background-colour has-shadow" role="navigation" aria-label="main navigation">
      <!-- Hidden checkbox for CSS toggle logic - must be a sibling of .navbar-menu -->
      <input type="checkbox" id="navbar-burger-toggle" class="navbar-burger-toggle is-hidden">

      <div class="navbar-brand">
        <a class="navbar-item {% if this_site.name == 'index' %}is-active{% endif %}"
          href="{{ static_url(dir=links.dir, file=links.index) }}">
          <img class="py-2 px-2" style="max-height: 60px;"
            src="{{ static_url(dir='../assets/', file='logo_dentosophia_klein2.png') }}" alt="Logo">
        </a>

        <!-- Visible burger icon, linked to the hidden checkbox above -->
        <label for="navbar-burger-toggle" class="navbar-burger">
          <span></span>
          <span></span>
          <span></span>
          <span></span> <!-- Extra span for visual styling -->
        </label>
      </div>

      <!-- navbar-menu must be a sibling to the checkbox for the CSS ~ selector -->
      <div class="navbar-menu">
        <div class="navbar-start">
          <!-- Apply is-active based on this_site.name -->
          <a class="navbar-item {% if this_site.name == 'about' %}is-active{% endif %}"
            href="{{ static_url(dir=links.dir, file=links.about) }}">Über mich</a>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link {% if this_site.name == 'dentosophie' %}is-active{% endif %}"
              href="{{ static_url(dir=links.dir, file=links.dentosophie) }}">Dentosophie</a>
            <div class="navbar-dropdown">
              <a class="navbar-item" href="{{ static_url(dir=links.dir, file=links.dentosophie) }}#about">Überblick</a>
              <a class="navbar-item" href="{{ static_url(dir=links.dir, file=links.dentosophie) }}#when">Symptome</a>
              <a class="navbar-item" href="{{ static_url(dir=links.dir, file=links.dentosophie) }}#offer">Angebot</a>
            </div>
          </div>
          <a class="navbar-item {% if this_site.name == 'cranio' %}is-active{% endif %}"
            href="{{ static_url(dir=links.dir, file=links.cranio) }}">Craniosacral Therapie</a>
        </div>
        <!-- start: on the right -->
        <div class="navbar-end">
          <a class="navbar-item {% if this_site.name == 'kosten' %}is-active{% endif %}"
            href="{{ static_url(dir=links.dir, file=links.kosten)}}">Kosten</a>
          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-item {% if this_site.name == 'material' %}is-active{% endif %}"
              href="{{ static_url(dir=links.dir, file=links.material)}}">Hilfsmittel</a>
            <div class="navbar-dropdown">
              <a class="navbar-item" href="{{ static_url(dir=links.dir, file=links.material) }}#balancer">Balancer</a>
              <a class="navbar-item" href="{{ static_url(dir=links.dir, file=links.material) }}#books">Bücher</a>
            </div>
          <a class="navbar-item {% if this_site.name == 'kontakt' %}is-active{% endif %}"
            href="{{ static_url(dir=links.dir, file=links.kontakt)}}">Karte / Kontakt</a>
        </div>
      </div>
    </nav>
    ```


### **CSS**  
- **BEM naming**: Use `.block__element--modifier` for clarity.  
- **Bulma**: We use Bulma CSS Framework Version 1.0.4 as our main source. Personalized CSS Code belongs into client.css.
- **Current client.css file**:
    ```css
    :root {
      --custom-shadow: 5px 5px 20px rgb(73, 71, 41);
      --custom-radius: 4px; /* matches Bulma's $radius */
      --main-color-light: rgba(255, 215, 0, 0.1);
    }
    /*
    background image
    */
    .hero-body.has-background {
      position: relative;
      overflow: hidden;
    }
    .hero-background {
      position: absolute;
      object-fit: contain;
      object-position: center center;
      pointer-events: none;   /* prevent interaction with the bg image */
      width: 100%;
      height: 100%;
    }
    .hero-background.is-transparent {
      opacity: 0.1;
    }
    @media (max-width: 720px) {
      .hero-background {
        object-fit: cover; /* Prevents tiny SVG on mobile */
      }
    }
    /*
      * Images
      */
    /* Consistent image styling (matches map) */
    .image-card {
      border-radius: var(--custom-radius);
      box-shadow: var(--custom-shadow);
      overflow: hidden;         /* Ensures radius clips image */
    }
    /*
    * customize nav bar
    */
    .navbar.is-warning {
      background-color: var(--main-color-light);
    }
    /*
    * customize footer
    */
    .footer {
      background-color: var(--main-color-light);
      margin-top: auto;
    }
    /*
    * responsive google maps
    * thanks to Amit Agarwal:
    * https://www.labnol.org/internet/embed-responsive-google-maps/28333/
    */
    .google-maps {
      position: relative;
      padding-bottom: 75%; 
      box-shadow: var(--custom-shadow);
      height: 0;
      overflow: hidden;
      border-radius: var(--custom-radius);
      margin: 1.5rem auto; /* consistent with Bulma's spacing */
    }
    .google-maps iframe {
      position: absolute;
      top: 0;
      left: 0;
      width: 100% !important;
      height: 100% !important;
      border: 0; /* remove default iframe border */
      filter: brightness(0.98); /* reduce glare */
    }
    @media screen and (max-width: 768px) {
      .google-maps {
        padding-bottom: 100%;
        margin-left: 0;
        margin-right: 0;
      }
    }
    /*
    * hide mobile number behind img
    */
    .responsive-img{
      width: 100%;
      max-width: 110px;
      height: auto;
    }
    /*
      * hyperlinks
      */
    .hyperlink{
      color: #120aee;
    }
    /* Auto-add to external links */
    a[target="_blank"]:not([href^="{{"])::after {
      content: "↗";
      display: inline-block;
      margin-left: 0.25em;
      font-size: 1em;
    }
    /*
    * justified text with auto hyphenation
    */
    .text-is-justified {
      text-align: justify;
      text-justify: inter-word;  /* Better than 'auto' */
      hyphens: auto;
      -webkit-hyphens: auto;     /* Safari */
      -ms-hyphens: auto;         /* IE/Edge */
      hyphenate-limit-chars: 6 3 3; /* min-length before/after hyphen */
      overflow-wrap: break-word;     /* Emergency break */
    }
    address {
      font-style: normal;
      font-family: inherit; /* Uses the same font as the rest of the page */
      line-height: 1.5; /* Match Bulma's default line height */
    }
    .navbar-burger-toggle:checked ~ .navbar-menu {
      display: block !important;  /* Force show menu */
    }
    ```

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