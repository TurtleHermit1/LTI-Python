n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n=int(input())


if n>=(n1+n2+n3+n4):
    print("EXIT")

elif(n<n1):
    print("B1") 

elif(n>=n1 and n<(n1+n2)):
    print("B2")

elif(n>=(n1+n2) and n<(n1+n2+n3)):
    print("B3")

elif(n>=(n1+n2+n3) and n<(n1+n2+n3+n4)):
    print("B4")
