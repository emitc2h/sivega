#**************************************************#
# file   : core/elements/box.py                    #
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
from ..styles import color
from axis import Axis

####################################################
class Box(Element, list):


    ## ------------------------------------------
    def __init__(self, x0,y0, x1,y1, parent_box=None):
        """
        Constructor
        """

        ## Initialize Element
        super(Box, self).__init__()

        ## Link to parent box
        self.set_parent_box = parent_box

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.width  = float(self.x1 - self.x0)
        self.height = float(self.y1 - self.y0)

        ## Specify basic coordinate systems
        self.coordinate_systems = {
                            'rel' : ((0,0), (1,1)),
                            'abs' : ((x0,y0), (x1,y1))
                            }

        ## List of elements
        self.elements = []

        ## graphical attributes
        self.fill   = color.white
        self.stroke = None
        self.stroke_width = None


    ## ------------------------------------------
    def add_scaled_coordinate_system(self, name, x0,y0, x1,y1):
        """
        Set the scaled coordinate system
        """

        self.coordinate_systems[name] = ((x0,y0),(x1,y1))


    ## ------------------------------------------
    def render_point_coordinates(self):
        """
        Returns the absolute coordinates corresponding to the given point
        """

        for element in self.elements:
            element.render_point_coordinates()


    ## ------------------------------------------
    def create_subbox(self, left_margin=0, right_margin=0, bottom_margin=0, top_margin=0):
        """
        Creates a sub-box, margins are specified as fractions of total width/height
        """

        x0 = self.x0 + left_margin * self.width
        x1 = self.x1 - right_margin * self.width

        y0 = self.y0 + bottom_margin * self.height
        y1 = self.y1 - top_margin * self.height

        subbox = Box(x0,y0, x1,y1, self)

        self.append(subbox)

        return subbox


    ## ------------------------------------------
    def create_subbox_array(self, columns, rows, left_margin=0, right_margin=0, bottom_margin=0, top_margin=0):
        """
        Creates an array of sub-boxes, margins are specified a as fraction of the maximum
        width/height a subbox can take
        """

        subbox_array = []

        subbox_width  = self.width/columns
        subbox_height = self.height/rows

        for i in range(columns):
            for j in range(rows):

                x0 = subbox_width*i + left_margin * subbox_width + self.x0
                x1 = subbox_width*(i+1) - right_margin * subbox_width + self.x0

                y0 = (self.height - subbox_height*(j+1)) + bottom_margin * subbox_height + self.y0
                y1 = (self.height - subbox_height*j)     - top_margin * subbox_height + self.y0

                subbox = Box(x0,y0, x1,y1, self)

                self.append(subbox)

                subbox_array.append(subbox)

        return subbox_array


    ## ------------------------------------------
    def create_axes(self, coordinates):
        """
        Create axes bounding the box
        """

        for edge in ['bottom', 'right', 'top', 'left']:
            axis = Axis(edge, coordinates)
            axis.set_parent_box(self)
            self.elements.append(axis)


    ## ------------------------------------------
    def render(self):
        """
        Renders the box to svg
        """

        ## Creates the group that will contain everything in the box
        self.xml = etree.Element('g')

        ## Creates the background rectangle
        background = etree.Element('rect')

        ## Set background attributes
        background.attrib['x']      = str(self.x0)
        background.attrib['y']      = str(self.y0)
        background.attrib['width']  = str(self.x1 - self.x0)
        background.attrib['height'] = str(self.y1 - self.y0)

        background.attrib['fill'] = self.fill
        if not self.stroke is None:
            background.attrib['stroke'] = self.stroke
            if not self.stroke_width is None:
                background.attrib['stroke-width'] = str(self.stroke_width)

        ## Append background first in the group (such that it IS the background to everything else)
        self.xml.append(background)

        ## Now render the elements included in the current box
        self.render_point_coordinates()

        definitions = []

        for element in self.elements:
            definitions += element.render()
            self.xml.append(element.xml)

        ## Now render the subboxes:
        for box in self:
            definitions += box.render()
            self.xml.append(box.xml)

        return definitions


    ## ------------------------------------------
    def flip(self, height):
        """
        flip elements that need to be flipped
        """

        for element in self.elements:
            element.flip(height)

        for box in self:
            box.flip(height)


    ## ------------------------------------------
    def add(self, element):
        """
        Adds an element to the box
        """

        element.set_parent_box(self)
        self.elements.append(element)








