# -*- coding: latin -*-

MSG = "%s %s"
NO_ARGS = "Go where?"
GO_USER = "You went to room \"%s\""
NO_SUCH_ROOM = "No such room \"%s\"."
HELP = """Usage: .go <room>\r
Moves the user to room <room>."""

import os
import src.messages
from config.config import ROOMS_DIR
from src.userdata import ROOM_FIELD

class Execute:
	def __init__(self,session,message):
		if not message:
			src.messages.Message(session).User(NO_ARGS)
			return
		#decode the room
		go_room=message.split()[0]
		found=0
		for room in os.listdir(ROOMS_DIR):
			if go_room == room:
				found=1
		if found:
			session.user.room.Go(go_room)
			src.messages.Message(session).User(GO_USER % go_room)
			src.userdata.SetField(session.username,ROOM_FIELD,go_room)
		else:
			src.messages.Message(session).User(NO_SUCH_ROOM % go_room)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
