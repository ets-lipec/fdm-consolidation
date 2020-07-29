import math
import numpy as np
import matplotlib.pyplot as plt



tini = 1
tf = 11
nt = np.linspace(tini,tf,10001)
dt = (tf-tini)/(len(nt)-1)
Vheal1 = np.zeros(len(nt))
Vheal2 = np.zeros(len(nt))
Vheal3 = np.zeros(len(nt))


def tw(t):
    
    return math.sqrt(t)

def do():
    
    for k in range (len(nt)-1):
    
        tk = k*dt+tini
        tk1 = (k+1)*dt+tini
        tav = (tk+tk1)/2
        Vheal1[k+1] = Vheal1[k]+((tk1**(1/4)-tk**(1/4))*tw(tav)**(1/4))
    
    return Vheal1

def do2():
       
    for k in range (len(nt)-1):
    
        tk = k*dt+tini
        tk1 = (k+1)*dt+tini
        tav = (tk+tk1)/2
        Vheal2[k+1] = (Vheal2[k]**4+tw(tav)*dt)**(1/4)


    return Vheal2

def do3():
    
    for k in range (len(nt)-1):
    
        tk = k*dt+tini
        tk1 = (k+1)*dt+tini
        Vheal3[k+1] = (Vheal3[k]**4+(1/2*(tw(tk)+tw(tk1))*dt))**(1/4)

    return Vheal3

a=do()
b=do2()
c=do3()

k=0
# =============================================================================
# d=np.zeros(len(nt))
# for i in nt:
#     d[k]=(math.sqrt(i)-math.sqrt(tini))**(1/4)
#     k=k+1
# 
# =============================================================================

d=(2/3*nt**(3/2)-2/3*tini**(3/2))**(1/4)

fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(1,1,1)
axes.plot(nt,a,label='Bastien & Gillespie Jr.')
axes.plot(nt,b,label='rectangle')
axes.plot(nt,c,label='trapezium')
axes.plot(nt,d,label='real integral')
axes.set_xlabel("Time (s)",fontsize=16)
axes.set_ylabel("(2/3*t**(3/2))**(1/4)",fontsize=16)
axes.set_title("Test of integral methods for the square root function")
axes.set_xlim((tini,tf))
axes.set_ylim((min(a.min(),b.min(),c.min()),max(a.max(),b.max(),c.max())))
axes.legend(loc='best')
axes.grid()
plt.show()