Number=int(input("Enter any number"))
sum=0
for i in range(1,Number):
    if(Number%i==0):
        sum+=i
        if(sum==Number):
            print(Number,"is a perfect number")
        else:
            print(Number,"is not a perfect number")