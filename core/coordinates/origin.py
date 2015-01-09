#**************************************************#
# file   : core/coordinates/origin.py              #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A coordinate system origin in the svg plane      #
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

####################################################
class Origin(object):

    ## ------------------------------------------
    def __init__(self, x=0, y=0, origin=None, transform=None):
        """
        Constructor
        """

        if origin is None and transform is None:
            self.x = x
            self.y = y
        elif origin is None:
            self.x, self.y = transform.apply(x, y)
        elif scaling is None:
            self.x = origin.x + x
            self.y = origin.y + y
        else:
            x_prime, y_prime = transform.apply(x, y)
            self.x = x_prime + origin.x
            self.y = y_prime + origin.y

