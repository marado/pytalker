# -*- coding: latin -*-

import messages,users,string,userdata,rooms
import commands
import os
from config.config import *
from config.messages import *
from config.ranks import DEFAULT_RANK
from src.userdata import RANK_FIELD
import socket
import hashlib

# This class registers each session. 
# That includes logging in each user.

class Session:
	def __init__(self,handler):
		self.handler = handler
		self.allusers = users.All()
		messages.Message(self).Prompt(LOGIN_PROMPT)
		self.username = self.Input().strip()
		if "\xff" in self.username: self.username = self.username[21: ]
		self.login = 0
		while (not self.username or not self.username.isalnum() or len(self.username) > LOGIN_MAX_LENGTH or (self.username.lower() in LOGIN_COMMANDS)):
			if not self.username: messages.Message(self).User(LOGIN_EMPTY)
			elif not self.username.isalnum(): messages.Message(self).User(LOGIN_ALNUM_ERROR)
			elif len(self.username) > LOGIN_MAX_LENGTH: messages.Message(self).User(LOGIN_LENGTH_ERROR % LOGIN_MAX_LENGTH)
			else: self.Process("." + self.username.lower())
			messages.Message(self).Prompt(LOGIN_PROMPT)
			self.username = self.Input().strip()
		if self.username.lower() == LOGIN_QUIT: self.logged = 0	
		else: 
			# CheckUser returns 1 if the guy is getting here for the first time
			newuser = self.CheckUser()
			# And we tell that to Login
			self.logged = self.Login(newuser)

	"""Only check for password."""
	def CheckUser(self):
		userlist = []
		for user in os.listdir(USERS_DIR):
			userlist.append(user)

		if self.username.lower() in userlist:
			# User is registred, let's check his password.
			realpassword = userdata.GetField(self.username.lower(),'passwd')
			self.handler.request.send(PASSWORD_PROMPT)
			self.password = self.Input().strip()
			if "\xff" in self.password: self.password = self.password[21: ]
			while (not hashlib.sha512(self.password).hexdigest() == realpassword):
				self.handler.request.send(PASSWORD_WRONG)
				self.handler.request.send(PASSWORD_PROMPT)
				self.password = self.Input().strip()
				if "\xff" in self.password: self.password = self.password[21: ]
			return 0
		else:
			# This user is not registred, let's register him
			self.handler.request.send(PASSWORD_CHOOSE)
			self.password = self.Input().strip()
			if "\xff" in self.password: self.password = self.password[21: ]
			userdata.SetField(self.username,'passwd',hashlib.sha512(self.password).hexdigest())
			userdata.SetField(self.username,'rank',DEFAULT_RANK)
			#
			return 1
	def Login(self, newuser):
		# CLS: both techniques since some telnet clients are less strict than others
		messages.Message(self).User(CLS)
		if (RULES_SHOW and (newuser == 1)):
			try:
				rules = open(RULES_FILE,mode='r')
                        	for line in rules: self.handler.request.send(line + "\r")
                        	rules.close()
				if RULES_SHOW == 2:
					messages.Message(self).Prompt(RULES_PROMPT)
                			acceptrules = self.Input().strip().lower()
					while (not acceptrules == RULES_ACCEPT.lower() and not acceptrules == RULES_DECLINE.lower()): 
						messages.Message(self).User(RULES_HELP % (RULES_ACCEPT, RULES_DECLINE))
						messages.Message(self).Prompt(RULES_PROMPT)
						acceptrules = self.Input().strip().lower()
					if acceptrules == RULES_DECLINE.lower(): return 0
			except IOError: self.handler.request.send("")	
		if MOTD_SHOW:
			try:
				motd = open(MOTD_FILE,mode='r')
				for line in motd: self.handler.request.send(line + "\r")
				motd.close()
				messages.Message(self).Prompt(MOTD_PROMPT)
			except IOError: self.handler.request.send("")
		motdprompt = self.Input().strip()
		newuser = 1
		#replace any old session. TODO: (is it working properly?)
		if self.allusers.userdict.has_key(self.username.lower()):
			newuser = 0
			olduser = self.allusers.Get(self.username.lower())
			olduser.session.logged = 0
			del(olduser.handler)
			del(olduser.session)
		#rank
		rank=userdata.GetField(self.username.lower(),RANK_FIELD)
		if(rank == ''): rank=DEFAULT_RANK
		#add it to the list
		self.user = users.User(self,self.handler,self.username,rank)
		self.allusers.Add(self.user)
		if (newuser == 1): messages.Message(self).All(SESSION_CONNECT % self.user.name)
		self.login = 1
		return 1

	def Logout(self):
		#leave
		self.allusers.Del(self.user)
		messages.Message(self).All(SESSION_DISCONNECT % self.user.name)
		self.logged = 0
		del(self.user)

	def Input(self):
		try:
			message = self.handler.request.recv(TALKER_BLOCK_SIZE)
			if message == "": return ""
			elif message.endswith("\n"): return self.CheckPrintable(message) + "\n"
			else: return self.CheckPrintable(message) + self.Input()
		except socket.error:
			self.logged = 0
			del self

	def CheckPrintable(self, message):
		printablemessage = ""
		for char in message.strip():
			if (char in string.printable or char in "áãàäâåéèëêíìïîóòõôöúùûü"): printablemessage = printablemessage + char
		return printablemessage

	def Process(self,message): commands.Command(self,self.handler,message)
