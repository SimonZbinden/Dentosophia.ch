For a **multi-language** website (German, French, English) with Jinja2/Bulma, here's the optimal directory structure I recommend for your Dentosophia project:

---

### **1. Recommended Structure**
```bash
dentosophia/
├── config/
│   ├── global.yaml          # Shared settings
│   ├── languages/           # Language-specific configs
│   │   ├── de.yaml          # German
│   │   ├── fr.yaml          # French
│   │   └── en.yaml          # English
│   └── pages/               # Page content per language
│       ├── about/
│       │   ├── de.yaml
│       │   ├── fr.yaml
│       │   └── en.yaml
│       └── contact/
│           ├── de.yaml
│           └── ...
│
├── templates/
│   ├── components/          # Reusable components
│   ├── languages/           # Language-specific template overrides
│   │   ├── de/
│   │   │   └── legal/       # German-specific legal templates
│   │   └── fr/
│   ├── macros/              # Language-aware macros
│   └── base.html.j2         # Main template
│
├── static/
│   ├── assets/
│   │   ├── de/              # German-specific images
│   │   ├── fr/
│   │   └── shared/
│   └── translations/        # JSON translations for JS
│       ├── de.json
│       └── ...
│
└── build.py                 # Build script with language handling
```

---

### **2. Key Features**
#### **A. Config Separation**
- `global.yaml`: Site-wide settings (GA4, social links)
  ```yaml
  analytics: GA-XXXX
  languages: [de, fr, en] 
  default_lang: de
  ```

- `languages/de.yaml`: Language-specific strings
  ```yaml
  nav:
    home: "Startseite"
    about: "Über uns"
  ```

#### **B. Smart Template Rendering**
`build.py` snippet:
```python
for lang in config['languages']:
    # Load language config
    lang_config = load_yaml(f"config/languages/{lang}.yaml")
    page_config = load_yaml(f"config/pages/about/{lang}.yaml")
    
    # Render
    output = template.render(
        lang=lang,
        t=lang_config,       # Translations
        page=page_config     # Page content
    )
    
    # Output to /de/about.html, /fr/about.html etc.
    Path(f"output/{lang}/about.html").write_text(output)
```

#### **C. Language Switching**
In `base.html.j2`:
```jinja
<div class="language-switcher">
  {% for l in ['de', 'fr', 'en'] %}
    <a href="/{{ l }}/{{ current_page }}" 
       class="{% if l == lang %}is-active{% endif %}">
      {{ l | upper }}
    </a>
  {% endfor %}
</div>
```

---

### **3. Bulma-Specific Tips**
1. **Right-to-Left (RTL) Support**  
   For languages like Arabic (future-proofing):
   ```jinja
   <html lang="{{ lang }}" dir="{% if lang == 'ar' %}rtl{% else %}ltr{% endif %}">
   ```
   ```css
   /* In your CSS */
   [dir="rtl"] .navbar-start { margin-right: auto; }
   ```

2. **Dynamic Font Sizes**  
   Some languages need more space:
   ```yaml
   # fr.yaml
   css_overrides:
     title_font_size: "1.1rem"  # French titles often longer
   ```

---

### **4. Translation Workflow**
1. **Use `gettext`-style keys** in templates:
   ```jinja
   <h1>{{ _('welcome_header') }}</h1>
   ```
2. **Extract strings** with:
   ```bash
   xgettext -L Python -o messages.pot templates/*.j2
   ```
3. **Convert YAML ↔ PO files** for translators

---

### **5. SEO Optimization**
Per-language in `header.html.j2`:
```jinja
<meta property="og:locale" content="{% if lang == 'de' %}de_CH{% elif lang == 'fr' %}fr_CH{% else %}en_US{% endif %}">
<link rel="alternate" hreflang="{{ lang }}" href="{{ current_url }}" />
```

---

### **Alternate Approach (If Preferring JSON)**
```bash
translations/
└── de
    ├── common.json   # { "cancel": "Abbrechen" }
    └── about.json    # Page-specific terms
```
```jinja
{# In templates #}
{{ load_translation('about')['section_title'] }}
```

---

### **Recommended Tools**
1. [Babel](https://babel.pocoo.org/) (Python i18n)
2. [i18next](https://www.i18next.com/) (for JS parts)
3. [Poedit](https://poedit.net/) (Translation GUI)

This structure keeps translations maintainable while supporting Bulma's layout system. Would you like me to adapt any part for Swiss German specifically?