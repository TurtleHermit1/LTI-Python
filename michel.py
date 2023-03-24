num = int(input())
lis=list()
count=0

lis=list(map(int,input().split(" ")))


lis.sort()
for i in range(int(num-1)):
    if lis[i]==lis[i+1]:
        count+=1


print(len(lis)-count)
