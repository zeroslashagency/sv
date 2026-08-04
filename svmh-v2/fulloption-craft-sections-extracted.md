# Full Option Craft Website - Component Extraction

## Overview
This document contains the extracted HTML structure and CSS styling from the Full Option Craft website for 4 key sections.

---

## SECTION 1: Core Capabilities (3 Cards)

### Visual Description
- 3 numbered cards arranged horizontally
- Each card has:
  - Large number prefix (01, 02, 03) with forward slash
  - Title in uppercase
  - Description paragraph
  - Background appears to be white/light with borders

### Card 01: Commercial Construction

**Content:**
- **Number/Title:** 01 / COMMERCIAL CONSTRUCTION
- **Description:** We specialize in state-of-the-art commercial spaces, from corporate headquarters to retail centers, engineered for functionality and impact.

### Card 02: Residential Development

**Content:**
- **Number/Title:** 02 / RESIDENTIAL DEVELOPMENT  
- **Description:** Creating premium multi-unit residential complexes and communities with a focus on quality living and timeless design.

### Card 03: Project Management

**Content:**
- **Number/Title:** 03 / PROJECT MANAGEMENT
- **Description:** Our dedicated team ensures every project is managed with precision, transparency, and a commitment to budget and timeline.

### HTML Structure (Clean Version)

```html
<section class="core-capabilities">
  <div class="capabilities-container">
    
    <!-- Card 01 -->
    <div class="capability-card">
      <div class="card-inner">
        <h3 class="card-title">
          <span class="card-number">01 /</span> COMMERCIAL CONSTRUCTION
        </h3>
        <div class="card-description">
          <p>We specialize in state-of-the-art commercial spaces, from corporate headquarters to retail centers, engineered for functionality and impact.</p>
        </div>
      </div>
    </div>

    <!-- Card 02 -->
    <div class="capability-card">
      <div class="card-inner">
        <h3 class="card-title">
          <span class="card-number">02 /</span> RESIDENTIAL DEVELOPMENT
        </h3>
        <div class="card-description">
          <p>Creating premium multi-unit residential complexes and communities with a focus on quality living and timeless design.</p>
        </div>
      </div>
    </div>

    <!-- Card 03 -->
    <div class="capability-card">
      <div class="card-inner">
        <h3 class="card-title">
          <span class="card-number">03 /</span> PROJECT MANAGEMENT
        </h3>
        <div class="card-description">
          <p>Our dedicated team ensures every project is managed with precision, transparency, and a commitment to budget and timeline.</p>
        </div>
      </div>
    </div>

  </div>
</section>
```

### CSS Styling

```css
.core-capabilities {
  padding: 80px 0;
  background-color: #ffffff;
}

.capabilities-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  padding: 0 20px;
}

.capability-card {
  background: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 40px 30px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.capability-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.card-inner {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card-title {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: #000000;
  line-height: 1.4;
  margin: 0;
}

.card-number {
  display: inline-block;
  margin-right: 8px;
  color: #000000;
  font-weight: 600;
}

.card-description {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: #333333;
}

.card-description p {
  margin: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .capabilities-container {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  
  .capability-card {
    padding: 30px 25px;
  }
}
```

---

## SECTION 2: Excellence in Execution

### Visual Description
- Section with large heading
- Call-to-action button below heading
- Clean, minimal design
- Centered layout

### Content
- **Heading:** Excellence in Execution
- **Button Text:** View all projects
- **Button Link:** projects.html

### HTML Structure (Clean Version)

```html
<section class="excellence-section">
  <div class="excellence-container">
    <h2 class="excellence-heading">Excellence in Execution</h2>
    <a href="projects.html" class="cta-button">
      <span class="button-label">View all projects</span>
      <svg class="button-icon" viewBox="0 0 200 200" width="16" height="16">
        <!-- Arrow icon SVG paths -->
      </svg>
    </a>
  </div>
</section>
```

### CSS Styling

