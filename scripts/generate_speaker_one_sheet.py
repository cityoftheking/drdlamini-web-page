from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT = Path("assets/dr-dlamini-speaker-one-sheet.pdf")
OUT.parent.mkdir(parents=True, exist_ok=True)

navy = HexColor("#10243d")
gold = HexColor("#c99a4a")
muted = HexColor("#56616c")
cream = HexColor("#f7f3eb")

c = canvas.Canvas(str(OUT), pagesize=letter)
W, H = letter
m = 46
y = H - 52

c.setFillColor(navy)
c.setFont("Helvetica-Bold", 10)
c.drawString(m, y, "DR. GEQIGULA DLAMINI")
c.setFillColor(gold)
c.drawRightString(W-m, y, "KEYNOTES  |  WORKSHOPS  |  ADVISORY")
y -= 30

c.setFillColor(navy)
c.setFont("Times-Bold", 27)
c.drawString(m, y, "Mission Enablement for an AI-Shaped World")
y -= 24
c.setFillColor(muted)
c.setFont("Helvetica", 10.5)
lines = [
    "I help public-sector and mission-driven leaders put people at the center of technology",
    "and organizational change, then translate that clarity into practical action."
]
for line in lines:
    c.drawString(m, y, line); y -= 15

y -= 12
c.setFillColor(navy); c.setFont("Helvetica-Bold", 10); c.drawString(m, y, "SPEAKING TOPICS")
y -= 18

topics = [
    ("Empowering Those Who Power Organizations", "Human-centered AI adoption, agency and leadership in periods of rapid change."),
    ("Mission Enablement in Complex Systems", "Aligning people, strategy and execution when the path forward is not obvious."),
    ("The Discipline of Optimism", "Optimism as a leadership practice for creating agency, possibility and durable progress.")
]
for title, desc in topics:
    c.setFillColor(cream); c.roundRect(m, y-50, W-2*m, 58, 8, fill=1, stroke=0)
    c.setFillColor(navy); c.setFont("Times-Bold", 13); c.drawString(m+14, y-12, title)
    c.setFillColor(muted); c.setFont("Helvetica", 8.8); c.drawString(m+14, y-30, desc)
    y -= 70

c.setFillColor(navy); c.setFont("Helvetica-Bold", 10); c.drawString(m, y, "SELECTED PROOF")
y -= 18
c.setFillColor(muted); c.setFont("Helvetica", 9)
proof = [
    "Closing keynote  |  Meeting of the Minds 2026",
    "Two-time University of the Pacific Changemakers presenter",
    "Doctoral Innovation in Research and Practice Award"
]
for item in proof:
    c.drawString(m+8, y, "- " + item); y -= 14

y -= 8
c.setFillColor(gold); c.setFont("Times-BoldItalic", 12); c.drawString(m, y, '"Terrific talk."')
c.setFillColor(muted); c.setFont("Helvetica", 7.5); c.drawString(m+115, y, "Meeting of the Minds conference attendee")
y -= 20
c.setFillColor(gold); c.setFont("Times-BoldItalic", 12); c.drawString(m, y, '"I love your messaging around empowerment."')
c.setFillColor(muted); c.setFont("Helvetica", 7.5); c.drawString(m+255, y, "Meeting of the Minds conference attendee")

y -= 15
c.setFillColor(navy); c.setFont("Helvetica-Bold", 8)
c.drawString(m, y, "RECORDED SPEAKING SAMPLE: UNIVERSITY OF THE PACIFIC CHANGEMAKERS")
y -= 14
c.setFillColor(muted); c.setFont("Helvetica", 8)
c.drawString(m, y, "youtube.com/watch?v=AJW-Kt0LcdU (not a keynote reel)")
c.linkURL("https://www.youtube.com/watch?v=AJW-Kt0LcdU", (m, y-2, m+330, y+12), relative=0)
y -= 34
c.setStrokeColor(gold); c.line(m, y, W-m, y)
y -= 20
c.setFillColor(navy); c.setFont("Helvetica-Bold", 10); c.drawString(m, y, "gq@drdlamini.com")
c.setFont("Helvetica", 9); c.drawRightString(W-m, y, "drdlamini.com  |  linkedin.com/in/gdlamini  |  deeplyoptimistic.com")
c.save()
print(OUT)
