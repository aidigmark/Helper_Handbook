# The Helper's Handbook — Brand Guide

**By Dr. DoGood**
*Last updated: March 2026*

---

## Brand Overview

**The Helper's Handbook** is a practical, open-source guide that empowers people of all backgrounds to make a meaningful impact. Our brand reflects **trust, energy, and accessibility** — welcoming everyone from first-time volunteers to seasoned advocates.

**Tagline:** *A practical guide for people who want to make the world better*

### Brand Values

| Value | What It Means |
|-------|---------------|
| **Practical** | Evidence-based, actionable guidance over inspiration alone |
| **Inclusive** | Designed for every ability, schedule, and budget |
| **Trustworthy** | Professional, transparent, and research-backed |
| **Empowering** | Small acts compound — everyone can contribute |

---

## Logo

- **Icon:** Heart-pulse (`material/heart-pulse`) — represents care, health, and active impact
- **Usage:** Appears in the site header alongside the wordmark
- **Clear space:** Maintain padding equal to the icon height on all sides
- **Minimum size:** 24px

---

## Color Palette

### Primary Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Black** | `#000000` | Header, footer, navigation backgrounds, primary text |
| **White** | `#FFFFFF` | Light-mode background, header/footer text |
| **Bright Blue** | `#0EA3E8` | Accent, links, buttons, interactive elements, brand highlight |

### Secondary / State Colors

| Color | Hex | Usage |
|-------|-----|-------|
| **Blue Hover** | `#0C8BC4` | Link & button hover states (darkened accent) |
| **Blue Tint 10%** | `rgba(14, 163, 232, 0.1)` | Code block backgrounds, tip admonition fills |
| **Light Gray** | `rgba(255, 255, 255, 0.7)` | Muted footer text, inactive nav tabs |
| **Dark Surface** | `#1A1A1A` | Dark-mode primary background |
| **Darkest Surface** | `#121212` | Dark-mode default background |

### Color Usage Rules

- **Always** pair bright blue (`#0EA3E8`) on black or white backgrounds for sufficient contrast.
- **Never** place bright blue text on medium-gray backgrounds.
- Links are **always** bright blue in both light and dark modes.
- Hover states darken to `#0C8BC4` — do not use other hover colors.

---

## Typography

### Typefaces

| Typeface | Source | Role |
|----------|--------|------|
| **League Spartan** | Google Fonts | Headings (H1–H6), site title, navigation labels |
| **Montserrat** | Google Fonts | Body text, UI elements, descriptions |

### Font Weights

| Element | Typeface | Weight |
|---------|----------|--------|
| H1 | League Spartan | **700 (Bold)** |
| H2–H6 | League Spartan | **600 (Semi-Bold)** |
| Site Title | League Spartan | **700 (Bold)** |
| Body Text | Montserrat | 400 (Regular) |
| Emphasis / Labels | Montserrat | 500–600 |

### Import Reference

```css
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@400;500;600;700;800;900&family=Montserrat:wght@300;400;500;600;700&display=swap');
```

---

## Layout & Structure

### Header

- **Background:** Black (`#000000`)
- **Text & icons:** White (`#FFFFFF`)
- **Hover state:** Bright blue (`#0EA3E8`)
- **Font:** League Spartan, 700

### Footer

- **Background:** Black (`#000000`)
- **Text:** White at 70% opacity (`rgba(255, 255, 255, 0.7)`)
- **Links:** White, hovering to bright blue
- **Social icons:** Heart (Our Story), GitHub

### Navigation Tabs

- **Background:** Black (`#000000`)
- **Inactive text:** White at 70% opacity
- **Active / hover text:** White (`#FFFFFF`)

### Content Area

- **Background:** White (light mode) / `#121212` (dark mode)
- **Max width:** Follows Material for MkDocs defaults
- **Links:** Bright blue, underlined on hover

---

## Interactive Elements

### Buttons

| State | Background | Border | Text |
|-------|-----------|--------|------|
| Default | `#0EA3E8` | `#0EA3E8` | White |
| Hover | `#0C8BC4` | `#0C8BC4` | White |

### Links

| State | Color |
|-------|-------|
| Default | `#0EA3E8` |
| Hover | `#0C8BC4` |
| Visited | `#0EA3E8` (no change) |

### Code Blocks

- **Background:** `rgba(14, 163, 232, 0.1)` — a subtle blue tint
- **Font:** Monospace system default

### Admonitions (Tip)

- **Left border:** `#0EA3E8`
- **Title background:** `rgba(14, 163, 232, 0.1)`
- **Title icon:** `#0EA3E8`

---

## Dark Mode

The site supports automatic dark mode via `prefers-color-scheme`. Key differences:

| Element | Light Mode | Dark Mode |
|---------|-----------|-----------|
| Page background | `#FFFFFF` | `#121212` |
| Primary surface | `#FFFFFF` | `#1A1A1A` |
| Accent color | `#0EA3E8` | `#0EA3E8` (unchanged) |
| Link color | `#0EA3E8` | `#0EA3E8` (unchanged) |
| Header/footer | Black | Black (unchanged) |

The bright blue accent and black header/footer remain **consistent across both modes**, ensuring brand recognition regardless of user preference.

---

## Iconography

- **Icon set:** Material Design Icons + Font Awesome
- **Logo icon:** `material/heart-pulse`
- **Theme toggle:** `material/brightness-7` (light) / `material/brightness-4` (dark)
- **Social:** `fontawesome/solid/heart`, `fontawesome/brands/github`
- **Style:** Outlined, consistent stroke weight, always white on header/footer

---

## Voice & Tone

| Attribute | Do | Don't |
|-----------|-----|-------|
| **Practical** | Give concrete steps and examples | Use vague, inspirational-only language |
| **Inclusive** | Address diverse abilities, budgets, schedules | Assume resources or specific backgrounds |
| **Warm** | Encourage and empower the reader | Guilt, shame, or lecture |
| **Evidence-based** | Cite research and vetted organizations | Make unsubstantiated claims |
| **Accessible** | Use plain language, short sentences | Use jargon or academic complexity |

### Writing Style

- **Headings:** Clear, action-oriented (e.g., "Find Your Local Food Bank" not "Food Banks")
- **Lists:** Use bullet points and tables for scannability
- **Calls to action:** Direct and specific (e.g., "Sign up for a 2-hour shift" not "Get involved")
- **Admonitions:** Use `tip` boxes for quick-win suggestions

---

## File & Asset Reference

| Asset | Location |
|-------|----------|
| Custom CSS | `docs/stylesheets/custom.css` |
| Site config | `mkdocs.yml` |
| Homepage | `docs/index.md` |
| Fonts | Google Fonts (loaded via CSS `@import`) |
| Icons | Material Design Icons + Font Awesome (via MkDocs Material theme) |

---

## Quick Reference Card

```
Brand:        The Helper's Handbook by Dr. DoGood
Tagline:      A practical guide for people who want to make the world better
Primary:      #000000 (Black)
Accent:       #0EA3E8 (Bright Blue)
Hover:        #0C8BC4 (Dark Blue)
Background:   #FFFFFF (Light) / #121212 (Dark)
Headings:     League Spartan, 600–700
Body:         Montserrat, 400
Logo icon:    material/heart-pulse
License:      CC BY-SA 4.0
```
