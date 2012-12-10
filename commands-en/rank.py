# -*- coding: latin -*-

TITLE= """- My rank: -------------------------------------------------------"""
TITLE_LIST= """- The ranks: -----------------------------------------------------"""
TITLE_UMOD= """- Changing the rank: ---------------------------------------------"""
TITLE_UMOD_CHANGED= """- Message from administrator! ------------------------------------"""
BODY = """  %s"""
BODY_LIST = """   %s - %s"""
BODY_LIST_ADM = """   (%s)\t %s - %s"""
BODY_UMOD = """   Changing user %s to rank %s."""
BODY_UMOD_CHANGED = """   your rank was changed to '%s'."""
END_UMOD_CHANGED = """- End of message from administrator. -----------------------------"""
END = """- End of 'rank' command ------------------------------------------"""
HELP = """Usage: .rank [[-l] | -s <user> [<rank>|+<n>|-<n>]]\r
Shows you your current rank.\r
Options:\r
    -l                 shows you all the ranks of the talker.\r
    -s [<nick>] <rank> promote or demote a user to rank <rank>.\r
                       You can use +n or -n to increase or lower by one rank.\r
                       If you omit <nick> then it applies to you."""
NO_SUCH_USER=""" No user with that name""" 
NO_SUCH_RANK=""" No rank with that name""" 
CANT_DO_THAT=""" You can't change your rank, unless you're an administrator."""

import time,os
import src.messages
import config.ranks
from src.userdata import *
from config.config import USERS_DIR

class Execute:
	def __init__(self,session,message):
		self.message=message.split()
		if(len(self.message)==0):
			"""show my rank"""
                	src.messages.Message(session).User(TITLE)
			src.messages.Message(session).User(BODY%session.user.rank.name)
                	src.messages.Message(session).User(END)
		elif(len(self.message)==1):
			"""show list"""
			if(self.message[0]=="-l"):
	                	src.messages.Message(session).User(TITLE_LIST)
				for key in config.ranks.RANKS.keys():
					"""if i'm op, then show the rank names"""
					if(session.user.rank.level==0):
						src.messages.Message(session).User(BODY_LIST_ADM%(key,config.ranks.RANKS[key]['name'],config.ranks.RANKS[key][RANK_FIELD_DESC]))
					else:
						src.messages.Message(session).User(BODY_LIST%(config.ranks.RANKS[key]['name'],config.ranks.RANKS[key][RANK_FIELD_DESC]))
	                	src.messages.Message(session).User(END)
			else:
				Help(session)
				return
		else:
			"""change rank"""
			if(self.message[0]!="-s"):
				Help(session)
				return
			if(len(self.message)==2):
				if(session.user.rank.level==0):
					self.usermod=session.user.name
				else:
					src.messages.Message(session).User(CANT_DO_THAT)
					return
				self.newrank=self.message[1]
			else:
				self.usermod=self.message[1]
				self.newrank=self.message[2]
			#validate user and rank
			name_lst= os.listdir(USERS_DIR)
			if(not self.usermod in os.listdir(USERS_DIR)):
                		src.messages.Message(session).User(NO_SUCH_USER)
				return
			if(not self.newrank in config.ranks.RANKS):
				src.messages.Message(session).User(NO_SUCH_RANK)
				return
			#now you can change the rank.
			#change in the file
			src.userdata.SetField(self.usermod,RANK_FIELD,self.newrank)
			#change if user loged in
			if(session.allusers.userdict.has_key(self.usermod.lower())):
				self.usermod_=session.allusers.Get(self.usermod.lower())
				self.usermod_.rank=src.users.Rank(self.newrank)
				#show the user it has new rank
				if(self.usermod.lower() != session.user.name):
					src.messages.Message(session).Target(self.usermod,TITLE_UMOD_CHANGED)
					src.messages.Message(session).Target(self.usermod,(BODY_UMOD_CHANGED%self.newrank))
					src.messages.Message(session).Target(self.usermod,END_UMOD_CHANGED)
			#show the admin(s) the user was changed
                	src.messages.Message(session).User(TITLE_UMOD)
			src.messages.Message(session).User(BODY_UMOD%(self.usermod,self.newrank))
                	src.messages.Message(session).User(END)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
