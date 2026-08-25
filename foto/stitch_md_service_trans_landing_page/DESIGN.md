---
name: Reliability in Motion
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#43474e'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#73777f'
  outline-variant: '#c3c6cf'
  surface-tint: '#3e6187'
  primary: '#001f3a'
  on-primary: '#ffffff'
  primary-container: '#0b3559'
  on-primary-container: '#7c9ec8'
  inverse-primary: '#a7c9f5'
  secondary: '#954a00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8a29'
  on-secondary-container: '#632f00'
  tertiary: '#1b1f21'
  on-tertiary: '#ffffff'
  tertiary-container: '#303436'
  on-tertiary-container: '#999c9f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e4ff'
  primary-fixed-dim: '#a7c9f5'
  on-primary-fixed: '#001d36'
  on-primary-fixed-variant: '#25496e'
  secondary-fixed: '#ffdcc6'
  secondary-fixed-dim: '#ffb785'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#713700'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Open Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Open Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  price-display:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  section-gap: 80px
  stack-sm: 12px
  stack-md: 24px
---

## Brand & Style
The design system for this logistics service is built on a foundation of **Seriosität (Trustworthiness)** and **Local Precision**. It targets a demographic that values efficiency and transparency during high-stress transitions like moving. 

The aesthetic is a refined **Corporate Modern** style, leaning heavily into a "Flat Plus" approach: clean, high-contrast interfaces with subtle depth cues. The visual language uses generous whitespace to reduce cognitive load, reflecting the organized and calm nature of a professional moving service. The tone is authoritative yet approachable, grounding the brand as a reliable local partner in the Franconia region.

## Colors
The palette is engineered for professional authority and urgent action. 
- **Deep Navy Blue (#0B3559):** Used for primary navigation, headers, and hero sections to establish an immediate sense of institutional trust and stability.
- **Warm Orange (#F0801E):** Reserved exclusively for Calls to Action (CTAs), price highlights, and critical "Get a Quote" touchpoints. It provides a high-contrast warmth that directs the eye to conversion paths.
- **Light Blue-Grey (#F7F9FC):** The foundational background color, chosen to feel cleaner and more modern than pure white, reducing screen glare while maintaining a "fresh start" feeling.
- **Functional Grays:** Used for secondary text and borders to maintain a clear visual hierarchy.

## Typography
The typography system balances modern geometric strength with technical precision. 
- **Plus Jakarta Sans** provides a bold, contemporary feel for headings, ensuring the brand feels up-to-date and energetic. 
- **Open Sans** handles the bulk of informational content, offering high legibility across all screen sizes. 
- **JetBrains Mono** is utilized as a tactical accent for non-prose data: phone numbers, pricing, and technical specifications. This monospaced choice signals transparency and "unfudged" data, reinforcing the value of efficiency.

## Layout & Spacing
This system utilizes a **12-column fluid grid** for desktop and a **single-column stack** for mobile. 
- **Vertical Rhythm:** Sections are separated by a generous `80px` gap to allow the content to breathe and prevent the "cluttered warehouse" feel often found in logistics websites.
- **The Multi-step Form:** Should be centered with a maximum width of `720px` to maintain focus and minimize scanning fatigue.
- **Horizontal Timeline:** On mobile, this should transform into a vertical stepper to ensure the technical font remains legible.

## Elevation & Depth
Depth is conveyed through **Tonal Layering** and **Soft Ambient Shadows**. 
- Surfaces use a base level of white (#FFFFFF) against the Light Blue-Grey background.
- Shadows are extremely diffused: `0px 4px 20px rgba(11, 53, 89, 0.08)`. The blue tint in the shadow ensures that even the elevation feels "on-brand" and integrated rather than a generic gray drop-shadow.
- For "Why Us" dark cards, use the Primary color as the surface with no shadow, relying on contrast to define the boundary.

## Shapes
A consistent **16px (1rem)** corner radius is applied to all primary UI elements (cards, containers, inputs). This "Rounded" setting softens the corporate aesthetic, making the service feel more approachable and modern. 
- **Buttons:** Use a `1rem` radius for a sturdy, rectangular-but-soft appearance.
- **Service Tags:** Use pill-shaping (`999px`) to distinguish them from interactive buttons.
- **Icons:** Should feature slightly rounded stroke terminals to match the font geometry.

## Components
- **Sticky Header:** A white background with a subtle bottom border (`1px solid rgba(11, 53, 89, 0.1)`). The logo sits on the left, with the phone number in `label-mono` on the right for instant utility.
- **Service Cards Grid:** White surfaces with 16px padding. Icons should be Primary Blue, and headlines should use `headline-md`.
- **Dark "Why Us" Cards:** Use the Primary Blue background with white text. High-contrast and impactful.
- **Multi-step Form:** Use a progress bar at the top in Accent Orange. Input fields should have a `2px` border in Light Blue-Grey that turns Primary Blue on focus.
- **Trust Badges:** Low-opacity background versions of the Primary Blue, keeping the logos legible but secondary to the Hero text.
- **Review Cards:** Features a small avatar, `body-md` text, and a row of stars in Accent Orange.
- **Service Area Tags:** Small, Light Blue-Grey chips with Primary Blue text in `label-mono`, used to list covered cities (Nürnberg, Fürth, Erlangen).