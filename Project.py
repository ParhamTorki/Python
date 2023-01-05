user_input=int(input("يک عدد بين 1 تا 9 وارد کنيد : "))
import math
match user_input:
    case 1:
        print("** مساحت و محيط مثلث **")
        r = float(input("شعاع را وارد کنيد: "))
        print("مساحت دايره : ",(math.pi*math.pow(r,2)))
        print("محيط دايزه : ",2*math.pi*r)
    case 2:
        print("** مساحت و محيط مربع **")
        x = float(input("طول ضلع را وارد کنيد: "))
        print("مساحت مربع : ",x*x)
        print("محيط مربع : ",x*4)
    case 3:
        print("** مساحت و محيط مثلث **")
        a1 = float(input("طول ضلع اول را وارد کنيد : "))
        a2 = float(input("طول ضلع دوم را وارد کنيد : "))
        a3 = float(input("طول ضلع سوم را وارد کنيد : "))
        #پيدا کردن قائده مثلث
        if a1>a2 and a1>a3:
            a=a1
        elif a2>a1 and a2>a3:
            a=a2
        elif a3>a1 and a3>a2:
            a=a3
        else:
            a=a2
        h = float(input("ارتفاع را وارد کتيد : "))
        print("مساحت مثلث : ",(a*h)/2)
        print("مثلث محيط : ",a1+a2+a3)
    case 4:
        print("** مساحت و محيط ذوزنقه **")
        a = float(input("قاعده بزرگ را وارد کنيد : "))
        b = float(input("قاعده کوچک را وارد کنيد : "))
        c = float(input("طول ضلع سوم را وارد کنيد : "))
        d = float(input("طول ضلع چهارم را وارد کنيد : "))
        h = float(input("طول ارتفاع را وارد کنيد : "))
        print("مساحت ذوزنقه : ",(((a+b)*h/2)))
        print("محيط ذوزنقه : ",a+b+c+d)

    case 5:
        print("** مساحت و محيط چند ضلعي منتظم **")
        x = float(input("تعداد اضلاع را وارد کنيد : "))
        y = float(input("طول يک ضلع را وارد کنيد : "))
        h = float(input("طول ارتفاع را وارد کنيد : "))
        print("مساحت چند ضلعي منتظم : ",((x*y*h)/2))
        print("محيط چند ضلعي منتظم : ",x*y)
    case 6:
        print("** مساحت و محيط مستطيل **")
        z = float(input("طول مستطيل را وارد کنيد : "))
        x = float(input("عرض مستطيل را وارد کنيد : "))
        print("مساحت مستطيل : ",z*x)
        print("محيط مستطيل : ",(z+x)*2)
    case 7:
        print("** حجم کره **")
        r = float(input("شعاع کره را وارد کنيد : "))
        print("حجم کره : ",((4/3)*math.pi)*math.pow(r,3))
    case 8:
        print("** حجم مخروط **")
        r = float(input("شعاع مخروط را وارد کنيد : "))
        h = float(input("ارتفاع مخروط را وارد کنيد : "))
        print("حجم مخروط : ",((math.pi*math.pow(r,2)*h)/3))
    case 9:
        print("** مساحت و محيط بيضي **")
        A = float(input("طول محور اصلي را وارد کنيد : "))
        B = float(input("طول محور فرعي را وارد کنيد : "))
        print("مساحت بيضي : ",math.pi*A*B)
        X = math.pi*(3*(A+B)-((((3*A)+B)*(A+(3*B)))**-0.5))
        print("محيط بيضي : ",X)

