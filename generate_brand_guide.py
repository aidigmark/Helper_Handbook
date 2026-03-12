#!/usr/bin/env python3
"""
MODRN Marketing Solutions — Brand Guide PDF Generator
Generates a professional, multi-page brand guide PDF.
"""

import os, sys

# Work around broken cryptography module in this environment
sys.modules['cryptography'] = type(sys)('cryptography')

from fpdf import FPDF

# Paths
FONT_DIR = os.path.join(os.path.dirname(__file__), "brand-assets", "fonts")
OUTPUT = os.path.join(os.path.dirname(__file__), "MODRN_Brand_Guide.pdf")

# Brand colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MODRN_BLUE = (41, 171, 226)  # #29ABE2
DARK_BLUE = (12, 139, 196)   # #0C8BC4
LIGHT_GRAY = (245, 245, 245)
MID_GRAY = (130, 130, 130)
DARK_GRAY = (51, 51, 51)


class BrandGuidePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False)
        self._load_fonts()

    def _load_fonts(self):
        self.add_font("Montserrat", "", os.path.join(FONT_DIR, "Montserrat-Regular.ttf"))
        self.add_font("Montserrat", "B", os.path.join(FONT_DIR, "Montserrat-Bold.ttf"))
        self.add_font("MontserratSB", "", os.path.join(FONT_DIR, "Montserrat-SemiBold.ttf"))
        self.add_font("MontserratLight", "", os.path.join(FONT_DIR, "Montserrat-Light.ttf"))
        self.add_font("LeagueSpartan", "B", os.path.join(FONT_DIR, "LeagueSpartan-Bold.ttf"))
        self.add_font("LeagueSpartanSB", "", os.path.join(FONT_DIR, "LeagueSpartan-SemiBold.ttf"))

    # ── Drawing helpers ──────────────────────────────────────────────

    def _bg(self, r, g, b):
        self.set_fill_color(r, g, b)
        self.rect(0, 0, 210, 297, "F")

    def _section_title(self, text, y=None):
        if y is not None:
            self.set_y(y)
        self.set_font("LeagueSpartan", "B", 28)
        self.set_text_color(*BLACK)
        self.cell(0, 14, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*MODRN_BLUE)
        self.set_line_width(1.2)
        self.line(20, self.get_y() + 2, 80, self.get_y() + 2)
        self.ln(10)

    def _page_header(self, num, title):
        """Blue banner at top of content pages."""
        self.set_fill_color(*MODRN_BLUE)
        self.rect(0, 0, 210, 40, "F")
        self.set_font("LeagueSpartan", "B", 24)
        self.set_text_color(*WHITE)
        self.text(20, 28, f"{num}  {title}")
        self.set_y(50)

    def _body(self, text, size=11, bold=False):
        if bold:
            self.set_font("Montserrat", "B", size)
        else:
            self.set_font("Montserrat", "", size)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, 6.5, text, new_x="LMARGIN", new_y="NEXT")

    def _label(self, text, size=9):
        self.set_font("MontserratSB", "", size)
        self.set_text_color(*MID_GRAY)
        self.cell(0, 5, text.upper(), new_x="LMARGIN", new_y="NEXT")

    def _draw_modrn_wordmark(self, x, y, scale=1.0, text_color=None):
        """Draw the MODRN wordmark. text_color controls m/drn color (default BLACK)."""
        if text_color is None:
            text_color = BLACK
        s = scale
        font_size = int(40 * s)
        self.set_font("LeagueSpartan", "B", font_size)

        # Measure "m" width to position the circle precisely
        m_width = self.get_string_width("m")

        # "m"
        self.set_text_color(*text_color)
        self.text(x, y, "m")

        # "o" — blue circle with black dot, sized to match letter height
        letter_h = font_size * 0.35  # approximate cap height in mm
        r_outer = letter_h * 0.52
        r_inner = r_outer * 0.3
        gap = 1.0 * s
        cx = x + m_width + gap + r_outer
        cy = y - letter_h * 0.45

        self.set_fill_color(*MODRN_BLUE)
        self.ellipse(cx - r_outer, cy - r_outer, r_outer * 2, r_outer * 2, "F")
        self.set_fill_color(*BLACK)
        self.ellipse(cx - r_inner, cy - r_inner, r_inner * 2, r_inner * 2, "F")

        # "drn"
        drn_x = cx + r_outer + gap
        self.set_text_color(*text_color)
        self.text(drn_x, y, "drn")

        # Return total width for positioning subtitles
        drn_w = self.get_string_width("drn")
        return drn_x + drn_w - x

    def _draw_gomodrn_wordmark(self, x, y, scale=1.0, text_color=None):
        """Draw the gomodrn.com wordmark."""
        if text_color is None:
            text_color = BLACK
        s = scale
        font_size = int(28 * s)
        self.set_font("LeagueSpartan", "B", font_size)

        # "go" in blue
        self.set_text_color(*MODRN_BLUE)
        self.text(x, y, "go")
        go_w = self.get_string_width("go")

        # "m" in text_color
        m_x = x + go_w
        self.set_text_color(*text_color)
        self.text(m_x, y, "m")
        m_w = self.get_string_width("m")

        # "o" circle
        letter_h = font_size * 0.35
        r_outer = letter_h * 0.5
        r_inner = r_outer * 0.3
        gap = 0.8 * s
        cx = m_x + m_w + gap + r_outer
        cy = y - letter_h * 0.45

        self.set_fill_color(*MODRN_BLUE)
        self.ellipse(cx - r_outer, cy - r_outer, r_outer * 2, r_outer * 2, "F")
        self.set_fill_color(*BLACK)
        self.ellipse(cx - r_inner, cy - r_inner, r_inner * 2, r_inner * 2, "F")

        # "drn" in text_color
        drn_x = cx + r_outer + gap
        self.set_text_color(*text_color)
        self.text(drn_x, y, "drn")
        drn_w = self.get_string_width("drn")

        # ".com" in blue
        com_x = drn_x + drn_w
        self.set_text_color(*MODRN_BLUE)
        self.text(com_x, y, ".com")

    def _color_swatch(self, x, y, r, g, b, name, hex_val, w=50, h=35):
        self.set_fill_color(r, g, b)
        if r > 240 and g > 240 and b > 240:
            self.set_draw_color(200, 200, 200)
            self.rect(x, y, w, h, "FD")
        else:
            self.rect(x, y, w, h, "F")
        self.set_font("MontserratSB", "", 9)
        self.set_text_color(*DARK_GRAY)
        self.text(x, y + h + 5, name)
        self.set_font("Montserrat", "", 8)
        self.set_text_color(*MID_GRAY)
        self.text(x, y + h + 10, hex_val)
        self.text(x, y + h + 14.5, f"RGB {r}, {g}, {b}")

    # ── Pages ────────────────────────────────────────────────────────

    def cover_page(self):
        self.add_page()
        self._bg(*BLACK)

        # Top accent line
        self.set_fill_color(*MODRN_BLUE)
        self.rect(0, 0, 210, 6, "F")

        # Main wordmark — WHITE text on black background
        self._draw_modrn_wordmark(40, 135, scale=1.6, text_color=WHITE)

        # Subtitle
        self.set_font("MontserratSB", "", 13)
        self.set_text_color(*WHITE)
        self.text(40, 152, "M A R K E T I N G   S O L U T I O N S")

        # Divider
        self.set_draw_color(*MODRN_BLUE)
        self.set_line_width(0.8)
        self.line(40, 162, 170, 162)

        # Title
        self.set_font("LeagueSpartan", "B", 36)
        self.set_text_color(*WHITE)
        self.text(40, 182, "Brand Guide")

        # Year
        self.set_font("MontserratLight", "", 12)
        self.set_text_color(*MID_GRAY)
        self.text(40, 196, "2026 Edition")

        # Bottom bar
        self.set_fill_color(*MODRN_BLUE)
        self.rect(0, 285, 210, 12, "F")
        self.set_font("Montserrat", "", 9)
        self.set_text_color(*WHITE)
        self.text(75, 293, "gomodrn.com")

    def toc_page(self):
        self.add_page()
        self._section_title("Contents", 30)

        items = [
            ("01", "Brand Overview"),
            ("02", "Logo & Wordmarks"),
            ("03", "Color Palette"),
            ("04", "Typography"),
            ("05", "Logo Usage Rules"),
            ("06", "Voice & Tone"),
            ("07", "Digital Applications"),
            ("08", "AI & LLM Reference"),
        ]
        y = 60
        for num, title in items:
            self.set_font("LeagueSpartan", "B", 14)
            self.set_text_color(*MODRN_BLUE)
            self.text(25, y, num)
            self.set_font("Montserrat", "", 13)
            self.set_text_color(*DARK_GRAY)
            self.text(42, y, title)
            self.set_draw_color(200, 200, 200)
            self.set_line_width(0.2)
            self.set_dash_pattern(1, 2)
            self.line(42 + self.get_string_width(title) + 3, y, 180, y)
            self.set_dash_pattern()
            y += 14

    def brand_overview_page(self):
        self.add_page()
        self._page_header("01", "Brand Overview")

        self._body(
            "MODRN Marketing Solutions is a modern, results-driven digital marketing agency. "
            "We combine bold creativity with data-backed strategy to help brands grow, connect, "
            "and thrive in the digital landscape.",
            size=12
        )
        self.ln(4)
        self._body(
            "Our brand identity reflects who we are: clean, confident, and forward-thinking. "
            "Every element — from our signature blue to our distinctive wordmark — signals "
            "professionalism, energy, and a modern approach to marketing."
        )

        self.ln(8)
        self._label("Mission")
        self.ln(2)
        self._body(
            "To empower businesses with modern marketing strategies that deliver measurable "
            "results and meaningful connections with their audiences."
        )

        self.ln(6)
        self._label("Brand Personality")
        self.ln(2)

        traits = [
            ("Bold", "We lead with confidence and aren't afraid to stand out."),
            ("Modern", "We stay ahead of trends and embrace what's next."),
            ("Strategic", "Every decision is backed by data and intent."),
            ("Approachable", "We make complex marketing feel accessible."),
        ]
        for trait, desc in traits:
            self.set_font("Montserrat", "B", 11)
            self.set_text_color(*MODRN_BLUE)
            self.cell(32, 7, trait)
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 7, desc, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

        self.ln(8)
        self._label("Brand Values")
        self.ln(2)
        values = [
            "Innovation  --  Push boundaries, embrace the new",
            "Transparency  --  Honest communication, clear results",
            "Impact  --  Every action drives measurable outcomes",
            "Partnership  --  Client success is our success",
        ]
        for v in values:
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 7, v, new_x="LMARGIN", new_y="NEXT")

    def logo_page(self):
        self.add_page()
        self._page_header("02", "Logo & Wordmarks")

        self._body(
            "Our brand uses two primary wordmarks. The signature element is the "
            "stylized 'o' -- a bright blue circle with a centered black dot -- "
            "representing focus, vision, and clarity."
        )

        # Primary logo box
        self.ln(6)
        self._label("Primary Wordmark -- MODRN Marketing Solutions")
        self.ln(4)
        box_y = self.get_y()
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(20, box_y, 170, 50, "F")
        self._draw_modrn_wordmark(60, box_y + 32, scale=1.3)
        self.set_font("MontserratSB", "", 10)
        self.set_text_color(*BLACK)
        self.text(60, box_y + 44, "M A R K E T I N G   S O L U T I O N S")
        self.set_y(box_y + 56)

        self._body(
            "The primary wordmark uses heavy, bold letterforms in black with the "
            "signature blue 'o'. The spaced-out 'MARKETING SOLUTIONS' tagline sits "
            "below in a clean, tracked-out style."
        )

        # Secondary logo box
        self.ln(6)
        self._label("Secondary Wordmark -- gomodrn.com")
        self.ln(4)
        box_y = self.get_y()
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(20, box_y, 170, 40, "F")
        self._draw_gomodrn_wordmark(55, box_y + 28, scale=1.1)
        self.set_y(box_y + 46)

        self._body(
            "The web wordmark uses the same signature 'o' element. 'go' and '.com' "
            "appear in brand blue, while 'modrn' is black -- reinforcing both the "
            "brand name and the URL."
        )

        # Signature element callout
        self.ln(6)
        self._label("The Signature 'O' Element")
        self.ln(4)
        # Draw a large standalone "o" element
        oy = self.get_y()
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(20, oy, 170, 45, "F")
        # Large blue circle
        cx, cy = 105, oy + 22
        self.set_fill_color(*MODRN_BLUE)
        self.ellipse(cx - 14, cy - 14, 28, 28, "F")
        self.set_fill_color(*BLACK)
        self.ellipse(cx - 4.5, cy - 4.5, 9, 9, "F")
        # Labels
        self.set_font("MontserratLight", "", 8)
        self.set_text_color(*MID_GRAY)
        self.text(35, oy + 20, "Blue circle: #29ABE2")
        self.text(35, oy + 26, "Black dot: #000000")
        self.text(140, oy + 20, "Outer/inner ratio: ~3:1")
        self.text(140, oy + 26, "Dot is always centered")

    def color_page(self):
        self.add_page()
        self._page_header("03", "Color Palette")

        self._body(
            "Our color palette is intentionally minimal: black, white, and bright blue. "
            "This high-contrast combination communicates confidence, clarity, and modernity."
        )

        # Primary colors
        self.ln(6)
        self._label("Primary Colors")
        y = self.get_y() + 6
        self._color_swatch(20, y, *MODRN_BLUE, "MODRN Blue", "#29ABE2")
        self._color_swatch(80, y, *BLACK, "Black", "#000000")
        self._color_swatch(140, y, *WHITE, "White", "#FFFFFF")

        self.set_y(y + 55)
        self._label("Secondary / UI Colors")
        y2 = self.get_y() + 6
        self._color_swatch(20, y2, *DARK_BLUE, "Blue Hover", "#0C8BC4")
        self._color_swatch(80, y2, *DARK_GRAY, "Dark Gray", "#333333")
        self._color_swatch(140, y2, *LIGHT_GRAY, "Light Gray", "#F5F5F5")

        self.set_y(y2 + 58)
        self._label("Color Usage Guidelines")
        self.ln(3)
        rules = [
            "MODRN Blue is the primary accent -- use for links, CTAs, highlights, and the 'o' element.",
            "Black is the dominant brand color -- used for wordmarks, headings, and backgrounds.",
            "White is for backgrounds, reversed text on dark surfaces, and breathing space.",
            "Blue Hover (#0C8BC4) is used exclusively for interactive hover/active states.",
            "Never place blue text on medium-gray backgrounds -- maintain WCAG contrast ratios.",
            "The blue-to-black ratio should be approximately 30/70 in any composition.",
        ]
        for rule in rules:
            self.set_font("Montserrat", "", 9.5)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 6, f"  -  {rule}", new_x="LMARGIN", new_y="NEXT")

    def typography_page(self):
        self.add_page()
        self._page_header("04", "Typography")

        self._body(
            "Typography is central to the MODRN identity. We pair a bold display "
            "font for impact with a clean sans-serif for readability."
        )

        # League Spartan
        self.ln(6)
        self._label("Primary Typeface -- Headings & Display")
        self.ln(4)
        self.set_fill_color(*LIGHT_GRAY)
        y = self.get_y()
        self.rect(20, y, 170, 38, "F")
        self.set_font("LeagueSpartan", "B", 30)
        self.set_text_color(*BLACK)
        self.text(30, y + 20, "League Spartan")
        self.set_font("LeagueSpartanSB", "", 11)
        self.set_text_color(*MID_GRAY)
        self.text(30, y + 31, "ABCDEFGHIJKLMNOPQRSTUVWXYZ  0123456789")
        self.set_y(y + 44)

        self._body("Used for: Headings (H1-H6), wordmarks, navigation labels, display text.")
        self._body("Weights: Semi-Bold (600) for subheadings, Bold (700) for primary headings.")

        # Montserrat
        self.ln(6)
        self._label("Secondary Typeface -- Body & UI")
        self.ln(4)
        self.set_fill_color(*LIGHT_GRAY)
        y = self.get_y()
        self.rect(20, y, 170, 38, "F")
        self.set_font("Montserrat", "B", 26)
        self.set_text_color(*BLACK)
        self.text(30, y + 19, "Montserrat")
        self.set_font("Montserrat", "", 11)
        self.set_text_color(*MID_GRAY)
        self.text(30, y + 30, "abcdefghijklmnopqrstuvwxyz  0123456789")
        self.set_y(y + 44)

        self._body("Used for: Body copy, UI elements, descriptions, captions, metadata.")
        self._body("Weights: Light (300), Regular (400), Semi-Bold (600), Bold (700).")

        # Type scale
        self.ln(6)
        self._label("Type Scale")
        self.ln(4)
        scales = [
            ("LeagueSpartan", "B", 24, "H1 -- League Spartan Bold"),
            ("LeagueSpartan", "B", 20, "H2 -- League Spartan Bold"),
            ("LeagueSpartanSB", "", 16, "H3 -- League Spartan Semi-Bold"),
            ("Montserrat", "B", 13, "H4 -- Montserrat Bold"),
            ("Montserrat", "", 11, "Body -- Montserrat Regular"),
            ("MontserratLight", "", 9, "Caption -- Montserrat Light"),
        ]
        for font, style, size, label in scales:
            self.set_font(font, style, size)
            self.set_text_color(*BLACK)
            self.cell(0, max(size * 0.55, 7), label, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

    def logo_usage_page(self):
        self.add_page()
        self._page_header("05", "Logo Usage Rules")

        self._label("Clear Space")
        self.ln(2)
        self._body(
            "Maintain a minimum clear space around the logo equal to the height "
            "of the 'o' circle element."
        )

        self.ln(4)
        self._label("Minimum Size")
        self.ln(2)
        self._body("Primary wordmark: min 120px wide (digital) or 30mm (print).")
        self._body("Secondary wordmark: min 100px wide (digital) or 25mm (print).")

        # Do's
        self.ln(4)
        self._label("Do's")
        self.ln(2)
        dos = [
            "Use the full-color logo on white or light backgrounds",
            "Use the all-white version on black or dark backgrounds",
            "Maintain the aspect ratio -- always scale proportionally",
            "Use the signature blue 'o' consistently in both wordmarks",
        ]
        for d in dos:
            self.set_font("Montserrat", "", 10)
            self.set_text_color(30, 150, 80)
            self.cell(6, 6, "+")
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 6, d, new_x="LMARGIN", new_y="NEXT")

        # Don'ts
        self.ln(4)
        self._label("Don'ts")
        self.ln(2)
        donts = [
            "Do not change the blue 'o' to any other color",
            "Do not rotate, skew, or distort the wordmark",
            "Do not add drop shadows, outlines, or effects",
            "Do not place on busy backgrounds without a solid overlay",
            "Do not separate the 'o' dot from the circle element",
            "Do not rearrange or re-space the letterforms",
        ]
        for d in donts:
            self.set_font("Montserrat", "", 10)
            self.set_text_color(220, 50, 50)
            self.cell(6, 6, "x")
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 6, d, new_x="LMARGIN", new_y="NEXT")

        # Background treatments
        self.ln(6)
        self._label("Approved Background Treatments")
        self.ln(4)

        bw = 80
        bh = 32
        y = self.get_y()

        # White bg
        self.set_fill_color(*WHITE)
        self.set_draw_color(200, 200, 200)
        self.rect(20, y, bw, bh, "FD")
        self._draw_modrn_wordmark(32, y + 22, scale=0.55, text_color=BLACK)

        # Black bg
        self.set_fill_color(*BLACK)
        self.rect(110, y, bw, bh, "F")
        self._draw_modrn_wordmark(122, y + 22, scale=0.55, text_color=WHITE)

    def voice_tone_page(self):
        self.add_page()
        self._page_header("06", "Voice & Tone")

        self._body(
            "The MODRN voice is confident, clear, and forward-thinking. We speak "
            "as strategic partners -- knowledgeable but never condescending, "
            "professional but never stuffy."
        )

        self.ln(6)
        self._label("Voice Attributes")
        self.ln(3)

        attrs = [
            ("Confident", "We lead with authority. We know our craft and aren't afraid to say so."),
            ("Clear", "We strip away jargon. Complex ideas, simple language."),
            ("Modern", "We sound current and relevant -- never dated or corporate-speak."),
            ("Action-Oriented", "We focus on what to do, not just what to think."),
        ]
        for attr, desc in attrs:
            self.set_font("Montserrat", "B", 12)
            self.set_text_color(*MODRN_BLUE)
            self.cell(0, 8, attr, new_x="LMARGIN", new_y="NEXT")
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*DARK_GRAY)
            self.multi_cell(0, 6, desc, new_x="LMARGIN", new_y="NEXT")
            self.ln(2)

        self.ln(4)
        self._label("Tone Examples")
        self.ln(3)

        # Example 1
        self.set_font("MontserratSB", "", 9)
        self.set_text_color(*MID_GRAY)
        self.cell(0, 5, "INSTEAD OF:", new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(255, 240, 240)
        self.set_font("Montserrat", "", 10)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, 6, "\"We synergize cross-functional paradigms to deliver holistic solutions.\"",
                        new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(2)
        self.set_font("MontserratSB", "", 9)
        self.set_text_color(30, 150, 80)
        self.cell(0, 5, "WRITE:", new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(240, 255, 240)
        self.set_font("Montserrat", "", 10)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, 6, "\"We connect your marketing channels so everything works together.\"",
                        new_x="LMARGIN", new_y="NEXT", fill=True)

        self.ln(6)

        # Example 2
        self.set_font("MontserratSB", "", 9)
        self.set_text_color(*MID_GRAY)
        self.cell(0, 5, "INSTEAD OF:", new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(255, 240, 240)
        self.set_font("Montserrat", "", 10)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, 6, "\"Maybe you should consider possibly looking into social media advertising.\"",
                        new_x="LMARGIN", new_y="NEXT", fill=True)
        self.ln(2)
        self.set_font("MontserratSB", "", 9)
        self.set_text_color(30, 150, 80)
        self.cell(0, 5, "WRITE:", new_x="LMARGIN", new_y="NEXT")
        self.set_fill_color(240, 255, 240)
        self.set_font("Montserrat", "", 10)
        self.set_text_color(*DARK_GRAY)
        self.multi_cell(0, 6, "\"Social media ads will put your brand in front of the right people. Here's how.\"",
                        new_x="LMARGIN", new_y="NEXT", fill=True)

    def digital_page(self):
        self.add_page()
        self._page_header("07", "Digital Applications")

        self._body(
            "Consistent application across digital platforms reinforces brand "
            "recognition. Below are specifications for key digital touchpoints."
        )

        self.ln(4)
        self._label("Website -- gomodrn.com")
        self.ln(2)
        specs = [
            ("Header / Footer", "Black (#000000) background, white text, blue hover"),
            ("Links", "MODRN Blue (#29ABE2), hover: #0C8BC4"),
            ("Headings", "League Spartan Bold, black"),
            ("Body text", "Montserrat Regular, 16px base, dark gray (#333)"),
            ("Buttons", "Blue fill, white text, rounded 4px corners"),
            ("Code blocks", "10% blue tint background"),
        ]
        for label, val in specs:
            self.set_font("Montserrat", "B", 10)
            self.set_text_color(*DARK_GRAY)
            self.cell(38, 6, label)
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*MID_GRAY)
            self.cell(0, 6, val, new_x="LMARGIN", new_y="NEXT")

        self.ln(6)
        self._label("Social Media")
        self.ln(2)
        social = [
            ("Profile image", "Blue 'o' circle with black dot on white background"),
            ("Cover images", "Black background with blue accent elements"),
            ("Post templates", "White or black backgrounds; blue for highlights"),
            ("Hashtag", "#gomodrn"),
        ]
        for label, val in social:
            self.set_font("Montserrat", "B", 10)
            self.set_text_color(*DARK_GRAY)
            self.cell(38, 6, label)
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*MID_GRAY)
            self.cell(0, 6, val, new_x="LMARGIN", new_y="NEXT")

        # Email signature
        self.ln(6)
        self._label("Email Signatures")
        self.ln(3)
        y = self.get_y()
        self.set_fill_color(*LIGHT_GRAY)
        self.rect(20, y, 170, 36, "F")
        # Blue left accent
        self.set_fill_color(*MODRN_BLUE)
        self.rect(20, y, 2, 36, "F")
        self.set_font("Montserrat", "B", 11)
        self.set_text_color(*BLACK)
        self.text(28, y + 10, "First Last")
        self.set_font("Montserrat", "", 9)
        self.set_text_color(*MID_GRAY)
        self.text(28, y + 17, "Title  |  MODRN Marketing Solutions")
        self.set_text_color(*MODRN_BLUE)
        self.text(28, y + 24, "gomodrn.com")
        self.set_text_color(*MID_GRAY)
        self.text(28, y + 31, "hello@gomodrn.com  |  (555) 000-0000")

    def ai_reference_page(self):
        self.add_page()
        self._page_header("08", "AI & LLM Reference")

        self._body(
            "This section provides structured brand data optimized for AI "
            "assistants, LLMs, and automated systems that generate content "
            "or design assets for MODRN."
        )

        self.ln(4)
        self._label("Machine-Readable Brand Summary")
        self.ln(4)

        block_y = self.get_y()
        self.set_fill_color(245, 247, 250)
        self.rect(20, block_y, 170, 125, "F")
        self.set_draw_color(*MODRN_BLUE)
        self.set_line_width(0.5)
        self.line(20, block_y, 20, block_y + 125)

        self.set_font("Montserrat", "", 8.5)
        self.set_text_color(*DARK_GRAY)

        lines = [
            "Brand Name:      MODRN Marketing Solutions",
            "URL:             gomodrn.com",
            "Tagline:         Modern marketing, measurable results.",
            "",
            "Primary Colors:",
            "  MODRN Blue:    #29ABE2  |  RGB(41, 171, 226)",
            "  Black:         #000000  |  RGB(0, 0, 0)",
            "  White:         #FFFFFF  |  RGB(255, 255, 255)",
            "",
            "Secondary Colors:",
            "  Blue Hover:    #0C8BC4  |  RGB(12, 139, 196)",
            "  Dark Gray:     #333333  |  RGB(51, 51, 51)",
            "  Light Gray:    #F5F5F5  |  RGB(245, 245, 245)",
            "",
            "Typography:",
            "  Headings:      League Spartan  |  Bold (700), Semi-Bold (600)",
            "  Body:          Montserrat      |  Regular (400), Light (300)",
            "  Source:        Google Fonts (open source)",
            "",
            "Logo Element:",
            "  Signature 'o': Blue circle (#29ABE2) + centered black dot",
            "  Always present in both wordmark variants",
            "",
            "Voice:           Confident, Clear, Modern, Action-Oriented",
            "Tone:            Professional but approachable, jargon-free",
        ]

        x = 26
        y = block_y + 6
        for line in lines:
            self.text(x, y, line)
            y += 5

        self.set_y(block_y + 132)
        self._body(
            "When generating content for MODRN, AI systems should: use active "
            "voice, lead with outcomes, avoid corporate jargon, and maintain a "
            "confident but approachable tone. Always use 'MODRN' (all caps, no "
            "'e') -- never 'Modern' or 'modrn' in copy."
        )

        self.ln(4)
        self._label("Brand Name Rules for AI")
        self.ln(2)
        rules = [
            "Full name: 'MODRN Marketing Solutions' (first reference)",
            "Short name: 'MODRN' (subsequent references, always capitalized)",
            "URL form: 'gomodrn.com' (lowercase, no www)",
            "Never: 'Modern', 'GoModrn', 'GOMODRN', 'modrn marketing'",
        ]
        for rule in rules:
            self.set_font("Montserrat", "", 10)
            self.set_text_color(*DARK_GRAY)
            self.cell(0, 6.5, f"  -  {rule}", new_x="LMARGIN", new_y="NEXT")

    def back_cover(self):
        self.add_page()
        self._bg(*BLACK)

        self.set_fill_color(*MODRN_BLUE)
        self.rect(0, 0, 210, 6, "F")

        # Centered wordmark — WHITE on black
        self._draw_modrn_wordmark(58, 140, scale=1.4, text_color=WHITE)
        self.set_font("MontserratSB", "", 10)
        self.set_text_color(*WHITE)
        self.text(58, 154, "M A R K E T I N G   S O L U T I O N S")

        self.set_font("Montserrat", "", 12)
        self.set_text_color(*MODRN_BLUE)
        self.text(82, 172, "gomodrn.com")

        self.set_font("MontserratLight", "", 9)
        self.set_text_color(*MID_GRAY)
        self.text(58, 260, "This brand guide is confidential property of")
        self.text(58, 266, "MODRN Marketing Solutions. 2026 All rights reserved.")

        self.set_fill_color(*MODRN_BLUE)
        self.rect(0, 285, 210, 12, "F")

    def build(self):
        self.cover_page()
        self.toc_page()
        self.brand_overview_page()
        self.logo_page()
        self.color_page()
        self.typography_page()
        self.logo_usage_page()
        self.voice_tone_page()
        self.digital_page()
        self.ai_reference_page()
        self.back_cover()
        self.output(OUTPUT)
        print(f"Brand guide generated: {OUTPUT}")
        print(f"Pages: {self.pages_count}")


if __name__ == "__main__":
    pdf = BrandGuidePDF()
    pdf.build()
