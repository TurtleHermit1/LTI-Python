tableNumber=int(input())
tableStartRange=int(input())
tableEndRange=int(input())

for i in range(tableStartRange,tableEndRange+1):
    print(f"{tableNumber} * {i} = {tableNumber*i}")
