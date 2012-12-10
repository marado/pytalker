# -*- coding: latin -*-

MSG = "%s %s"
NO_ARGS = "Emote what?"
HELP = """Usage: .emote <emotion>\r
Shows an <emotion> to all the users in the talker."""

import src.messages

class Execute:
	def __init__(self,session,message):
		if not message: src.messages.Message(session).User(NO_ARGS)
		else: src.messages.Message(session).Room(MSG % (session.user.name, message))

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
