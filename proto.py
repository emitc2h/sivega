import cairosvg

f_in = open('logo.svg')
svg_code = f_in.read()
f_png_out = open('test.png', 'w')
f_pdf_out = open('test.pdf', 'w')
cairosvg.svg2png(bytestring=svg_code, write_to=f_png_out)
cairosvg.svg2pdf(bytestring=svg_code, write_to=f_pdf_out)
f_png_out.close()
f_pdf_out.close()