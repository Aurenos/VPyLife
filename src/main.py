# VPyLife - Main module
# Kile Deal

from visual import scene
from environment import Environment

def main():
	rule = "23/3"
	# Scene settings
	scene.title = "VPyLife (Rule: %s)" % rule 
	scene.width = 800
	scene.height = 600

	# Rendering
	environment = Environment(rule=rule)
	

if __name__ == '__main__':
	main()