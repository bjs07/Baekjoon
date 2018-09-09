
def Three(num):
    global sum
    sum=sum+1
    return num//3

def Two(num):
    global sum
    sum=sum+1
    return num//2

def minus(num):
    global sum
    sum=sum+1
    return num-1


num=int(input())
sum=0


while(num!=1):
    if((num%3==0)and(num%2==0)):

       num=Three(num)

    elif (num==2):
        num=Two(num)

    elif((num%3==0)and(num%2!=0)):
        num=Three(num)

    elif ((num%3!=0)and(num%2!=0)):
        num=minus(num)

    elif ((num%3)!=0)and((num%2)==0):
        if((num-1)%3==0)and((num-1)%2!=0):
            num=minus(num)
            num=Three(num)
        else:
            num=Two(num)




print(sum)