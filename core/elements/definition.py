#**************************************************#
# file   : core/elements/definition.py             #
# author : Michel Trottier-McDonald                #
# date   : February 2015                           #
# description:                                     #
# A base class for svg definitions                 #
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
class Definition(Element):

    ## ------------------------------------------
    def __init__(self):
        """
        Constructor
        """

        self.xml_id = None

        super(Definition, self).__init__()


    ## ------------------------------------------
    def compare(self, other):
        """
        Compare two definitions to see if equivalent
        """

        if self.xml_id == other.xml_id:
            return True

        return False


