# n=int(input())
n=int(input())

evenCount=0
oddCount=0

numIs=list(map(int,input().split(" ")))

for i in range(n):

    if(numIs[i]%2==0):
        evenCount+=1
    else:
        oddCount+=1



print(evenCount,oddCount)



