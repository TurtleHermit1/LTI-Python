liftFloor=int(input())
floor1=int(input())
floor2=int(input())
floor3=int(input())

common1=abs(liftFloor-floor1)
common2=abs(liftFloor-floor2)
common3=abs(liftFloor-floor3)

if floor1<floor2<floor3:
    if common1<common3 and common1<common2:
        print(floor1)

    elif common2<common1 and common2<common3:
        print(floor2)

    elif common3<common1 and common3<common2:
        print(floor3)

    elif common1==common2:
        if liftFloor<floor1:
            print(floor1)
        else:
            print(floor2)

    elif common2==common3:
        if liftFloor<common2:
            print(floor2)
        else:
            print(floor3)

    elif common3==common1:
        if liftFloor<floor3:
            print(floor3)
        else:
            print(floor1)
        


    
        
    
    
    
    
    








