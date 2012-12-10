# -*- coding: latin -*-

NO_ARGS = "Emote what, to whom?"
SELF = "Emoting to youself?"
TARGET = "Privately, %s %s"
MSG = "To %s, you %s"
NO_TARGET = "There's no user name '%s' online."
HELP = """Usage: .pemote <user> <emotion>\r
Sends <emotion> privately to the specified user."""

import src.messages

class Execute:
	def __init__(self,session,message):
		self.message = message.split()
		
		if len(self.message) < 2 : src.messages.Message(session).User(NO_ARGS)
		else:
			if self.message[0].strip().lower() == session.user.name.strip().lower(): src.messages.Message(session).User(SELF)
			elif self.message[0].strip().lower() in session.allusers.userdict:
				src.messages.Message(session).Target(self.message[0].strip().lower(),(TARGET % (session.user.name, message[len(self.message[0]) + 1: ])))
                                src.messages.Message(session).User(MSG % (session.allusers.userdict[self.message[0].strip().lower()].name, message[len(self.message[0]) + 1: ]))
			else: src.messages.Message(session).User(NO_TARGET % self.message[0])

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
