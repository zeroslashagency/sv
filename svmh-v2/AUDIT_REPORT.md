# Website Project Audit & Organization Report
**Date:** 2026-08-03  
**Project:** SVMH-v2 (S.V. Material Handling System website)

---

## EXECUTIVE SUMMARY

**Critical Findings:**
1. ✅ **Downloaded website is WRONG SOURCE** - FullOption Craft renovation company, NOT crane manufacturer
2. ❌ **hub.html is a duplicate/clone** with incorrect navigation paths (relative vs absolute)
3. ⚠️ **Navigation inconsistency** - Mix of `/services.html`, `/pages/services/services.html`, `/about.html`, `/pages/company/about.html`
4. ⚠️ **Multiple index.html files** with same canonical URL in eot-cranes folder
5. 🗑️ **6 .DS_Store files** polluting the repository

---

## PART 1: DOWNLOADED WEBSITE AUDIT

### Location
```
/Users/xoxo/Downloads/us.sitesucker.mac.sitesucker-pro/www.fulloptioncraftreno.ca/
```

### ⛔ CRITICAL ISSUE: WRONG WEBSITE

**This is NOT the SVMH crane manufacturer website!**

The downloaded site is **FullOption Craft** (www.fulloptioncraftreno.ca), a renovation/home improvement company, NOT a crane manufacturer.

**Evidence:**
- Domain: www.fulloptioncraftreno.ca
- Company: "Full Option Craft" 
- Business: Home renovation services
- Schema.org: "WebSite" name: "Full Option Craft"

### Downloaded Website Structure
```
www.fulloptioncraftreno.ca/
├── index.html (2.0M) - Home page
├── about.html (1.3M) - About page
├── contact.html (1.5M) - Contact page
├── projects.html (2.6M) - Projects gallery
├── services.html (1.2M) - Services page
├── privacy-policy.html (1.2M)
├── accessibility-statement.html (1.2M)
└── _downloads.html (313B) - Stub/placeholder

Total: 8 HTML files, 0 subdirectories
No assets downloaded (CSS/JS/images missing)
```

**Files are Wix-generated** (bloated with Wix JavaScript, 1-2MB each)

### ❌ ACTION REQUIRED
**Delete or ignore this download entirely** - it's the wrong source and provides no value to the crane manufacturer website project.

---

## PART 2: 03_BUILD FOLDER AUDIT

### Current Structure
```
03_BUILD/
├── .DS_Store ❌ DELETE
├── .htaccess ✓
├── index.html ✓ (58K) - Homepage
├── sitemap.xml ✓
│
├── assets/
│   ├── .DS_Store ❌ DELETE
│   ├── css/
│   │   ├── base.css
│   │   ├── components.css
│   │   ├── dna.css
│   │   ├── tokens.css
│   │   └── COMPONENT_CONTRACT.md
│   ├── js/
│   │   ├── site.js
│   │   └── JS_CONTRACT.md
│   ├── img/
│   │   ├── .DS_Store ❌ DELETE
│   │   ├── bands/ (3 images)
│   │   ├── cards/ (9 images)
│   │   ├── cutouts/ 
│   │   │   ├── .DS_Store ❌ DELETE
│   │   │   └── (2 images)
│   │   ├── people/ (1 image)
│   │   └── README.md
│   └── docs/
│       └── README.md
│
├── locations/
│   └── bangalore.html ✓ (63K)
│
├── pages/
│   ├── .DS_Store ❌ DELETE
│   ├── company/
│   │   ├── about.html ✓ (5.1K)
│   │   └── contact.html ✓ (22K)
│   ├── resources/
│   │   ├── downloads.html ✓ (19K)
│   │   └── resources.html ✓ (5.1K)
│   └── services/
│       ├── services.html ✓ (5.2K)
│       └── request-a-quote.html ✓ (54K)
│
└── products/
    ├── .DS_Store ❌ DELETE
    ├── eot-cranes/
    │   ├── index.html ✓ (25K) - EOT cranes hub
    │   ├── hub.html ⚠️ DUPLICATE/CLONE - DELETE
    │   └── double-girder.html ✓ (66K) - Product detail page
    ├── gantry-cranes/
    │   └── index.html ✓ (25K)
    ├── hoists/
    │   └── index.html ✓ (25K)
    ├── jib-cranes/
    │   └── index.html ✓ (25K)
    └── spare-parts/
        └── index.html ✓ (24K)
```

