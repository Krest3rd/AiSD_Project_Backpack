#!/usr/bin/env python3
import sys
import menu

def main():
    if len(sys.argv) > 1:
        print("Usage: python main.py")
        sys.exit(1)
    menu.run()

if __name__ == "__main__":
    main()