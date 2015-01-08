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

        self.type = 'plotbox'

        self.width  = 0.90*canvas.width
        self.height = 0.90*canvas.height
        self.x      = 0.05*canvas.width
        self.y      = 0.05*canvas.height

        self.plotting_tranform = ''

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

        self.background.attrib['x']      = '0'
        self.background.attrib['y']      = '0'
        self.background.attrib['width']  = '{0}'.format(self.width)
        self.background.attrib['height'] = '{0}'.format(self.height)

        self.compile_style(fill='{0}'.format(self.background_color), stroke='{0}'.format(self.box_color), stroke_width='3')

        super(PlotBox, self).update_xml()


    ## ------------------------------------------
    def calculate_plotting_transform(self):
        """
        Calculates the transformation
        """

        maximum_y = -float('inf')
        minimum_y = float('inf')

        maximum_x = -float('inf')
        minimum_x = float('inf')

        ## Find the minimum and maximum values for the plot
        for plot_item in self:
            if not plot_item.type == 'distribution': continue

            if minimum_x > maximum_x:
                minimum_x = plot_item.bins[0].xlo
                maximum_x = plot_item.bins[-1].xhi

            distribution_maximum = plot_item.max()
            distribution_minimum = plot_item.min()

            if distribution_maximum > maximum_y: maximum_y = distribution_maximum
            if distribution_minimum < minimum_y: minimum_y = distribution_minimum

        ## Make sure there is space beyond the maximum and below the minimum
        maximum_y *= 1.3
        if minimum_y < 0.0: minimum_y *= 1.3

        ## Calculate the transformations
        scale_x = self.width/abs(maximum_x - minimum_x)
        scale_y = self.height/abs(maximum_y - minimum_y)

        self.plotting_scale     = '{0},{1}'.format(scale_x, scale_y)
        self.plotting_translate = '{0},{1}'.format(-minimum_x*scale_x, -minimum_y*scale_y)

        ## Apply the transformations
        for plot_item in self:
            if not plot_item.type == 'distribution': continue
            plot_item.compile_transform(scale=self.plotting_scale, translate=self.plotting_translate)













