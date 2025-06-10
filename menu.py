from backpack import BackpackBrute, BackpackDP
from help import printSolution, benchmark
from time import process_time
from invalid import invalid_command, invalid_eof, invalid_keyboard_interrupt, invalid_usage
from decorations import header, footer
from input import file_handler, user_input


def run(input_type: str = "file") -> None:
    if input_type not in ("file", "user"):
        invalid_usage()
        return
    
    if input_type == "file":
        capacity, values, volumes = file_handler()
    else:
        capacity, values, volumes = user_input()

    # Display loaded items
    header(f"Items list (Capacity={capacity}, Amount={len(values)}):")
    print("Value\tVolume")
    for i, (p, w) in enumerate(zip(values, volumes), start=1):
        print(f"{p}\t{w}")
    footer()

    # Step 5: Method selection
    while True:
        try:
            choice = input("Choose method:\n  brute-force (bf)\n  dynamic-programming (dp)\nmethod> ").strip().lower()
        except EOFError:
            invalid_eof(); return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt(); return
        if choice in ("brute-force", "bf", "dynamic-programming", "dp"):
            break
        invalid_command()

    # Step 6: Solve and time
    if choice in ("brute-force", "bf"):
        header("Brute Force Solution:")
        t0 = process_time()
        sol = BackpackBrute(capacity, values, volumes)
        t = process_time() - t0
        printSolution(sol)
        header(f"Computation time (brute force): {t:.6f} seconds", length=70)
    else:
        header("Dynamic Programming Solution:")
        t0 = process_time()
        sol = BackpackDP(capacity, values, volumes)
        t = process_time() - t0
        printSolution(sol)
        header(f"Computation time (dynamic programming): {t:.6f} seconds", length=70)
