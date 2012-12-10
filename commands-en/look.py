# -*- coding: latin -*-

MSG = "You are in room \"%s\""
HELP = """Usage: .look\r
Shows you the room where you are."""

import src.messages

class Execute:
	def __init__(self,session,message):
		src.messages.Message(session).User(MSG % session.user.room.name )

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)

