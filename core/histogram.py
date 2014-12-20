#**************************************************#
# file   : histogram.py                            #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# An axis that goes on the edge of a box           #
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

from elements import canvas, plotbox
from styles import color
from utilities import th1futils
import exceptions


####################################################
class Component:

    ## ------------------------------------------
    def __init__(self, th1f, label, fill_color, stroke_color, fill, stroke):
        """
        Constructor
        """

        self.th1f         = th1f
        self.label        = label
        self.fill_color   = fill_color
        self.fill         = fill
        self.stroke_color = stroke_color
        self.stroke       = stroke




####################################################
class Stack(list):

    ## ------------------------------------------
    def __init__(self, component, label=None):
        """
        Constructor
        """

        self.label = label
        self.append(component)
        self.sum = th1futils.copy_empty(component.th1f, label='sum')


    ## ------------------------------------------
    def add(self, component):
        """
        Add a component to the stack
        """

        self.append(component)




####################################################
class Histogram(list):

    ## ------------------------------------------
    def __init__(self, name, xtitle='', ytitle='Yields', *args, **kwargs):
        """
        Constructor
        """

        self.name    = name
        self.binning = None
        self.xlo     = None
        self.xhi     = None

        self.xtitle = xtitle
        self.ytitle = ytitle

        self.canvas = canvas.Canvas(*args, **kwargs)
        self.plotbox = plotbox.PlotBox(self.canvas)
        self.canvas.add(self.plotbox)


    ## -------------------------------------------
    def add(self, th1f, label, fill_color=color.white, stroke_color=color.black, fill='', stroke='', stack=None):
        """
        Add a th1f to the histogram
        """

        if len(self):
            for my_stack in self:
                for my_component in my_stack:
                    if not th1futils.consistent_binning(my_component.th1f, th1f):
                        raise exceptions.InconsistentBinningError('new ROOT.TH1F labelled {0} has different binning than other ROOT.TH1Fs already present in Histogram {1}'.format(label, self.name))

        new_component = Component(
                                th1f,
                                label,
                                fill_color=fill_color,
                                stroke_color=stroke_color,
                                fill=fill,
                                stroke=stroke)

        if not stack is None:
            for my_stack in self:
                if my_stack.label == stack:
                    my_stack.add(new_component)
                    return

        new_stack = Stack(new_component)
        self.append(new_stack)


    ## -------------------------------------------
    def draw(self, *args, **kwargs):
        """
        Draws the current histogram to file
        """

        self.canvas.draw(*args, **kwargs)









