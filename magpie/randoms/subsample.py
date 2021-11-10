import numpy as np


def shuffle(sample):
    """Shuffles the ordering of a sample.

    Parameters
    ----------
    sample : array
        Input sample data.
    """
    u_r = np.random.random_sample(len(sample))
    sortind = np.argsort(u_r)
    return sample[sortind]


def random_draw(sample, size):
    """Draws a random sample from an input function, the algorithm ensures there
    can be no repeats.

    Parameters
    ----------
    sample : array
        Input sample data.
    size : int
        Size of the random draws.

    Returns
    -------
    randsamp : array
        Random subsample.
    """
    assert size < len(sample), "Size must be less than the input sample."
    u_r = np.random.random_sample(len(sample))
    sortind = np.argsort(u_r)
    randsamp = sample[sortind[:size]]
    return randsamp


def random_prob_draw(sample, prob, size=None):
    """Probabilistic draw from an input sample.

    Parameters
    ----------
    sample : array
        Input sample data.
    prob : array, optional
        The probability assigned to each sample.
    size : int, optional
        Size of the probabilistic draw.

    Returns
    -------
    randsamp : array
        Random subsample.
    """
    u_r = np.random.random_sample(len(sample))
    if size is None:
        cond = np.where(u_r <= prob)[0]
        randsamp = sample[cond]
        randsamp = shuffle(randsamp)
    else:
        assert size < len(sample), "Size must be less than the input sample."
        assert any(prob <= 0.) == False, "Probabilities assigned 0 must be removed."
        u_w = u_r/prob
        sortind = np.argsort(u_w)
        randsamp = sample[sortind[:size]]
        randsamp = shuffle(randsamp)
    return randsamp
