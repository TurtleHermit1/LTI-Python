# n=int(input("Enter the number"))
# l=[]


# for i in range(n):
#     num=int(input())
#     l.append(num)


# print(l)

totalAmount=int(input("Enter the total amount\n"))
# print()
numberOfDays=int(input("Enter the number of days\n"))

enterTheCost=int(input("Enter the cost of 1 litre of milk\n"))

lis=[]
count=0
print(f"Amount of milk Shruthi will buy for {numberOfDays} days is:\n")

for i in range(numberOfDays):
    num=int(input())
    count+= num*enterTheCost


print(f"Remaining amount with Shruthi is:{totalAmount-count}\n")




