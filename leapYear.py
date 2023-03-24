yearIs=int(input())

def leapYear(year):
    if yearIs%400==0:
        return True
    
    if yearIs%100==0:
        return False
    
    if yearIs%4==0:
        return True
    return False
    

if leapYear(yearIs):
    print(f"{yearIs} is a leap year")

else:
    print(f"{yearIs} is not a leap year")
    



    