import os
from generate import generate_backpack_inputs
from backpack import BackpackBrute, BackpackDP
from help import printSolution
from time import process_time
from invalid import invalid_integer, invalid_command, invalid_eof, invalid_keyboard_interrupt
from decorations import header, footer

def run():
    # Prompt for knapsack capacity
    while True:
        try:
            capacity = int(input("Enter knapsack capacity C:\ncapacity>  "))
            if capacity <= 0:
                invalid_integer(what="Capacity")
                continue
            break
        except ValueError:
            invalid_integer(what="Capacity")
            return
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return

    # Prompt for number of items
    while True:
        try:
            n = int(input("Enter number of items n:\nnumber> "))
            if n <= 0:
                invalid_integer(what="Number of items")
                continue
            break
        except ValueError:
            invalid_integer(what="Number of items")
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return

 
    # Generate and write input file
    os.makedirs("input", exist_ok=True)
    generate_backpack_inputs("capacity", capacity, n, n, 1)
    filename = f"./input/backpack_{n:07}.txt"
    header(f"Input data written to {filename}")

    # Read input data from file
    with open(filename) as f:
        data = f.read().strip().split()
    it = iter(data)
    file_capacity = int(next(it))
    file_n = int(next(it))
    values, volumes = [], []
    for _ in range(file_n):
        p = int(next(it)); w = int(next(it))
        values.append(p); volumes.append(w)

    # Display loaded items
    header("Loaded items from file:")
    for i, (p, w) in enumerate(zip(values, volumes), start=1):
        print(f"Item {i}: value={p}, volume={w}")
    footer()

    # method selection
    while True:
        try:
            choice = input("Choose method \n\tbrute-force (or 'bf')\n\tdynamic-programming (or 'dp')\nmethod> ").strip().lower()
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return
        if choice in ("brute-force","bf","dynamic-programming", "dp"):
            break
        invalid_command()
        
    #timing
    if choice == "brute-force" or choice == "bf":
        header("Brute Force Solution:")
        t0 = process_time()
        solution = BackpackBrute(capacity, values, volumes)
        t = process_time() - t0
        printSolution(solution)
        header(f"Computation time (brute force): {t:.6f} seconds",length=70)
    else:
        header("Dynamic Programming Solution:")
        t0 = process_time()
        solution = BackpackDP(capacity, values, volumes)
        t = process_time() - t0
        printSolution(solution)
        header(f"Computation time (dynamic programming): {t:.6f} seconds",length=64)
