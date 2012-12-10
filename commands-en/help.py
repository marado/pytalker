# -*- coding: latin -*-

TITLE = "- Commands available: --------------------------------"
BODY = " %s"
END = "- End of 'help' command ------------------------------"
TITLE_COMMAND = "- Help for '%s': -------------------------------------"
END_COMMAND = "- End of 'help' command ------------------------------"
LEN = 50
SEPARATOR = " "
NO_COMMAND = "The command '%s' doesn't exist"
NA = "Help for '%s' is not available"
HELP = """Usage: .help [<command (without the '.')>]\r
If command is specified, display's the help of that command,\r
otherwise shows a list of all available commands."""
import src.messages
import os
from config.config import COMMANDS_DIR

class Execute: 
	def __init__(self,session,message):
		self.message = message.strip().lower().split()
		commandlist = []
                for command in os.listdir(COMMANDS_DIR):
                        if not command == "__init__.py" and not command == "command.py":
                                if command.endswith(".py"): commandlist.append(command[:-3])
		
		if not self.message:
			src.messages.Message(session).User(TITLE)
			bigger = 0
			for word in commandlist: 
				if len(word) > bigger: bigger = len(word)

			commands = ""
			for word in commandlist:
				if len(commands) < LEN: commands = commands + word + SEPARATOR + (" " * (bigger - len(word) + len(SEPARATOR)))
				else:
					src.messages.Message(session).User(BODY % commands)
					commands = "" + word + SEPARATOR + (" " * (bigger - len(word) + len(SEPARATOR)))
			src.messages.Message(session).User(BODY % commands)
			src.messages.Message(session).User(END)

		else:
			if not self.message[0] in commandlist: src.messages.Message(session).User(NO_COMMAND % self.message[0])
			else:
                                commandfile = COMMANDS_DIR + "." + self.message[0]
                                commandmodule = __import__(commandfile)
                                components = commandfile.split(".")
                                for component in components[1:]:
                                        commandmodule = getattr(commandmodule, component)
				if not hasattr(commandmodule,'Help'): src.messages.Message(session).User(NA % self.message[0])
				else: 
					src.messages.Message(session).User(TITLE_COMMAND % self.message[0])
					getattr(commandmodule,'Help')(session)
					src.messages.Message(session).User(END_COMMAND)

class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
