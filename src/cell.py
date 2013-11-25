# VPyLife - Cell module
# Kile Deal

from visual import box, color, materials

class Cell(box):
	__count = 0
	def __init__(self, length=1, height=1, width=1, pos=(0,0,0), color=color.white, material=None, opacity=1.0,
					visible=True, active=False):
		box.__init__(self) # call super constructor
		
		self.length = length
		self.height = height
		self.width = width
		self.pos = pos
		self.color = color
		self.material = material
		self.opacity = opacity
		self.visible = visible
		self.active = active
		self.id = Cell.__count
		Cell.__count += 1

		## Cell Links
		# Each cell has 26 adjacent cells or boundaries, one for each direction in 3D space
		self.link_u   = None 	# Up               (+y)
		self.link_d   = None 	# Down             (-y)
		self.link_l   = None 	# Left             (-x)
		self.link_r   = None 	# Right            (+x)
		self.link_f   = None 	# Front            (+z)
		self.link_b   = None 	# Back             (-z)
		self.link_ul  = None 	# Up-Left          (-x, +y)
		self.link_ur  = None 	# Up-Right         (+x, +y)
		self.link_dl  = None 	# Down-Left        (-x, -y)
		self.link_dr  = None 	# Down-Right       (+x, -y)
		self.link_fu  = None 	# Front-Up         (+y, +z)
		self.link_fd  = None 	# Front-Down       (-y, +z)
		self.link_fl  = None 	# Front-Left       (-x, +z)
		self.link_fr  = None 	# Front-Right      (+x, +z)
		self.link_bu  = None 	# Back-Up          (+y, -z)
		self.link_bd  = None 	# Back-Down        (-y, -z)
		self.link_bl  = None 	# Back-Left        (-x, -z)
		self.link_br  = None 	# Back-Right       (+x, -z)
		self.link_ful = None 	# Front-Up-Left    (-x, +y, +z)
		self.link_fur = None 	# Front-Up-Right   (+x, +y, +z)
		self.link_fdl = None 	# Front-Down-Left  (-x, -y, +z)
		self.link_fdr = None 	# Front-Down-Right (+x, -y, +z)
		self.link_bul = None 	# Back-Up-Left     (-x, +y, -z)
		self.link_bur = None 	# Back-Up-Right    (+x, +y, -z)
		self.link_bdl = None 	# Back-Down-Left   (-x, -y, -z)
		self.link_bdr = None 	# Back-Down-Right  (+x, -y, -z)

	@property
	def links(self):
		return [self.link_u, self.link_d, self.link_l, self.link_r, self.link_f, self.link_b,
				self.link_ul, self.link_ur, self.link_dl, self.link_dr, self.link_fu, self.link_fd, 
				self.link_fl, self.link_fr, self.link_bu, self.link_bd, self.link_bl, self.link_br, 
				self.link_ful, self.link_fur, self.link_fdl, self.link_fdr, self.link_bul, self.link_bur, 
				self.link_bdl, self.link_bdr]

	@property 
	def active_links(self):
		total = 0
		for link in self.links:
			if link != None:
				if link.active:
					total += 1
		return total

	def activate(self):
		"""
		Change the state of the cell to active
		"""
		self.active = True
		self.visible = True

	def deactivate(self):
		"""
		Change the state of the cell to inactive
		"""
		self.active = False
		self.visible = False

	def __str__(self):
		return "Cell %3d" % self.id
