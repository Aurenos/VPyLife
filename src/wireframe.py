# VPyLife Wireframe Grid module
# Kile Deal

from visual import frame, curve, materials, color, rate, scene, box

class WireFrameGrid:
	def __init__(self, scale=1, length=1, width=1, height=1, pos=(0,0,0), visible=True,
					thickness=0, color=color.white, material=None, animate_gen=False, 
					animate_rate=5):

		self.scale = scale
		self.length = length
		self.width = width
		self.height = height
		self.frame = frame()
		self.outline = frame()
		self.visible = visible
		self.thickness = thickness
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]
		self.color = color
		self.material = material
		self.animate_gen = animate_gen
		self.animate_rate = animate_rate

	@property
	def volume(self):
	    return self.length * self.width * self.height # The number of boxes

	def set_pos(self, value):
		"""
		Set the position of the entire frame
		"""
		self.pos = value
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]

	def set_visibility(self, val):
		"""
		Change visibility of the grid
		"""
		self.visible = val
		self.frame.visible = self.visible

	def set_outline_visibility(self, val):
		"""
		Change visibility of outline
		"""
		self.outline.visible = val
	
	def generate(self):
		"""
		Render the curves that make up the 3D Grid
		"""
		sref = self.scale/2.0
		outline_curves = list()
		# Lines from back to front
		mult = 0
		yval = self.y+self.height*sref
		for y in xrange(self.height+1):
			if self.animate_gen: rate(self.animate_rate)
			for x in xrange(self.length+1):
				if self.animate_gen: rate(self.animate_rate)
				c = curve(pos=[(self.x-self.length*sref+sref*mult, yval, self.z+self.width*sref),
						   (self.x-self.length*sref+sref*mult, yval, self.z-self.width*sref)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)

				if (y == 0 and x == 0):
					outline_curves.append(c)
				elif (y == self.height and x == self.length):
					outline_curves.append(c)
				elif (y == 0 and x == self.length):
					outline_curves.append(c)
				elif (y == self.height and x == 0):
					outline_curves.append(c)

				mult += 2
			yval -= sref*2
			mult = 0

		# Lines from left to right
		mult = 0
		yval = self.y+self.height*sref
		for y in xrange(self.height+1):
			if self.animate_gen: rate(self.animate_rate)
			for z in xrange(self.width+1):
				if self.animate_gen: rate(self.animate_rate)
				c = curve(pos=[(self.x-self.length*sref, yval, self.z-self.width*sref+sref*mult),
						   (self.x+self.length*sref, yval, self.z-self.width*sref+sref*mult)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)

				if (y == 0 and z == 0):
					outline_curves.append(c)
				elif (y == self.height and z == self.width):
					outline_curves.append(c)
				elif (y == 0 and z == self.width):
					outline_curves.append(c)
				elif (y == self.height and z == 0):
					outline_curves.append(c)

				mult += 2
			yval -= sref*2
			mult = 0

		# Lines from top to bottom
		mult = 0
		xval = self.x-self.length*sref
		for x in xrange(self.length+1):
			if self.animate_gen: rate(self.animate_rate)
			for z in xrange(self.width+1):
				if self.animate_gen: rate(self.animate_rate)
				c = curve(pos=[(xval, self.y+self.height*sref, self.z-self.width*sref+sref*mult),
					   (xval, self.y-self.height*sref, self.z-self.width*sref+sref*mult)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)

				if (z == 0 and x == 0):
					outline_curves.append(c)
				elif (z == self.width and x == self.length):
					outline_curves.append(c)
				elif (z == 0 and x == self.length):
					outline_curves.append(c)
				elif (z == self.width and x == 0):
					outline_curves.append(c)

				mult += 2
			xval += sref*2
			mult = 0

		for c in outline_curves:
			c.frame = self.outline

		self.set_visibility(self.visible)			