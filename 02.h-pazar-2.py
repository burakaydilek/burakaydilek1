import turtle as t 
#buyukluk=int(input("Büyüklük ne olsun:"))
#tekrar=int(input("Kaç tane olsun:"))

def kareciz(xx):
    for k in range(15):
        t.forward(xx)
        t.right(90)
def sekilciz(buy,ken):
    for k in range(ken):
        t.forward(buy)
        t.right(360/ken)    
for a in range(50,350,30):
    sekilciz(100,6)
    kareciz(20)            
input()   