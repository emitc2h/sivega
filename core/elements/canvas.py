#**************************************************#
# file   : canvas.py                               #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A canvas to house one or more boxes              #
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

from element import Element

####################################################
class Canvas(Element):

    ## ------------------------------------------
    def __init__(self):
        """
        Constructor
        """

        super(Canvas, self).__init__('svg', width='800', height='600', viewBox='0 0 800 600', style='fill:white')

