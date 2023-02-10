n=int(input("enter n value"))
a=0
b=1
Sum=0
if(n<=0):
    print ("give n value greater than zero")
elif(n==1):
    print(a)
else:
   print(a)
   print(b)
   i=3
   while(i<n+1):
       sum=a+b
       print(sum)
       a=b
       b=sum
       i+=1
