def printSolution(Solution: tuple[int,list[tuple[int,int]]]) -> None:
    print("Value\tVolume\n--------------")
    for i in Solution[1]:
        print(i[0],"\t",i[1])
    print("--------------")
    print("Maximum value that can be carried: ", Solution[0])

printSolution((1249,[(14,2), (1235,1)]))