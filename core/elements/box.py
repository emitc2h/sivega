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

####################################################
class Box(Element, List):


    ## ------------------------------------------
    def __init__(self, x0,y0, x1,y1, parent=None):
        """
        Constructor
        """

        ## Initialize Element
        super(Box, self).__init__()

        ## Link to parent box
        self.parent = parent

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        ## Specify basic coordinate systems
        self.coordinates = {
                            'rel' : ((0,0), (1,1)),
                            'abs' : ((x0,y0), (x1,y1))
                            }

        ## List of primitives
        self.primitives = []


    ## ------------------------------------------
    def add_scaled_coordinate_system(name, x0,y0, x1,y1):
        """
        Set the scaled coordinate system
        """

        self.coordinates[name] = ((x0,y0),(x1,y1))


    ## ------------------------------------------
    def render_point_coordinates(self):
        """
        Returns the absolute coordinates corresponding to the given point
        """

        for primitive in self.primitives:
            for point in primitive.points:

                x0_abs = self.coordinates['abs'][0][0]
                y0_abs = self.coordinates['abs'][0][1]
                x1_abs = self.coordinates['abs'][1][0]
                y1_abs = self.coordinates['abs'][1][1]

                x0_point = self.coordinates[point.system][0][0]
                y0_point = self.coordinates[point.system][0][1]
                x1_point = self.coordinates[point.system][1][0]
                y1_point = self.coordinates[point.system][1][1]

                a = (x1_abs - x0_abs) / (x1_point - x0_point)
                b = (x1_point*x0_abs - x0_point*x1_abs) / (x1_point - x0_point)

                c = (y1_abs - y0_abs) / (y1_point - y0_point)
                d = (y1_point*y0_abs - y0_point*y1_abs) / (y1_point - y0_point)

                point.abs_x = a*point.x + b
                point.abs_y = c*point.y + d


    ## ------------------------------------------
    def create_subbox(left_margin=0, right_margin=0, bottom_margin=0, top_margin=0):
        """
        Creates a sub-box, margins are specified as fractions of total width/height
        """

        width = float(self.x1 - self.x0)

        x0 = self.x0 + left_margin * width
        x1 = self.x1 - right_margin * width

        height = float(self.y1 - self.y0)

        y0 = self.y0 + bottom_margin * height
        y1 = self.y1 - top_margin * height

        subbox = Box(x0,y0, x1,y1)
        subbox.parent = self

        self.append(subbox)

        return subbox


    ## ------------------------------------------
    def create_subbox_array(columns, rows, left_margin=0, right_margin=0, bottom_margin=0, top_margin=0):
        """
        Creates an array of sub-boxes, margins are specified a as fraction of the maximum
        width/height a subbox can take
        """

        width = float(self.x1 - self.x0)
        height = float(self.y1 - self.y0)

        subbox_width  = width/columns
        subbox_height = height/rows

        for i in columns:
            for j in rows:

                x0 = subbox_width*i + left_margin * subbox_width
                y0 = subbox_width*(i+1) - right_margin * subbox_width

                y0 = (height - subbox_height*(j+1)) + bottom_margin * subbox_height
                y1 = (height - subbox_height*j)     - top_margin * subbox_height

                subbox = Box(x0,y0, x1,y1)
                subbox.parent = self

                self.append(subbox)







