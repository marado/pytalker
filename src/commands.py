# -*- coding: latin -*-

import messages
import time,os
from config.messages import COMMANDS_EMPTY,COMMANDS_NA,MESSAGE,MESSAGE_EMPTY,COMMANDS_MULTIMATCH 
from config.config import COMMANDS_DIR,COMMANDS_EXCEPTIONS

class Command:
	def __init__(self,session,handler,message):
		commandlist = []
		for command in os.listdir(COMMANDS_DIR):
  			if not command in COMMANDS_EXCEPTIONS and command.endswith(".py"): commandlist.append(command[:-3])

		if session.login: session.user.time = time.time()
		
		message = message.strip()
		
		if message.startswith("."):	
			command = message.split()[0]
			command = command[1: ].lower()
			message = message[len(command) + 2: ]
			
			#empty command
			if command == "":
				messages.Message(session).User(COMMANDS_EMPTY)
				return
			#command completion
			cmd_match=[]
			for cmd in commandlist:
				#break if matches exactly
				if cmd == command:
					cmd_match = [ cmd ]
					break
				if cmd.startswith(command): cmd_match.append(cmd)
			if len(cmd_match)==1:
				command=cmd_match[0]
			elif len(cmd_match)>1:
				messages.Message(session).User(COMMANDS_MULTIMATCH % cmd_match )
				return
			#use command or command not available
			if command in commandlist: 
				commandfile = COMMANDS_DIR + "." + command
				commandmodule = __import__(commandfile)
				components = commandfile.split(".")
				for component in components[1:]: commandmodule = getattr(commandmodule, component)
				getattr(commandmodule,'Execute')(session,message)
			else: messages.Message(session).User(COMMANDS_NA % command)
		else:
			#its a .say
			if message: messages.Message(session).Room(MESSAGE % (session.user.name, message))
