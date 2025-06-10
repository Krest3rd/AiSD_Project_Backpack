import os
from generate import generate_input
from backpack import BackpackBrute, BackpackDP
from help import printSolution
from time import process_time
from invalid import invalid_integer, invalid_command, invalid_eof, invalid_keyboard_interrupt
from decorations import header, footer


def run():
    input_dir = 'input'
    if os.path.isdir(input_dir):
        for fname in os.listdir(input_dir):
            file_path = os.path.join(input_dir, fname)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(input_dir)
    generate_input()
    try:
        files = sorted(f for f in os.listdir(input_dir) if f.endswith('.txt'))
    except FileNotFoundError:
        header("No 'input' directory found. Generate inputs first.")
        return
    if not files:
        header("No input files found in 'input/'.")
        return

    header("Available input files:")
    for idx, fname in enumerate(files, start=1):
        print(f"{idx}. {fname}")
    footer()
 # Step 3: User selects file
    while True:
        try:
            sel = input("Select file by number> ").strip()
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return
        if not sel.isdigit():
            invalid_integer(what="Selection")
            continue
        idx = int(sel)
        if 1 <= idx <= len(files):
            filename = os.path.join(input_dir, files[idx-1])
            break
        else:
            invalid_command()


    # Step 4: Read selected file
    with open(filename) as f:
        data = f.read().strip().split()
    it = iter(data)
    try:
        capacity = int(next(it))
        n = int(next(it))
    except (StopIteration, ValueError):
        header("Invalid file format.")
        return
    values, volumes = [], []
    for _ in range(n):
        try:
            p = int(next(it)); w = int(next(it))
        except (StopIteration, ValueError):
            header("Invalid item data in file.")
            return
        values.append(p)
        volumes.append(w)

    # Display loaded items
    header(f"Loaded items from '{files[idx-1]}' (Capacity={capacity}, n={n}):")
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
