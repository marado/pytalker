# -*- coding: latin -*-

ENTER_ROOM = "You are entering room \"%s\"\r"

import common,time
import src.messages
import src.rooms
from config.ranks import *

class User:
	def __init__(self,session,handler,name,rank):
		self.session = session
		self.handler = handler
		self.name = name
		self.rank = Rank(rank)
		self.room = src.rooms.Room(session)
		self.time = time.time()
		self.messages = src.messages.Message(session)
		src.messages.Message(session).User(ENTER_ROOM % self.room.name)

class All (common.Common):
	def __init__(self):
		common.Common.__init__(self)
		if not hasattr(self,'userdict'): self.userdict = {}
    
	def Add(self,user): self.userdict[user.name.lower()] = user
    
	def Del(self,user): del(self.userdict[user.name.lower()])

	def Get(self,username): return(self.userdict[username.lower()])

class Rank:
	def __init__(self,rank):
		if(not rank.isalpha()):
			rank=DEFAULT_RANK
		self.key=rank
		self.name=RANKS[rank]['name']
		self.level=RANKS[rank]['level']