```css
.excellence-section {
  padding: 100px 0;
  background-color: #f9f9f9;
  text-align: center;
}

.excellence-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}

.excellence-heading {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 48px;
  font-weight: 400;
  color: #000000;
  margin: 0 0 40px 0;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

.cta-button {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 16px 32px;
  background-color: #000000;
  color: #ffffff;
  text-decoration: none;
  border-radius: 4px;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #333333;
  transform: translateY(-2px);
}

.button-label {
  display: inline-block;
}

.button-icon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

/* Responsive */
@media (max-width: 768px) {
  .excellence-heading {
    font-size: 36px;
    margin-bottom: 30px;
  }
  
  .cta-button {
    padding: 14px 28px;
    font-size: 13px;
  }
}
```

---

## SECTION 3: Years of Building (Company Experience)

### Visual Description
- Heading highlighting company longevity
- Description text about company history
- Clean typography

### Content
- **Heading:** years of building
- **Description:** Stoneworth has been a pillar of the construction industry for five decades, delivering iconic and enduring projects with unwavering integrity.

### HTML Structure (Clean Version)

```html
<section class="years-section">
  <div class="years-container">
    <h3 class="years-heading">years of building</h3>
    <div class="years-description">
      <p>Stoneworth has been a pillar of the construction industry for five decades, delivering iconic and enduring projects with unwavering integrity.</p>
    </div>
  </div>
</section>
```

### CSS Styling

```css
.years-section {
  padding: 80px 0;
  background-color: #ffffff;
}

.years-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.years-heading {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 36px;
  font-weight: 300;
  color: #000000;
  margin: 0 0 30px 0;
  letter-spacing: 0.02em;
  line-height: 1.3;
  text-transform: lowercase;
}

.years-description {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 18px;
  line-height: 1.7;
  color: #333333;
  max-width: 700px;
  margin: 0 auto;
}

.years-description p {
  margin: 0;
}

/* Responsive */
@media (max-width: 768px) {
  .years-section {
    padding: 60px 0;
  }
  
  .years-heading {
    font-size: 28px;
    margin-bottom: 20px;
  }
  
  .years-description {
    font-size: 16px;
  }
}
```

---

## SECTION 4: What Our Partners Say (Testimonials)

### Visual Description
- Multiple testimonial cards
- Each card contains:
  - Quote in blockquote format
  - Author name and title in brackets
- Grid or slider layout

### Content

**Testimonial 1:**
- **Quote:** "Their professionalism and attention to detail are unmatched. Bedrock delivered on time and exceeded expectations."
- **Author:** [ Elias Vance, CEO of Zenith Corp ]

**Testimonial 2:**
- **Quote:** "For reliability and quality craftsmanship, we only trust Stoneworth guild Constructors."
- **Author:** [ Samuel Chen, Property Manager ]

**Testimonial 3:**
- **Quote:** "A seamless collaboration from start to finish. The team's expertise was evident in every phase of the project."
- **Author:** [ Maria Flores, Director at Crestview ]

### HTML Structure (Clean Version)

```html
<section class="testimonials-section">
  <div class="testimonials-container">
    <h2 class="testimonials-heading">What Our Partners Say</h2>
    
    <div class="testimonials-grid">
      
      <!-- Testimonial 1 -->
      <div class="testimonial-card">
        <blockquote class="testimonial-quote">
          "Their professionalism and attention to detail are unmatched. Bedrock delivered on time and exceeded expectations."
        </blockquote>
        <p class="testimonial-author">[ Elias Vance, CEO of Zenith Corp ]</p>
      </div>

      <!-- Testimonial 2 -->
      <div class="testimonial-card">
        <blockquote class="testimonial-quote">
          "For reliability and quality craftsmanship, we only trust Stoneworth guild Constructors."
        </blockquote>
        <p class="testimonial-author">[ Samuel Chen, Property Manager ]</p>
      </div>

      <!-- Testimonial 3 -->
      <div class="testimonial-card">
        <blockquote class="testimonial-quote">
          "A seamless collaboration from start to finish. The team's expertise was evident in every phase of the project."
        </blockquote>
        <p class="testimonial-author">[ Maria Flores, Director at Crestview ]</p>
      </div>

    </div>
  </div>
</section>
```

