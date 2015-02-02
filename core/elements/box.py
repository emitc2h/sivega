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

####################################################
class Box(Element):

    ## ------------------------------------------
    def __init__(self, x0,y0, x1,y1):
        """
        Constructor
        """

        super(Box, self).__init__()

        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

        self.coordinates = {
                            'rel' : ((0,0), (1,1)),
                            'abs' : ((x0,y0), (x1,y1)),
                            'scl' : ((x0,y0), (x1,y1))
                            }


    ## ------------------------------------------
    def set_scl(x0,y0, x1,y1):
        """
        Set the scaled coordinate system
        """

        self.coordinates['scl'] = ((x0,y0),(x1,y1))


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







