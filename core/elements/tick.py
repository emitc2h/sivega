#**************************************************#
# file   : core/elements/tick.py                   #
# author : Michel Trottier-McDonald                #
# date   : February 2015                           #
# description:                                     #
# A definition for an axis tick                    #
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
from definition import Definition
from ..styles import color

####################################################
class Tick(Definition):

    ## ------------------------------------------
    def __init__(self, stroke=color.black, stroke_width=2, length=5):
        """
        Constructor
        """

        self.stroke       = stroke
        self.stroke_width = stroke_width
        self.length       = length

        super(Tick, self).__init__()

        ## Generate ID
        self.xml_id = 'tick.{0}.{1}.{2}'.format(self.stroke.lstrip('#'), self.stroke_width, self.length)


    ## ------------------------------------------
    def render(self):
        """
        Renders the tick definition
        """

        ## Generate line
        line = etree.Element('line')
        line.attrib['x1'] = '0'
        line.attrib['y1'] = '0'
        line.attrib['x2'] = '0'
        line.attrib['y2'] = '{0}'.format(self.length)
        line.attrib['stroke'] = self.stroke
        line.attrib['stroke-width'] = '{0}'.format(self.stroke_width)

        ## Generate the marker
        self.xml = etree.Element('marker')
        self.xml.attrib['id'] = self.xml_id
        self.xml.attrib['markerWidth'] = '5'
        self.xml.attrib['markerHeight'] = '{0}'.format(self.length)
        self.xml.attrib['orient'] = 'auto'

        self.xml.append(line)





