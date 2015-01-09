#**************************************************#
# file   : core/coordinates/point.py               #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A single point in the svg plane                  #
#**************************************************#

#############################################################################
#   Copyright 2014-2015 Michel Trottier-McDonald                            #
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

import absolute_origin
import absolute_transform

####################################################
class Point(object):

    ## ------------------------------------------
    def __init__(self, x, y, origin=absolute_origin, transform=absolute_transform):
        """
        Constructor
        """

        self.x = x
        self.y = y

        self.origin    = origin
        self.transform = transform

        self.absolute_origin  = absolute_origin
        self.absolute_transform = absolute_transform


    ## ------------------------------------------
    def get():
        """
        return the coordinates as provided originally
        """

        return self.x, self.y


    ## ------------------------------------------
    def get_absolute():
        """
        return the coordinates in the absolute coordinate system
        """

        x_prime, y_prime = self.transform.apply(self.x, self.y)
        return x_prime + self.origin.x, y_prime + self.origin.y


    ## ------------------------------------------
    def get_render():
        """
        return the coordinates for the final render, in svg coordinates
        """

        x_prime, y_prime = self.absolute_transform.apply(*self.get_absolute())
        return x_prime + self.absolute_origin.x, y_prime + self.absolute_origin.y
