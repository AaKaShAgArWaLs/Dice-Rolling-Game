import Dice
import Dice2
import nu_int
import Result
number_of_rolls=nu_int.maii()
scorea=[]
scoreb=[]
i=0
j=2
num=number_of_rolls*2
for i in range(num): 
    if i%2==0:
        a=Dice.ma()
        scorea.append(a[0]+a[1])
    else:
        a=Dice2.ma()
        scoreb.append(a[0]+a[1])
a=0
b=0
for i in scorea:
    a+=i

for i in scoreb:
    b+=i
if a>b:
    Result.res1(a)
elif b>a:
    Result.res2(b)
else:
    Result.res3()

