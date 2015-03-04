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
        self.xml = etree.Element('svg')
        self.xml.attrib['width']  = str(self.width)
        self.xml.attrib['height'] = str(self.height)
        self.xml.attrib['viewbox'] = '0 0 {0} {1}'.format(self.width, self.height)
        self.xml.attrib['xmlns'] = 'http://www.w3.org/2000/svg'

        ## Collect definitions

        ## Creates the background rectangle
        background = etree.Element('rect')

        ## Set background attributes
        background.attrib['x']      = '0'
        background.attrib['y']      = '0'
        background.attrib['width']  = str(self.width)
        background.attrib['height'] = str(self.height)

        background.attrib['fill'] = self.fill
        if not self.stroke is None:
            background.attrib['stroke'] = self.stroke
            if not self.stroke_width is None:
                background.attrib['stroke-width'] = str(self.stroke_width)

        ## Append background first in the group (such that it IS the background to everything else)
        self.xml.append(background)

        ## Now render the primitives included in the current box
        self.render_point_coordinates()

        for primitive in self.primitives:
            primitive.render()
            self.xml.append(primitive.xml)

        ## Now render the subboxes:
        for box in self:
            box.render()
            self.xml.append(box.xml)


    ## ------------------------------------------
    def draw(self, name, extension='svg'):
        """
        Draw the canvas
        """

        self.render()

        if extension == 'svg':
            output_file = open('{0}.{1}'.format(name, extension), 'w')
            output_file.write(etree.tostring(self.xml))
            output_file.close()
        else:
            print 'File not produced. Extension {0} unknown.'.format(extension)


