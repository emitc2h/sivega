#import cairosvg
#from core.elements.canvas import Canvas
#
#c = Canvas()
#
#f_svg_out = open('test.svg', 'w')
#f_png_out = open('test.png', 'w')
#f_pdf_out = open('test.pdf', 'w')
#
#f_svg_out.write(c.string())
#cairosvg.svg2png(bytestring=c.string(), write_to=f_png_out)
#cairosvg.svg2pdf(bytestring=c.string(), write_to=f_pdf_out)
#
#f_svg_out.close()
#f_png_out.close()
#f_pdf_out.close()

from core.histogram import Histogram
import ROOT

th1f_gaus = ROOT.TH1F('Gaussian', '', 20, -3, 3)
th1f_gaus.FillRandom('gaus', 10000)

h_gaus = Histogram('gaussian-test', 'arbitrary units')
h_gaus.add(th1f_gaus, 'gaussian')
h_gaus.draw('hgaus', 'png')
h_gaus.draw('hgaus', 'svg')

