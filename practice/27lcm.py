x=int(input())
y=int(input())
if x>y:
    great=x
else:
    great=y
while(True):
    if(great%x==0) and (great%y==0):
        lcm=great
        break
    great+=1

print(lcm) 

