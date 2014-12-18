#**************************************************#
# file   : histogram.py                            #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# An axis that goes on the edge of a box           #
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

from elements import canvas, plotbox
from styles import color
from utilities import th1futils


####################################################
class Component:

    ## ------------------------------------------
    def __init__(self, th1f, fill_color=color.white, stroke_color=color.black, fill='', stroke=''):
        """
        Constructor
        """

        self.th1f         = th1f
        self.fill_color   = fill_color
        self.fill         = fill
        self.stroke_color = stroke_color
        self.stroke       = stroke




####################################################
class Stack(list):

    ## ------------------------------------------
    def __init__(self, component):
        """
        Constructor
        """

        self.append(component)
        self.sum = th1futils.copy_empty(component, label='sum')



    ## ------------------------------------------
    def add(self, component):
        """
        Add a component to the stack
        """

        self.append(component)




####################################################
class Histogram(list):

    ## ------------------------------------------
    def __init__(self, xtitle='', ytitle=''):
        """
        Constructor
        """

        self.binning = None
        self.xlo     = None
        self.xhi     = None

        self.xtitle = xtitle
        self.ytitle = ytitle


