
Sample PDF/CDF Functions
------------------------

.. function:: pdf2cdf(xmid, pdf[, return_normpdf=True])

    Calculates the CDF from a given PDF.

    :param xmid: Linearly spaced x-values given at the middle of a bin of length dx.
    :type xmid: array
    :param pdf: Probabilty distribution function.
    :type pdf: array
    :param return_normpdf: Normalise PDF is also outputed.
    :type return_normpdf: bool

    :returns: Returns a tuple of the following:

        * **x** *(array)* -- X-coordinates.
        * **cdf** *(array)* -- Cumulative distribution function with extreme points set 0 and 1.
        * **normpdf** *(array)* -- Normalised PDF.


.. function:: randoms_cdf(x, cdf, size[, kind='cubic'])

    Generates randoms from a given cumulative distribution function.

    :param x: X-coordinates.
    :type x: array
    :param cdf: Cumulative distribution function, extreme points must be 0 and 1 i.e. cdf[0] = 0 and cdf[-1] = 1.
    :type cdf: array
    :param size: Size of the random sample.
    :type size: int
    :param kind: Scipy CDF interpolation kind.
    :type kind: str

    :returns: **rands** *(array)* -- Randoms drawn from sample CDF.


.. function:: randoms_pdf(x, pdf, size[, kind='cubic'])

    Generates randoms from a given probability distribution function by first calculating a CDF.

    :param xmid: Linearly spaced x-values given at the middle of a bin of length dx.
    :type xmid: array
    :param pdf: Probabilty distribution function.
    :type pdf: array
    :param size: Size of the random sample.
    :type size: int
    :param kind: Scipy CDF interpolation kind.
    :type kind: str

    :returns: **rands** *(array)* -- Randoms drawn from sample PDF.
