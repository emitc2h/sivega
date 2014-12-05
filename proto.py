import cairosvg, lxml

f_in = open('logo.svg')
svg_code = f_in.read()
f_out = open('logo.png', 'w')
cairosvg.svg2png(bytestring=svg_code, write_to=f_out)
f_out.close()