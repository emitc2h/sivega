from core.elements.canvas import Canvas

from core.styles import color

c = Canvas()

plot_area = c.create_subbox(0.10, 0.10, 0.10, 0.10)
plot_area.fill = color.red
plot_area.stroke = color.black
plot_area.stroke_width = 3

array = plot_area.create_subbox_array(2, 2, 0.1, 0.1, 0.1, 0.1)

array[0].fill = color.blue
array[0].stroke = color.white
array[0].stroke_width = 3

array[1].fill = color.green
array[1].stroke = color.black
array[1].stroke_width = 3

array[2].fill = color.white
array[2].stroke = color.black
array[2].stroke_width = 3

array[3].fill = color.black
array[3].stroke = color.white
array[3].stroke_width = 3

c.draw('test', 'svg')

