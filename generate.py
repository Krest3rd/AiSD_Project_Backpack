from random import randint

def generate_const_capacity(Capacity: int, start: int, end: int, step: int) -> None:
    """
    Generates multiple input files for the knapsack problem with a constant capacity and varying item counts.
    Each generated file contains:
    - The knapsack capacity on the first line.
    - The number of items on the second line.
    - For each item, a line with two random integers representing the item's weight and value.
    Args:
        Capacity (int): The fixed capacity of the knapsack for all generated files.
        start (int): The starting number of items.
        end (int): The ending number of items (inclusive).
        step (int): The increment between the number of items for each file.
    Files are saved in the './input/' directory with names formatted as 'backpack_{item_count:07}.txt'.
    """
    if Capacity <= 0:
            raise ValueError("Capacity of items has to be grater than 0")


    for i in range(start,end+1,step):
        with open(f"./input/backpack_{i:07}.txt","+w") as f:
            f.write(f"{Capacity}\n")
            f.write(f"{i}\n")
            for _ in range(i):
                f.write(f"{randint(1,Capacity)} {randint(1,Capacity)}\n")

def generate_const_amount(Amount: int, start: int, end: int, step: int) -> None:
    """
    Generates multiple input files for a backpack problem, each containing a specified number of items with random weights and values.
    For each value in the range from `start` to `end` (inclusive) with a given `step`, this function creates a file named
    `backpack_{i:07}.txt` in the `./input/` directory. Each file contains:
      - The current value of `i` (representing, for example, the backpack's capacity) on the first line,
      - The constant number of items (`Amount`) on the second line,
      - Followed by `Amount` lines, each with two random integers between 1 and `i` (inclusive), representing the weight and value of an item.
    Args:
        Amount (int): The number of items to generate for each file.
        start (int): The starting value for the range (inclusive).
        end (int): The ending value for the range (inclusive).
        step (int): The increment between values in the range.
    """
    if Amount <= 0:
        raise ValueError("Amount of items has to be grater than 0")
    
    for i in range(start,end+1,step):
        with open(f"./input/backpack_{i:07}.txt","+w") as f:
            f.write(f"{i}\n")
            f.write(f"{Amount}\n")
            for _ in range(Amount):
                f.write(f"{randint(1,i)} {randint(1,i)}\n")

if __name__ == "__main__":
    generate_const_capacity(10,1,5,2)
    generate_const_amount(10,1,5,2)