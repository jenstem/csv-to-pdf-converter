from fpdf import FPDF
from fpdf.fonts import FontFace
import csv


with open("countries.txt", encoding="utf-8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))


pdf = FPDF()
pdf.set_font("Arial", size=14)


pdf.add_page()