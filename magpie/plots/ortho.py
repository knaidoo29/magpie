import numpy as np
import matplotlib.pylab as plt

from . import shapes as plot_shapes
from .. import shapes


class PlotOrtho:


    def __init__(self, heal2ortho):
        """

        Parameters
        ----------
        heal2ortho : class
            For transformation.
        """
        self.heal2ortho = heal2ortho


    def imshow(self, dmap, cmap=plt.cm.viridis, ax=None, returncb=False):
        """

        Parameters
        ----------
        dmap : 2darray
            Data map given in orthographic projection.
        cmap : class, optional
            Colormap.
        ax : class, optional
            Axis to plot on.
        returncb : bool, optional
            Return imshow for colorbar plots.
        """
        if ax is None:
            cb = plt.imshow(dmap, origin='lower', extent=[self.heal2ortho.xedges[0], self.heal2ortho.xedges[-1],
                           self.heal2ortho.yedges[0], self.heal2ortho.yedges[-1]], cmap=cmap)
        else:
            cb = ax.imshow(dmap, origin='lower', extent=[self.heal2ortho.xedges[0], self.heal2ortho.xedges[-1],
                           self.heal2ortho.yedges[0], self.heal2ortho.yedges[-1]], cmap=cmap)
        if returncb == True:
            return cb


    def plot_grid(self, dtheta=15., dphi=None, zeropoint=[0., np.pi/2.],
                  shift=[1.5, 2.], ax=None, color='k', linestyle='--', **kwargs):
        """Plots labels on the orthographic grid.

        Parameters
        ----------
        dtheta : float, optional
            Separation in the grid.
        dphi : float, optional
            To specify different grid spacing in phi.
        zeropoint : list, optional
            Axis zero-point.
        shift : list, optional
            Shift in degrees to place on the coordinates.
        ax : class, optional
            Axis to plot on.
        color : str, optional
            Color of the grid lines.
        linestyle : str, optional
            Linestyle of the grid lines.
        """
        if dphi is None:
            dphi = dtheta
        nlines = int(360/dphi)
        phi_grid = np.linspace(0., 2.*np.pi, nlines + 1)[:-1]
        nlines = int(180/dtheta)
        theta_grid = np.linspace(0., np.pi, nlines + 1)[:-1]

        for ii in range(0, len(phi_grid)):
            points = 100
            phi = np.ones(points)*phi_grid[ii]
            theta = np.linspace(0., np.pi, points)
            x, y = self.heal2ortho.transform(phi, theta)
            if ax is None:
                plt.plot(x, y, color=color, linestyle=linestyle, **kwargs)
            else:
                ax.plot(x, y, color=color, linestyle=linestyle, **kwargs)

        for ii in range(0, len(theta_grid)):
            points = 100
            theta = np.ones(points)*theta_grid[ii]
            phi = np.linspace(0., 2.*np.pi, points)
            x, y = self.heal2ortho.transform(phi, theta)
            if ax is None:
                plt.plot(x, y, color=color, linestyle=linestyle, **kwargs)
            else:
                ax.plot(x, y, color=color, linestyle=linestyle, **kwargs)


    def plot_labels(self, dtheta=15., dphi=None, decimals=0, lonlat=False, zeropoint=[0., np.pi/2.],
                    shift=[1.5, 2.], ax=None, **kwargs):
        """Plots labels on the orthographic grid.

        Parameters
        ----------
        heal2ortho : class
            For transformation.
        dtheta : float, optional
            Separation in the grid.
        dphi : float, optional
            To specify different grid spacing in phi.
        decimals : int, optional
            Number of decimals to place in labels.
        lonlat : bool, optional
            Determines whether to plot coordinates in longitude and latitude.
        zeropoint : list, optional
            Axis zero-point.
        shift : list, optional
            Shift in degrees to place on the coordinates.
        ax : class, optional
            Axis to plot on.
        """
        if dphi is None:
            dphi = dtheta
        nlines = int(360/dphi)
        phi_grid = np.linspace(0., 2.*np.pi, nlines + 1)[:-1]
        nlines = int(180/dtheta)
        theta_grid = np.linspace(0., np.pi, nlines + 1)[1:-1]
        for ii in range(0, len(phi_grid)):
            phi_val = phi_grid[ii]
            phi_str = r'$ %s ^{\circ}$' % str(np.round(np.rad2deg(phi_val), decimals=decimals))[:-2]
            theta_val = zeropoint[1]
            theta_val += np.deg2rad(shift[0])
            x, y = self.heal2ortho.transform(phi_val, theta_val)
            if x >= self.heal2ortho.xedges[0] and x <= self.heal2ortho.xedges[-1] and y >= self.heal2ortho.yedges[0] and y <= self.heal2ortho.yedges[-1]:
                if ax is None:
                    plt.text(x, y, phi_str, **kwargs)
                else:
                    ax.text(x, y, phi_str, **kwargs)

        for ii in range(0, len(theta_grid)):
            theta_val = theta_grid[ii]
            if lonlat == True:
                theta_val = np.pi/2. - theta_val
            theta_str = r'$ %s ^{\circ}$' % str(np.round(np.rad2deg(theta_val), decimals=decimals))[:-2]
            theta_val = theta_grid[ii]
            phi_val = zeropoint[0]
            phi_val -= np.deg2rad(2.)
            if phi_val < 0.:
                phi_val += 2.*np.pi
            elif phi_val >= 2.*np.pi:
                phi_val -= 2.*np.pi
            x, y = self.heal2ortho.transform(phi_val, theta_val)
            if x >= self.heal2ortho.xedges[0] and x <= self.heal2ortho.xedges[-1] and y >= self.heal2ortho.yedges[0] and y <= self.heal2ortho.yedges[-1]:
                if ax is None:
                    plt.text(x, y, theta_str, **kwargs)
                else:
                    ax.text(x, y, theta_str, **kwargs)

    def plot_polar_box(self, phi_min, phi_max, theta_min, theta_max, lonlat=False,
                 ax=None, divisions=100, **kwargs):
        """Plots a polar grid box.

        Parameters
        ----------
        phi_min : float
            Minimum phi-value of the box.
        phi_max : float
            Maximum phi-value of the box.
        theta_min : float
            Minimum theta-value of the box.
        theta_max : float
            Maximum theta-value of the box.
        lonlat : bool, optional
            Determines whether coordinates are in longitude and latitude convention.
        ax : class, optional
            Axis to plot on.
        divisions : int, optional
            Divisions in each line segment.
        """
        if lonlat == True:
            _t1, _t2 = theta_min, theta_max
            theta_min = np.pi/2. - _t2
            theta_max = np.pi/2. - _t1
        phi_box, theta_box = shapes.get_box(phi_min, phi_max, theta_min, theta_max, divisions=divisions)
        x, y = self.heal2ortho.transform(phi_box, theta_box)
        if ax is None:
            plt.plot(x, y, **kwargs)
        else:
            ax.plot(x, y, **kwargs)


    def finalize(self, insphere=True, ax=None, outeredge=True, edgecolor='k',
                 edgelinewidth=10, edgelength=1000, edgecenter=[0., 0.], **kwargs):
        """Finalize the orthographic plot.

        Parameters
        ----------
        heal2ortho : class
            For transformation.
        insphere : bool, optional
            If true then this means we are plotting as though we are looking from
            inside the sphere, as you would if your map is of the sky.
        ax : class, optional
            Axis to plot on.
        outeredge : bool, optional
            This will plot a circle defining the edge of the sphere.
        edgecolor : str, optional
            Color of the outeredge.
        edgelinewidth : float, optional
            Linewidth of the circle edge.
        edgelength : int, optional
            Length of the datapoints used to create the edge circle.
        edgecenter : list, optional
            Center of the outeredge circle.
        """
        if outeredge is True:
             plot_shapes.plot_circle(radius=self.heal2ortho.radius, center=edgecenter,
                                     length=edgelength, color=edgecolor,
                                     linewidth=edgelinewidth, ax=ax, **kwargs)
        if ax is None:
            if insphere == True:
                plt.xlim(self.heal2ortho.xedges[-1], self.heal2ortho.xedges[0])
            else:
                plt.xlim(self.heal2ortho.xedges[0], self.heal2ortho.xedges[-1])
            plt.ylim(self.heal2ortho.yedges[0], self.heal2ortho.yedges[-1])
        else:
            if insphere == True:
                ax.set_xlim(self.heal2ortho.xedges[-1], self.heal2ortho.xedges[0])
            else:
                ax.set_xlim(self.heal2ortho.xedges[0], self.heal2ortho.xedges[-1])
            ax.set_ylim(self.heal2ortho.yedges[0], self.heal2ortho.yedges[-1])
        if ax is None:
            plt.axis('off')
        else:
            ax.axis('off')
