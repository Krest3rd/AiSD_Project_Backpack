#!/usr/bin/env python3
import sys
import menu
from invalid import invalid_usage

def main():
    if len(sys.argv) > 1:
        invalid_usage()
        sys.exit(1)
    menu.run()

if __name__ == "__main__":
    main()