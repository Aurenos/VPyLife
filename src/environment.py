# VPyLife - Environment module
# Kile Deal

from visual import color, materials, rate, label
from numpy import array
from cell import Cell
from wireframe import WireFrameGrid

age_colors = ((0.08,0.81,0.0), (0.16,0.62,0.0), (0.24,0.43,0.0), (0.32,0.24,0.0))

class Environment:
	def __init__(self, size=10, grid_color=color.white, grid_material=None,
				visible=False, thickness=0, scale=1, cell_color=color.green, cell_material=None,
				rule="23/3", gen_rate=1):
		### Physical Parts ###
		self.size = size
		self.grid_color = grid_color
		self.grid_material = grid_material
		self.visible = visible
		self.thickness = thickness
		self.scale = scale
		self.cell_color = cell_color
		self.cell_material = cell_material

		self.grid = WireFrameGrid(length=self.size, width=self.size, height=self.size,
			color=self.grid_color, visible=self.visible, thickness=self.thickness, 
			scale=self.scale, material=self.grid_material)

		self.cells = None

		### Data ###
		"""
		Rules are in the notation '{S}/{B}' where {S} is a string containing a list of numbers to determine
		how many adjacent cells are necessary for a cell to survive, and {B} is a string containing a list of
		numbers to determine how many adjacent cells are necessary to be born (activate).
		"""
		self.rule = rule
		self.generation = 1
		self.gen_rate = gen_rate

	@property 
	def survival_conditions(self):
		return [int(s) for s in self.rule.split('/')[0]]

	@property 
	def birth_conditions(self):
		return [int(s) for s in self.rule.split('/')[1]]

	def render(self):
		self.grid.generate()
		self.fill_grid()
		self.link_cells() 		

	def get_next_gen(self):
		kill_list = []
		birth_list = []
		for cell in self.cells.flatten():
			if cell.active:
				if cell.active_links not in self.survival_conditions:
					kill_list.append(cell)
				else:
					cell.age += 1
					if cell.age >= 8:
						cell.color = age_colors[3]
					elif cell.age >= 6:
						cell.color = age_colors[2]
					elif cell.age >= 4:
						cell.color = age_colors[1]
					elif cell.age >= 2:
						cell.color = age_colors[0]
			else:
				if cell.active_links in self.birth_conditions:
					birth_list.append(cell)

		for cell in kill_list:  cell.deactivate() 
		for cell in birth_list: cell.activate()
		self.generation += 1

	def toggle_grid(self):
		"""
		Toggle the visibilty of the WireFrameGrid
		"""
		if self.grid.visible:
			self.grid.set_visibility(False)
		else:
			self.grid.set_visibility(True)

	def toggle_outline(self):
		"""
		Toggle the visibility of the WireFrameGrid's outline
		"""
		if self.grid.outline.visible:
			self.grid.set_outline_visibility(False)
		else:
			self.grid.set_outline_visibility(True)

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
			if x > self.size*(self.scale*2):
				y += 2
				x = 1

				if y > self.size*(self.scale*2):
					z += 2
					y = 1

			newcell = Cell(color=self.cell_color, material=self.cell_material, visible=False,
						pos=(-self.size/2.0+sref*x, -self.size/2.0+sref*y, -self.size/2.0+sref*z))

			c.append(newcell)

			x += 2

		self.cells = array(c).reshape(self.size, self.size, self.size)

	def link_cells(self):
		"""
		Assigns the 26 links for each cell in the 3D matrix.
		"""
		for z in xrange(self.size):
			for y in xrange(self.size):
				for x in xrange(self.size):
					self.cells[z][y][x].link_r   = self.cells[z][y][x+1]     if x + 1 < self.size else None
					self.cells[z][y][x].link_l   = self.cells[z][y][x-1]     if x - 1 >= 0 else None
					self.cells[z][y][x].link_u   = self.cells[z][y+1][x]     if y + 1 < self.size else None
					self.cells[z][y][x].link_d   = self.cells[z][y-1][x]     if y - 1 >= 0 else None
					self.cells[z][y][x].link_f   = self.cells[z+1][y][x]     if z + 1 < self.size else None
					self.cells[z][y][x].link_b   = self.cells[z-1][y][x]     if z - 1 >= 0 else None
					self.cells[z][y][x].link_ul  = self.cells[z][y+1][x-1]   if y + 1 < self.size and x - 1 >= 0 else None
					self.cells[z][y][x].link_ur  = self.cells[z][y+1][x+1]   if y + 1 < self.size and x + 1 < self.size else None
					self.cells[z][y][x].link_dl  = self.cells[z][y-1][x-1]   if y - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_dr  = self.cells[z][y-1][x+1]   if y - 1 >= 0 and x + 1 < self.size else None
					self.cells[z][y][x].link_fu  = self.cells[z+1][y+1][x]   if z + 1 < self.size and y + 1 < self.size else None
					self.cells[z][y][x].link_fd  = self.cells[z+1][y-1][x]   if z + 1 < self.size and y - 1 >= 0 else None
					self.cells[z][y][x].link_fl  = self.cells[z+1][y][x-1]   if z + 1 < self.size and x - 1 >= 0 else None
					self.cells[z][y][x].link_fr  = self.cells[z+1][y][x+1]   if z + 1 < self.size and x + 1 < self.size else None
					self.cells[z][y][x].link_bu  = self.cells[z-1][y+1][x]   if z - 1 >= 0 and y + 1 < self.size else None
					self.cells[z][y][x].link_bd  = self.cells[z-1][y-1][x]   if z - 1 >= 0 and y - 1 >= 0 else None
					self.cells[z][y][x].link_bl  = self.cells[z-1][y][x-1]   if z - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_br  = self.cells[z-1][y][x+1]   if z - 1 >= 0 and x + 1 < self.size else None
					self.cells[z][y][x].link_ful = self.cells[z+1][y+1][x-1] if z + 1 < self.size and y + 1 < self.size and x - 1 >= 0 else None
					self.cells[z][y][x].link_fur = self.cells[z+1][y+1][x+1] if z + 1 < self.size and y + 1 < self.size and x + 1 < self.size else None
					self.cells[z][y][x].link_fdl = self.cells[z+1][y-1][x-1] if z + 1 < self.size and y - 1 >= 0 and x - 1 >= 0 else None 
					self.cells[z][y][x].link_fdr = self.cells[z+1][y-1][x+1] if z + 1 < self.size and y - 1 >= 0 and x + 1 < self.size else None
					self.cells[z][y][x].link_bul = self.cells[z-1][y+1][x-1] if z - 1 >= 0 and y + 1 < self.size and x - 1 >= 0 else None
					self.cells[z][y][x].link_bur = self.cells[z-1][y+1][x+1] if z - 1 >= 0 and y + 1 < self.size and x + 1 < self.size else None
					self.cells[z][y][x].link_bdl = self.cells[z-1][y-1][x-1] if z - 1 >= 0 and y - 1 >= 0 and x - 1 >= 0 else None
					self.cells[z][y][x].link_bdr = self.cells[z-1][y-1][x+1] if z - 1 >= 0 and y - 1 >= 0 and x + 1 < self.size else None
			