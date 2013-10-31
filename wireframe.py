# VPyLife Wireframe Grid module
# Kile Deal

from visual import frame, curve, materials, color, rate, scene, box
from random import randrange

class WireFrameGrid:
	def __init__(self, scale=1, length=1, width=1, height=1, pos=(0,0,0), visible=True, thickness=0, color=color.white,
				 material=None, animate_gen=False, animate_rate=5):

		self.scale = scale
		self.length = length
		self.width = width
		self.height = height
		self.frame = frame()
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
		self.pos = value
		self.x = pos[0]
		self.y = pos[1]
		self.z = pos[2]

	def set_visibility(self, val):
		self.visible = val
		self.frame.visible = self.visible
	
	def generate(self):
		sref = self.scale/2.0

		# Lines from back to front
		mult = 0
		yval = self.y+self.height*sref
		for y in xrange(self.height+1):
			if self.animate_gen: rate(self.animate_rate)
			for x in xrange(self.length+1):
				if self.animate_gen: rate(self.animate_rate)
				curve(pos=[(self.x-self.length*sref+sref*mult, yval, self.z+self.width*sref),
						   (self.x-self.length*sref+sref*mult, yval, self.z-self.width*sref)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)
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
				curve(pos=[(self.x-self.length*sref, yval, self.z-self.width*sref+sref*mult),
						   (self.x+self.length*sref, yval, self.z-self.width*sref+sref*mult)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)
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
				curve(pos=[(xval, self.y+self.height*sref, self.z-self.width*sref+sref*mult),
					   (xval, self.y-self.height*sref, self.z-self.width*sref+sref*mult)],
					frame=self.frame, radius=self.thickness, material=self.material, color=self.color)
				mult += 2
			xval += sref*2
			mult = 0				

if __name__ == '__main__': # For fun and testing purposes
	scene.height=800
	scene.width=800
	scene.range = 5
	var = 1
	test = WireFrameGrid(length = var, width = var, height = var, thickness=0.005, color=color.green,
		animate_gen=False, animate_rate=20)
	test.generate() 
	box(color=color.green, material=materials.emissive, frame=test.frame, length=var, height=var, width=var)

	## Just for fun
	# ax = randrange(0,10,1)
	# ay = randrange(0,10,1)
	# az = randrange(0,10,1)
	# dx, dy, dz = 0, 0, 0
	# change = 0
	# changing = False
	# while True:
	# 	rate(25)
	# 	test.frame.rotate(axis=(ax,ay,az), angle=3.14/70)
	
	# 	if changing:
	# 		if ax == dx and ay == dy and az == dz:
	# 			changing = False
	# 			print "Changed"
	# 			change = 0
	# 		else:
	# 			if ax > dx: ax -= 1
	# 			elif ax < dx: ax += 1
	# 			if ay > dy: ay -= 1
	# 			elif ay < dy: ay += 1
	# 			if az > dz: az -= 1
	# 			elif az < dz: az += 1
	# 	else:	
	# 		change += 1
	# 		if change == 100:
	# 			dx = randrange(0,10,1)
	# 			dy = randrange(0,10,1)
	# 			dz = randrange(0,10,1)
	# 			changing = True