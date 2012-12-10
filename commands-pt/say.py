# -*- coding: latin -*-

MSG = "%s diz: %s"
NO_ARGS = "Dizer o que?"
HELP = """Uso: .say <texto>\r
Envia o <texto> para todas as pessoas no talker."""

import src.messages

class Execute:
	def __init__(self,session,message):
		if not message: src.messages.Message(session).User(NO_ARGS)
		else: src.messages.Message(session).All(MSG % (session.user.name, message))

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