**Total Files:** 47 files  
**Total HTML:** 15 files  
**Junk Files:** 6 .DS_Store files

---

## PART 3: PROBLEMS IDENTIFIED

### 🔴 CRITICAL PROBLEMS

#### 1. hub.html is a DUPLICATE with WRONG NAVIGATION

**File:** `03_BUILD/products/eot-cranes/hub.html`

**Problem:**
- Same content as `index.html` in the same folder
- Same canonical URL: `https://www.svind.co.in/eot-cranes`
- Same line count: 525 lines
- **BUT:** Uses relative paths (`../`) instead of absolute paths (`/`)

**Differences (86 lines):**
```diff
hub.html uses:                     index.html uses:
href="../"                    →    href="/"
href="../eot-cranes"          →    href="/products/eot-cranes"
href="../request-a-quote"     →    href="/pages/services/request-a-quote"
href="../crane-spare-parts"   →    href="/products/spare-parts"
href="../about"               →    href="/about"
href="../contact"             →    href="/contact"
```

**Why this is a problem:**
- Creates confusion about which file is "correct"
- Relative paths will break navigation
- Duplicate content = SEO penalty if both accessible
- Wastes development time

**Root Cause:**
You likely created `hub.html` as a working draft/experiment, then corrected the paths in `index.html`, but forgot to delete `hub.html`.

**Solution:** DELETE `hub.html` immediately.

---

#### 2. NAVIGATION PATH INCONSISTENCY

**Problem:** The site uses two different URL patterns for the same pages.

**Index.html links to:**
```
/services.html          (root level - DOESN'T EXIST)
/resources.html         (root level - DOESN'T EXIST)  
/about.html             (root level - DOESN'T EXIST)
```

**Actual file locations:**
```
/pages/company/about.html
/pages/company/contact.html
/pages/resources/resources.html
/pages/resources/downloads.html
/pages/services/services.html
/pages/services/request-a-quote.html
```

**Why this works (currently):**
The `.htaccess` file has URL rewriting enabled:
```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]
```

**But this creates problems:**
1. Files need to exist at root OR in subdirectories, not referenced both ways
2. Broken links if .htaccess fails or is removed
3. Confusion about file organization
4. Canonical URLs don't match file paths

**Affected pages:**
- `/about.html` → should be `/pages/company/about.html` OR moved to root
- `/services.html` → should be `/pages/services/services.html` OR moved to root  
- `/resources.html` → should be `/pages/resources/resources.html` OR moved to root
- `/contact.html` → should be `/pages/company/contact.html` OR moved to root

---

### ⚠️ MODERATE PROBLEMS

#### 3. Double-girder.html has WRONG CSS paths

**File:** `03_BUILD/products/eot-cranes/double-girder.html`

**Problem:**
```html
<link rel="stylesheet" href="../assets/css/tokens.css">
```

Should be:
```html
<link rel="stylesheet" href="../../assets/css/tokens.css">
```

**Current path:** `products/eot-cranes/double-girder.html`  
**Assets path:** `assets/css/`  
**Correct relative:** `../../assets/css/`  
**Currently uses:** `../assets/css/` ❌

This will cause CSS to NOT load on double-girder.html page.

---

#### 4. .DS_Store Files Polluting Repository

**Files to delete:**
```
03_BUILD/.DS_Store
03_BUILD/assets/.DS_Store
03_BUILD/assets/img/.DS_Store
03_BUILD/assets/img/cutouts/.DS_Store
03_BUILD/pages/.DS_Store
03_BUILD/products/.DS_Store
```

These are macOS metadata files that should NEVER be committed to a repository.

**Add to .gitignore:**
```
.DS_Store
**/.DS_Store
```

---

### ℹ️ MINOR ISSUES / OBSERVATIONS

#### 5. URL Structure Philosophy

The site canonical URLs suggest flat structure:
```
https://www.svind.co.in/
https://www.svind.co.in/eot-cranes
https://www.svind.co.in/about
https://www.svind.co.in/services
https://www.svind.co.in/downloads
```

