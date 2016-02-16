#**************************************************#
# file   : core/elements/element.py                #
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
class Element(object):

    ## ------------------------------------------
    def __init__(self, parent_box=None):
        """
        Constructor
        """

        self.xml = None
        self.parent_box = parent_box


    ## ------------------------------------------
    def render(self):
        """
        Generates the svg code for this element
        To be implemented by child classes
        """
        pass


    ## ------------------------------------------
    def render_point_coordinates(self):
        """
        Returns the absolute coordinates corresponding to the given point
        To be implemented by the child classes
        """
        pass