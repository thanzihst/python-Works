
number=int(input("enter number"))

isPrime=True

for i in range(2,number):

    if number%i==0:

        isPrime=False

        break

print(f"{number} is prime" if isPrime==True else f"{number}not prime")



