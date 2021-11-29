import numpy as np

from .. import utils


def healpix_pix2ij(p, nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    p : int
        Healpix pixel index.
    nside : int
        Healpix nside.

    Returns
    -------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    """
    if utils.isscalar(p) == True:
        if p <= 2*nside*(nside+1):
            # top polar cap
            ph = (p+1)/2
            i = np.floor(np.sqrt(ph - np.sqrt(np.floor(ph))))+1
            j = p + 1 - 2*i*(i-1)
            ringi, ringj = int(i), int(j)
        elif p > 2*nside*(nside+1) and p < 2*nside*(5*nside-1):
            # equatorial sector
            pd = p - 2*nside*(nside-1)
            i = np.floor(pd/(4*nside)) + nside
            j = (pd % (4*nside)) + 1
            ringi, ringj = int(i), int(j)
        elif p >= 2*nside*(5*nside-1) and p <= 12*nside**2:
            # bottom polar cap
            ph = (12*nside**2 - p)/2
            i = np.floor(np.sqrt(ph-np.sqrt(np.floor(ph))))+1
            j = p + 2*i*(i + 1) + 1 - 12*nside**2
            ringi, ringj = int(4*nside-i), int(j)
    else:
        i, j = np.zeros(len(p)), np.zeros(len(p))
        # top polar cap
        cond = np.where(p <= 2*nside*(nside+1))[0]
        ph = (p[cond]+1)/2
        i[cond] = np.floor(np.sqrt(ph - np.sqrt(np.floor(ph)))) + 1
        j[cond] = p[cond] + 1 - 2*i[cond]*(i[cond]-1)
        # equatorial sector
        cond = np.where((p > 2*nside*(nside+1)) & (p < 2*nside*(5*nside-1)))[0]
        pd = p[cond] - 2*nside*(nside-1)
        i[cond] = np.floor(pd/(4*nside)) + nside
        j[cond] = (pd % (4*nside)) + 1
        # bottom polar cap
        cond = np.where((p >= 2*nside*(5*nside-1)) & (p <= 12*nside**2))[0]
        ph = (12*nside**2 - p[cond])/2
        i[cond] = np.floor(np.sqrt(ph-np.sqrt(np.floor(ph)))) + 1
        j[cond] = p[cond] + 2*i[cond]*(i[cond] + 1) + 1 - 12*nside**2
        i[cond] = 4*nside - i[cond]
        ringi = i.astype('int')
        ringj = j.astype('int')
    return ringi, ringj


def healpix_ij2pix(ringi, ringj, nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    nside : int
        Healpix nside.

    Returns
    -------
    p : int
        Healpix pixel index.
    """
    if utils.isscalar(ringi) == True:
        if ringi <= nside:
            # top polar cap
            p = 2*ringi*(ringi - 1) + ringj - 1
        elif ringi > nside and ringi < 3*nside:
            # equatorial sector
            p = 4*nside*(ringi - nside) + ringj - 1 + 2*nside*(nside - 1)
        elif ringi >= 3*nside:
            # bottom polar cap
            i = 4*nside - ringi
            p = 12*nside**2 + ringj - 2*i*(i + 1) - 1
        p = int(p)
    else:
        p = np.zeros(len(ringi))
        # top polar cap
        cond = np.where(ringi <= nside)[0]
        p[cond] = 2*ringi[cond]*(ringi[cond] - 1) + ringj[cond] - 1
        # equatorial sector
        cond = np.where((ringi > nside) & (ringi < 3*nside))[0]
        p[cond] = 4*nside*(ringi[cond] - nside) + ringj[cond] - 1 + 2*nside*(nside - 1)
        # bottom polar cap
        cond = np.where(ringi >= 3*nside)[0]
        i = 4*nside - ringi[cond]
        p[cond] = 12*nside**2 + ringj[cond] - 2*i*(i + 1) - 1
        p = p.astype('int')
    return p


def healpix_i2id(ringi, nside):
    """Converts ringi to idash.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    nside : int
        Healpix nside.

    Returns
    -------
    idash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix y without a factor.
    """
    idash = nside - ringi/2
    return idash


def healpix_j2jd(ringi, ringj, nside):
    """Converts ringj to jdash.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    nside : int
        Healpix nside.

    Returns
    -------
    jdash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix x without a factor.
    """
    if utils.isscalar(ringi) == True:
        # North Polar Cap
        if ringi <= nside:
            jlen = 4*ringi
            k = np.floor(4*(ringj-1)/jlen)
            x0 = int(nside/2) + nside*k
            if nside % 2 == 0:
                x0 = x0 - 0.5*(ringi-1)
            else:
                x0 = x0 - 0.5*(ringi) + 1
            jdash = x0 + ((ringj - 1) % (jlen/4))

        # Equatorial Segment
        elif ringi > nside and ringi < 3*nside:
            if nside % 2 == 0:
                x0 = 0.5*((ringi+1) % 2)
            else:
                x0 = 0.5*(ringi % 2)
            jdash = x0 + ringj - 1.

        # South Polar Cap
        elif ringi >= 3*nside:
            jlen = 4*(4*nside - ringi)
            k =  np.floor(4*(ringj-1)/jlen)
            x0 = int(nside/2) + nside*k
            if nside % 2 == 0:
                x0 = x0 - 0.5*(4*nside-ringi-1)
            else:
                x0 = x0 - 0.5*(4*nside-ringi) + 1
            jdash = x0 + ((ringj - 1) % (jlen/4))

    else:

        jdash = np.zeros(len(ringi))

        # North Polar Cap
        cond = np.where(ringi <= nside)[0]

        jlen = 4*ringi[cond]
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(nside/2) + nside*k
        if nside % 2 == 0:
            x0 = x0 - 0.5*(ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(ringi[cond]) + 1
        jdash[cond] = x0 + ((ringj[cond]-1) % (jlen/4))

        # Equatorial Segment
        cond = np.where((ringi > nside) & (ringi < 3*nside))[0]

        if nside % 2 == 0:
            x0 = 0.5*((ringi[cond]+1) % 2)
        else:
            x0 = 0.5*(ringi[cond] % 2)
        jdash[cond] = x0 + ringj[cond] - 1.

        # South Polar Cap
        cond = np.where(ringi >= 3*nside)[0]

        jlen = 4*(4*nside - ringi[cond])
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(nside/2) + nside*k
        if nside % 2 == 0:
            x0 = x0 - 0.5*(4*nside-ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(4*nside-ringi[cond]) + 1
        jdash[cond] = x0 + ((ringj[cond]-1) % (jlen/4))

    return jdash


def healpix_ijd2ijs(idash, jdash, nside):
    """Converts from healpix i and j dash to i and j star, which is useful for
    finding neighbours.

    Parameters
    ----------
    idash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix y without a factor.
    jdash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix x without a factor.

    Returns
    -------
    istar : array
        Healpix integer i star index.
    jstar : array
        Healpix integer i star index.
    """
    istar = jdash - idash + nside/2
    jstar = jdash + idash + nside/2
    istar -= 0.5
    istar = istar.astype('int')
    jstar -= 0.5
    jstar = jstar.astype('int')
    return istar, jstar


def healpix_ijs2ijd(istar, jstar, nside):
    """Converts from healpix i and j star to i and j dash, which is useful for
    finding neighbours.

    Parameters
    ----------
    istar : array
        Healpix integer i star index.
    jstar : array
        Healpix integer i star index.

    Returns
    -------
    idash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix y without a factor.
    jdash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix x without a factor.
    """
    istar = istar.astype('float') + 0.5
    jstar = jstar.astype('float') + 0.5
    jdash = (istar + jstar - nside)/2
    idash = (jstar - istar)/2
    return idash, jdash


def healpix_ijs_neighbours(istar, jstar, nside):
    """Gets the healpix i, jstar neighbours for a single healpix pixel.

    Parameters
    ----------
    istar : array
        Healpix integer i star index.
    jstar : array
        Healpix integer i star index.
    nside : int
        Healpix nside.

    Returns
    -------
    istar_neigh : array
        Neighbour healpix integer i star index.
    jstar_neigh : array
        Neighbour healpix integer j star index.
    """
    if jstar - istar + 1 == 2*nside:
        istar_neigh = [istar, istar + 1, istar + 1, istar + nside, istar + nside, istar - nside, istar + 1 - nside, istar+2*nside]
        jstar_neigh = [jstar - 1,  jstar - 1, jstar, jstar - 1 + nside, jstar + nside, jstar - nside, jstar - nside, jstar+2*nside]
    elif istar - jstar + 1 == 2*nside:
        istar_neigh = [istar, istar - 1, istar - 1, istar - nside, istar - nside, istar + nside, istar - 1 + nside, istar-2*nside]
        jstar_neigh = [jstar + 1,  jstar + 1, jstar, jstar + 1 - nside, jstar - nside, jstar + nside, jstar + nside, jstar-2*nside]
    elif jstar - istar + 1 == nside and istar % nside == 0:
        istar_neigh = [istar - 1, istar, istar + 1,  istar - 1, istar + 1, istar, istar + 1]
        jstar_neigh = [jstar - 1, jstar - 1, jstar - 1, jstar, jstar, jstar + 1, jstar + 1]
    elif istar - jstar + 1 == nside and jstar % nside == 0:
        istar_neigh = [istar - 1, istar, istar - 1, istar + 1, istar - 1, istar, istar + 1]
        jstar_neigh = [jstar - 1, jstar - 1, jstar, jstar, jstar + 1, jstar + 1, jstar + 1]
    elif istar % nside == 0 and jstar + 1 - nside*(np.floor(istar/nside) + 1) > 0:
        istar_neigh = [istar, istar + 1, istar + 1, istar, istar + 1,
                       istar - ((jstar+1)-nside*np.floor(jstar/nside)),
                       istar - ((jstar)-nside*np.floor(jstar/nside)),
                       istar - ((jstar-1)-nside*np.floor(jstar/nside))]
        jstar_neigh = [jstar - 1, jstar - 1, jstar, jstar + 1, jstar + 1,
                       nside*np.floor(jstar/nside)-1,
                       nside*np.floor(jstar/nside)-1,
                       nside*np.floor(jstar/nside)-1]
    elif jstar % nside == 0 and istar + 1 - nside*(np.floor(jstar/nside) + 1) > 0:
        jstar_neigh = [jstar, jstar + 1, jstar + 1, jstar, jstar + 1,
                       jstar - ((istar+2)-nside*np.floor(istar/nside)),
                       jstar - ((istar+1)-nside*np.floor(istar/nside)),
                       jstar - ((istar)-nside*np.floor(istar/nside))]
        istar_neigh = [istar - 1, istar - 1, istar, istar + 1, istar + 1,
                       nside*np.floor(istar/nside)-1,
                       nside*np.floor(istar/nside)-1,
                       nside*np.floor(istar/nside)-1]
    elif (jstar + 1 - nside) % nside == 0 and jstar + 1 - nside*(np.floor(istar/nside) + 1) > 0:
        jstar_neigh = [jstar, jstar - 1, jstar - 1, jstar, jstar - 1,
                       jstar + nside*(np.floor(istar/nside)+1)-istar,
                       jstar + nside*(np.floor(istar/nside)+1)-istar-1,
                       jstar + nside*(np.floor(istar/nside)+1)-istar+1]
        istar_neigh = [istar - 1, istar - 1, istar, istar + 1, istar + 1,
                       nside*(np.floor(istar/nside)+1),
                       nside*(np.floor(istar/nside)+1),
                       nside*(np.floor(istar/nside)+1)]
    elif (istar + 1 - nside) % nside == 0 and istar + 1 - nside*(np.floor(jstar/nside) + 1) > 0:
        istar_neigh = [istar, istar - 1, istar - 1, istar, istar - 1,
                       istar + nside*(np.floor(jstar/nside)+1)-jstar,
                       istar + nside*(np.floor(jstar/nside)+1)-jstar-1,
                       istar + nside*(np.floor(jstar/nside)+1)-jstar+1]
        jstar_neigh = [jstar - 1, jstar - 1, jstar, jstar + 1, jstar + 1,
                       nside*(np.floor(jstar/nside)+1),
                       nside*(np.floor(jstar/nside)+1),
                       nside*(np.floor(jstar/nside)+1)]
    else:
        istar_neigh = [istar - 1, istar, istar + 1, istar - 1, istar + 1, istar - 1, istar, istar + 1]
        jstar_neigh = [jstar - 1, jstar - 1, jstar - 1, jstar, jstar, jstar + 1, jstar + 1, jstar + 1]

    istar_neigh = np.array(istar_neigh)
    jstar_neigh = np.array(jstar_neigh)

    cond = np.where(istar_neigh + jstar_neigh > 9*nside-1)[0]
    istar_neigh[cond] = istar_neigh[cond] - 4*nside
    jstar_neigh[cond] = jstar_neigh[cond] - 4*nside

    cond = np.where(istar_neigh + jstar_neigh < nside-1)[0]
    istar_neigh[cond] = istar_neigh[cond] + 4*nside
    jstar_neigh[cond] = jstar_neigh[cond] + 4*nside

    istar_neigh = np.unique(istar_neigh)
    jstar_neigh = np.unique(jstar_neigh)
    return istar_neigh, jstar_neigh


def healpix_ij2xy(ringi, ringj, nside):
    """Conversion of healpix ring i and j to healpix x and y.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    nside : int
        Healpix nside.

    Returns
    -------
    healx : array
        Healpix x coordinates.
    healy : array
        Healpix y coordinates.
    """
    jdash = healpix_j2jd(ringi, ringj, nside)
    idash = healpix_i2id(ringi, nside)
    healx = jdash * np.pi/(2*nside)
    healy = idash * np.pi/(2*nside)
    return healx, healy


def healpix_pix2xy(p, nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    p : int
        Healpix pixel index.
    nside : int
        Healpix nside.

    Returns
    -------
    healx : array
        Healpix x coordinates.
    healy : array
        Healpix y coordinates.
    """
    ringi, ringj = healpix_pix2ij(p, nside)
    healx, healy = healpix_ij2xy(ringi, ringj, nside)
    return healx, healy
