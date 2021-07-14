# user handling calculater
import banner as bn
def repeat(data):
    udata = data.lower()
    if(udata=='y'):
        return 1
    else:
        return 2
bn.banner()
while(1==1):
    print("\n1 >> Sum \n2 >> Multiply\n3 >> Exit")
    userData = int(input("what's your choise ? "))
    if(userData == 1):
        number = input("Enter values seperated by ',' >>>").split(",")
        sum=0
        for x in number:
            x=int(x)
            sum+=x
        print("Values sum are >>> ",sum)
        wantagain = input("do you want to continue y or n ? ")
        rtrn = repeat(wantagain)
        if(rtrn==1):
            continue
        else:
            exit(0)
    elif(userData == 2):
        number = input("Enter values seperated by ',' >>>").split(",")
        mul=1
        for x in number:
            x=int(x)
            mul*=x
        print("Values Multiplies are >>> ",mul)
        wantagain = input("do you want to continue y or n ? ")
        rtrn = repeat(wantagain)
        if(rtrn==1):
            continue
        else:
            exit(0)
    elif(userData == 3):
        exit(0)
    else:
        continue

number = input("Enter values seperated by ',' >>>").split(",")
print(number)

number = input("Enter values seperated by ',' >>>").split(",")
sum=0
for x in number:
    x=int(x)
    sum+=x
print(sum)
