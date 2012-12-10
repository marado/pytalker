# -*- coding: latin -*-

NO_NEWS = "Nao existem noticias."
HELP = """Uso: .news\r
Mostra as noticias do talker."""

import src.messages
from config.config import NEWS_FILE

class Execute:
	def __init__(self,session,message):
		try:
			news = open(NEWS_FILE,mode='r')
			for line in news: session.handler.request.send(line + "\r")
			news.close()
		except IOError: src.messages.Message(session).User(NO_NEWS)

class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
