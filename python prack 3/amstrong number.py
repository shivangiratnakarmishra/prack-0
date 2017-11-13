#Program to check enter number is amstrong no
num=int(input("Please enter number to check amstrong or not:"))
order=len(str(num))
sum=0
temp=num
while(int(temp)>0):
    digit=int(temp)%10
    sum+=digit**order
    temp=temp/10
if(num==sum):
    print(num,"is a amstrong number")
else:
    print(num,"is not a amstrong number")
    
