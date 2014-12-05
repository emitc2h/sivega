import cairosvg, lxml

f_in = open('test.svg')
svg_code = f_in.read()
f_out = open('test.png', 'w')
cairosvg.svg2png(bytestring=svg_code, write_to=f_out)
f_out.close()