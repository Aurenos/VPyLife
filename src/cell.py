# VPyLife - Cell module
# Kile Deal

from visual import box, color, materials

class Cell(box):
	def __init__(self, length=1, height=1, width=1, pos=(0,0,0), color=color.white, material=None, opacity=1.0,
					visible=True, alive=False):
		box.__init__(self) # call super constructor
		
		self.length = length
		self.height = height
		self.width = width
		self.pos = pos
		self.color = color
		self.material = material
		self.opacity = opacity
		self.visible = visible
		self.alive = alive

