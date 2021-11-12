import numpy as np


def healpix_pix2ij(p, Nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    p : int
        Healpix pixel index.
    Nside : int
        Healpix Nside.

    Returns
    -------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    """
    if np.isscalar(p) == True:
        if p <= 2*Nside*(Nside+1):
            # top polar cap
            ph = (p+1)/2
            i = np.floor(np.sqrt(ph - np.sqrt(np.floor(ph))))+1
            j = p + 1 - 2*i*(i-1)
            ringi, ringj = int(i), int(j)
        elif p > 2*Nside*(Nside+1) and p < 2*Nside*(5*Nside-1):
            # equatorial sector
            pd = p - 2*Nside*(Nside-1)
            i = np.floor(pd/(4*Nside)) + Nside
            j = (pd % (4*Nside)) + 1
            ringi, ringj = int(i), int(j)
        elif p >= 2*Nside*(5*Nside-1) and p <= 12*Nside**2:
            # bottom polar cap
            ph = (12*Nside**2 - p)/2
            i = np.floor(np.sqrt(ph-np.sqrt(np.floor(ph))))+1
            j = p + 2*i*(i + 1) + 1 - 12*Nside**2
            ringi, ringj = int(4*Nside-i), int(j)
    else:
        i, j = np.zeros(len(p)), np.zeros(len(p))
        # top polar cap
        cond = np.where(p <= 2*Nside*(Nside+1))[0]
        ph = (p[cond]+1)/2
        i[cond] = np.floor(np.sqrt(ph - np.sqrt(np.floor(ph)))) + 1
        j[cond] = p[cond] + 1 - 2*i[cond]*(i[cond]-1)
        # equatorial sector
        cond = np.where((p > 2*Nside*(Nside+1)) & (p < 2*Nside*(5*Nside-1)))[0]
        pd = p[cond] - 2*Nside*(Nside-1)
        i[cond] = np.floor(pd/(4*Nside)) + Nside
        j[cond] = (pd % (4*Nside)) + 1
        # bottom polar cap
        cond = np.where((p >= 2*Nside*(5*Nside-1)) & (p <= 12*Nside**2))[0]
        ph = (12*Nside**2 - p[cond])/2
        i[cond] = np.floor(np.sqrt(ph-np.sqrt(np.floor(ph)))) + 1
        j[cond] = p[cond] + 2*i[cond]*(i[cond] + 1) + 1 - 12*Nside**2
        i[cond] = 4*Nside - i[cond]
        ringi = i.astype('int')
        ringj = j.astype('int')
    return ringi, ringj


def healpix_ij2pix(ringi, ringj, Nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    Nside : int
        Healpix Nside.

    Returns
    -------
    p : int
        Healpix pixel index.
    """
    if np.isscalar(ringi) == True:
        if ringi <= Nside:
            # top polar cap
            p = 2*ringi*(ringi - 1) + ringj - 1
        elif ringi > Nside and ringi < 3*Nside:
            # equatorial sector
            p = 4*Nside*(ringi - Nside) + ringj - 1 + 2*Nside*(Nside - 1)
        elif ringi >= 3*Nside:
            # bottom polar cap
            i = 4*Nside - ringi
            p = 12*Nside**2 + ringj - 2*i*(i + 1) - 1
        p = int(p)
    else:
        p = np.zeros(len(ringi))
        # top polar cap
        cond = np.where(ringi <= Nside)[0]
        p[cond] = 2*ringi[cond]*(ringi[cond] - 1) + ringj[cond] - 1
        # equatorial sector
        cond = np.where((ringi > Nside) & (ringi < 3*Nside))[0]
        p[cond] = 4*Nside*(ringi[cond] - Nside) + ringj[cond] - 1 + 2*Nside*(Nside - 1)
        # bottom polar cap
        cond = np.where(ringi >= 3*Nside)[0]
        i = 4*Nside - ringi[cond]
        p[cond] = 12*Nside**2 + ringj[cond] - 2*i*(i + 1) - 1
        p = p.astype('int')
    return p


def healpix_i2id(ringi, Nside):
    """Converts ringi to idash.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    Nside : int
        Healpix Nside.

    Returns
    -------
    idash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix y without a factor.
    """
    idash = Nside - ringi/2
    return idash


def healpix_j2jd(ringi, ringj, Nside):
    """Converts ringj to jdash.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    Nside : int
        Healpix Nside.

    Returns
    -------
    jdash : int
        Alternate pixel index along each ring. This is for pixel transformations
        as this maps exactly to healpix x without a factor.
    """
    if np.isscalar(ringi) == True:
        # North Polar Cap
        if ringi <= Nside:
            jlen = 4*ringi
            k = np.floor(4*(ringj-1)/jlen)
            x0 = int(Nside/2) + Nside*k
            if Nside % 2 == 0:
                x0 = x0 - 0.5*(ringi-1)
            else:
                x0 = x0 - 0.5*(ringi) + 1
            jdash = x0 + ((ringj - 1) % (jlen/4))

        # Equatorial Segment
        elif ringi > Nside and ringi < 3*Nside:
            if Nside % 2 == 0:
                x0 = 0.5*((ringi+1) % 2)
            else:
                x0 = 0.5*(ringi % 2)
            jdash = x0 + ringj - 1.

        # South Polar Cap
        elif ringi >= 3*Nside:
            jlen = 4*(4*Nside - ringi)
            k =  np.floor(4*(ringj-1)/jlen)
            x0 = int(Nside/2) + Nside*k
            if Nside % 2 == 0:
                x0 = x0 - 0.5*(4*Nside-ringi-1)
            else:
                x0 = x0 - 0.5*(4*Nside-ringi) + 1
            jdash = x0 + ((ringj - 1) % (jlen/4))

    else:

        jdash = np.zeros(len(ringi))

        # North Polar Cap
        cond = np.where(ringi <= Nside)[0]

        jlen = 4*ringi[cond]
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(Nside/2) + Nside*k
        if Nside % 2 == 0:
            x0 = x0 - 0.5*(ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(ringi[cond]) + 1
        jdash[cond] = x0 + ((ringj[cond]-1) % (jlen/4))

        # Equatorial Segment
        cond = np.where((ringi > Nside) & (ringi < 3*Nside))[0]

        if Nside % 2 == 0:
            x0 = 0.5*((ringi[cond]+1) % 2)
        else:
            x0 = 0.5*(ringi[cond] % 2)
        jdash[cond] = x0 + ringj[cond] - 1.

        # South Polar Cap
        cond = np.where(ringi >= 3*Nside)[0]

        jlen = 4*(4*Nside - ringi[cond])
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(Nside/2) + Nside*k
        if Nside % 2 == 0:
            x0 = x0 - 0.5*(4*Nside-ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(4*Nside-ringi[cond]) + 1
        jdash[cond] = x0 + ((ringj[cond]-1) % (jlen/4))

    return jdash


def healpix_ijd2ijs(idash, jdash, Nside):
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
    istar = jdash - idash + Nside/2
    jstar = jdash + idash + Nside/2
    istar -= 0.5
    istar = istar.astype('int')
    jstar -= 0.5
    jstar = jstar.astype('int')
    return istar, jstar


def healpix_ijs2ijd(istar, jstar, Nside):
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
    jdash = (istar + jstar - Nside)/2
    idash = (jstar - istar)/2
    return idash, jdash


def healpix_ijs_neighbours(isd, jsd, Nside):
    """Gets the healpix i, jstar neighbours for a single healpix pixel.

    Parameters
    ----------
    istar : array
        Healpix integer i star index.
    jstar : array
        Healpix integer i star index.
    Nside : int
        Healpix Nside.

    Returns
    -------
    istar_neigh : array
        Neighbour healpix integer i star index.
    jstar_neigh : array
        Neighbour healpix integer j star index.
    """
    if jsd - isd + 1 == 2*Nside:
        isd_neigh = [isd, isd + 1, isd + 1, isd + Nside, isd + Nside, isd - Nside, isd + 1 - Nside, isd+2*Nside]
        jsd_neigh = [jsd - 1,  jsd - 1, jsd, jsd - 1 + Nside, jsd + Nside, jsd - Nside, jsd - Nside, jsd+2*Nside]
    elif isd - jsd + 1 == 2*Nside:
        isd_neigh = [isd, isd - 1, isd - 1, isd - Nside, isd - Nside, isd + Nside, isd - 1 + Nside, isd-2*Nside]
        jsd_neigh = [jsd + 1,  jsd + 1, jsd, jsd + 1 - Nside, jsd - Nside, jsd + Nside, jsd + Nside, jsd-2*Nside]
    elif jsd - isd + 1 == Nside and isd % Nside == 0:
        isd_neigh = [isd - 1, isd, isd + 1,  isd - 1, isd + 1, isd, isd + 1]
        jsd_neigh = [jsd - 1, jsd - 1, jsd - 1, jsd, jsd, jsd + 1, jsd + 1]
    elif isd - jsd + 1 == Nside and jsd % Nside == 0:
        isd_neigh = [isd - 1, isd, isd - 1, isd + 1, isd - 1, isd, isd + 1]
        jsd_neigh = [jsd - 1, jsd - 1, jsd, jsd, jsd + 1, jsd + 1, jsd + 1]
    elif isd % Nside == 0 and jsd + 1 - Nside*(np.floor(isd/Nside) + 1) > 0:
        isd_neigh = [isd, isd + 1, isd + 1, isd, isd + 1,
                     isd - ((jsd+1)-Nside*np.floor(jsd/Nside)),
                     isd - ((jsd)-Nside*np.floor(jsd/Nside)),
                     isd - ((jsd-1)-Nside*np.floor(jsd/Nside))]
        jsd_neigh = [jsd - 1, jsd - 1, jsd, jsd + 1, jsd + 1,
                     Nside*np.floor(jsd/Nside)-1,
                     Nside*np.floor(jsd/Nside)-1,
                     Nside*np.floor(jsd/Nside)-1]
    elif jsd % Nside == 0 and isd + 1 - Nside*(np.floor(jsd/Nside) + 1) > 0:
        jsd_neigh = [jsd, jsd + 1, jsd + 1, jsd, jsd + 1,
                     jsd - ((isd+2)-Nside*np.floor(isd/Nside)),
                     jsd - ((isd+1)-Nside*np.floor(isd/Nside)),
                     jsd - ((isd)-Nside*np.floor(isd/Nside))]
        isd_neigh = [isd - 1, isd - 1, isd, isd + 1, isd + 1,
                     Nside*np.floor(isd/Nside)-1,
                     Nside*np.floor(isd/Nside)-1,
                     Nside*np.floor(isd/Nside)-1]
    elif (jsd + 1 - Nside) % Nside == 0 and jsd + 1 - Nside*(np.floor(isd/Nside) + 1) > 0:
        jsd_neigh = [jsd, jsd - 1, jsd - 1, jsd, jsd - 1,
                     jsd + Nside*(np.floor(isd/Nside)+1)-isd,
                     jsd + Nside*(np.floor(isd/Nside)+1)-isd-1,
                     jsd + Nside*(np.floor(isd/Nside)+1)-isd+1]
        isd_neigh = [isd - 1, isd - 1, isd, isd + 1, isd + 1,
                     Nside*(np.floor(isd/Nside)+1),
                     Nside*(np.floor(isd/Nside)+1),
                     Nside*(np.floor(isd/Nside)+1)]
    elif (isd + 1 - Nside) % Nside == 0 and isd + 1 - Nside*(np.floor(jsd/Nside) + 1) > 0:
        isd_neigh = [isd, isd - 1, isd - 1, isd, isd - 1,
                     isd + Nside*(np.floor(jsd/Nside)+1)-jsd,
                     isd + Nside*(np.floor(jsd/Nside)+1)-jsd-1,
                     isd + Nside*(np.floor(jsd/Nside)+1)-jsd+1]
        jsd_neigh = [jsd - 1, jsd - 1, jsd, jsd + 1, jsd + 1,
                     Nside*(np.floor(jsd/Nside)+1),
                     Nside*(np.floor(jsd/Nside)+1),
                     Nside*(np.floor(jsd/Nside)+1)]
    else:
        isd_neigh = [isd - 1, isd, isd + 1, isd - 1, isd + 1, isd - 1, isd, isd + 1]
        jsd_neigh = [jsd - 1, jsd - 1, jsd - 1, jsd, jsd, jsd + 1, jsd + 1, jsd + 1]

    isd_neigh = np.array(isd_neigh)
    jsd_neigh = np.array(jsd_neigh)

    cond = np.where(isd_neigh + jsd_neigh > 9*Nside-1)[0]
    isd_neigh[cond] = isd_neigh[cond] - 4*Nside
    jsd_neigh[cond] = jsd_neigh[cond] - 4*Nside

    cond = np.where(isd_neigh + jsd_neigh < Nside-1)[0]
    isd_neigh[cond] = isd_neigh[cond] + 4*Nside
    jsd_neigh[cond] = jsd_neigh[cond] + 4*Nside

    isd_neigh = np.unique(isd_neigh)
    jsd_neigh = np.unique(jsd_neigh)
    return isd_neigh, jsd_neigh


def healpix_ij2xy(ringi, ringj, Nside):
    """Conversion of healpix ring i and j to healpix x and y.

    Parameters
    ----------
    ringi : int
        Pixel ring index.
    ringj : int
        Pixel index along each ring.
    Nside : int
        Healpix Nside.

    Returns
    -------
    healx : array
        Healpix x coordinates.
    healy : array
        Healpix y coordinates.
    """
    jdash = healpix_j2jd(ringi, ringj, Nside)
    idash = healpix_i2id(ringi, Nside)
    healx = jdash * np.pi/(2*Nside)
    healy = idash * np.pi/(2*Nside)
    return healx, healy


def healpix_pix2xy(p, Nside):
    """Returns the healpix ring i and pixel along the ring j.

    Parameters
    ----------
    p : int
        Healpix pixel index.
    Nside : int
        Healpix Nside.

    Returns
    -------
    healx : array
        Healpix x coordinates.
    healy : array
        Healpix y coordinates.
    """
    ringi, ringj = healpix_pix2ij(p, Nside)
    healx, healy = healpix_ij2xy(ringi, ringj, Nside)
    return healx, healy
