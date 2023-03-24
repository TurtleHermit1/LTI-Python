info=input()

def toLis(s):
    lis=list(s.split(","))
    
    return lis

l=toLis(info)

print(f"Door-no: {l[0]}")
print(f"Street: {l[1]}")
print(f"Area: {l[2]}")
print(f"City: {l[3]}")
print(f"State: {l[4]}")
print(f"Zipcode: {l[5]}")
print(f"Country: {l[6]}")


