num=int(input())
count=0;

if num==0:
    count+=1
else:

    while(num>0):
        count+=1
        num=int(num/10)

print(count)