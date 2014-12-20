#**************************************************#
# file   : exceptions.py                           #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# A library of exceptions for sivega               #
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

####################################################
class Error(Exception):
    """
    A base class for exceptions specific to Sivega
    """
    pass



####################################################
class InconsistentBinningError(Error):
    """
    An error thrown by the Histogram class when th1fs
    with inconsistent binnings are provided
    """

    ## ------------------------------------------
    def __init__(self, expr, msg):
        """
        Constructor
        """
        self.expr = expr
        self.msg = msg



####################################################
class OutputTypeError(Error):
    """
    An error thrown by Canvas when the output type
    provided is wrong
    """

    ## ------------------------------------------
    def __init__(self, expr, msg):
        """
        Constructor
        """
        self.expr = expr
        self.msg = msg

        