# -*- coding: latin -*-

NO_ARGS = "Quem queres acordar?"
SELF = "Estas a dormir ou que?"
TARGET = "=> %s quer que tu... ACORDES!!! %s"
TARGET_MSG = "%s sussurra-te: %s"
MSG = "Tentas ACORDAR %s!"
MSG_MSG = "Tu sussuras a %s: %s"
NO_TARGET = "O '%s' nao esta' online."
HELP = """Uso: .wake <utilizador> [<texto>]\r
Envia um beep e um [<texto>], se ele for apresentado, ao <utilizador>."""

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
