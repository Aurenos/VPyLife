# VPyLife - Main module
# Kile Deal

from visual import window, display
import wx
from environment import Environment
from random import seed

def set_rule(r):
	pass

def set_rate(x):
	pass

def toggle_grid():
	pass

def toggle_outline():
	pass

WIN_WIDTH    = 1024
WIN_HEIGHT   = 680
DISP_HEIGHT  = 600
DISP_WIDTH   = 600
font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
header = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
d = 10 # Widget distance offset

def main():
	## GUI Setup
	win = window(menus=True, title="VPyLife - Generation: 0 - Rule: 23/3", x=wx.SystemSettings.GetMetric(wx.SYS_SCREEN_X)/2-WIN_WIDTH/2, 
		y=wx.SystemSettings.GetMetric(wx.SYS_SCREEN_Y)/2-WIN_HEIGHT/2, width=WIN_WIDTH, height=WIN_HEIGHT)
	disp = display(window=win, x=d, y=d, height=DISP_HEIGHT, width=DISP_WIDTH)

	p = win.panel

	# Rule
	rule_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, d), label="Rule: ", )
	rule_txt.SetFont(font)
	rule_txtctrl = wx.TextCtrl(p, pos=(rule_txt.Position.Get()[0]+rule_txt.Size.Get()[0], rule_txt.Position.Get()[1]),
		size=(200,22), style=wx.ALIGN_RIGHT)
	rule_txtctrl.SetFont(font)
	rule_set = wx.Button(p, label="Set Rule", pos=(rule_txtctrl.Position.Get()[0]+rule_txtctrl.Size.Get()[0]+d, rule_txtctrl.Position.Get()[1]-2))

	# Environment Size
	env_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, rule_txt.Position.Get()[1]+d*4), label="Environment Size: ", )
	env_txt.SetFont(font)
	env_txtctrl = wx.TextCtrl(p, pos=(env_txt.Position.Get()[0]+env_txt.Size.Get()[0], env_txt.Position.Get()[1]),
		size=(110,22), style=wx.ALIGN_RIGHT)
	env_txtctrl.SetFont(font)
	env_set = wx.Button(p, label="Set Size", pos=(env_txtctrl.Position.Get()[0]+env_txtctrl.Size.Get()[0]+d, env_txtctrl.Position.Get()[1]-2))

	# Seed
	seed_txt = wx.StaticText(p, pos=(DISP_WIDTH+d*2, env_txt.Position.Get()[1]+d*4), label="Life Seed: ", )
	seed_txt.SetFont(font)
	seed_txtctrl = wx.TextCtrl(p, pos=(seed_txt.Position.Get()[0]+seed_txt.Size.Get()[0], seed_txt.Position.Get()[1]),
		size=(162,22), style=wx.ALIGN_RIGHT)
	seed_txtctrl.SetFont(font)
	seed_set = wx.Button(p, label="Set Seed", pos=(seed_txtctrl.Position.Get()[0]+seed_txtctrl.Size.Get()[0]+d, seed_txtctrl.Position.Get()[1]-2))

	# Grid Toggle Buttons
	grid = wx.Button(p, label="Toggle Wireframe Grid", pos=(DISP_WIDTH+d*2, seed_txt.Position.Get()[1]+d*4), size=(240, 25))
	outline = wx.Button(p, label="Toggle Outline", pos=(DISP_WIDTH+d*2, grid.Position.Get()[1]+d*4), size=(240,25))

	# Play, Next, and Previous
	previous = wx.Button(p, label="Previous", pos=(DISP_WIDTH+d*2, DISP_HEIGHT-d*5), size=(100, 60))
	previous.Disable()
	play = wx.Button(p, label="Start", pos=(previous.Position.Get()[0]+previous.Size.Get()[0], DISP_HEIGHT-d*5), size=(150, 60))
	next = wx.Button(p, label="Next", pos=(play.Position.Get()[0]+play.Size.Get()[0], DISP_HEIGHT-d*5), size=(100, 60))
	next.Disable()

	gen_ctrl_txt = wx.StaticText(p, pos=(play.Position.Get()[0]+1, previous.Position.Get()[1]-d*4), label="Generation Control")
	gen_ctrl_txt.SetFont(header)

	# Rendering
	environment = Environment()
	

if __name__ == '__main__':
	main()