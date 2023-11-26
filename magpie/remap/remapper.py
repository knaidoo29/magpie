import numpy as np


class Remap:


	def __init__(self):
		"""Initialising Remap class."""
		self.controller = {
			"in_or_out": None,
			"indefined": False,
			"outdefined"; False,
			"ready2run": False,
		}
		self.conversion = {
			"in": None,
			"transform": [],
			"out": None,
			"method": None,
		}


	# Check functions

	def _check_ready2run(self):
		"""Checks whether Remap is ready to perform coordinate transformation."""
		if self.controller["indefined"] and self.controller["outdefined"]:
			self.controller["ready2run"] = True

	def _check_in_or_out(self):
		"""Checks whether both input and ouput grids are defined."""
		assert self.controller["in_or_out"] is not None,
			"Input/Output must be called prior to grid definitions."
		assert self.controller["in_or_out"] == "in" or self.controller["in_or_out"] == "out",
			"Unsupported 'in_or_out' definition in controler dictionary."

	# Switch for defining Input/Outputs

	def input(self):
		"""Switches input grid axes on."""
		self.controller["in_or_out"] = "in"


	def output(self):
		"""Switches output grid axes on."""
		self.controller["in_or_out"] = "out"

	# Grid input functions.

	def _get_grid_dict(self, grid, mode, params):
		"""Returns grid definition dictionary.

		Parameters
		----------
		grid : str
			Grid type string definition.
		mode : str
			Grid dimension definition: '1D', '2D', '3D' or 'usphere'.
		params : args
			Additional grid-specific definitions.

		Returns
		-------
		grid_dict : dict
			Dictionary defining properties of the grid.
		"""
		grid_dict = {
			"grid": grid,
			"mode": mode,
			"params": params
		}
		return grid_dict


	def _add_grid(self, grid_dict):
		"""Adds grid dictionary to either input or output.

		Parameters
		----------
		grid_dict : dict
			Dictionary defining properties of the grid.
		"""
		self.conversion[self.controller["in_or_out"]] = grid_dict


	# Grid definitions

	def grid2D(self, ngrid, boxsize, origin=0.):
		"""Grid 2D defintion.

		
		"""
		params = {
			"ngrid": ngrid,
			"boxsize": boxsize,
			"origin": origin
		}
		grid_dict = self._get_grid_dict("cart", "2D", params)
		self._add_grid(grid_dict)


	def clean(self):
		"""Cleans and reinitialised the Remap class."""
		self.__init__()
