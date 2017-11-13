#program to display fibbonaci sequence
num=int(input("Please enter the number of elements to be printed : "))
n1=1
n2=1
count=0
print('Fibconaci Elements :\n1\n1')
while(count<(num-2)):
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1
    print(nth)
    
    
