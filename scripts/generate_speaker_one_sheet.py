"""Create a polished, single-page speaker sheet for GitHub Pages."""
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

OUT = Path('assets/dr-dlamini-speaker-one-sheet.pdf')
PORTRAIT = Path('assets/img/hero-portrait.jpg')
OUT.parent.mkdir(parents=True, exist_ok=True)

navy = HexColor('#10243d')
gold = HexColor('#c99a4a')
gold_light = HexColor('#ead4a8')
muted = HexColor('#526171')
cream = HexColor('#f7f3eb')
paper = HexColor('#fffdf9')
line = HexColor('#d7dce1')
white = HexColor('#ffffff')

c = canvas.Canvas(str(OUT), pagesize=letter, pageCompression=1)
c.setTitle('Dr. Geqigula Dlamini | Speaker One-Sheet')
c.setAuthor('Dr. Geqigula Dlamini')
W, H = letter
m = 46

# A restrained editorial header with a photographic portrait.
c.setFillColor(paper)
c.rect(0, 0, W, H, stroke=0, fill=1)
c.setFillColor(navy)
c.rect(0, 568, W, H-568, stroke=0, fill=1)
c.setFillColor(gold_light)
c.setFont('Helvetica-Bold', 10)
c.drawString(m, 751, 'DR. GEQIGULA DLAMINI')
c.setFont('Helvetica', 8.5)
c.drawString(m, 733, 'KEYNOTES  /  LEADERSHIP WORKSHOPS  /  ADVISORY')
c.setFillColor(white)
c.setFont('Times-Bold', 29)
c.drawString(m, 686, 'Turn complexity')
c.drawString(m, 654, 'into capability.')
c.setFillColor(HexColor('#e4e9ef'))
c.setFont('Helvetica', 9.4)
c.drawString(m, 628, 'Helping mission-driven organizations align people,')
c.drawString(m, 614, 'technology and execution to create lasting results.')

# Use the same high-quality, professional headshot as the website.
with Image.open(PORTRAIT) as original:
    portrait = ImageOps.fit(original.convert('RGB'), (410, 540),
                            method=Image.Resampling.LANCZOS, centering=(0.5, 0.35))
    blob = BytesIO()
    portrait.save(blob, format='JPEG', quality=91, optimize=True)
    blob.seek(0)
    c.setFillColor(gold)
    c.rect(440, 582, 132, 162, fill=1, stroke=0)
    c.drawImage(ImageReader(blob), 444, 586, width=124, height=154, mask='auto')

c.setFillColor(gold)
c.rect(m, 553, 28, 2, fill=1, stroke=0)
c.setFillColor(navy)
c.setFont('Helvetica-Bold', 9.5)
c.drawString(m, 534, 'SPEAKING THEMES')

def topic(top, number, title, description):
    c.setFillColor(cream)
    c.roundRect(m, top-59, W-2*m, 60, 8, stroke=0, fill=1)
    c.setFillColor(gold)
    c.setFont('Helvetica-Bold', 8)
    c.drawString(m+15, top-18, number)
    c.setFillColor(navy)
    c.setFont('Times-Bold', 13.5)
    c.drawString(m+43, top-18, title)
    c.setFillColor(muted)
    c.setFont('Helvetica', 8.8)
    c.drawString(m+43, top-36, description)

topic(517, '01', 'Empowering Those Who Power Organizations',
      'A human-centered approach to AI adoption, agency and change.')
topic(447, '02', 'Mission Enablement in Complex Systems',
      'Aligning people, strategy and execution when the path is unclear.')
topic(377, '03', 'The Discipline of Optimism',
      'Leadership practices that make progress and possibility actionable.')

c.setFillColor(navy)
c.setFont('Helvetica-Bold', 9.5)
c.drawString(m, 289, 'EXPERIENCE AND EVIDENCE')
c.setStrokeColor(line)
c.line(m, 277, W-m, 277)
c.setFillColor(muted)
c.setFont('Helvetica', 9.25)
for y, item in [
    (257, 'Closing keynote, California Workforce Association Meeting of the Minds 2026'),
    (240, 'Two-time University of the Pacific Changemakers presenter'),
    (223, 'Doctoral Innovation in Research and Practice Award'),
]:
    c.setFillColor(gold)
    c.circle(m+3, y+3, 2.1, stroke=0, fill=1)
    c.setFillColor(muted)
    c.drawString(m+13, y, item)

c.setFillColor(navy)
c.setFont('Times-Italic', 13)
c.drawString(m, 185, '"I love your messaging around empowerment."')
c.setFillColor(muted)
c.setFont('Helvetica', 8.4)
c.drawString(m, 170, 'Meeting of the Minds conference attendee')

c.setStrokeColor(line)
c.line(m, 151, W-m, 151)
c.setFillColor(navy)
c.setFont('Helvetica-Bold', 8.5)
c.drawString(m, 133, 'WATCH A RECORDED PRESENTATION')
c.setFont('Helvetica', 9)
c.setFillColor(muted)
c.drawString(m, 117, 'University of the Pacific Changemakers  |  youtube.com/watch?v=AJW-Kt0LcdU')
c.linkURL('https://www.youtube.com/watch?v=AJW-Kt0LcdU', (m, 111, W-m, 133), relative=0)

c.setFillColor(navy)
c.rect(0, 0, W, 76, stroke=0, fill=1)
c.setFillColor(gold_light)
c.setFont('Helvetica-Bold', 11)
c.drawString(m, 44, 'gq@drdlamini.com')
c.linkURL('mailto:gq@drdlamini.com?subject=Speaking%20Inquiry', (m, 38, 245, 58), relative=0)
c.setFillColor(white)
c.setFont('Helvetica', 9)
c.drawString(m, 25, 'drdlamini.com   |   linkedin.com/in/gdlamini')
c.save()
print(OUT)
