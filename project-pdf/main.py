#! /usr/bin/python2
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def hello_pdf():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(0,0,"HelloxWorld")
    c.showPage()
    c.save()

def disk_report():
    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
#   print p.stdout.readlines()
    return p.stdout.readlines()

def create_pdf(input, output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11*inch)
    textobject.textLines('''Disk Capcity Report: %s''' %date)
    for line in input:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()

if __name__ == "__main__":
    print("Enter ReportLab project ...")
    report = disk_report()
    create_pdf(report)
