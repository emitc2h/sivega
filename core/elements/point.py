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

import box

####################################################
class Point(object):

    ## ------------------------------------------
    def __init__(self, x, y, parent_box, coordinates='abs'):
        """
        Constructor
        """

        ## Coordinates specified in coordinate system of choice
        self.x = x
        self.y = y

        ## Assert that the parent_box is indeed a box object
        assert type(parent_box) is box.Box, 'parent_box argument needs a Box instance, not a {0}'.format(type(parent_box))
        self.parent_box = parent_box

        ## Coordinate system for x & y
        assert coordinates in self.parent_box.coordinate_systems.keys(), \
         '\'{0}\' is not a coordinate system of the parent box. Options are {1}'.format(coordinates, self.parent_box.coordinate_systems.keys())
        self.coordinates = coordinates

        ## Corresponding absolute coordinates, calculated during rendering
        self.abs_x, self.abs_y = self.calculate_for_coordinates('abs')


    ## ------------------------------------------
    def calculate_for_coordinates(self, coordinates):
        """
        Calculates the point in a provided coordinate system
        """

        assert coordinates in self.parent_box.coordinate_systems.keys(), \
         '\'{0}\' is not a coordinate system of the parent box. Options are {1}'.format(coordinates, self.parent_box.coordinate_systems.keys())

        ## Retrieve the coordinates of the bounding box in the new coordinate system
        x0 = self.parent_box.coordinate_systems[coordinates][0][0]
        y0 = self.parent_box.coordinate_systems[coordinates][0][1]
        x1 = self.parent_box.coordinate_systems[coordinates][1][0]
        y1 = self.parent_box.coordinate_systems[coordinates][1][1]

        ## Retrieve the coordinates of the bounding box in the point's own coordinate system
        x0_own = self.parent_box.coordinate_systems[self.coordinates][0][0]
        y0_own = self.parent_box.coordinate_systems[self.coordinates][0][1]
        x1_own = self.parent_box.coordinate_systems[self.coordinates][1][0]
        y1_own = self.parent_box.coordinate_systems[self.coordinates][1][1]

        ## Apply the function mapping from the point's coordinates to the new coordinate system
        x0_trf, y0_trf = self.parent_box.coordinate_systems[self.coordinates][2](x0_own, y0_own)
        x1_trf, y1_trf = self.parent_box.coordinate_systems[self.coordinates][2](x1_own, y1_own)

        a = (x1 - x0) / (x1_trf - x0_trf)
        b = (x1_trf*x0 - x0_trf*x1) / (x1_trf - x0_trf)

        c = (y1 - y0) / (y1_trf - y0_trf)
        d = (y1_trf*y0 - y0_trf*y1) / (y1_trf - y0_trf)

        x, y = self.parent_box.coordinate_systems[self.coordinates][2](self.x, self.y)

        return  a*x + b, c*y + d


    ## -------------------------------------------
    def __repr__(self):
        """
        String representation
        """

        absx = self.abs_x if not self.abs_x is None else float('nan')
        absy = self.abs_y if not self.abs_y is None else float('nan')

        return '({x:.2},{y:.2}) in \'{coord}\' coordinates, ({absx:.2},{absy:.2}) in absolute coordinates'.format(
            x=float(self.x),
            y=float(self.y),
            coord=self.coordinates,
            absx=float(absx),
            absy=float(absy)
            )



