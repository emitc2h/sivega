#**************************************************#
# file   : core/elements/text.py                   #
# author : Michel Trottier-McDonald                #
# date   : February 2015                           #
# description:                                     #
# A text label                                     #
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

import math

from lxml import etree

from primitive import Primitive

####################################################
class Text(Primitive):

    ## ------------------------------------------
    def __init__(self, label, point, *args, **kwargs):
        """
        Constructor
        """

        super(Text, self).__init__(*args, **kwargs)

        self.points.append(point)

        self.flipped = True

        self.label      = label
        self.font       = 'sans-serif'
        self.size       = 18
        self.weight     = 'normal'
        self.style      = 'normal'
        self.decoration = 'none'
        self.anchor     = 'middle'
        self.offset_x   = 0
        self.offset_y   = 0
        self.rotation   = 0


    ## ------------------------------------------
    def render(self):
        """
        render
        """

        self.xml = etree.Element('text')
        self.xml.text = self.label

        self.xml.attrib['x']        = '{0}'.format(self.points[0].abs_x)
        self.xml.attrib['y']        = '{0}'.format(self.points[0].abs_y)
        self.xml.attrib['dx']       = '{0}'.format(self.offset_x*math.cos(-self.rotation*math.pi/180.0) - self.offset_y*math.sin(-self.rotation*math.pi/180.0))
        self.xml.attrib['dy']       = '{0}'.format(self.offset_x*math.sin(-self.rotation*math.pi/180.0) + self.offset_y*math.cos(-self.rotation*math.pi/180.0))
        if self.rotation:
            self.xml.attrib['transform'] = 'rotate({0},{1},{2})'.format(self.rotation, self.points[0].abs_x, self.points[0].abs_y)

        self.xml.attrib['font-family']     = self.font
        self.xml.attrib['font-size']       = '{0}'.format(self.size)
        self.xml.attrib['font-weight']     = self.weight
        self.xml.attrib['font-style']      = self.style
        self.xml.attrib['font-decoration'] = self.decoration
        self.xml.attrib['text-anchor']     = self.anchor

        return super(Text, self).render()

