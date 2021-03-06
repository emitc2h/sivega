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
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """

        super(Primitive, self).__init__(*args, **kwargs)

        self.points = []
        self.definitions = []
        self.flipped = False


    ## ------------------------------------------
    def render_point_coordinates(self):
        """
        Returns the absolute coordinates corresponding to the given point
        """

        for point in self.points:
            point.abs_x, point.abs_y = point.calculate_for_coordinates('abs')


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
