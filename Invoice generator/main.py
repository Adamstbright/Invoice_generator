import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")


    pdf.set_font(family="Times", size=16, )
    pdf.cell(w=50, h=8, ln=1, txt=f"Invoice nr{invoice_nr}.pdf")

    pdf.set_font(family="Times", size=16, )
    pdf.cell(w=50, h=8, txt=f"Date: {date}.pdf")

    pdf.output(f"PDFs/{filename}.pdf")
