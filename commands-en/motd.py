# -*- coding: latin -*-

NO_MOTD = "This talker has no motd"
MOTD_NA = "The motd file for this talker is not available."
HELP = """Usage: .motd\r
Shows you the talker's message of the day."""

import src.messages
from config.config import MOTD_SHOW, MOTD_FILE

class Execute:
	def __init__(self,session,message):
                if MOTD_SHOW:
                        try:
                                motd = open(MOTD_FILE,mode='r')
                                for line in motd: session.handler.request.send(line + "\r")
                                motd.close()
                        except IOError: src.messages.Message(session).User(MOTD_NA)
		else: src.messages.Message(session).User(NO_MOTD)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
