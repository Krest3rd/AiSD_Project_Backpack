import sys
from decorations import header, footer, line, print_text_multiline

def invalid_usage():
    header("Correct usage: ./file", pattern="-")
    sys.exit(1)
def invalid_integer():
    header("Values must be integers", pattern="-")

def invalid_command():
    header("INVALID COMMAND", pattern="-", length=43)
    print_text_multiline("Please enter a valid command or type 'help' for assistance.", width=43)
    footer("-",length=43)

def invalid_eof():
    header("Ctrl+D detected. Exiting.", pattern="-")
    sys.exit(1)
    
def invalid_keyboard_interrupt():
    header("Ctrl+C detected. Exiting.", pattern="-")
    sys.exit(0)