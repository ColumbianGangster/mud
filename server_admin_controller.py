from server_admin_commands import QUIT, PERF, QUIT_WITHOUT_SAVE, KICK, HELP, BAN, STATUS, TIME, COMMANDS
from server_admin_command_quit import quit
from server_admin_command_time import time
from server_admin_command_commands import commands
from server_admin_input_parser import get_command_from_input
from switch import Switch

# When adding a new command, first:
# # Add to the switch, below.
# # Add the imports
# # Create a new .py file for the command
# # Add the string to server_admin_commands.py
def invoke_command_on(input):
	for case in Switch(get_command_from_input(input)):
	    if case(QUIT):
	    	quit()
	    	break
	    if case(PERF):
	        break
	    if case(QUIT_WITHOUT_SAVE):
	        break
	    if case(KICK):
	        break
	    if case(HELP):
	        break
	    if case(BAN):
	        print("This will execute a kick ban. It will then be broadcast to the entire server.")
	        break
	    if case(STATUS):
	        print("This will cause the console to print out a partial list of connected clients along with their ping, ip")
	        break
	    if case(TIME):
	        time()
	        break
	    if case(COMMANDS):
	    	commands()
	    	break
	    if case(): # default, could also just omit condition or 'if True'
	        print("Command not found. For information on the commands, type commands")