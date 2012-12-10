# -*- coding: latin -*-

NO_MOTD = "Este talker nao tem motd"
MOTD_NA = "O ficheiro de motd deste talker nao esta' disponivel."
HELP = """Uso: .motd\r
Mostra-te a mensagem do dia do talker."""

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
