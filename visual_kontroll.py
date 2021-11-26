from random import *
for i in range(1, 11, 1):
   y = -0.5*i + i
   print("x равняется ",i,". y значение выходит ",y)


#5
s=0
for i in range(0,12,1):
    print("плотность района", i)
    p=randint(1,20)
    square=randint(10,50)
    s=0
    s+=p/square
    print("km2:",round(s,1))
#4
a=0
b=2
k=randint(20,30)
while k>0:
    k-=1
    k1=uniform(1.0,5.0)
    if a<k1:
       a=0
       a+=k1
    elif b>k1:
        b=0
        b+=k1
print("наибольший: ", round(a,1))
print("наименьший: ", round(b,1))
#3
a=20
b=20
k1=20
k2=20
s1=0
while b>=0:
    b-=1
    rand=randint(1,5)
    s1+=rand
s1=s1/k1
print("Средний первого: ", s1)
s2=0
while a>=0:
    a-=1
    rand=randint(1,5)
    s2+=rand
s2=s2/k2
print("Средний второго: ", s2)
#2
n=int(input("Введи количество, сколько ты хочешь домов: "))
while n>9:
          print("Незя, не подходит")
          n=int(input("Введи количество, сколько ты хочешь домов: "))
dom = ['   ~~~~~   ',
       '  /_____\  ',
       '  | []  |  ',
       '   -----   ',]
for i in dom:
    print(i * n)
if n==0:
        print ("Ну и ладно тебя, не хочешь чтобы я рисовал((")
#1
