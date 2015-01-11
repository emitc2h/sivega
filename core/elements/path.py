#**************************************************#
# file   : core/elements/path.py                  #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A base class for an graphical object with a      #
# geometrical description                          #
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
from basic import Basic
from ..styles import color

####################################################
class Path(Basic):

    ## ------------------------------------------
    def __init__(self, fill_color=color.none, stroke_color=color.black, stroke_width=1, closed=False):
        """
        Constructor
        """

        super(Path, self).__init__()

        self.points = []
        self.closed = closed
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width



    ## -------------------------------------------
    def render_xml(self):
        """
        Renders the path to xml
        """

        self.xml = etree.Element('path')

        ## Compile path from points
        d_string = 'M {0},{1} L '
        for i, point in enumerate(self.points):
            if i == 0:
                d_string = d_string.format(*point.get_render())
            else:
                d_string += '{0},{1} '.format(*point.get_render())

        if self.closed:
            d_string += 'Z'

        self.xml.attrib['d'] = d_string

        self.compile_style(fill='{0}'.format(self.fill_color), 
                           stroke='{0}'.format(self.stroke_color),
                           stroke_width='{0}'.format(self.stroke_width))

        super(Path, self).render_xml()
