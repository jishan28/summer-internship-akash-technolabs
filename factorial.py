n1= int(input('enter a value:'))
factorial= 1
if n1<0:
    print('factorial of this number does not exist:')
elif n1==0:
    print('factorial of 0 is 1:')
else:
    for i in range(1,n1+1):
        factorial=factorial*i
        print('factorial of this number is:',factorial)

