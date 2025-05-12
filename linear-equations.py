from fpdf import FPDF
from sympy import preview
import os

# Create a custom PDF class to support math images
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Linear Equations Practice Worksheet", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(3)

    def add_math_eq(self, number, latex_expr):
        # Render LaTeX expression to image
        image_path = f"/mnt/data/eq_{number}.png"
        preview(latex_expr, viewer='file', filename=image_path, euler=False, dvioptions=['-D', '150'])
        self.image(image_path, w=170)
        os.remove(image_path)

# Create PDF instance
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Section A
pdf.chapter_title("Section A: Fraction-Based Linear Equations")
section_a = [
    r"\frac{2(x + 3)}{5} + \frac{3(x - 2)}{7} = \frac{4(x + 1)}{10}",
    r"\frac{3(x - 1)}{4} - \frac{2(x + 2)}{3} = \frac{x + 5}{6}",
    r"\frac{2x + 3}{8} + \frac{4(x - 1)}{5} = \frac{3(x + 2)}{10}",
    r"\frac{5(x + 2)}{6} - \frac{2x - 3}{9} = \frac{x + 1}{12}",
    r"\frac{2(x - 4)}{7} + \frac{3(x + 5)}{3} = \frac{5x + 3}{6}",
    r"\frac{4x + 6}{5} - \frac{2(x - 3)}{8} = \frac{x + 9}{10}",
    r"\frac{x + 2}{6} + \frac{x - 3}{4} = \frac{2x - 1}{9}",
    r"\frac{3(x + 1)}{5} - \frac{x - 2}{6} = \frac{2(x + 2)}{10}",
    r"\frac{2(x + 3)}{9} + \frac{x - 4}{7} = \frac{3x + 1}{6}",
    r"\frac{6x - 2}{4} - \frac{2(x + 5)}{9} = \frac{2x - 6}{12}",
    r"\frac{3(x - 1)}{8} + \frac{2(x + 2)}{5} = \frac{5x + 1}{10}",
    r"\frac{4(x - 2)}{3} - \frac{x + 3}{7} = \frac{3x - 11}{9}",
    r"\frac{5x + 2}{12} + \frac{3(x - 1)}{4} = \frac{8x - 1}{6}",
    r"\frac{2x + 5}{5} - \frac{x - 1}{8} = \frac{x + 6}{10}",
    r"\frac{4(x - 3)}{9} + \frac{2(x + 4)}{6} = \frac{6x - 2}{12}",
    r"\frac{3(x + 5)}{7} - \frac{x - 2}{5} = \frac{2x + 17}{8}",
    r"\frac{5x - 4}{6} + \frac{x + 3}{9} = \frac{6x - 1}{10}",
    r"\frac{2(x + 7)}{5} - \frac{x - 3}{6} = \frac{x + 11}{4}",
    r"\frac{4x + 1}{9} + \frac{2(x - 2)}{7} = \frac{6x - 3}{8}",
    r"\frac{6(x - 1)}{10} - \frac{3(x + 2)}{6} = \frac{3x - 12}{9}"
]
for i, eq in enumerate(section_a, 1):
    pdf.add_math_eq(i, f"${eq}$")

# Section B
pdf.chapter_title("Section B: Mixed Linear Equations")
section_b = [
    r"3(x - 2) + 2(x + 4) = 5x + 2",
    r"2x + 3 = 4x - 7",
    r"5(x + 1) = 2(x + 4) + x",
    r"4x - 3 = 2x + 7",
    r"7(x - 1) - 3(x + 2) = 2x + 1",
    r"2(x - 3) + 3(2x + 1) = x + 11",
    r"x + 2 = 3(x - 1) - 4",
    r"3(x + 5) - 2(x - 3) = 4x + 9"
]
for j, eq in enumerate(section_b, 21):
    pdf.add_math_eq(j, f"${eq}$")

# Save the PDF
pdf_output_path = "/mnt/data/Linear_Equations_Worksheet_Rendered.pdf"
pdf.output(pdf_output_path)
pdf_output_path
