num=int(input())
max=int(input())
l=[]

for i in range(num):
    ls=[]
    regId=input();
    numId=input()
    reg=input()
    name=input()
    state=input()
    ls.extend((regId, numId, reg, name, state))
    l.append(ls)

print("Reg.no: chassis no: engine no: owner name: address:")
for i in l:
    print(i[0],i[1],i[2],i[3],i[4])
