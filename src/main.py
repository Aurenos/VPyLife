# VPyLife - Main module
# Kile Deal

from visual import window, display, rate
from environment import Environment
from random import seed, randint
from math import ceil
import wx, re

### Global variables ###
environ = Environment()
life_seed = None
rule = "23/3"
gen_rate = 1
paused = True
_title = "VPyLife - Generation: {0} - Rule: {1}".format(environ.generation, rule)

WIN_WIDTH    = 1024
WIN_HEIGHT   = 680
DISP_HEIGHT  = 600
DISP_WIDTH   = 600
font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
header = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
d = 10 # Widget distance offset
########################

def show_error(msg):
	wx.MessageBox(msg, "Error!", wx.ICON_ERROR | wx.OK)

def update_title():
	global _title
	global win
	_title = "VPyLife - Generation: {0} - Rule: {1}".format(environ.generation, rule)
	win.win.SetTitle(_title)

def new_generation():
	global life_seed
	global environ
	environ.clear_grid()
	environ.generation = 1
	seed(life_seed)
	amt = randint(1,ceil(environ.grid.volume/randint(3,10)))
	cells = environ.cells.flatten()
	for i in xrange(amt):
		c = cells[randint(0, len(cells)-1)]
		c.activate()

def set_rule(evt):
	global rule
	global environ
	val = str(rule_txtctrl.GetValue().replace(" ",""))
	if re.match("[0-9]{1,10}\/[0-9]{1,10}", val):
		rule = val
		environ.rule = rule
		update_title()
	else:
		show_error("Invalid rule string. Rule strings must be of the form {S}/{B}\nwhere {S} and {B} are strings of integers of max length 10.\n\nExample: 234/15")

def set_rate(evt):
	global gen_rate
	val = int(rate_ctrl.GetValue())
	gen_rate = val

def set_environ_size(evt):
	global environ
	try:
		val = abs(int(env_txtctrl.GetValue().replace(" ","")))
		environ.clear_grid()
		environ.grid.set_visibility(False)
		environ.grid.set_outline_visibility(False)
		environ = Environment(size=val)
		environ.render()
		new_generation()
		update_title()
	except ValueError:
		show_error("Invalid value for Environment Size. Please enter an integer.")

def set_seed(evt):
	global life_seed
	global environ
	val = seed_txtctrl.GetValue()
	if val == "":
		life_seed = None
	else:
		life_seed = seed_txtctrl.GetValue()
		environ.generation = 1
		new_generation()
		update_title()

def next_generation(evt):
	global environ
	environ.get_next_gen()
	update_title()

def tg_grid(evt):
	global environ
	environ.toggle_grid()

def tg_outline(evt):
	global environ
	environ.toggle_outline()

def play_pause(evt):
	global paused
	global play
	if paused:
		paused = False
		next.Disable()
		play.SetLabel("Pause")
	else:
		paused = True
		next.Enable()
		play.SetLabel("Start")


win = window(menus=True, title=_title, x=wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)/2-WIN_WIDTH/2, 
	y=wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)/2-WIN_HEIGHT/2, width=WIN_WIDTH, height=WIN_HEIGHT)
win.win.SetMinSize((WIN_WIDTH, WIN_HEIGHT))
win.win.SetMaxSize((WIN_WIDTH, WIN_HEIGHT))
disp = display(window=win, x=d, y=d, height=DISP_HEIGHT, width=DISP_WIDTH)

p = win.panel

# Rule
rule_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, d), label="Rule: ", )
rule_txt.SetFont(font)
rule_txtctrl = wx.TextCtrl(p, pos=(rule_txt.Position.Get()[0]+rule_txt.Size.Get()[0], rule_txt.Position.Get()[1]),
	size=(200,22), style=wx.ALIGN_RIGHT)
rule_txtctrl.SetFont(font)
rule_set = wx.Button(p, label="Set Rule", pos=(rule_txtctrl.Position.Get()[0]+rule_txtctrl.Size.Get()[0]+d, rule_txtctrl.Position.Get()[1]-2))
rule_set.Bind(wx.EVT_BUTTON, set_rule)

# Environment Size
env_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, rule_txt.Position.Get()[1]+d*4), label="Environment Size: ", )
env_txt.SetFont(font)
env_txtctrl = wx.TextCtrl(p, pos=(env_txt.Position.Get()[0]+env_txt.Size.Get()[0], env_txt.Position.Get()[1]),
	size=(110,22), style=wx.ALIGN_RIGHT)
env_txtctrl.SetFont(font)
env_set = wx.Button(p, label="Set Size", pos=(env_txtctrl.Position.Get()[0]+env_txtctrl.Size.Get()[0]+d, env_txtctrl.Position.Get()[1]-2))
env_set.Bind(wx.EVT_BUTTON, set_environ_size)

# Seed
seed_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, env_txt.Position.Get()[1]+d*4), label="Life Seed: ", )
seed_txt.SetFont(font)
seed_txtctrl = wx.TextCtrl(p, pos=(seed_txt.Position.Get()[0]+seed_txt.Size.Get()[0], seed_txt.Position.Get()[1]),
	size=(162,22), style=wx.ALIGN_RIGHT)
seed_txtctrl.SetFont(font)
seed_set = wx.Button(p, label="Set Seed", pos=(seed_txtctrl.Position.Get()[0]+seed_txtctrl.Size.Get()[0]+d, seed_txtctrl.Position.Get()[1]-2))
seed_set.Bind(wx.EVT_BUTTON, set_seed)

# Grid Toggle Buttons
grid = wx.Button(p, label="Toggle Wireframe Grid", pos=(DISP_WIDTH+d*2, seed_txt.Position.Get()[1]+d*4), size=(240, 25))
grid.Bind(wx.EVT_BUTTON, tg_grid)
outline = wx.Button(p, label="Toggle Outline", pos=(DISP_WIDTH+d*2, grid.Position.Get()[1]+d*4), size=(240,25))
outline.Bind(wx.EVT_BUTTON, tg_outline)

# Play, Next, Previous, and Rate control

rate_txt = wx.StaticText(p, label="Rate:", pos=(DISP_WIDTH+d*2, DISP_HEIGHT-d*2))
rate_txt.SetFont(font)
rate_ctrl = wx.Slider(p, pos=(rate_txt.Position.Get()[0]+rate_txt.Size.Get()[0], rate_txt.Position.Get()[0]-d*4),
	minValue=1, value=1, maxValue=20, size=(320, 25))
rate_ctrl.Bind(wx.EVT_SLIDER, set_rate)

previous = wx.Button(p, label="Previous", pos=(rate_txt.Position.Get()[0], rate_txt.Position.Get()[1]-d*7), size=(100, 60))
previous.Disable()

play = wx.Button(p, label="Start", pos=(previous.Position.Get()[0]+previous.Size.Get()[0], rate_txt.Position.Get()[1]-d*7), size=(150, 60))
play.Bind(wx.EVT_BUTTON, play_pause)

next = wx.Button(p, label="Next", pos=(play.Position.Get()[0]+play.Size.Get()[0], rate_txt.Position.Get()[1]-d*7), size=(100, 60))
next.Bind(wx.EVT_BUTTON, next_generation)

gen_ctrl_txt = wx.StaticText(p, pos=(play.Position.Get()[0]+1, previous.Position.Get()[1]-d*4), label="Generation Control")
gen_ctrl_txt.SetFont(header)

# Rendering
environ.render()
new_generation()

while True:
	rate(gen_rate)
	if not paused:
		environ.get_next_gen()
		update_title()
	else:
		pass