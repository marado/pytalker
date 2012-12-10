# -*- coding: latin -*-

NO_ARGS = "Contar o que a quem?"
SELF = "A falar contigo proprio?"
TARGET = "%s conta-te: %s"
MSG = "Tu contas a %s: %s"
NO_TARGET = "O '%s' nao esta' online."
HELP = """Uso: .tell <utilizador> <texto>\r
Envia o <texto> ao <utilizador> de forma privada."""

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
