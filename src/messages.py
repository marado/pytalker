# -*- coding: latin -*-

import socket
import src.messages

class Message:
	def __init__(self,session): 
		self.handler = session.handler
		self.allusers = session.allusers
		self.session = session
		
	def Prompt(self,message): 
		try: self.handler.request.send(message)
		except socket.error:
			self.session.logged = 0
			self.session.Logout()
			del self.session

	def User(self,message): 
		try: self.handler.request.send("%s\n\r" % message)
		except socket.error:
			self.session.logged = 0
			self.session.Logout()
			del self.session

	def Room(self,message): 
		for user in self.allusers.userdict.copy():
			if self.allusers.userdict[user].room.name == self.session.user.room.name:
				self.allusers.userdict[user].messages.User(message)

	def All(self,message): 
		for user in self.allusers.userdict.copy(): self.allusers.userdict[user].messages.User(message)

	def Target(self,target,message): self.allusers.userdict[target].messages.User(message)
