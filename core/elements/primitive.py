#**************************************************#
# file   : core/elements/primitive.py              #
# author : Michel Trottier-McDonald                #
# date   : February 2015                           #
# description:                                     #
# A base class for an xml element                  #
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
from element import Element

####################################################
class Primitive(Element):

    ## ------------------------------------------
    def __init__(self):
        """
        Constructor
        """

        self.points = []
        self.definitions = []
        self.flipped = False

        super(Primitive, self).__init__()


    ## ------------------------------------------
    def render_point_coordinates(self):
        """
        Returns the absolute coordinates corresponding to the given point
        """

        for point in self.points:

            x0_abs = self.parent_box.coordinate_systems['abs'][0][0]
            y0_abs = self.parent_box.coordinate_systems['abs'][0][1]
            x1_abs = self.parent_box.coordinate_systems['abs'][1][0]
            y1_abs = self.parent_box.coordinate_systems['abs'][1][1]

            x0_point = self.parent_box.coordinate_systems[point.coordinates][0][0]
            y0_point = self.parent_box.coordinate_systems[point.coordinates][0][1]
            x1_point = self.parent_box.coordinate_systems[point.coordinates][1][0]
            y1_point = self.parent_box.coordinate_systems[point.coordinates][1][1]

            a = (x1_abs - x0_abs) / (x1_point - x0_point)
            b = (x1_point*x0_abs - x0_point*x1_abs) / (x1_point - x0_point)

            c = (y1_abs - y0_abs) / (y1_point - y0_point)
            d = (y1_point*y0_abs - y0_point*y1_abs) / (y1_point - y0_point)

            point.abs_x = a*point.x + b
            point.abs_y = c*point.y + d


    ## ------------------------------------------
    def render(self):
        """
        Render definitions
        """

        for definition in self.definitions:
            definition.render()

        return self.definitions


    ## ------------------------------------------
    def flip(self, height):
        """
        flip upside-down to compensation for transformation to cartesian coordinates
        mostly for text, to be performed after rendering
        """

        if self.flipped:
            y = float(self.xml.attrib['y'])
            if 'transform' in self.xml.attrib.keys():
                self.xml.attrib['transform'] = ' '.join(['translate(0,{0}), scale(1,-1)'.format(2*y), self.xml.attrib['transform']])
            else:
                self.xml.attrib['transform'] = 'translate(0,{0}), scale(1,-1)'.format(2*y)
