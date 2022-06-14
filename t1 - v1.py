from operator import truediv
from pickle import FALSE, TRUE
from tkinter import Y


class date:
    def __init__(self, y, m, d):
        self.y=y
        self.m=m
        self.d=d
    def __gt__(self, other):
        ours=int(self.y*10000+self.m*100+self.d)
        others=int(other.y*10000+other.m*100+other.d)
        return ours>others

    def __eq__(self, other):
        ours=int(self.y*10000+self.m*100+self.d)
        others=int(other.y*10000+other.m*100+other.d)
        return ours==others
    def __lt__(self, other):
        ours=int(self.y*10000+self.m*100+self.d)
        others=int(other.y*10000+other.m*100+other.d)
        return ours<others
    def __str__(self):
        return str(self.y)+"/"+str(self.m)+"/"+str(self.d)


        # ret=TRUE
        # if self.y<other.y :
        #     ret=FALSE
        # elif self.y==other.y:
        #     if self.m < other.m :
        #         ret=FALSE
        #     elif self.m==other.m :
        #         if self.d <= other.d :
        #             ret=FALSE







def isLeap(year) :
    leap=False
    if year % 400==0 :
        leap=True
    else:
        if year % 4 == 0 and year % 100!=0:
            leap=True
    return leap

def test(instance):
    print(instance.y, instance.m, instance.d, sep='/')
def MonthHasDays(d1):
    m=d1.m
    days=30
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        days=31
    elif m==2:
        if isLeap(d1.y) :
            days=29
        else:
            days=28
    else:
        days=30
    return days



def HowManyDays(d1, d2):
    days=0
    if d1>d2 :
        d3=d1
        d1=d2
        d2=d3
    if d1.y==d2.y:
        if d1.m==d2.m:
            days=d2.d-d1.d+1
        else:
            days=MonthHasDays(d1)-d1.d + 1
            em=d2.m+1
            for i in range(d1.m+1, em):
                d3=date(d1.y, i, 1)
                days+=MonthHasDays(d3)
            days+=d2.d
    else:
        days=MonthHasDays(d1)-d1.d + 1
        em=13
        for i in range(d1.m+1, em):
            d3=date(d1.y, i, 1)
            days+=MonthHasDays(d3)
        for i in range(d1.y+1, d2.y):
            yd=365
            if isLeap(i):
                yd=366
            days+=yd
        for i in range(1, d2.m) :
            d3=date(d2.y, i, 1)
            days+=MonthHasDays(d3)
        days+=d3.d
    return days
    

dd1=date(2022, 6, 12)
dd2=date(2023, 6, 12)

print(dd1)
print(dd2)
print(HowManyDays(dd1, dd2))
    
    

