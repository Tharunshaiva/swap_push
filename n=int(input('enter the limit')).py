n=int(input('enter the limit'))
a,b=0,1
if n==0:
    print('ans is zero')
if n==1:
    print('ans is one')
else:
    print(a,b, end=" ")
    for i in range(2,n+1):
        c=a+b
        a,b=b,c
        print(c,end=" ")