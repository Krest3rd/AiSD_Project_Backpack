def BackpackBrute(Capacity: int, Values: list[int], Volume: list[int]) -> tuple[int,list[tuple[int,int]]]:
    """
    Solves the 0/1 Knapsack (Backpack) problem using dynamic programming.
    Given a maximum capacity, a list of item values, and a list of item volumes (weights),
    determines the maximum total value that can be carried in the backpack without exceeding
    the capacity. Returns both the maximum value and the list of selected items.

    Parameters:
        Capacity - maximum capacity of the backpack
        Values - list of values of diffrent items
        Volume - list of volumes taken up by diffrent items

    Returns:
        tuple[int, list[tuple[int, int]]]: A tuple containing:
            - The maximum total value achievable.
            - A list of tuples, each representing a selected item as (value, volume).
    
    Raises:
        TypeError: If Values or Volume are not lists of integers.
        ValueError: If Values and Volume have different lengths or Capacity is negative.
    """
    # Check if params are correct
    if not(all(type(i) == int for i in Values)):
        return TypeError("Values must be a list of ints")
    
    if not(all(type(i) == int for i in Volume)):
        return TypeError("Volume must be a list of ints")

    if len(Values) != len(Volume):
        raise ValueError("Values and Volume must be the same length")
    
    if Capacity < 0:
        raise ValueError("Capacity cannot be negative")
    
    # Function that recursively checks every option
    def BackpackBruteRec(Capacity: int, Values: list[int], Volume: list[int], Amount: int) -> tuple[int,list[tuple[int,int]]]:
        # Checked all items or filled the backpack
        if Amount==0 or Capacity ==0:
            return (0,[])
        
        pick = 0
        pick_items = []

        # Pick Amount-1 item
        if Volume[Amount-1] <= Capacity:
            pick, pick_items = BackpackBruteRec(Capacity - Volume[Amount-1], Values, Volume, Amount-1)
            pick += Values[Amount-1]
            pick_items.append((Values[Amount-1],Volume[Amount-1]))

        # Don't pick Amount-1 item
        noPick, noPick_items = BackpackBruteRec(Capacity, Values, Volume, Amount-1)

        if pick >= noPick:
            return (pick,pick_items)
        else:
            return (noPick,noPick_items)
    
    return BackpackBruteRec(Capacity, Values, Volume, len(Values))


def BackpackDP(Capacity: int, Values: list[int], Volume: list[int]) -> tuple[int,list[tuple[int,int]]]:
    """
    Solves the 0/1 Knapsack (Backpack) problem using dynamic programming.
    Given a maximum capacity, a list of item values, and a list of item volumes (weights),
    determines the maximum total value that can be carried in the backpack without exceeding
    the capacity. Returns both the maximum value and the list of selected items.
    Parameters:
        Capacity (int): The maximum capacity of the backpack.
        Values (list[int]): A list of integer values for each item.
        Volume (list[int]): A list of integer volumes (weights) for each item.
    Returns:
        tuple[int, list[tuple[int, int]]]: A tuple containing:
            - The maximum total value achievable.
            - A list of tuples, each representing a selected item as (value, volume).
    Raises:
        TypeError: If Values or Volume are not lists of integers.
        ValueError: If Values and Volume have different lengths or Capacity is negative.
    """

    # Check if params are correct
    if not(all(type(i) == int for i in Values)):
        return TypeError("Values must be a list of ints")
    
    if not(all(type(i) == int for i in Volume)):
        return TypeError("Volume must be a list of ints")

    if len(Values) != len(Volume):
        raise ValueError("Values and Volume must be the same length")
    
    if Capacity < 0:
        raise ValueError("Capacity cannot be negative")
    
    Amount = len(Values)
    Table = [[0 for _ in range(Capacity+1)] for _ in range(Amount+1)]

    for item in range(1,Amount+1):
        for cap in range(1,Capacity+1):
            pick = 0

            # If you pick the item
            if Volume[item-1] <= cap:
                pick = Values[item-1] + Table[item-1][cap - Volume[item - 1]]

            # If you don't pick the item
            notPick = Table[item-1][cap]

            # Pick best of the 2 options
            Table[item][cap] = max(pick,notPick)

    # Reverse the solution from the table
    def SolutionFromTable(Table):
        item = len(Table)-1
        cap = len(Table[0])-1
        pickedItems = []
        while Table[item][cap] != 0:
            # If condition is met that means that item was used in the solution
            if Table[item][cap] > Table[item-1][cap]:
                pickedItems.append((Values[item-1],Volume[item-1]))
                cap -= Volume[item-1]
            item -= 1
        return pickedItems


    return (Table[-1][-1],SolutionFromTable(Table))


# Example usage
if __name__ == "__main__":
    print(BackpackBrute(3, [1,2,3,4,5], [5,4,3,2,1]))
    print(BackpackDP(3, [1,2,3,4,5], [5,4,3,2,1]))