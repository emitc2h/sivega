#**************************************************#
# file   : core/elements/element.py                #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A base class for an xml element                  #
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
from ..coordinates import absolute_origin, absolute_transform

####################################################
class Element(list):

    ## ------------------------------------------
    def __init__(self, xml=None, type=None):
        """
        Constructor
        """

        self.xml  = xml
        self.type = type

        self.origin    = absolute_origin
        self.transform = absolute_transform


    ## ------------------------------------------
    def string(self):
        """
        Dump a string containing the xml code for this element and all it contains
        """

        self.render_xml()
        return etree.tostring(self.xml, pretty_print=True)


    ## -------------------------------------------
    def add(self, element):
        """
        Add an element to the current element
        """

        if isinstance(element, Element):
            self.append(element)
        else:
            raise TypeError('object {0} is not of type Element'.format(element.__class__))


    ## -------------------------------------------
    def render_xml(self):
        """
        Updates the xml representation
        """

        del self.xml[:]
        for element in self:
            element.render_xml()
            self.xml.append(element.xml)


    ## --------------------------------------------
    def compile_style(self, **kwargs):
        """
        Compiles the style of the element
        """

        style_strings = []

        for key,value in kwargs.iteritems():
            style_strings.append('{0}:{1}'.format(key.replace('_', '-'), value))

        self.xml.attrib['style'] = '; '.join(style_strings)