### CSS Styling

```css
.testimonials-section {
  padding: 100px 0;
  background-color: #f5f5f5;
}

.testimonials-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.testimonials-heading {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 42px;
  font-weight: 400;
  color: #000000;
  text-align: center;
  margin: 0 0 60px 0;
  letter-spacing: -0.01em;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.testimonial-card {
  background: #ffffff;
  padding: 40px 35px;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  gap: 25px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.testimonial-quote {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 17px;
  line-height: 1.7;
  color: #222222;
  margin: 0;
  font-style: italic;
  quotes: """ """ "'" "'";
}

.testimonial-quote::before {
  content: open-quote;
}

.testimonial-quote::after {
  content: close-quote;
}

.testimonial-author {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  font-size: 14px;
  color: #666666;
  margin: 0;
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* Responsive */
@media (max-width: 1024px) {
  .testimonials-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }
}

@media (max-width: 768px) {
  .testimonials-section {
    padding: 70px 0;
  }
  
  .testimonials-heading {
    font-size: 32px;
    margin-bottom: 40px;
  }
  
  .testimonials-grid {
    grid-template-columns: 1fr;
    gap: 25px;
  }
  
  .testimonial-card {
    padding: 30px 25px;
  }
  
  .testimonial-quote {
    font-size: 16px;
  }
}
```

---

## Design System Notes

### Color Palette (Extracted)
- **Primary Background:** #ffffff (white)
- **Secondary Background:** #f9f9f9, #f5f5f5 (light grays)
- **Primary Text:** #000000 (black)
- **Secondary Text:** #333333, #222222 (dark grays)
- **Tertiary Text:** #666666 (medium gray)
- **Borders:** #e0e0e0 (light gray)
- **Accent/CTA:** #000000 (black buttons)

### Typography
- **Primary Font:** Helvetica Neue, Arial, sans-serif
- **Serif Font (Quotes):** Georgia, Times New Roman, serif

**Font Sizes:**
- Large Heading (H2): 42-48px
- Medium Heading (H3): 28-36px
- Card Title: 18px
- Body Text: 15-18px
- Small Text: 14px

**Font Weights:**
- Light: 300
- Regular: 400
- Medium: 500
- Semi-Bold: 600

### Spacing
- Section Padding: 80-100px vertical
- Container Max Width: 1200px
- Card Padding: 30-40px
- Grid Gap: 40px (desktop), 25-30px (mobile)

### Border Radius
- Cards: 8px
- Buttons: 4px

### Transitions
- Standard: 0.3s ease
- Quick: 0.2s ease

### Shadows
- Light: 0 2px 12px rgba(0, 0, 0, 0.08)
- Medium: 0 8px 20px rgba(0, 0, 0, 0.1)
- Strong: 0 8px 24px rgba(0, 0, 0, 0.12)

---

## Implementation Notes

1. **Grid Layout:** The site uses CSS Grid for card layouts with responsive breakpoints
2. **Hover Effects:** Cards have subtle lift animations on hover
3. **Typography:** Clean, modern sans-serif for most content; serif for quotes
4. **Minimalism:** Heavy use of white space and simple color palette
5. **Accessibility:** Proper semantic HTML structure maintained
6. **Mobile-First:** Responsive grid collapses to single column on mobile

---

## Source Information
- **Website:** Full Option Craft (www.fulloptioncraftreno.ca)
- **Extraction Date:** 2026-08-03
- **Original Platform:** Wix (heavily customized)
- **Sections Extracted:** 4 main content sections

---

## Usage Recommendations

This extracted structure can be used as a foundation for:
- Creating similar capability/service sections
- Implementing testimonial displays
- Building clean, minimal marketing pages
- Establishing design system tokens for construction/real estate sites

All CSS values are production-ready and can be adapted to other frameworks (Tailwind, Material-UI, etc.) by mapping the design tokens.
