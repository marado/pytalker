# -*- coding: latin -*-

NO_ARGS = "Who do want to wake up?"
SELF = "It seems to me you are already awake!"
TARGET = "%s wants you to... WAKE UP!!! %s"
TARGET_MSG = "%s whispers to you: %s"
MSG = "You try to WAKE UP %s!"
MSG_MSG = "You whisper to %s: %s"
NO_TARGET = "There's no user named '%s' online."
HELP = """Usage: .wake <user> [<text>]\r
Sends a beep and [<text>] if available privately to the specified user."""

import src.messages

class Execute:
	def __init__(self,session,message):
		self.message = message.split()
		
		if not message: src.messages.Message(session).User(NO_ARGS)
		else:
			if self.message[0].strip().lower() == session.user.name.strip().lower(): src.messages.Message(session).User(SELF)
			elif self.message[0].strip().lower() in session.allusers.userdict:
				src.messages.Message(session).Target(self.message[0].strip().lower(),(TARGET % (session.user.name, "\a")))
                                src.messages.Message(session).User(MSG % session.allusers.userdict[self.message[0].strip().lower()].name)
				if len(self.message) > 1:
					src.messages.Message(session).Target(self.message[0].strip().lower(),(TARGET_MSG % (session.user.name, message[len(self.message[0]) + 1: ])))
					src.messages.Message(session).User(MSG_MSG % (session.allusers.userdict[self.message[0].strip().lower()].name, message[len(self.message[0]) + 1: ]))
			else: src.messages.Message(session).User(NO_TARGET % self.message[0])

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
