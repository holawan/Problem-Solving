n, money = map(int,input().split())
lst = [int(input()) for _ in range(n)] 
i = 0
while money >0 :
    if money//lst[-1] != 0 :
        i+= money//lst[-1]
        money -= lst[-1]*(money//lst[-1])
    elif money//lst[-2] !=0 :
        i+= money//lst[-2]
        money-= lst[-2]*(money//lst[-2])
    elif money//lst[-3] !=0 :
        i+= money//lst[-3]
        money-= lst[-3]*(money//lst[-3])
    elif money//lst[-4] !=0 :
        i+= money//lst[-4]        
        money-= lst[-4]*(money//lst[-4])
    elif money//lst[-5] !=0 :
        i+= money//lst[-5]
        money-= lst[-5]*(money//lst[-5])
    elif money//lst[-6] !=0 :
        i+= money//lst[-6]
        money-= lst[-6]*(money//lst[-6])
    elif money//lst[-7] !=0 :
        i+= money//lst[-7]
        money-= lst[-7]*(money//lst[-7])
    elif money//lst[-8] !=0 :
        i+= money//lst[-8]
        money-= lst[-8]*(money//lst[-8])
    elif money//lst[-9] !=0 :
        i+= money//lst[-9]
        money-= lst[-9]*(money//lst[-9])
    elif money//lst[0] !=0 :
        i+= money//lst[0]
        money-= lst[0]*(money//lst[0])
print(i)