inValue=list(map(int,input().split(" ")))

fiValue=[]
count=0


for i in range(len(inValue)):
    if inValue[i]!=0:
        fiValue.append(inValue[i])
        count+=1


n1 = int(len(inValue))
n2 = int(len(fiValue))

if n1!=n2:
    for i in range(count,n1):
        fiValue.append(0)

f1=tuple(inValue)
f2=tuple(fiValue)


print(f"Initial Value: {f1}\nFinal value: {f2}")
        



    

    