But the file structure is hierarchical:
```
03_BUILD/index.html
03_BUILD/products/eot-cranes/index.html
03_BUILD/pages/company/about.html
03_BUILD/pages/services/services.html
03_BUILD/pages/resources/downloads.html
```

This is OK if using .htaccess rewriting, but creates organizational confusion.

---

## PART 4: CANONICAL URL vs FILE LOCATION MAP

| Canonical URL | File Location | Status |
|--------------|---------------|--------|
| `/` | `03_BUILD/index.html` | ✅ |
| `/eot-cranes` | `03_BUILD/products/eot-cranes/index.html` | ✅ |
| `/eot-cranes/double-girder` | `03_BUILD/products/eot-cranes/double-girder.html` | ⚠️ CSS paths broken |
| `/gantry-cranes` | `03_BUILD/products/gantry-cranes/index.html` | ✅ |
| `/hoists` | `03_BUILD/products/hoists/index.html` | ✅ |
| `/jib-cranes` | `03_BUILD/products/jib-cranes/index.html` | ✅ |
| `/crane-spare-parts` | `03_BUILD/products/spare-parts/index.html` | ✅ |
| `/locations/bangalore` | `03_BUILD/locations/bangalore.html` | ✅ |
| `/about` | `03_BUILD/pages/company/about.html` | ❌ Linked as `/about.html` (doesn't exist at root) |
| `/contact` | `03_BUILD/pages/company/contact.html` | ❌ Linked as `/contact.html` (doesn't exist at root) |
| `/services` | `03_BUILD/pages/services/services.html` | ❌ Linked as `/services.html` (doesn't exist at root) |
| `/downloads` | `03_BUILD/pages/resources/downloads.html` | ❌ Linked as `/downloads` (works via rewrite) |
| `/resources` | `03_BUILD/pages/resources/resources.html` | ❌ Linked as `/resources.html` (doesn't exist at root) |
| `/request-a-quote` | `03_BUILD/pages/services/request-a-quote.html` | ✅ Correctly linked |

---

## PART 5: PROPOSED CLEAN STRUCTURE

### Option A: FLAT STRUCTURE (Recommended for SEO)

Move files to match canonical URLs:

```
03_BUILD/
├── .htaccess
├── index.html
├── sitemap.xml
│
├── about.html          ← MOVE from pages/company/
├── contact.html        ← MOVE from pages/company/
├── services.html       ← MOVE from pages/services/
├── resources.html      ← MOVE from pages/resources/
├── downloads.html      ← MOVE from pages/resources/
├── request-a-quote.html ← MOVE from pages/services/
│
├── locations/
│   └── bangalore.html
│
├── eot-cranes/         ← RENAME from products/eot-cranes/
│   ├── index.html
│   └── double-girder.html
│
├── gantry-cranes/      ← RENAME from products/gantry-cranes/
│   └── index.html
│
├── hoists/             ← RENAME from products/hoists/
│   └── index.html
│
├── jib-cranes/         ← RENAME from products/jib-cranes/
│   └── index.html
│
├── spare-parts/        ← RENAME from products/spare-parts/
│   └── index.html
│
└── assets/
    ├── css/
    ├── js/
    ├── img/
    └── docs/
```

**Advantages:**
- File paths match canonical URLs exactly
- No .htaccess rewriting needed (more portable)
- Clear, predictable structure
- Easier debugging

**Disadvantages:**
- More files at root level
- Less semantic organization (no "pages" or "products" grouping)

---

### Option B: HIERARCHICAL STRUCTURE (Current, needs fixes)

Keep current structure but fix links and create proper rewrites:

```
03_BUILD/
├── .htaccess (update rewrite rules)
├── index.html
├── sitemap.xml
│
├── locations/
│   └── bangalore.html
│
├── pages/
│   ├── company/
│   │   ├── about.html       → accessible as /about
│   │   └── contact.html     → accessible as /contact
│   ├── resources/
│   │   ├── downloads.html   → accessible as /downloads
│   │   └── resources.html   → accessible as /resources
│   └── services/
│       ├── services.html    → accessible as /services
│       └── request-a-quote.html → accessible as /request-a-quote
│
└── products/
    ├── eot-cranes/
    │   ├── index.html           → accessible as /eot-cranes
    │   └── double-girder.html   → accessible as /eot-cranes/double-girder
    ├── gantry-cranes/
    │   └── index.html           → accessible as /gantry-cranes
    ├── hoists/
    │   └── index.html           → accessible as /hoists
    ├── jib-cranes/
    │   └── index.html           → accessible as /jib-cranes
    └── spare-parts/
        └── index.html           → accessible as /spare-parts
```

**Advantages:**
- Semantic grouping (products/, pages/)
- Easier to understand content categories
- Less cluttered root

**Disadvantages:**
- Requires .htaccess rewriting
- File paths don't match URLs
- More complex debugging
- Rewrite rules must be perfect

---

## PART 6: STEP-BY-STEP MIGRATION PLAN

### PHASE 1: CLEANUP (IMMEDIATE)

#### Step 1: Delete junk files
```bash
cd /Users/xoxo/Documents/resreah/sv/svmh-v2/03_BUILD

# Delete all .DS_Store files
find . -name ".DS_Store" -type f -delete

# Verify deletion
find . -name ".DS_Store"
```

#### Step 2: Delete duplicate hub.html
```bash
# Backup first (optional)
cp products/eot-cranes/hub.html products/eot-cranes/hub.html.backup

# Delete
rm products/eot-cranes/hub.html

# Verify
ls products/eot-cranes/
```

#### Step 3: Add .gitignore rules
```bash
# Create/update .gitignore in project root
echo ".DS_Store" >> .gitignore
echo "**/.DS_Store" >> .gitignore
echo "*.backup" >> .gitignore
```

---

### PHASE 2: FIX CRITICAL ISSUES

#### Step 4: Fix double-girder.html CSS paths
```bash
# File: 03_BUILD/products/eot-cranes/double-girder.html
# Lines 9-12

# FIND:
<link rel="stylesheet" href="../assets/css/tokens.css">
<link rel="stylesheet" href="../assets/css/base.css">
<link rel="stylesheet" href="../assets/css/components.css">
<link rel="stylesheet" href="../assets/css/dna.css">

# REPLACE WITH:
<link rel="stylesheet" href="../../assets/css/tokens.css">
<link rel="stylesheet" href="../../assets/css/base.css">
<link rel="stylesheet" href="../../assets/css/components.css">
<link rel="stylesheet" href="../../assets/css/dna.css">
```

---

### PHASE 3: CHOOSE STRUCTURE & MIGRATE

#### Option A: FLAT STRUCTURE MIGRATION

```bash
cd /Users/xoxo/Documents/resreah/sv/svmh-v2/03_BUILD

# Move company pages to root
mv pages/company/about.html ./about.html
mv pages/company/contact.html ./contact.html

# Move service pages to root
mv pages/services/services.html ./services.html
mv pages/services/request-a-quote.html ./request-a-quote.html

# Move resource pages to root
mv pages/resources/resources.html ./resources.html
mv pages/resources/downloads.html ./downloads.html

# Rename products/ folder to match canonical URLs
mv products/eot-cranes ./eot-cranes
mv products/gantry-cranes ./gantry-cranes
mv products/hoists ./hoists
mv products/jib-cranes ./jib-cranes
mv products/spare-parts ./spare-parts

# Delete empty folders
rm -rf pages/
rm -rf products/

# Update all CSS paths in moved files
# about.html, contact.html, services.html, etc.
# FROM: href="../../assets/css/
# TO:   href="assets/css/

# Update CSS paths in product folders
# FROM: href="../../assets/css/
# TO:   href="../assets/css/
```

**Files requiring CSS path updates after moving:**
- `about.html` → `href="assets/css/"`
- `contact.html` → `href="assets/css/"`
- `services.html` → `href="assets/css/"`
- `request-a-quote.html` → `href="assets/css/"`
- `resources.html` → `href="assets/css/"`
- `downloads.html` → `href="assets/css/"`
- `eot-cranes/index.html` → `href="../assets/css/"` (no change)
- `eot-cranes/double-girder.html` → `href="../assets/css/"` (change from `href="../../assets/css/"`)

---

#### Option B: HIERARCHICAL STRUCTURE (Keep current, fix links)

**Update .htaccess:**
```apache
RewriteEngine On

# Product rewrites
RewriteRule ^eot-cranes/?$ products/eot-cranes/index.html [L]
RewriteRule ^eot-cranes/(.+)$ products/eot-cranes/$1 [L]
RewriteRule ^gantry-cranes/?$ products/gantry-cranes/index.html [L]
RewriteRule ^hoists/?$ products/hoists/index.html [L]
RewriteRule ^jib-cranes/?$ products/jib-cranes/index.html [L]
RewriteRule ^spare-parts/?$ products/spare-parts/index.html [L]
RewriteRule ^crane-spare-parts/?$ products/spare-parts/index.html [L]

# Company pages
RewriteRule ^about/?$ pages/company/about.html [L]
RewriteRule ^contact/?$ pages/company/contact.html [L]

# Service pages
RewriteRule ^services/?$ pages/services/services.html [L]
RewriteRule ^request-a-quote/?$ pages/services/request-a-quote.html [L]

# Resource pages
RewriteRule ^resources/?$ pages/resources/resources.html [L]
RewriteRule ^downloads/?$ pages/resources/downloads.html [L]

# Default rule for other pages
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]
```

**Update index.html navigation links:**
```html
<!-- FIND these -->
<a href="/services.html">
<a href="/resources.html">
<a href="/about.html">

<!-- REPLACE with -->
<a href="/services">
<a href="/resources">
<a href="/about">
```

---

### PHASE 4: VALIDATION

#### Verify all links work
```bash
# Install link checker (if needed)
npm install -g broken-link-checker

# Check all internal links
blc http://localhost:8000 -ro
```

#### Manual checklist:
- [ ] Homepage loads with CSS
- [ ] All navigation links work
- [ ] Product pages load correctly
- [ ] Double-girder.html CSS loads
- [ ] No 404 errors in browser console
- [ ] All images load
- [ ] Breadcrumbs work
- [ ] Footer links work

---

## PART 7: EXACT COMMAND SEQUENCE

### RECOMMENDED: FLAT STRUCTURE MIGRATION

```bash
#!/bin/bash
# SVMH Website Cleanup & Migration Script
# Run from: /Users/xoxo/Documents/resreah/sv/svmh-v2

cd 03_BUILD

echo "=== Phase 1: Cleanup ==="

# Delete .DS_Store files
find . -name ".DS_Store" -type f -delete
echo "✓ Deleted .DS_Store files"

# Delete duplicate hub.html
rm products/eot-cranes/hub.html
echo "✓ Deleted hub.html duplicate"

echo ""
echo "=== Phase 2: Backup ==="

# Create backup
cd ..
tar -czf 03_BUILD_backup_$(date +%Y%m%d_%H%M%S).tar.gz 03_BUILD/
echo "✓ Created backup"

cd 03_BUILD

echo ""
echo "=== Phase 3: File Migration ==="

# Move pages to root
mv pages/company/about.html ./about.html
mv pages/company/contact.html ./contact.html
mv pages/services/services.html ./services.html
mv pages/services/request-a-quote.html ./request-a-quote.html
mv pages/resources/resources.html ./resources.html
mv pages/resources/downloads.html ./downloads.html
echo "✓ Moved pages to root"

# Rename product folders
mv products/eot-cranes ./eot-cranes
mv products/gantry-cranes ./gantry-cranes
mv products/hoists ./hoists
mv products/jib-cranes ./jib-cranes
mv products/spare-parts ./spare-parts
echo "✓ Moved product folders"

# Delete empty directories
rm -rf pages/
rm -rf products/
echo "✓ Removed empty directories"

echo ""
echo "=== Phase 4: Update CSS Paths ==="

# Root-level pages: ../../assets/css/ → assets/css/
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' about.html
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' contact.html
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' services.html
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' request-a-quote.html
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' resources.html
sed -i '' 's|href="../../assets/css/|href="assets/css/|g' downloads.html
echo "✓ Updated root-level page CSS paths"

# bangalore.html: ../assets/css/ → assets/css/
sed -i '' 's|href="../assets/css/|href="assets/css/|g' locations/bangalore.html
echo "✓ Updated bangalore.html CSS paths"

# double-girder.html: ../assets/css/ → ../assets/css/ (was wrong before)
sed -i '' 's|href="../assets/css/|href="../assets/css/|g' eot-cranes/double-girder.html
echo "✓ Fixed double-girder.html CSS paths"

echo ""
echo "=== Phase 5: Update Internal Links ==="

# Update index.html navigation
sed -i '' 's|href="/products/eot-cranes"|href="/eot-cranes"|g' index.html
sed -i '' 's|href="/products/gantry-cranes"|href="/gantry-cranes"|g' index.html
sed -i '' 's|href="/products/hoists"|href="/hoists"|g' index.html
sed -i '' 's|href="/products/jib-cranes"|href="/jib-cranes"|g' index.html
sed -i '' 's|href="/products/spare-parts"|href="/spare-parts"|g' index.html
echo "✓ Updated navigation links"

echo ""
echo "=== MIGRATION COMPLETE ==="
echo ""
echo "Next steps:"
echo "1. Test locally: python3 -m http.server 8000"
echo "2. Open http://localhost:8000"
echo "3. Check all navigation links"
echo "4. Verify CSS loads on all pages"
echo "5. Run link checker"
echo ""
echo "Backup location: ../03_BUILD_backup_*.tar.gz"
```

---

## PART 8: FINAL FILE MANIFEST

### After cleanup and flat structure migration:

```
03_BUILD/
├── .htaccess
├── index.html
├── sitemap.xml
├── about.html
├── contact.html
├── services.html
├── request-a-quote.html
├── resources.html
├── downloads.html
│
├── locations/
│   └── bangalore.html
│
├── eot-cranes/
│   ├── index.html
│   └── double-girder.html
│
├── gantry-cranes/
│   └── index.html
│
├── hoists/
│   └── index.html
│
├── jib-cranes/
│   └── index.html
│
├── spare-parts/
│   └── index.html
│
└── assets/
    ├── css/
    │   ├── base.css
    │   ├── components.css
    │   ├── dna.css
    │   ├── tokens.css
    │   └── COMPONENT_CONTRACT.md
    ├── js/
    │   ├── site.js
    │   └── JS_CONTRACT.md
    ├── img/
    │   ├── bands/ (3 images)
    │   ├── cards/ (9 images)
    │   ├── cutouts/ (2 images)
    │   ├── people/ (1 image)
    │   └── README.md
    └── docs/
        └── README.md
```

**Total:** 15 HTML files, 29 CSS/JS/doc files, 15 images = 59 files (clean)

---

## SUMMARY

### What's broken:
1. ❌ Downloaded website is wrong source (FullOption Craft, not SVMH)
2. ❌ hub.html is duplicate with broken navigation
3. ❌ double-girder.html has wrong CSS paths
4. ❌ Navigation links point to non-existent root files
5. ❌ 6 .DS_Store junk files

### What needs to be done:
1. **Delete** downloaded website (wrong source)
2. **Delete** hub.html duplicate
3. **Delete** all .DS_Store files
4. **Fix** double-girder.html CSS paths
5. **Choose structure** (flat vs hierarchical)
6. **Migrate files** to match canonical URLs
7. **Update** all internal links
8. **Test** thoroughly

### Recommended approach:
**FLAT STRUCTURE** - Move files to root to match canonical URLs. Simpler, more portable, easier to debug.

---

## APPENDIX: Quick Reference

### Files to DELETE:
```
03_BUILD/.DS_Store
03_BUILD/assets/.DS_Store
03_BUILD/assets/img/.DS_Store
03_BUILD/assets/img/cutouts/.DS_Store
03_BUILD/pages/.DS_Store
03_BUILD/products/.DS_Store
03_BUILD/products/eot-cranes/hub.html
```

### Navigation Links to Fix:
```
/products/eot-cranes → /eot-cranes
/products/gantry-cranes → /gantry-cranes
/products/hoists → /hoists
/products/jib-cranes → /jib-cranes
/products/spare-parts → /spare-parts
/services.html → /services
/resources.html → /resources
/about.html → /about
```

### CSS Path Corrections:
```
double-girder.html: ../assets/css/ → ../../assets/css/ (BEFORE migration)
                    or ../assets/css/ (AFTER migration to eot-cranes/ at root)

Root pages:        ../../assets/css/ → assets/css/ (AFTER moving to root)
bangalore.html:    ../assets/css/ → assets/css/ (IF locations/ moves to root)
```

---

**END OF REPORT**
