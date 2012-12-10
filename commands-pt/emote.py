# -*- coding: latin -*-

MSG = "%s %s"
NO_ARGS = "Estas muito emotivo, mas queres fazer o que?"
HELP = """Uso: .emote <emocao>\r
Mostra uma <emocao> para todos aqueles que estao no talker."""

import src.messages

class Execute:
	def __init__(self,session,message):
		if not message: src.messages.Message(session).User(NO_ARGS)
		else: src.messages.Message(session).All(MSG % (session.user.name, message))

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
