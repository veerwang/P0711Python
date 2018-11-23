#! /usr/bin/python2
from reportlab.pdfgen import canvas

def hello_pdf():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(0,0,"Hello,World")
    c.showPage()
    c.save()

if __name__ == "__main__":
    print("Enter ReportLab project ...")
    hello_pdf();
