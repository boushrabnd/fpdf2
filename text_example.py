from fpdf import FPDF
pdf = FPDF()
pdf.compress= False
pdf.add_page()
pdf.set_font('helvetica', size=12)
pdf.cell(text="hello world")
pdf.set_font('times', size=13)
pdf.cell(text="hello world")
pdf.output("hello_world_2.pdf")
