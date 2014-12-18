#**************************************************#
# file   : th1futils.py                            #
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

import ROOT, time

## ================================================
def unique_label():
    """
    Produces a unique string label to distinguish histograms in ROOT memory allocation
    """

    return str(hex(int(time.time()*1e6)))




## ================================================
def copy_empty(th1f, label='empty', variable_binning=False):
    """
    Creates an empty copy of a histogram with the same binning & range
    """

    if not variable_binning:
        name  = th1f.GetName()
        nbins = th1f.GetNbinsX()
        axis  = th1f.GetXaxis()
        xlo   = axis.GetBinLowEdge(1)
        xhi   = axis.GetBinUpEdge(nbins)
    
        return ROOT.TH1F('{0}_{1}_{2}'.format(name, label, unique_label()), '', nbins, xlo, xhi)

