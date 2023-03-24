num=int(input())
count=0;

while (num>0):
    
    if int(num%10)==4:        
        count+=1
    num=(num/10)   


print(count)
