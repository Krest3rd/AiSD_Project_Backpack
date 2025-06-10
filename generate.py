from random import randint
from invalid import invalid_integer, invalid_constant, invalid_eof, invalid_keyboard_interrupt
from decorations import print_text_multiline,line

def generate_backpack_inputs(mode: str, constant_value: int, start: int, end: int, step: int) -> None:
    """
    Generates multiple input files for the knapsack problem, supporting two modes:
    - 'capacity': Keeps capacity constant, varies item count.
    - 'amount': Keeps item count constant, varies capacity.

    Args:
        mode (str): 'capacity' or 'amount'.
        constant_value (int): The fixed value (capacity or amount, depending on mode).
        start (int): The starting value for the variable parameter.
        end (int): The ending value for the variable parameter (inclusive).
        step (int): The increment between values.
    """
    if constant_value <= 0:
        raise ValueError("Constant value must be greater than 0")
    if mode not in ("capacity", "amount"):
        raise ValueError("Mode must be 'capacity' or 'amount'")

    for i in range(start, end + 1, step):
        with open(f"./input/backpack_{i:07}.txt", "+w") as f:
            if mode == "capacity":
                capacity = constant_value
                amount = i
            else:  # mode == "amount"
                capacity = i
                amount = constant_value
            f.write(f"{capacity}\n")
            f.write(f"{amount}\n")
            for _ in range(amount):
                f.write(f"{randint(1, capacity)} {randint(1, capacity)}\n")


def generate_input():
    while True:
        line()
        print_text_multiline("Choose a constant for the knapsack problem: 'capacity' or 'amount'.")
        line()
        try:
            constant = input("constant> ")
            constant = constant.lower()
            if constant not in ("capacity","amount"):
                invalid_constant()
                continue
            break
        except EOFError:   
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return
    while True:
        try:
            value = int(input("constant-value> "))
            if value <= 0:
                invalid_integer(what="constant-value")
                continue
            try:
                start = int(input("start> "))
                end = int(input("end> "))
                step = int(input("step> "))
                break
            except ValueError:
                invalid_integer(what="start, end or step")
                continue
            except EOFError:
                invalid_eof()
                return
            except KeyboardInterrupt:
                invalid_keyboard_interrupt()
                return
        except TypeError:
            invalid_integer(what="Values")
            continue
        except ValueError:
            invalid_integer(what="constant-value")
            continue
        except EOFError:
            invalid_eof()
            return
        except KeyboardInterrupt:
            invalid_keyboard_interrupt()
            return
    generate_backpack_inputs(constant,value,start,end,step)

if __name__ == "__main__":
    generate_input()