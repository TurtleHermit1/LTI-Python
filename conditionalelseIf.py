n=int(input("Enter Number"))

if n>0:
    print("Positive", end=" ")
    if n%2==0 :
        print("Even")
    else :
        print("Odd")
    
elif n < 0 :
    print("Negetive", end=" ")

    if n%2==0 :
        print("Even")

    else :
        print("Odd")

else :
    print("Zero")




