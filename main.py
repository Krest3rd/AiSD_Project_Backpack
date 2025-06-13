#!/usr/bin/env python3
import sys
import menu
from invalid import invalid_usage

def main():
    if (len(sys.argv) != 2 or sys.argv[1] not in ("--user", "--file")):
        invalid_usage()
        sys.exit(1)
    if sys.argv[1] == "--user":
        menu.run("user")
    elif sys.argv[1] == "--file":
        menu.run("file")

if __name__ == "__main__":
    main()