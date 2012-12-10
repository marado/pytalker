# -*- coding: latin -*-

HELP = """Usage: .version\r
Shows you the talker version."""

import src.messages
from config.messages import TALKER_VERSION

class Execute:
	def __init__(self,session,message): self.messages = src.messages.Message(session).User(TALKER_VERSION)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
