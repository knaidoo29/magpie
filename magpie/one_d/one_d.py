import numpy as np

from .. import utils


def rebin_1d_single_bin(bin_edges, data, bin_min, bin_max):
    """Rebins to a single bin.

    Parameters
    ----------
    bin_edges : array
        Edges of the bins.
    data : array
        The value for each bin.
    bin_min : float
        Minimum edge for the new bin.
    bin_max : float
        Maximum edge for the new bin.
    """
    condition = np.where((bin_edges >= bin_min) & (bin_edges <= bin_max))[0]
    if len(condition) == 0:
        condition1 = np.where((bin_edges >= bin_min))[0]
        if len(condition1) != 0 and len(condition1) != len(bin_edges):
            return data[condition1[0]-1]
        else:
            # If we can't find any bins then we return a NaN
            return np.nan
    elif len(condition) == 1:
        # To ensure we are not looking at the edges
        if condition > 0 and condition < len(bin_edges)-1:
            w1 = (bin_edges[condition[0]] - bin_min)/(bin_edges[condition[0]] - bin_edges[condition[0]-1])
            w2 = (bin_max - bin_edges[condition[0]])/(bin_edges[condition[0]+1] - bin_edges[condition[0]])
            return (w1*data[condition[0]-1] + w2*data[condition[0]])/(w1+w2)
        # To deal with edges
        elif (condition) == 0:
            return data[0]
        elif (condition) == len(bin_edges)-1:
            return data[-1]
    else:
        # General case
        # Create weights equal to one
        w = np.ones(len(condition) + 1)
        if condition[0] != 0:
            # Alter first weight to account for the fact that the new bin intersects the first bin.
            w[0] = (bin_edges[condition[0]] - bin_min)/(bin_edges[condition[0]] - bin_edges[condition[0]-1])
        if condition[-1] != len(bin_edges)-1:
            # Alter last weight to account for the fact that the new bin intesrsects the last bin.
            w[-1] = (bin_edges[condition[-1]] - bin_min)/(bin_edges[condition[-1]] - bin_edges[condition[-1]-1])
        return np.sum(w*data[np.array(np.ndarray.tolist(condition-1) + [condition[-1]])])/np.sum(w)


def rebin_1d(bin_edges, data, new_bin_edges):
    """Rebins 1 dimensional data into an arbitrarily defined new bins.

    Parameters
    ----------
    bin_edges : array
        Edges of the bins.
    data : array
        The value for each bin.
    new_bin_edges : array
        Edges of the new bins.
    """
    # Sanity checks
    assert len(bin_edges)-1 == len(data), "Bin edges and data are the wrong dimensions."
    assert utils.is_pos_monotonic(bin_edges) == True, "Bin edges are not positively monotonic."
    assert utils.is_pos_monotonic(new_bin_edges) == True, "New bin edges are not positively monotonic."
    # Rebin using the rebin_1d_val function
    data_new = np.array([rebin_1d_single_bin(bin_edges, data, new_bin_edges[i], new_bin_edges[i+1]) for i in range(0, len(new_bin_edges)-1)])
    # Return rebinned data
    return data_new
