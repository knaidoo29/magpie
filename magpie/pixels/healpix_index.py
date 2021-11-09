import numpy as np


def healpix2healringij(p, Nside):
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


def healringij2healpix(ringi, ringj, Nside):
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


def healringij2healxy(ringi, ringj, Nside):
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
    i = ringi
    j = ringj
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
            x = x0 + ((ringj - 1) % (jlen/4))
            y = ringi

        # Equatorial Segment
        elif ringi > Nside and ringi < 3*Nside:
            if Nside % 2 == 0:
                x0 = 0.5*((ringi+1) % 2)
            else:
                x0 = 0.5*(ringi % 2)
            x = x0 + ringj - 1.
            y = ringi

        # South Polar Cap
        elif ringi >= 3*Nside:
            jlen = 4*(4*Nside - ringi)
            k =  np.floor(4*(ringj-1)/jlen)
            x0 = int(Nside/2) + Nside*k
            if Nside % 2 == 0:
                x0 = x0 - 0.5*(4*Nside-ringi-1)
            else:
                x0 = x0 - 0.5*(4*Nside-ringi) + 1
            x = x0 + ((ringj - 1) % (jlen/4))
            y = ringi

    else:

        x = np.zeros(len(ringj))
        y = np.zeros(len(ringi))

        # North Polar Cap
        cond = np.where(ringi <= Nside)[0]

        jlen = 4*ringi[cond]
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(Nside/2) + Nside*k
        if Nside % 2 == 0:
            x0 = x0 - 0.5*(ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(ringi[cond]) + 1
        x[cond] = x0 + ((ringj[cond]-1) % (jlen/4))
        y[cond] = ringi[cond]

        # Equatorial Segment
        cond = np.where((ringi > Nside) & (ringi < 3*Nside))[0]

        if Nside % 2 == 0:
            x0 = 0.5*((ringi[cond]+1) % 2)
        else:
            x0 = 0.5*(ringi[cond] % 2)
        x[cond] = x0 + ringj[cond] - 1.
        y[cond] = ringi[cond]

        # South Polar Cap
        cond = np.where(ringi >= 3*Nside)[0]

        jlen = 4*(4*Nside - ringi[cond])
        k = np.floor(4*(ringj[cond]-1)/jlen)
        x0 = int(Nside/2) + Nside*k
        if Nside % 2 == 0:
            x0 = x0 - 0.5*(4*Nside-ringi[cond]-1)
        else:
            x0 = x0 - 0.5*(4*Nside-ringi[cond]) + 1
        x[cond] = x0 + ((ringj[cond]-1) % (jlen/4))
        y[cond] = ringi[cond]

    healx = x * np.pi/(2*Nside)
    healy = y * np.pi/(4*Nside)
    healy = np.pi/2. - healy
    return healx, healy


def healpix2healxy(p, Nside):
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
    ringi, ringj = healpix2healringij(p, Nside)
    healx, healy = healringij2healxy(ringi, ringj, Nside)
    return healx, healy
