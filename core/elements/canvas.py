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

from lxml import etree
import cairosvg

from element import Element
from ..styles import color
import exceptions

####################################################
class Canvas(Element):

    ## ------------------------------------------
    def __init__(self, width=800, height=600, background_color=color.white):
        """
        Constructor
        """

        self.type = 'canvas'

        self.width            = width
        self.height           = height
        self.background_color = background_color

        self.svg = etree.Element('svg')
        super(Canvas, self).__init__('g')
        self.background = etree.Element('rect')

        self.xml.append(self.background)
        self.svg.append(self.xml)



    ## --------------------------------------------
    def compile_style(self, **kwargs):
        """
        Compiles the style of the element
        """

        style_strings = []

        for key,value in kwargs.iteritems():
            style_strings.append('{0}:{1}'.format(key.replace('_', '-'), value))

        self.background.attrib['style'] = ' ;'.join(style_strings)



    ## ------------------------------------------
    def update_xml(self):
        """
        Updates the xml data
        """

        self.svg.attrib['width']   = '{0}'.format(self.width)
        self.svg.attrib['height']  = '{0}'.format(self.height)
        self.svg.attrib['viewBox'] = '0 0 {0} {1}'.format(self.width, self.height)
        self.svg.attrib['xmlns']   =  'http://www.w3.org/2000/svg'

        self.compile_transform(scale='1,-1', translate='0,{0}'.format(self.height))

        self.background.attrib['x']      = '0'
        self.background.attrib['y']      = '0'
        self.background.attrib['width']  = '{0}'.format(self.width)
        self.background.attrib['height'] = '{0}'.format(self.height)

        self.compile_style(fill='{0}'.format(self.background_color))

        super(Canvas, self).update_xml()


    ## ------------------------------------------
    def string(self):
        """
        Dump a string containing the xml code for this element and all it contains
        """

        self.update_xml()
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


