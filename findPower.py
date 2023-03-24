



def Power(a,b,c) :
    for i in range(a,c+2):
        x=pow(i,b)
        print(i,"**",b,"=",x)


x = int(input())
y=int(input())
z=int(input())
Power(x,y,z)