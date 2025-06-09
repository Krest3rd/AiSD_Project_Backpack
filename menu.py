import random
from backpack import BackpackBrute, BackpackDP
from help import printSolution
from time import process_time
from invalid import invalid_integer, invalid_command
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

    # Prompt for number of items
    while True:
        try:
            n = int(input("Enter number of items n:\n n> "))
            if n <= 0:
                invalid_integer(what="Number of items")
                continue
            break
        except ValueError:
            invalid_integer(what="Number of items")

    # Generate random items
    values = [random.randint(1, 100) for _ in range(n)]
    volumes = [random.randint(1, capacity) for _ in range(n)]

    # Display generated items
    header("Generated items:")
    for i, (p, w) in enumerate(zip(values, volumes), start=1):
        print(f"Item {i}: value={p}, volume={w}")
    footer()

    # Choose solution method
    while True:
        choice = input("Choose method \n\tbrute-force (or 'bf')\n\tdynamic-programming (or 'dp)\nmethod> ").strip().lower()
        if choice in ("brute-force","bf","dynamic-programming", "dp"):
            break
        invalid_command()

    # Solve and measure time
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
        header(f"Computation time (dynamic programming): {t:.6f} seconds",length=70)
