import io
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

FONTS_DIR = Path(__file__).parent / "fonts"
FONT_NAME = "DejaVuSans"

# ReportLab's built-in base14 fonts (Helvetica etc.) use WinAnsi encoding, which
# does not include Polish diacritics (ą, ć, ę, ł, ń, ś, ź, ż). DejaVu Sans covers
# full Unicode / Latin Extended-A, so it must be embedded rather than relying on
# a base font.
pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONTS_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont(f"{FONT_NAME}-Bold", str(FONTS_DIR / "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont(f"{FONT_NAME}-Oblique", str(FONTS_DIR / "DejaVuSans-Oblique.ttf")))
pdfmetrics.registerFont(TTFont(f"{FONT_NAME}-BoldOblique", str(FONTS_DIR / "DejaVuSans-BoldOblique.ttf")))
pdfmetrics.registerFontFamily(
    FONT_NAME,
    normal=FONT_NAME,
    bold=f"{FONT_NAME}-Bold",
    italic=f"{FONT_NAME}-Oblique",
    boldItalic=f"{FONT_NAME}-BoldOblique",
)


SECTION_LABELS = {
    "pl": {
        "contact": "DANE KONTAKTOWE",
        "summary": "PODSUMOWANIE ZAWODOWE",
        "experience": "DOŚWIADCZENIE ZAWODOWE",
        "education": "WYKSZTAŁCENIE",
        "skills": "UMIEJĘTNOŚCI",
        "certifications": "CERTYFIKATY / SZKOLENIA",
        "languages": "JĘZYKI OBCE",
        "rodo": "KLAUZULA RODO",
    },
    "en": {
        "contact": "CONTACT INFORMATION",
        "summary": "PROFESSIONAL SUMMARY",
        "experience": "PROFESSIONAL EXPERIENCE",
        "education": "EDUCATION",
        "skills": "SKILLS",
        "certifications": "CERTIFICATIONS / TRAINING",
        "languages": "LANGUAGES",
        "rodo": "GDPR CONSENT",
    },
}


def _esc(value) -> str:
    return escape(str(value or ""))


def _styles() -> dict:
    return {
        "name": ParagraphStyle(
            "name", fontName=f"{FONT_NAME}-Bold", fontSize=20, leading=24,
            alignment=TA_CENTER, spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "title", fontName=FONT_NAME, fontSize=13, leading=16,
            alignment=TA_CENTER, spaceAfter=6,
        ),
        "contact": ParagraphStyle(
            "contact", fontName=FONT_NAME, fontSize=10, leading=13,
            alignment=TA_CENTER, spaceAfter=2,
        ),
        "section": ParagraphStyle(
            "section", fontName=f"{FONT_NAME}-Bold", fontSize=14, leading=17,
            spaceBefore=10, spaceAfter=2,
        ),
        "entry_title": ParagraphStyle(
            "entry_title", fontName=f"{FONT_NAME}-Bold", fontSize=11, leading=14,
            spaceBefore=6, spaceAfter=0,
        ),
        "entry_meta": ParagraphStyle(
            "entry_meta", fontName=f"{FONT_NAME}-Oblique", fontSize=10, leading=13,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body", fontName=FONT_NAME, fontSize=11, leading=15, spaceAfter=2,
        ),
        "body_justify": ParagraphStyle(
            "body_justify", fontName=FONT_NAME, fontSize=11, leading=15,
            alignment=TA_JUSTIFY, spaceAfter=4,
        ),
        "skills_line": ParagraphStyle(
            "skills_line", fontName=FONT_NAME, fontSize=11, leading=15, spaceAfter=3,
        ),
        "rodo": ParagraphStyle(
            "rodo", fontName=f"{FONT_NAME}-Oblique", fontSize=8, leading=10,
            spaceBefore=14,
        ),
    }


def _bullet_list(items, style) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(_esc(item), style), spaceAfter=2) for item in items],
        bulletType="bullet",
        bulletFontName=FONT_NAME,
        bulletFontSize=style.fontSize,
        leftIndent=14,
    )


def render_cv_pdf(cv_data: dict, language: str = "pl") -> bytes:
    labels = SECTION_LABELS.get(language, SECTION_LABELS["pl"])

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        topMargin=2.54 * cm,
        bottomMargin=2.54 * cm,
        leftMargin=2.54 * cm,
        rightMargin=2.54 * cm,
        title=cv_data.get("contact", {}).get("name") or "CV",
    )
    styles = _styles()
    story = []

    def section_header(text: str):
        story.append(Paragraph(text, styles["section"]))
        story.append(HRFlowable(width="100%", thickness=1, color=black, spaceBefore=1, spaceAfter=6))

    contact = cv_data.get("contact") or {}

    section_header(labels["contact"])
    story.append(Paragraph(_esc(contact.get("name")), styles["name"]))
    if contact.get("professional_title"):
        story.append(Paragraph(_esc(contact["professional_title"]), styles["title"]))
    contact_line = " | ".join(filter(None, [contact.get("phone"), contact.get("email"), contact.get("location")]))
    if contact_line:
        story.append(Paragraph(_esc(contact_line), styles["contact"]))
    if contact.get("linkedin"):
        story.append(Paragraph(_esc(contact["linkedin"]), styles["contact"]))
    story.append(Spacer(1, 4))

    section_header(labels["summary"])
    story.append(Paragraph(_esc(cv_data.get("summary")), styles["body_justify"]))

    experience = cv_data.get("experience") or []
    if experience:
        section_header(labels["experience"])
        for job in experience:
            meta = " | ".join(filter(None, [job.get("company"), job.get("location"), job.get("dates")]))
            story.append(Paragraph(f"<b>{_esc(job.get('title'))}</b>", styles["entry_title"]))
            if meta:
                story.append(Paragraph(f"<i>{_esc(meta)}</i>", styles["entry_meta"]))
            bullets = job.get("bullets") or []
            if bullets:
                story.append(_bullet_list(bullets, styles["body"]))

    education = cv_data.get("education") or []
    if education:
        section_header(labels["education"])
        for edu in education:
            meta = " | ".join(filter(None, [edu.get("school"), edu.get("location"), edu.get("dates")]))
            story.append(Paragraph(f"<b>{_esc(edu.get('degree'))}</b>", styles["entry_title"]))
            if meta:
                story.append(Paragraph(f"<i>{_esc(meta)}</i>", styles["entry_meta"]))
            details = edu.get("details") or []
            if details:
                story.append(_bullet_list(details, styles["body"]))

    skills = cv_data.get("skills") or []
    if skills:
        section_header(labels["skills"])
        for group in skills:
            items = ", ".join(group.get("items") or [])
            story.append(Paragraph(f"<b>{_esc(group.get('category'))}:</b> {_esc(items)}", styles["skills_line"]))

    certifications = cv_data.get("certifications") or []
    if certifications:
        section_header(labels["certifications"])
        story.append(_bullet_list(certifications, styles["body"]))

    languages = cv_data.get("languages") or []
    if languages:
        section_header(labels["languages"])
        story.append(_bullet_list(languages, styles["body"]))

    section_header(labels["rodo"])
    story.append(Paragraph(_esc(cv_data.get("rodo_clause")), styles["rodo"]))

    doc.build(story)
    return buffer.getvalue()
