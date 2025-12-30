from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_bill(
    bill_no,
    name_en,
    name_kn,
    phone,
    bike_no,
    bike_model,
    subtotal,
    gst,
    total
):
    filename = f"Bill_{bill_no}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-50, "BIKE SERVICE BILL / ಬೈಕ್ ಸರ್ವೀಸ್ ಬಿಲ್")

    # Shop details
    c.setFont("Helvetica", 10)
    c.drawCentredString(width/2, height-70, "ABC Bike Service Center")
    c.drawCentredString(width/2, height-85, "Phone: 9XXXXXXXXX | GSTIN: 29XXXXX")

    y = height - 130
    c.drawString(50, y, f"Bill No: {bill_no}")
    c.drawString(350, y, f"Date: {datetime.now().strftime('%d-%m-%Y')}")

    y -= 30
    c.drawString(50, y, f"Customer: {name_en} / {name_kn}")
    y -= 20
    c.drawString(50, y, f"Mobile: {phone}")
    y -= 20
    c.drawString(50, y, f"Bike No: {bike_no}")
    y -= 20
    c.drawString(50, y, f"Bike Model: {bike_model}")

    y -= 40
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Description")
    c.drawString(400, y, "Amount (₹)")
    c.line(50, y-5, 550, y-5)

    c.setFont("Helvetica", 10)
    y -= 25
    c.drawString(50, y, "Bike Service / ಬೈಕ್ ಸರ್ವೀಸ್")
    c.drawString(400, y, f"{subtotal:.2f}")

    y -= 30
    c.drawString(350, y, "Subtotal:")
    c.drawString(450, y, f"{subtotal:.2f}")

    y -= 20
    c.drawString(350, y, "GST (18%):")
    c.drawString(450, y, f"{gst:.2f}")

    y -= 20
    c.setFont("Helvetica-Bold", 11)
    c.drawString(350, y, "TOTAL:")
    c.drawString(450, y, f"{total:.2f}")

    y -= 60
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, y, "Thank you / ಧನ್ಯವಾದಗಳು")

    c.showPage()
    c.save()

    return filename

