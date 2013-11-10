# VPyLife - Environment module
# Kile Deal

from visual import * 
from cell import Cell
from wireframe import WireFrameGrid
import pprint
import copy

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

		self.cells = None
		self.fill_grid()
		self.link_cells()

	def toggle_grid(self):
		if self.grid.visible:
			self.grid.set_visibility(False)
		else:
			self.grid.set_visibility(True)

	def fill_grid(self):
		sref = self.scale/2.0
		x = 1
		y = 1
		z = 1
		c = []
		row = 0
		column = 0
		for i in xrange(self.grid.volume):
			# rate(10)
			if x > self.length*(self.scale*2):
				y += 2
				x = 1

				if y > self.height*(self.scale*2):
					z += 2
					y = 1

			newcell = Cell(color=color.green, material=materials.glass, visible=False,
						pos=(-self.length/2.0+sref*x, -self.height/2.0+sref*y, -self.width/2.0+sref*z))

			c.append(newcell)

			x += 2

		self.cells = array(c).reshape(self.width, self.height, self.length)
		pprint.pprint(self.cells)

	def link_cells(self):
		for z in xrange(self.width):
			for y in xrange(self.height):
				for x in xrange(self.length):
					self.cells[z][y][x].rightlink = self.cells[z][y][x+1] if x + 1 < self.length else None
					self.cells[z][y][x].leftlink  = self.cells[z][y][x-1] if x - 1 >= 0 else None
					self.cells[z][y][x].uplink    = self.cells[z][y+1][x] if y + 1 < self.height else None
					self.cells[z][y][x].downlink  = self.cells[z][y-1][x] if y - 1 >= 0 else None
					self.cells[z][y][x].frontlink = self.cells[z+1][y][x] if z + 1 < self.width else None
					self.cells[z][y][x].backlink  = self.cells[z-1][y][x] if z - 1 >= 0 else None
			

