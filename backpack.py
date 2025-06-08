def BackpackBrute(Capacity: int, Values: list[int], Volume: list[int]) -> tuple[int,list[tuple[int,int]]]:
    """
    This function solves the backpack/knapsack problem using the brute force method
    Maximizes the value of items that can be put into the backpack without going over backpacks capacity

    :param Capacity - maximum capacity of the backpack
    :param Values - list of values of diffrent items
    :param Volume - list of volumes taken up by diffrent items
    :param Amount - amount of items that are being considered

    :returns: tuple of (max value found, list of tuples of (item value, item volume)) returns only one possible combination
    """
    if all(type(i) == int for i in Values):
        return TypeError("Values must be a list of ints")
    
    if all(type(i) == int for i in Volume):
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

        # Pick n-1 item
        if Volume[Amount-1] <= Capacity:
            pick, pick_items = BackpackBrute(Capacity - Volume[Amount-1], Values, Volume, Amount-1)
            pick += Values[Amount-1]
            pick_items.append((Values[Amount-1],Volume[Amount-1]))

        # Don't pick n-1 item
        noPick, noPick_items = BackpackBrute(Capacity, Values, Volume, Amount-1)

        if pick >= noPick:
            return (pick,pick_items)
        else:
            return (noPick,noPick_items)
    
    return BackpackBruteRec(Capacity, Values, Volume, len(Values))


if __name__ == "__main__":
    print(BackpackBrute(5, [1,2,3,4,5], [5,4,3,2,1]))
    