# PROPOSED CLEAN FILE STRUCTURE FOR 03_BUILD

## CURRENT (Messy - files scattered)
```
03_BUILD/
├── index.html
├── about.html
├── contact.html
├── services.html
├── resources.html
├── downloads.html
├── request-a-quote.html
├── eot-cranes.html
├── gantry-cranes.html
├── hoists.html
├── jib-cranes.html
├── crane-spare-parts.html
├── eot-cranes/
├── gantry-cranes/
├── locations/
└── assets/
```

## PROPOSED (Clean - organized by type)

```
03_BUILD/
│
├── index.html                    # Homepage only at root
│
├── pages/                        # All other pages organized
│   ├── company/
│   │   ├── about.html
│   │   └── contact.html
│   │
│   ├── services/
│   │   ├── services.html
│   │   └── request-a-quote.html
│   │
│   └── resources/
│       ├── resources.html
│       └── downloads.html
│
├── products/                     # All product pages
│   ├── eot-cranes/
│   │   ├── index.html           # Pillar page
│   │   ├── single-girder.html
│   │   ├── double-girder.html
│   │   └── hot-metal-ladle.html
│   │
│   ├── gantry-cranes/
│   │   └── index.html
│   │
│   ├── jib-cranes/
│   │   └── index.html
│   │
│   ├── hoists/
│   │   └── index.html
│   │
│   └── spare-parts/
│       └── index.html
│
├── locations/                    # Location pages
│   └── bangalore.html
│
└── assets/                       # All static assets
    ├── css/
    ├── js/
    └── img/
```

## IMPLEMENTATION PLAN

1. Create organized folder structure
2. Move files to proper locations
3. Update all internal links (href paths)
4. Update asset paths (CSS, JS, images)
5. Test all pages work correctly

**Should I implement this clean structure?**
