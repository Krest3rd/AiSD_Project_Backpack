from random import randint
from invalid import invalid_integer

def generate_backpack_inputs(mode: str, fixed_value: int, start: int, end: int, step: int) -> None:
    """
    Generates multiple input files for the knapsack problem, supporting two modes:
    - 'capacity': Keeps capacity constant, varies item count.
    - 'amount': Keeps item count constant, varies capacity.

    Args:
        mode (str): 'capacity' or 'amount'.
        fixed_value (int): The fixed value (capacity or amount, depending on mode).
        start (int): The starting value for the variable parameter.
        end (int): The ending value for the variable parameter (inclusive).
        step (int): The increment between values.
    """
    if fixed_value <= 0:
        raise ValueError("Fixed value must be greater than 0")
    if mode not in ("capacity", "amount"):
        raise ValueError("Mode must be 'capacity' or 'amount'")

    for i in range(start, end + 1, step):
        with open(f"./input/backpack_{i:07}.txt", "+w") as f:
            if mode == "capacity":
                capacity = fixed_value
                amount = i
            else:  # mode == "amount"
                capacity = i
                amount = fixed_value
            f.write(f"{capacity}\n")
            f.write(f"{amount}\n")
            for _ in range(amount):
                f.write(f"{randint(1, capacity)} {randint(1, capacity)}\n")


def generate_input():
    while True:
        constant = input("constant>")
        constant = constant.lower()
        if constant not in ("capacity","amount"):
            print("Allowed inputs: 'constant' or 'amount'")
            continue
        break
    while True:
        try:
            value = int(input("fixed-value>"))
            if value <= 0:
                print("fixed-value must be positive")
                continue
            start = int(input("start>"))
            end = int(input("end>"))
            step = int(input("step>"))
            break
        except TypeError:
            invalid_integer(what="Values")
            continue
    generate_backpack_inputs(constant,value,start,end,step)

if __name__ == "__main__":
    generate_input()