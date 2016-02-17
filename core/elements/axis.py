#**************************************************#
# file   : core/elements/axis.py                   #
# author : Michel Trottier-McDonald                #
# date   : March 2015                              #
# description:                                     #
# An axis, stating the coordinate system of a box  #
#**************************************************#

#############################################################################
#   Copyright 2015 Michel Trottier-McDonald                                 #
#                                                                           #
#   This file is part of sivega.                                            #
#                                                                           #
#   sivega is free software: you can redistribute it and/or modify          #
#   it under the terms of the GNU General Public License as published by    #
#   the Free Software Foundation, either version 3 of the License, or       #
#   (at your option) any later version.                                     #
#                                                                           #
#   sivega is distributed in the hope that it will be useful,               #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#   GNU General Public License for more details.                            #
#                                                                           #
#   You should have received a copy of the GNU General Public License       #
#   along with sivega.  If not, see <http://www.gnu.org/licenses/>.         #
#############################################################################

from lxml import etree
from primitive import Primitive
from composite import Composite
from tick import Tick
from point import Point
from ..styles import color

####################################################
class Comb(Primitive):

    vertical_tick_density   = 50.0/600 ## Assuming default canvas size of 800x600 pixels
    horizontal_tick_density = 40.0/800 ## is adjusted for aspect-ratio

    ## ------------------------------------------
    def __init__(self, edge, coordinates, divisions=None, labels=False, *args, **kwargs):
        """
        Constructor
        """

        super(Comb, self).__init__(*args, **kwargs)

        self.tick_stroke       = color.black
        self.tick_stroke_width = 1
        self.tick_length       = 3

        self.axis_stroke       = color.black
        self.axis_stroke_width = 3

        self.labels         = labels
        self.labels_offset  = 3
        self.labels_size    = 5
        self.labels_strings = []

        ## Assert that the edge provided is one of the 4 possible edges
        self.edge        = edge
        assert self.edge in ['bottom', 'right', 'top', 'left']

        self.coordinates = coordinates
        assert self.coordinates in self.parent_box.coordinate_systems.keys()

        self.divisions = divisions


    ## ------------------------------------------
    def generate_ticks(self):
        """
        Generate the position of the ticks
        """

        ## Automatically generate a sensible number of divisions
        if self.divisions is None:
            if self.edge == 'top' or self.edge == 'bottom':
                self.divisions = int(self.parent_box.width*Comb.horizontal_tick_density)
            else:
                self.divisions = int(self.parent_box.height*Comb.vertical_tick_density)


        ## Figure out axis range and increments
        if self.edge == 'top' or self.edge == 'bottom':
            k0 = self.parent_box.coordinate_systems[self.coordinates][0][0]
            k1 = self.parent_box.coordinate_systems[self.coordinates][1][0]
        else:
            k0 = self.parent_box.coordinate_systems[self.coordinates][0][1]
            k1 = self.parent_box.coordinate_systems[self.coordinates][1][1]

        length = abs(k1-k0)
        origin = k0
        increment = float(length)/self.divisions

        ## Generate points
        if self.edge == 'bottom':
            h0 = self.parent_box.coordinate_systems[self.coordinates][0][1]
            for i in range(self.divisions + 1):
                self.points.append(Point(origin + i*increment, h0, self.parent_box, self.coordinates))

        if self.edge == 'right':
            h0 = self.parent_box.coordinate_systems[self.coordinates][1][0]
            for i in range(self.divisions + 1):
                self.points.append(Point(h0, origin + i*increment,self.parent_box, self.coordinates))

        if self.edge == 'top':
            h0 = self.parent_box.coordinate_systems[self.coordinates][1][1]
            for i in range(self.divisions + 1):
                self.points.append(Point(origin + length - i*increment, h0, self.parent_box, self.coordinates))

        if self.edge == 'left':
            h0 = self.parent_box.coordinate_systems[self.coordinates][0][0]
            for i in range(self.divisions + 1):
                self.points.append(Point(h0, origin + length - i*increment, self.parent_box, self.coordinates))


    ## ------------------------------------------
    def render(self):
        """
        Render the axis
        """

        ## Generate the tick definition
        new_tick = Tick(self.tick_stroke, self.tick_stroke_width, self.tick_length)
        self.definitions.append(new_tick)

        ## Generate the ticks
        self.generate_ticks()

        ## Create the path
        self.xml = etree.Element('path')

        ## Render the path coordinates
        path_string = ''

        for i, point in enumerate(self.points):
            if i == 0:
                path_string = 'M {0},{1}, L '.format(point.abs_x, point.abs_y)
            else:
                path_string += '{0},{1} '.format(point.abs_x, point.abs_y)

        self.xml.attrib['d'] = path_string

        ## Other attributes
        self.xml.attrib['fill'] = 'none'
        self.xml.attrib['stroke'] = self.axis_stroke
        self.xml.attrib['stroke-width'] = '{0}'.format(self.axis_stroke_width)
        self.xml.attrib['marker-mid'] = 'url(#{0})'.format(new_tick.xml_id)

        return super(Comb, self).render()




####################################################
class Axis(Composite):
    """
    An axis object, containing at least one comb, an axis title, and tick labels
    """

    ## ------------------------------------------
    def __init__(self, edge, coordinates, *args, **kwargs):
        """
        Constructor
        """

        super(Axis, self).__init__(*args, **kwargs)

        ## Secondary comb, fine ticks
        self.comb2 = Comb(edge, coordinates, parent_box=self.parent_box)
        self.comb2.divisions = 30

        ## Primary comb, the one corresponding to the tick labels
        self.comb1 = Comb(edge, coordinates, parent_box=self.parent_box)
        self.comb1.divisions = self.comb2.divisions/5
        self.comb1.tick_length = 5

        self.combs = [self.comb1, self.comb2]

        self.primitives.extend(self.combs)









