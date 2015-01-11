import cairosvg
from core.elements.canvas import Canvas

## First create the canvas
c = Canvas()

## Establish coordinate systems
from core.coordinates.origin import Origin
from core.coordinates.transform import Transform, Function, linear, linear_flat, linear_neutral

## I want a plot where the x-axis covers from 20-180 and the y-axis covers from 0 to 1
plot_x_lo = 20.0
plot_x_hi = 180.0
plot_y_lo = 0.0
plot_y_hi = 1.0

## Determine a plot area within the canvas using relative margins
left_margin = 0.15
right_margin = 0.05
bottom_margin = 0.10
top_margin = 0.05

## Make an absolute origin for the plotbox
plotbox_origin_absolute = Origin(left_margin*c.width, bottom_margin*c.height)

## Construct the plot transform
plot_x_linear = Function(linear, 0, 0, (c.width*(1-left_margin-right_margin))/(plot_x_hi-plot_x_lo))
plot_y_linear = Function(linear, 0, 0, (c.height*(1-top_margin-bottom_margin))/(plot_y_hi-plot_y_lo))

## These transforms should allow one to input points in the canvas using the plot coordinates
plotbox_transform = Transform(plot_x_linear, plot_y_linear)
plotbox_origin    = Origin(-plot_x_lo, -plot_y_lo, plotbox_origin_absolute, plotbox_transform)

## Create the path that will encircle the plotbox
from core.elements.path import Path
from core.coordinates.point import Point
from core.styles import color
plotbox = Path(stroke_width=2, closed=True)
arrow   = Path(fill_color=color.red, closed=True)

## Add the points
plotbox.points.append(Point(20.0, 0.0, plotbox_origin, plotbox_transform))
plotbox.points.append(Point(180.0, 0.0, plotbox_origin, plotbox_transform))
plotbox.points.append(Point(180.0, 1.0, plotbox_origin, plotbox_transform))
plotbox.points.append(Point(20.0, 1.0, plotbox_origin, plotbox_transform))

## Make an arrow
arrow.points.append(Point(60.0, 0.10, plotbox_origin, plotbox_transform))
arrow.points.append(Point(60.0, 0.40, plotbox_origin, plotbox_transform))
arrow.points.append(Point(50.0, 0.40, plotbox_origin, plotbox_transform))
arrow.points.append(Point(70.0, 0.60, plotbox_origin, plotbox_transform))
arrow.points.append(Point(90.0, 0.40, plotbox_origin, plotbox_transform))
arrow.points.append(Point(80.0, 0.40, plotbox_origin, plotbox_transform))
arrow.points.append(Point(80.0, 0.10, plotbox_origin, plotbox_transform))

## Add the plotbox to the canvas
c.append(plotbox)
c.append(arrow)

c.draw('canvas_test', 'svg')

