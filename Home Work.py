#دريافت 3 عدد و ساختن مثلث با آنها
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
if ((a+b>c) and (a+c>b) and (b+c>a)):
    print("with this 3 number can make triangle")
else:
    print("with this 3 number can not make triangle")
    

#محاسبه کنيد
a=10
b=20.5
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=b//a
i=a**b
print("c:",c)
print("d:",d)
print("e:",e)
print("f:",f)
print("g:",g)
print("h:",h)
print("i:",i)


#پياده صازي شکل ستاره
for i in range (5):
    print("*"*i)

#شمارنده 0 تا 100
for i in range (100):
    print (i)

#جدول ضرب
for i in range (10):
    for j in range (10):
        A=i*j
        print(A)
    print(" ")



#دريافت نام با حلقه و چاپ آن
Name=[]
for i in range(0,5):
    str=input("enter Names : ")
    Name.append(str)
for i in Name:
    print(i)

#حاصل جمع دو عدد با استفاده از تابع
def calc(x,y):
    z=x+y
    return z
a=int(input("Enter Number1 : "))
b=int(input("Enter Number2 : "))
c=calc(a,b)
print(c)


#محاسبه ک م م
def kmm (x,y):
    n=z=0
    j = abs (x*y)+1
    if abs(x) > abs(y):
        n=abs(x)
    else:
        n=abs(y)
    #print(n)
    #print(j)
    for i in range (n,j):
        if i%x==0 and i%y==0:
            z=i
            #print(z)
            break
    return (z)
x=int(input("please enter x:"))
y=int(input("please enter y:"))
Answer = kmm(x,y)
print("Answer is:",Answer)


#بدست آوردن فاصله دو نقطه با مختصات آنها
import math
def distance(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
x1=int(input("Enter x for Point 1:"))
y1=int(input("Enter y for Point 1:"))
x2=int(input("Enter x for Point 2:"))
y2=int(input("Enter y for Point 2:"))
print ("distance is:",distance(x1,y1,x2,y2))





