x=int(input())
y=int(input())
if x>y:
    small=x
else:
    small=y
while True:
    if small%x==0 and small%y==0:
        hcf=small
        break;
    small+=1

print(hcf)
