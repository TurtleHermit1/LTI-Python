
num=list(map(int,input("Enter the numbers\n").split(" ")))
n=int(len(num))

evenLs=[]
oddLs=[]




for i in range(n):
    
    if num[i]%2==0:
        evenLs.append(num[i])
    else:
        oddLs.append(num[i])



print(f"Even the numbers from the list:\n{evenLs}\nOdd numbers from the list:\n{oddLs}")




