import sys
from decorations import header, footer, line, print_text_multiline

def invalid_usage():
    header("Correct usage: ./file", pattern="-")
    sys.exit(1)
def invalid_integer(what):
    header(f"{what} must be positive integer", pattern="-")

def invalid_command():
    header("INVALID COMMAND", pattern="-", length=43)
    print_text_multiline("Invalid choice. Enter 'brute-force' or 'bf' for brute-force method. Or Enter 'dynamic-programming' or 'dp' for dynamic programming method.", width=43)
    footer("-",length=43)

def invalid_eof():
    header("Ctrl+D detected. Exiting.", pattern="-")
    sys.exit(1)
    
def invalid_keyboard_interrupt():
    header("Ctrl+C detected. Exiting.", pattern="-")
    sys.exit(0)