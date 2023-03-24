isSet1=set(map(int,input().split(",")))
isSet2=set(map(int,input().split(",")))

lis=list()

if isSet1==isSet2:
    print("Invalid")
else:
       
    lis=isSet1.symmetric_difference(isSet2)

    li=[]

    for i in lis:
        li.append(i)

    li=li.sort()
    l=str(li)
    l=l.replace(' ','')
    l=l.replace('[','{')
    l=l.replace(']','}')
    print(l)
    


# for i in isSet1:
#     if((isSet2.count(i))<=0):
#         lis.append(i)

# for i in isSet2:
#     if((isSet1.count(i))<=0):
#         lis.append(i)

# l=[]

# for i in lis:
#     l.append(i)


# l=str(lis)
# l=l.replace(' ','')
# l=l.replace('[','{')
# l=l.replace(']','}')
# print(l)