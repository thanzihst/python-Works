# read a number and extract digits from number


num=int(input("enter number"))

while(num!=0):

    digit=num%10

    print(digit)

    num=num//10




