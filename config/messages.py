# -*- coding: latin -*-

"""This is the file which contains the messages displayed to users"""

# GENERAL TALKER MESSAGES
### This is the version of the talker with all the information.
TALKER_VERSION = """PyTalker v0.1.12 - http://talkerspt.no-ip.org/~tip/projects/pytalker/\r
\r
Made by:\r
	Mind Booster Noori 	marcos.marado@sonae.com\r
	Daniel Alexandre 	dfcruz@student.dei.uc.pt\r
	Jose Martins 		jemart@student.dei.uc.pt\r
\r
Based on:\r
	python-talk v0.001 	http://talk.sf.net"""

### Message displayed when the talker is started. The %s refers to the 
### the port where the talker is running, configured in config/config.py.
TALKER_STARTED = """\n\rThe talker is now running.\r
Listening for incoming connections on port %s.\r
The Process ID for this talker is: %s."""
### Message displayed when the talker can't be started because the port
### defined in config/config.py is already in use.
TALKER_PORT_IN_USE = """\n\rCan't bind socket, port %s is already in use.\r
Please wait until it gets free or change the port in the config/config.py file."""
### Message displayed when the talker is stopped (ex: when using ctrl+c)
TALKER_STOPPED = """\n\rThe talker has been stopped.\r
REASON: %s"""
### Message sent to server.Stop() when using ctrl+c.
TALKER_CTRL_C = "Interrupt Key (CTRL+C?) pressed."

# LOGIN SCREEN
### This is the message displayed to users who connect to the talker.
### It waits for the users to type in their name.
LOGIN_PROMPT = "Enter your name: "
### This is the message that appears if a user pressed the [enter] key
### without giving a name.
LOGIN_EMPTY = """You must enter your name or:\r
'who' - to see who's online\r
'version' - to see the talker's version\r
'rules' - to view the talker's rules\r
'quit' - to quit the talker"""
### This is the message that appears if a user tries to use a
### non-alphanumeric username.
LOGIN_ALNUM_ERROR = "Your name must be alphanumeric (letters and numbers only)"
### This is the message that appears if a user tries to use a name that
### is already in use.
LOGIN_IN_USE = "That name is already in use, please choose another."
### This is the message that appears if a user tries to use a name with
### more characters than the permitted (configurable in config.py file).
### The %s refers to the maximum number of characters permitted
### (LOGIN_MAX_LENGTH in config.py file).
LOGIN_LENGTH_ERROR = "Your name must be lower that %s characters"
### Asking for a password...
PASSWORD_PROMPT = "Password: "
### User is trying the wrong password
PASSWORD_WRONG = "Wrong password, try again!\n\r"
### User has to choose a password
PASSWORD_CHOOSE = "You're new here... Let's register you!\r\nChoose a password: "

# SESSION
### This is the message that is displayed to all the users in the talker
### when someone connects. 
### The %s refers to the user who has just connected to the talker.
SESSION_CONNECT = "Enters: %s"
### This is the message that is displayed to all the users in the talker
### when someone disconnects.
### The %s refers to the user who has just disconnected from the talker.
SESSION_DISCONNECT = "Leaves: %s"

# COMMANDS
### This is the message that appears if a user types a '.' without anything 
### else.
COMMANDS_EMPTY = "In this talker, commands start with a '.'. You typed a '.' at the beginning of the text but didn't specify the command to execute. If you intented to write the text including the leading '.' please use .say 'text'"
### This is the message that appears if a user tries to use a commands that 
### is not available.
### The %s refers to the command typed by the user (without the '.').
COMMANDS_NA = "The command '%s' doens't exist."
### This is the text it appears after the command completion saying it
### has several options.
COMMANDS_MULTIMATCH = "The abreviation matches several commands %s."

# MESSAGE EXCHANGE
### This is the text that is displayed to all users in the talker if anyone
### types a message that isn't a command. 
### The first %s refers to the user who typed the text, and the second %s
### refers to the message typed.
MESSAGE = "%s says: %s"
### This is the text that is displayed to the user if it typed only [enter]
### without any other text.
MESSAGE_EMPTY = "Say what?"

# RULES SYSTEM
### This is the message displayed to the user after reading the rules.
### It waits for the user to accept or decline the rules. If declined, the
### user will be disconnected. For this enforcement option to be available
### you must set RULES_SHOW = 2 in the config.py file.
RULES_PROMPT = "Do you accept the rules? "
### This is the message displayed to the user if he didn't typed the correct
### string to accept or decline de rules.
### The first %s refers to the string the user has to type to accept the rules
### (RULES_ACCEPT in config.py file), the second %s refers to the string the
### user has to type to decline the rules (RULES_DECLINE in config.py file).
### For this option to be available you must set RULES_SHOW = 2 in the 
### config.py file.
RULES_HELP = """You must type:\r
(case insensitive)\r
'%s' - You accept the rules.\r
'%s' - You decline the rules. You quit the talker."""

# MOTD SCREEN
### This is the message displayed to the user after reading the motd.
### It waits for the user to type [enter] to continue with the login
### method.
MOTD_PROMPT = "Press [Enter] to continue..."

# CLS
#### This is what it's printed to the user when we're trying to clean his screen
CLS = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\x01"
