---
name: Precision Core
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001a42'
  on-tertiary-container: '#3980f4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#adc6ff'
  on-tertiary-fixed: '#001a42'
  on-tertiary-fixed-variant: '#004395'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max-width: 1200px
  gutter: 24px
  margin-mobile: 16px
  bento-gap: 24px
---

## Brand & Style

The brand personality is anchored in the intersection of human career aspirations and machine-learning precision. It must feel **trustworthy** (handling sensitive personal data), **efficient** (saving time in the job hunt), and **innovative** (utilizing cutting-edge LLMs).

The design style follows a **SaaS-modern "Bento" aesthetic**. This approach uses modular containers to organize complex data into digestible, high-contrast chunks. It prioritizes clarity through generous whitespace and a "Quiet Luxury" aesthetic—where the UI recedes to let the user's content (their resume) take center stage. The emotional response should be one of calm confidence; the user should feel that their professional narrative is being handled by a premium, intelligent tool.

## Colors

The palette is professional and high-contrast to ensure maximum readability and a "clean slate" feel.

- **Primary (Deep Blue):** `#0F172A`. Used for core branding, primary headings, and high-emphasis actions. It communicates stability and corporate authority.
- **Secondary (Emerald Green):** `#10B981`. Reserved for "Optimization" states, success indicators, and growth metrics. It signals that the AI has successfully enhanced the content.
- **Tertiary (Action Blue):** `#3B82F6`. Used for interactive elements like links and secondary buttons to differentiate from the authoritative primary blue.
- **Neutral (Slate/White):** A scale ranging from `#F8FAFC` (backgrounds) to `#94A3B8` (secondary text). This provides the necessary "breathing room" for the bento layout.

## Typography

This design system utilizes **Inter** for its systematic, neutral, and highly legible qualities—essential for scanning dense resume text. To introduce a sense of "AI precision" and technical optimization, **JetBrains Mono** is used sparingly for labels, metadata, and ATS-matching percentages.

Headlines should use tighter letter spacing to maintain a "SaaS-modern" look. Body text must maintain a generous line height (1.5x minimum) to reduce eye strain during resume comparison tasks.

## Layout & Spacing

The layout is built on a **12-column fluid grid** that transitions into a **Bento-style modular system** for dashboard views. 

- **Grid:** Use 24px gutters to ensure distinct separation between data modules.
- **Bento Modules:** Components should span 3, 6, or 12 columns. For example, a "Score" module may take 3 columns, while the "Resume Comparison" view takes the full 12 columns or a 6/6 split.
- **Vertical Rhythm:** Follow an 8px spacing scale (8, 16, 24, 32, 48, 64) to maintain consistency in padding and margins.
- **Mobile:** Elements reflow into a single column. The "Original vs. Optimized" view switches from a side-by-side horizontal layout to a stacked vertical layout with a persistent toggle for easy switching.

## Elevation & Depth

To achieve the "SaaS-modern" aesthetic, this design system avoids heavy shadows and instead uses **Tonal Layers** and **Ambient Depth**.

- **Surface Levels:** The main background is the lowest level (`#F8FAFC`). Bento cards sit on top with a pure white background (`#FFFFFF`).
- **Shadows:** Use a single, very soft, highly-diffused shadow for cards: `0px 4px 20px rgba(15, 23, 42, 0.05)`. This creates a "lifted" effect without feeling heavy.
- **Borders:** Use subtle 1px borders (`#E2E8F0`) on all cards to define edges in high-brightness environments. 
- **Comparison View:** The "Optimized" side of a comparison should have a subtle emerald-tinted outer glow to visually distinguish it as the improved version.

## Shapes

The shape language is **Rounded**, reflecting a modern and approachable tool. 

- **Cards/Bento Modules:** Use `rounded-xl` (1.5rem / 24px) to create a soft, friendly container for technical data.
- **Buttons/Inputs:** Use `rounded-md` (0.5rem / 8px) for a more professional, precise look for interactive elements.
- **Chips/Badges:** Use a full pill shape for keyword tags and status indicators to differentiate them from functional buttons.

## Components

- **Bento Cards:** The foundational container. Must include a title and optional icon in the top-left, with content padded at 24px.
- **File Upload Zone:** A large, dashed-border area using the primary blue for the stroke. It should transition to a solid emerald border when a file is successfully detected.
- **Comparison View:** A split-pane component. The "Original" side uses a neutral slate treatment, while the "Optimized" side uses subtle green text highlights for new keywords and bold primary blue for structural improvements.
- **Progress Indicators:** Linear bars with a 12px height. Use a gradient from Tertiary Blue to Secondary Green to represent the "Optimization" journey.
- **Keyword Chips:** Small, pill-shaped elements. "Missing" keywords are shown in a light slate outline; "Optimized" keywords use a soft emerald background with dark green text.
- **Primary Buttons:** Solid Deep Blue (`#0F172A`) with white text. High-contrast, no gradient, subtle lift on hover.