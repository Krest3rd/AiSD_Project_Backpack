import random
from backpack import BackpackBrute, BackpackDP
from help import printSolution
from time import process_time

def run():
    # Prompt for knapsack capacity
    while True:
        try:
            capacity = int(input("Enter knapsack capacity C: "))
            if capacity <= 0:
                print("Capacity must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for capacity.")
            return

    # Prompt for number of items
    while True:
        try:
            n = int(input("Enter number of items n: "))
            if n <= 0:
                print("Number of items must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for number of items.")

    # Generate random items
    values = [random.randint(1, 100) for _ in range(n)]
    volumes = [random.randint(1, capacity) for _ in range(n)]

    # Display generated items
    print("\nGenerated items:")
    for i, (p, w) in enumerate(zip(values, volumes), start=1):
        print(f"Item {i}: value={p}, volume={w}")
    print()

    # Choose solution method
    while True:
        choice = input("Choose method ('brute' for brute-force, 'dp' for dynamic programming): ").strip().lower()
        if choice in ("brute", "dp"):
            break
        print("Invalid choice. Please enter 'brute' or 'dp'.")

    # Solve and measure time
    if choice == "brute":
        print("\nBrute Force Solution:")
        t0 = process_time()
        solution = BackpackBrute(capacity, values, volumes)
        t = process_time() - t0
        printSolution(solution)
        print(f"Computation time (brute force): {t:.6f} seconds")
    else:
        print("\nDynamic Programming Solution:")
        t0 = process_time()
        solution = BackpackDP(capacity, values, volumes)
        t = process_time() - t0
        printSolution(solution)
        print(f"Computation time (dynamic programming): {t:.6f} seconds")
