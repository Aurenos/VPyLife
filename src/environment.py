# VPyLife - Environment module
# Kile Deal

from visual import * 
from cell import Cell
from wireframe import WireFrameGrid

class Environment:
	def __init__(self, length=10, width=10, height=10, grid_color=color.white, grid_material=None,
				visible=True, thickness=0, scale=1, cell_color=color.green, cell_material=None,
				rule="23/3"):
		self.length = length
		self.width = width
		self.height = height
		self.grid_color = grid_color
		self.grid_material = grid_material
		self.visible = visible
		self.thickness = thickness
		self.scale = scale
		self.cell_color = cell_color
		self.cell_material = cell_material
		
		self.rule = rule 
		"""
		Rules are in the notation '{S}/{B}' where {S} is a string containing a list of numbers to determine
		how many adjacent cells are necessary for a cell to survive, and {B} is a string containing a list of
		numbers to determine how many adjacent cells are necessary to be born (activate).
		"""


		self.grid = WireFrameGrid(length=self.length, width=self.width, height=self.height,
			color=self.grid_color, visible=self.visible, thickness=self.thickness, 
			scale=self.scale, material=self.grid_material)

		self.grid.generate()

		self.cells = None
		self.fill_grid()
		self.link_cells()

	def toggle_grid(self):
		"""
		Toggle the visibilty of the WireFrameGrid
		"""
		if self.grid.visible:
			self.grid.set_visibility(False)
		else:
			self.grid.set_visibility(True)

	def fill_grid(self):
		"""
		Render the Cells in the appropriate places in space to fit the WireFrameGrid
		"""
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

			newcell = Cell(color=self.cell_color, material=self.cell_material, visible=False,
						pos=(-self.length/2.0+sref*x, -self.height/2.0+sref*y, -self.width/2.0+sref*z))

			c.append(newcell)

			x += 2

		self.cells = array(c).reshape(self.width, self.height, self.length)

	def link_cells(self):
		"""
		Assigns the 26 links for each cell in the 3D matrix.
		"""
		for z in xrange(self.width):
			for y in xrange(self.height):
				for x in xrange(self.length):
					self.cells[z][y][x].link_r   = self.cells[z][y][x+1]     if x + 1 < self.length else None
					self.cells[z][y][x].link_l   = self.cells[z][y][x-1]     if x - 1 >= 0 else None
					self.cells[z][y][x].link_u   = self.cells[z][y+1][x]     if y + 1 < self.height else None
					self.cells[z][y][x].link_d   = self.cells[z][y-1][x]     if y - 1 >= 0 else None
					self.cells[z][y][x].link_f   = self.cells[z+1][y][x]     if z + 1 < self.width else None
					self.cells[z][y][x].link_b   = self.cells[z-1][y][x]     if z - 1 >= 0 else None
					self.cells[z][y][x].link_ul  = self.cells[z][y+1][x-1]   if y + 1 < self.height and x - 1 >= 0 else None
					self.cells[z][y][x].link_ur  = self.cells[z][y+1][x+1]   if y + 1 < self.height and x + 1 < self.length else None
					self.cells[z][y][x].link_dl  = self.cells[z][y-1][x-1]   if y - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_dr  = self.cells[z][y-1][x+1]   if y - 1 >= 0 and x + 1 < self.length else None
					self.cells[z][y][x].link_fu  = self.cells[z+1][y+1][x]   if z + 1 < self.width and y + 1 < self.height else None
					self.cells[z][y][x].link_fd  = self.cells[z+1][y-1][x]   if z + 1 < self.width and y - 1 >= 0 else None
					self.cells[z][y][x].link_fl  = self.cells[z+1][y][x-1]   if z + 1 < self.width and x - 1 >= 0 else None
					self.cells[z][y][x].link_fr  = self.cells[z+1][y][x+1]   if z + 1 < self.width and x + 1 < self.length else None
					self.cells[z][y][x].link_bu  = self.cells[z-1][y+1][x]   if z - 1 >= 0 and y + 1 < self.height else None
					self.cells[z][y][x].link_bd  = self.cells[z-1][y-1][x]   if z - 1 >= 0 and y - 1 >= 0 else None
					self.cells[z][y][x].link_bl  = self.cells[z-1][y][x-1]   if z - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_br  = self.cells[z-1][y][x+1]   if z - 1 >= 0 and x + 1 < self.length else None
					self.cells[z][y][x].link_ful = self.cells[z+1][y+1][x-1] if z + 1 < self.width and y + 1 < self.height and x - 1 >= 0 else None
					self.cells[z][y][x].link_fur = self.cells[z+1][y+1][x+1] if z + 1 < self.width and y + 1 < self.height and x + 1 < self.length else None
					self.cells[z][y][x].link_fdl = self.cells[z+1][y-1][x-1] if z + 1 < self.width and y - 1 >= 0 and x - 1 >= 0 else None 
					self.cells[z][y][x].link_fdr = self.cells[z+1][y-1][x+1] if z + 1 < self.width and y - 1 >= 0 and x + 1 < self.length else None
					self.cells[z][y][x].link_bul = self.cells[z-1][y+1][x-1] if z - 1 >= 0 and y + 1 < self.height and x - 1 >= 0 else None
					self.cells[z][y][x].link_bur = self.cells[z-1][y+1][x+1] if z - 1 >= 0 and y + 1 < self.height and x + 1 < self.length else None
					self.cells[z][y][x].link_bdl = self.cells[z-1][y-1][x-1] if z - 1 >= 0 and y - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_bdr = self.cells[z-1][y-1][x+1] if z - 1 >= 0 and y - 1 >= 0 and x + 1 < self.length else None
			

