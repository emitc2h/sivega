#**************************************************#
# file   : core/coordinates/origin.py              #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A coordinate transform from a given coordinate   #
# system back to the absolute system               #
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

import math

####################################################
class Function(object):

    ## ------------------------------------------
    def __init__(self, function, *args):
        """
        Constructor
        ---
        the first parameter of function must always be the variable
        """

        self.function   = function
        self.parameters = args


    ## ------------------------------------------
    def evaluate(self, x):
        """
        Evaluate the function
        """
        return function(x, *self.parameters)




## Define convenient functions
def linear(x, x_origin=0, y_origin=0, slope=1):
    return slope*(x - x_origin) + y_origin

def logarithm(x, base=10):
    return math.log(x, base)

linear_flat      = Function(linear)
linear_neutral   = Function(linear, 0,0,0)
linear_invert    = Function(linear, 0,0,-1)
logarithm_base10 = Function(logarithm)





####################################################
class Transform(object):

    ## ------------------------------------------
    def __init__(self, x=linear_flat, y=linear_flat, xy=linear_neutral, yx=linear_neutral):
        """
        Constructor

        |x'| = |x  xy| |x|
        |y'|   |yx  y| |y|
        """

        self.x  = x
        self.y  = y
        self.xy = xy
        self.yx = yx


    ## ------------------------------------------
    def apply(self, x, y):
        """
        Apply the transformation to a set of coordinates
        """

        x_prime = self.x.evaluate(x) + self.xy.evaluate(y)
        y_prime = self.y.evaluate(y) + self.yx.evaluate(x)

        return x_prime, y_prime
