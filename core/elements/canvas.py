#**************************************************#
# file   : core/elements/canvas.py                 #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A canvas to house graphical elements, provides   #
# the <svg> element in the xml tree                #
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
import cairosvg

from element import Element

from ..coordinates.transform import Transform, linear_flat, linear_invert
from ..coordinates.origin import Origin

from ..styles import color

import exceptions

####################################################
class Canvas(Element):

    ## ------------------------------------------
    def __init__(self, width=800, height=600, background_color=color.white):
        """
        Constructor
        """

        super(Canvas, self).__init__(type='canvas')

        self.width            = width
        self.height           = height
        self.background_color = background_color

        absolute_origin    = Origin(x=0, y=self.height)
        absolute_transform = Transform(x=linear_flat, y=linear_invert)

        self.origin    = Origin(x=0, y=self.height)
        self.transform = Transform(x=linear_flat, y=linear_invert)


    ## ------------------------------------------
    def render_xml(self):
        """
        Updates the xml data
        """

        self.xml = etree.Element('g')
        self.background = Element(etree.Element('rect'), type='background')
        self.insert(0,self.background)

        self.background.xml.attrib['x']      = '0'
        self.background.xml.attrib['y']      = '0'
        self.background.xml.attrib['width']  = '{0}'.format(self.width)
        self.background.xml.attrib['height'] = '{0}'.format(self.height)

        self.compile_style(fill='{0}'.format(self.background_color))

        self.set_absolute_coord()

        super(Canvas, self).render_xml()

        self.svg = etree.Element('svg')

        self.svg.attrib['width']   = '{0}'.format(self.width)
        self.svg.attrib['height']  = '{0}'.format(self.height)
        self.svg.attrib['viewBox'] = '0 0 {0} {1}'.format(self.width, self.height)
        self.svg.attrib['xmlns']   =  'http://www.w3.org/2000/svg'

        self.svg.append(self.xml)


    ## ------------------------------------------
    def string(self):
        """
        Dump a string containing the xml code for this element and all it contains
        """

        self.render_xml()
        return etree.tostring(self.svg, pretty_print=True)


    ## ------------------------------------------
    def draw(self, name, output_type='png'):
        """
        Renders the svg and prints to file
        """

        f_out = open('{0}.{1}'.format(name, output_type), 'w')

        if (output_type == 'png') or \
           (output_type == 'pdf') or \
           (output_type == 'ps'):

           getattr(cairosvg, 'svg2{0}'.format(output_type))(bytestring=self.string(), write_to=f_out)
           f_out.close()
           return

        elif (output_type == 'svg'):
            f_out.write(self.string())
            f_out.close()
            return

        else:
            raise exceptions.OutputTypeError('The provided output type (\'{0}\') is unavailable. \'pdf\', \'png\', \'ps\', and \'svg\' are the available types.')
            return