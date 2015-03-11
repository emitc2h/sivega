#**************************************************#
# file   : core/elements/point.py                  #
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

####################################################
class Point(object):

    ## ------------------------------------------
    def __init__(self, x, y, coordinates='abs'):
        """
        Constructor
        """

        ## Coordinates specified in coordinate system of choice
        self.x = x
        self.y = y

        ## Coordinate system for x & y
        self.coordinates = coordinates

        ## Corresponding absolute coordinates, calculated during rendering
        self.abs_x = None
        self.abs_y = None