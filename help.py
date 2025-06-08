from time import process_time
from collections.abc import Callable

def printSolution(Solution: tuple[int,list[tuple[int,int]]]) -> None:
    """
    Prints out the solution to Knapsack problem as returned by functions in backpack.py
    """

    print("Value\tVolume\n--------------")
    for i in Solution[1]:
        print(i[0],"\t",i[1])
    print("--------------")
    print("Maximum value that can be carried: ", Solution[0])

def benchmark(func: Callable, args: tuple) -> None:

    if not callable(func):
        raise TypeError("func must be a callable (function)")
    
    start = process_time()
    func(args)
    end = process_time()
    return end - start

if __name__=="__main__":
    print("Execution time: ",benchmark(printSolution,(1249,[(14,2), (1235,1)])))