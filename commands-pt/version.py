# -*- coding: latin -*-

HELP = """Uso: .version\r
Mostra-te a versao do talker."""

import src.messages
from config.messages import TALKER_VERSION

class Execute:
	def __init__(self,session,message): self.messages = src.messages.Message(session).User(TALKER_VERSION)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
