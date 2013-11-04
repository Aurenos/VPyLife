# VPyLife - Environment module
# Kile Deal

from visual import * 
from cell import Cell
from wireframe import WireFrameGrid

class Environment:
	def __init__(self, length=10, width=10, height=10, grid_color=color.white, material=None,
				visible=True, thickness=0, scale=1, cell_color=color.green):
		self.length = length
		self.width = width
		self.height = height
		self.grid_color = grid_color
		self.material = material
		self.visible = visible
		self.thickness = thickness
		self.scale = scale
		self.cell_color = cell_color

		self.grid = WireFrameGrid(length=self.length, width=self.width, height=self.height,
			color=self.grid_color, visible=self.visible, thickness=self.thickness, 
			scale=self.scale, material=self.material)

		self.grid.generate()

		self.cells = []
		self.fill_grid()

	def toggle_grid(self):
		if self.grid.visible:
			self.grid.set_visibility(False)
		else:
			self.grid.set_visibility(True)

	def fill_grid(self):
		pass
