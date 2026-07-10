#!/usr/bin/env python3
"""Generate the CV PDF from the al-folio CV data file."""

from __future__ import annotations

import html
from datetime import date
from pathlib import Path

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    Image,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "_data" / "cv.yml"
OUTPUT_FILE = ROOT / "assets" / "pdf" / "CV_SYanyong.pdf"
PHOTO_FILE = ROOT / "assets" / "img" / "cv-profile-2026.png"
NAVY = colors.HexColor("#1f4e79")
TEXT = colors.HexColor("#202020")
MUTED = colors.HexColor("#555555")


def paragraph(text: object, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(str(text)).replace("\n", "<br/>"), style)


class CVCanvas(canvas.Canvas):
    """Add page numbers everywhere and the modification date on the final page."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._page_states = []

    def showPage(self):
        self._page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self._page_states)
        for page_number, state in enumerate(self._page_states, start=1):
            self.__dict__.update(state)
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#a3a3a3"))
            if page_number == page_count:
                self.drawString(0.65 * inch, 24, f"Modified on {date.today().isoformat()}")
            self.drawRightString(A4[0] - 0.65 * inch, 24, f"Page {page_number}")
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)


def experience_block(entry: dict, styles: dict) -> Table:
    details = [paragraph(entry.get("title", ""), styles["entry_title"])]
    if entry.get("institution"):
        details.append(paragraph(entry["institution"], styles["entry_body"]))
    for item in entry.get("description", []):
        details.append(paragraph(f"- {item}", styles["entry_body"]))

    table = Table(
        [[paragraph(entry.get("year", ""), styles["year"]), details]],
        colWidths=[1.15 * inch, 5.75 * inch],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def awards_block(entry: dict, styles: dict) -> Table:
    items = [paragraph(f"- {item}", styles["entry_body"]) for item in entry.get("items", [])]
    table = Table(
        [[paragraph(entry.get("year", ""), styles["year"]), items]],
        colWidths=[0.65 * inch, 6.25 * inch],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def build_pdf(data: list[dict]):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(OUTPUT_FILE),
        pagesize=A4,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.5 * inch,
        title="CV - Sarucha Yanyong",
        author="Sarucha Yanyong",
    )
    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "CVName", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=22,
            leading=26, textColor=NAVY, spaceAfter=4,
        ),
        "role": ParagraphStyle(
            "CVRole", parent=base["Normal"], fontName="Helvetica", fontSize=14,
            leading=18, textColor=NAVY,
        ),
        "header": ParagraphStyle(
            "CVHeader", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=14,
            leading=17, textColor=NAVY, spaceBefore=13, spaceAfter=5,
        ),
        "body": ParagraphStyle(
            "CVBody", parent=base["Normal"], fontName="Helvetica", fontSize=9.5,
            leading=12, textColor=TEXT,
        ),
        "entry_title": ParagraphStyle(
            "CVEntryTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
            leading=13, textColor=TEXT,
        ),
        "entry_body": ParagraphStyle(
            "CVEntryBody", parent=base["Normal"], fontName="Helvetica", fontSize=9.2,
            leading=11.5, textColor=TEXT,
        ),
        "year": ParagraphStyle(
            "CVYear", parent=base["Normal"], fontName="Helvetica", fontSize=9.5,
            leading=12, textColor=TEXT,
        ),
        "skill_title": ParagraphStyle(
            "CVSkillTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.5,
            leading=12, textColor=TEXT,
        ),
        "skill_body": ParagraphStyle(
            "CVSkillBody", parent=base["Normal"], fontName="Helvetica", fontSize=7.7,
            leading=9.0, textColor=TEXT,
        ),
    }

    sections = {section["title"]: section for section in data}
    general = sections["General Information"]
    fields = {entry["name"]: entry["value"] for entry in general["contents"]}

    story = []
    header_text = [
        paragraph(fields["Full Name"], styles["name"]),
        paragraph(fields["Title"], styles["role"]),
        Spacer(1, 5),
        paragraph(fields["Department"], styles["body"]),
        paragraph(fields["Institution"], styles["body"]),
    ]
    photo = Image(str(PHOTO_FILE), width=1.2 * inch, height=1.6 * inch) if PHOTO_FILE.exists() else ""
    header = Table([[header_text, photo]], colWidths=[5.55 * inch, 1.35 * inch], hAlign="LEFT")
    header.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    story.extend([header, Spacer(1, 10)])

    contact = [
        [paragraph("Email", styles["skill_title"]), paragraph(fields["Email"], styles["body"])],
        [paragraph("Website", styles["skill_title"]), paragraph(fields["Website"], styles["body"])],
        [paragraph("Nationality", styles["skill_title"]), paragraph(fields["Nationality"], styles["body"])],
        [paragraph("Date of Birth", styles["skill_title"]), paragraph(fields["Date of Birth"], styles["body"])],
    ]
    contact_table = Table(contact, colWidths=[0.95 * inch, 5.95 * inch], hAlign="LEFT")
    contact_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    story.append(contact_table)

    for section in data:
        if section["title"] == "General Information":
            continue
        story.append(Paragraph(section["title"], styles["header"]))
        if section["type"] == "nested_list":
            cells = []
            for entry in section["contents"]:
                items = " ".join(entry.get("items", []))
                cells.append(Paragraph(f"<b>{html.escape(entry['title'])}:</b> {html.escape(items)}", styles["skill_body"]))
            rows = [cells[index : index + 2] for index in range(0, len(cells), 2)]
            if len(rows[-1]) == 1:
                rows[-1].append("")
            skills_table = Table(rows, colWidths=[3.45 * inch, 3.45 * inch], hAlign="LEFT")
            skills_table.setStyle(
                TableStyle(
                    [
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                        ("TOPPADDING", (0, 0), (-1, -1), 0),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                    ]
                )
            )
            story.append(skills_table)
            continue
        for entry in section["contents"]:
            if "items" in entry:
                story.append(awards_block(entry, styles))
            else:
                story.append(experience_block(entry, styles))

    document.build(story, canvasmaker=CVCanvas)
    print(f"Generated {OUTPUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    with DATA_FILE.open(encoding="utf-8") as source:
        build_pdf(yaml.safe_load(source))
