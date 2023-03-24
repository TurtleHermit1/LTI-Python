length=int(input())
width=int(input())


lengthIs=0
widthIs=0

# lengthIs=(int(length/8)) if length%8!=0 else 0 
# widthIs=(int(width/8)) if width%8!=0 else 0

if(length%8!=0):
    lengthIs=int(length/8)

if(width%8!=0):
    widthIs=int(width/8)



area=((length*width)/64)-(lengthIs*widthIs)

print(f"{lengthIs*widthIs}\n{int(2*area)}")