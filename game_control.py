#!/usr/bin/python

import Player

pl1 = Player.Player(1, 0)
pl2 = Player.Player(1, 1)
pl3 = Player.Player(1, 2)
pl4 = Player.Player(0, 3)
pl5 = Player.Player(0, 4)

play_list = [pl1, pl2, pl3, pl4, pl5]

game = Player.Game(play_list)
try:
	game.game_start(pl1)
except Player.Game_Exception as e:
	if(e.value == Player.Game_Rule.GAME_FREEDOM_WARRIOR_WIN):
		print "game success"
	else:
		print "game loss"
	
