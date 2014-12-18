#**************************************************#
# file   : element.py                              #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A base class for a graphical element             #
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

from lxml import etree

####################################################
class Element(object):

    ## ------------------------------------------
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """

        self.xml = etree.Element(*args, **kwargs)




    ## ------------------------------------------
    def string(self):
        """
        Dump a string containing the xml code for this element and all it contains
        """

        return etree.tostring(self.xml, pretty_print=True)
