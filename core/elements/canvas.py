#**************************************************#
# file   : core/elements/canvas.py                 #
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
import cairosvg

from box import Box

####################################################
class Canvas(Box):

    ## ------------------------------------------
    def __init__(self, width=800, height=600):
        """
        Constructor
        """

        self.width  = width
        self.height = height

        super(Canvas, self).__init__(0, 0, width, height)


    ## ------------------------------------------
    def render(self):
        """
        Renders the canvas to xml
        """

        ## Creates the group that will contain everything in the box
        self.svg = etree.Element('svg')
        self.svg.attrib['width']  = str(self.width)
        self.svg.attrib['height'] = str(self.height)
        self.svg.attrib['viewbox'] = '0 0 {0} {1}'.format(self.width, self.height)
        self.svg.attrib['xmlns'] = 'http://www.w3.org/2000/svg'

        definitions = super(Canvas, self).render()

        ## Flip primitives
        self.flip(self.height)

        ## Collect definitions
        if definitions:
            self.defs = etree.Element('defs')
            for definition in definitions:
                self.defs.append(definition.xml)
            self.svg.append(self.defs)

        ## Transform master group to cartesian coordinates
        self.xml.attrib['transform'] = 'translate(0,{0}) scale(1,-1)'.format(self.height)
        self.svg.append(self.xml)


    ## ------------------------------------------
    def draw(self, name, extension='svg'):
        """
        Draw the canvas
        """

        self.render()

        if extension == 'svg':
            output_file = open('{0}.{1}'.format(name, extension), 'w')
            output_file.write(etree.tostring(self.svg, pretty_print=True))
            output_file.close()

        elif extension == 'png':
            pass
        elif extension == 'pdf':
            pass
        elif extension == 'eps':
            pass
        else:
            print 'File not produced. Extension {0} unknown.'.format(extension)


