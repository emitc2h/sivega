import cairosvg
from core.elements.canvas import Canvas

c = Canvas()

f_svg_out = open('test.svg', 'w')
f_png_out = open('test.png', 'w')
f_pdf_out = open('test.pdf', 'w')

f_svg_out.write(c.string())
cairosvg.svg2png(bytestring=c.string(), write_to=f_png_out)
cairosvg.svg2pdf(bytestring=c.string(), write_to=f_pdf_out)

f_svg_out.close()
f_png_out.close()
f_pdf_out.close()