# -*- coding: latin -*-

NO_ARGS = "Say what, to whom?"
SELF = "Talking to youself?"
MSG = "%s says (to %s): %s"
NO_TARGET = "There's no user name '%s' online."
HELP = """Usage: .sayto <user> <text>\r
Sends <text> to the specified user, all users see the <text>."""

import src.messages

class Execute:
	def __init__(self,session,message):
		self.message = message.split()
		
		if len(self.message) < 2 : src.messages.Message(session).User(NO_ARGS)
		else:
			if self.message[0].strip().lower() == session.user.name.strip().lower(): src.messages.Message(session).User(SELF)
			elif self.message[0].strip().lower() in session.allusers.userdict:
				src.messages.Message(session).All(MSG % (session.user.name, session.allusers.userdict[self.message[0].lower()].name, message[len(self.message[0]) + 1: ]))
			else: src.messages.Message(session).User(NO_TARGET % self.message[0])

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
