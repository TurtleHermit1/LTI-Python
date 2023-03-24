flashPerSec=int(input())
print("Enter x and y indicates  x/y of an hour")
x=int(input())
y=int(input())

inSec=(x/y)*60*60;
flash=inSec/flashPerSec
print(f"The light will flash {int(flash+1)} times.")