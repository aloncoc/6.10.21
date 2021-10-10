a=int(input('enter number:'))
low=a
while a>0:
 a = int(input('enter number:'))
 while a>0 and a<low:
     low=a
if a<=0:
    print(low)


