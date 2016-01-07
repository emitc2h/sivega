from core.elements.canvas import Canvas
from core.elements.text import Text
from core.elements.point import Point

from core.styles import color

c = Canvas()
c.stroke = color.black
c.stroke_width = 3

plot_main = c.create_subbox(0.10, 0.10, 0.40, 0.10)
plot_main.fill = color.red
plot_main.stroke = color.black
plot_main.stroke_width = 3
plot_main.create_axes('abs')

plot_ratio = c.create_subbox(0.10, 0.10, 0.10, 0.60)
plot_ratio.fill = color.blue
plot_ratio.stroke = color.black
plot_ratio.stroke_width = 3

plot_ratio_subboxes = plot_ratio.create_subbox_array(2, 1, 0.05, 0.05)
plot_ratio_subboxes[0].fill = color.green
plot_ratio_subboxes[0].create_axes('abs')
plot_ratio_subboxes[1].fill = color.yellow

text_main = Text('Main box', Point(0.5, 0.5, 'rel'))
text_main.weight = 'bold'
text_main.size = 32
text_main.anchor = 'middle'
plot_main.add(text_main)

c.draw('test', 'svg')

