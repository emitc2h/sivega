import ROOT
from core.elements.canvas import Canvas
from core.elements.plotarea import Plotarea
from core.elements.plotbox import Plotbox

from core.styles import color

## First create the canvas
c  = Canvas()
pa = Plotarea(c.width, c.height, background_color=color.pale_grey)
pb = Plotbox(20.0, 180.0, 0.0, 1.0, background_color=color.grey)
pb.provide_context(pa)
c.append(pa)

## Create the path that will encircle the plotbox
from core.elements.path import Path
from core.coordinates.point import Point

plotbox = Path(stroke_width=2, closed=True)
arrow   = Path(fill_color=color.red, closed=True)

## Add the points
plotbox.points.append(Point(20.0, 0.0,  pb.origin, pb.transform))
plotbox.points.append(Point(180.0, 0.0, pb.origin, pb.transform))
plotbox.points.append(Point(180.0, 1.0, pb.origin, pb.transform))
plotbox.points.append(Point(20.0, 1.0,  pb.origin, pb.transform))

## Make an arrow
arrow.points.append(Point(60.0, 0.10, pb.origin, pb.transform))
arrow.points.append(Point(60.0, 0.40, pb.origin, pb.transform))
arrow.points.append(Point(50.0, 0.40, pb.origin, pb.transform))
arrow.points.append(Point(70.0, 0.60, pb.origin, pb.transform))
arrow.points.append(Point(90.0, 0.40, pb.origin, pb.transform))
arrow.points.append(Point(80.0, 0.40, pb.origin, pb.transform))
arrow.points.append(Point(80.0, 0.10, pb.origin, pb.transform))

## Add the plotbox to the canvas
pb.append(plotbox)
pb.append(arrow)

c.draw('canvas_test', 'svg')

