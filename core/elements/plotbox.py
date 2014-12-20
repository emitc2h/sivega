#**************************************************#
# file   : plotbox.py                              #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A plot area to be fitted within a canvas         #
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

from element import Element
from ..styles import color

####################################################
class PlotBox(Element):

    ## ------------------------------------------
    def __init__(self, canvas):
        """
        Constructor
        """

        self.width  = 0.90*canvas.width
        self.height = 0.90*canvas.height
        self.x      = 0.05*canvas.width
        self.y      = 0.05*canvas.height

        self.background_color = color.none
        self.box_color        = color.black

        super(PlotBox, self).__init__('svg')

        self.background = etree.Element('rect')
        self.xml.append(self.background)


    ## --------------------------------------------
    def compile_style(self, **kwargs):
        """
        Compiles the style of the element
        """

        style_strings = []

        for key,value in kwargs.iteritems():
            style_strings.append('{0}:{1}'.format(key.replace('_', '-'), value))

        self.background.attrib['style'] = '; '.join(style_strings)


    ## ------------------------------------------
    def update_xml(self):
        """
        Updates the xml data
        """

        self.xml.attrib['x']          = '{0}'.format(self.x)
        self.xml.attrib['y']          = '{0}'.format(self.y)
        self.xml.attrib['width']      = '{0}'.format(self.width)
        self.xml.attrib['height']     = '{0}'.format(self.height)
        self.xml.attrib['viewBox']    = '0 0 {0} {1}'.format(self.width, self.height)

        #self.compile_transform(scale='1,-1', translate='0,{0}'.format(self.height))

        self.background.attrib['x']      = '0'
        self.background.attrib['y']      = '0'
        self.background.attrib['width']  = '{0}'.format(self.width)
        self.background.attrib['height'] = '{0}'.format(self.height)

        self.compile_style(fill='{0}'.format(self.background_color), stroke='{0}'.format(self.box_color), stroke_width='3')

        super(PlotBox, self).update_xml()
