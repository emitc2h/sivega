#**************************************************#
# file   : th1futils.py                            #
# author : Michel Trottier-McDonald                #
# date   : December 2014                           #
# description:                                     #
# Utilities to manipulate ROOT TH1Fs               #
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




## ================================================
def consistent_binning(th1f_i, th1f_j, variable_binning=False):
    """
    Checks that two histograms have consistent binnings
    """

    if not variable_binning:
        nbins_i = th1f_i.GetNbinsX()
        axis_i  = th1f_i.GetXaxis()
        xlo_i   = axis_i.GetBinLowEdge(1)
        xhi_i   = axis_i.GetBinUpEdge(nbins)

        nbins_j = th1f_j.GetNbinsX()
        axis_j  = th1f_j.GetXaxis()
        xlo_j   = axis_j.GetBinLowEdge(1)
        xhi_j   = axis_j.GetBinUpEdge(nbins)

        if (nbins_i == nbins_j) and \
            (xlo_i == x_lo_j) and \
            (xhi_i == xhi_j):
            return True
        else:
            return False
