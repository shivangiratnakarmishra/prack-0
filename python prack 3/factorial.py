#program to print factorial number
n=int(input("Please enter the number : "))
i=1
fact=1
while(i<=n):
    fact=fact*i
    i=i+1
print('The factorial of ',n,' is : ',fact)
