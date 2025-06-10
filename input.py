import os
from decorations import header, footer
from invalid import invalid_integer, invalid_command, invalid_eof, invalid_keyboard_interrupt

def file_handler() -> tuple[int, list[int], list[int]]:
    """
    Handles file input for the knapsack problem.
    Reads a file from the 'input' directory, extracts the capacity, number of items,
    and their values and volumes. Returns these as a tuple.
    Returns:
        tuple[int, list[int], list[int]]: A tuple containing:
            - Capacity (int): The maximum capacity of the knapsack.
            - Values (list[int]): A list of item values.
            - Volumes (list[int]): A list of item volumes (weights).
    Raises:
        FileNotFoundError: If the 'input' directory does not exist.
        ValueError: If the file format is invalid or contains non-integer values.
    """
    input_dir = 'input'
    try:
        print(os.listdir(input_dir))
        files = sorted(f for f in os.listdir(input_dir) if f.endswith('.txt'))
    except FileNotFoundError:
        header("No 'input' directory found. Generate inputs first using generate.py.")
        return
    if not files:
        header("No input files found in 'input/'. Generate inputs first using generate.py.")
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

    return capacity, values, volumes

def user_input() -> tuple[int, list[int], list[int]]:
    """
    Handles user input for the knapsack problem.
    Prompts the user to enter the capacity, number of items, and their values and volumes.
    Returns these as a tuple.
    Returns:
        tuple[int, list[int], list[int]]: A tuple containing:
            - Capacity (int): The maximum capacity of the knapsack.
            - Values (list[int]): A list of item values.
            - Volumes (list[int]): A list of item volumes (weights).
    Raises:
        ValueError: If the input format is invalid or contains non-integer values.
    """
    while True:
        try:
            capacity = int(input("Enter capacity> "))
            if capacity <= 0:
                invalid_integer(what="Capacity")
                continue
            break
        except ValueError:
            invalid_integer(what="Capacity")
            continue
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return

    while True:
        try:
            n = int(input("Enter number of items> "))
            if n <= 0:
                invalid_integer(what="Number of items")
                continue
            break
        except ValueError:
            invalid_integer(what="Number of items")
            continue
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return

    values, volumes = [], []
    for i in range(n):
        while True:
            try:
                p, w = map(int, input(f"Enter value and volume for item {i+1} (space-separated)> ").split())
                if p <= 0 or w <= 0:
                    raise ValueError("Values and volumes must be positive integers.")
                values.append(p)
                volumes.append(w)
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
            except EOFError:
                invalid_eof()
                return
            except KeyboardInterrupt:
                invalid_keyboard_interrupt()
                return

    return capacity, values, volumes
