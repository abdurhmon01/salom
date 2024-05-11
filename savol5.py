n1 = int(input())
n2=n1
sum=0
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    sum+=digit
if n2%sum==0:
    print('yes')
else : 
    print('no')