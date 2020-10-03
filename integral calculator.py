import math

import numpy as np #Importa la biblioteca numpy -requerimiento de matplotlib- y la llamamos "np".
import matplotlib.pyplot as plt #Importa la biblioteca matplotlib y la llamamos "plt".
from matplotlib.patches import Polygon #Importa específicamente "Polygon" para trazar áreas bajo curvas.

def interval_test(lower,upper):
    #El límite inferior debe ser menor al límite superior
    if lower > upper:
        return False
    else:
        return True

def riemann(integrand,lower,upper):
    Area = 0
    step = lower
    interval = (upper-lower)/10000
    
    if interval_test(lower,upper) is True:
        while step < upper:
            Area = Area + eval(integrand,{"x":step,"e":math.e,"pi":math.pi,"sin":math.sin,"cos":math.cos,"tan":math.tan})*interval
            step = step + interval
        return Area
    else: 
        return "not obtainalbe because lower limit > upper limit."

def rotation_volume(integrand,lower,upper):
    sqr_integrand="math.pi"+"("+integrand+")"+"**2"
    return riemann(sqr_integrand,lower,upper)
    
def position(position_0,velocity_0,t_0,t_f):
    displacement = riemann(velocity_0,t_0,t_f)
    return position_0+displacement

def func(x,function): #Define función para trazar el diagrama más tarde.
    return eval(function,{"x":x,"e":math.e,"pi":math.pi,"sin":math.sin,"cos":math.cos,"tan":math.tan})

print("Select an option from below:\n \
    1) Area under a curve \n \
    2) Revolving solid's volume \n \
    3) Displacement from a time-dependent velocity")

#Recibe valores del usuario.
option = int(input())

if option == 1: #Area under a curve
    #Recibe valores del usuario.
    integrand = str(input("Input the integrand in terms of x. \nMake sure it does not contain 1/x of any form. \n"))
    lower_limit = float(input("Input the value of the lower limit: "))
    upper_limit = float(input("Input the value of the upper limit: "))

    print("The area under the curve is", riemann(integrand,lower_limit,upper_limit))

#Traza la función y el área bajo la curva usando matplotlib.

    #Crea el plano x,y.
    a,b = lower_limit,upper_limit #Define los límites de la integral.
    x = np.linspace(lower_limit*0.8, upper_limit*1.2) #Crea el intervalo del eje x y agrega 20% más espacio antes y después de los límites.
    y = func(x,integrand) #Crea el intervalo del eje y define la curva.

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2) 
    ax.set_ylim(bottom=0) #Establece la porción visible del eje y.

    #Crea el área sombreada bajo la curva.
    ix = np.linspace(a,b)
    iy = func(ix,integrand)
    verts = [(a, 0), *zip(ix, iy), (b, 0)] #Definimos los vértices del área entre los límites. 
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    #Configuraciones visuales
    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticks((lower_limit,upper_limit))
    ax.set_xticklabels(('$a$', '$b$'))
    ax.set_yticks([])

    plt.show()

elif option == 2: #Revolving solid's volume
    #Recibe valores del usuario.
    integrand = str(input("Input the integrand in terms of x. \nMake sure it does not contain 1/x of any form. \n"))
    lower_limit = float(input("Input the value of the lower limit:"))
    upper_limit = float(input("Input the value of the upper limit:"))

    print("The volume is", rotation_volume(integrand,lower_limit,upper_limit))

elif option == 3: #Displacement from a time-dependent acceleration
    pos_0=[]
    counter=0
    while counter<3:
        pos = float(input("Input one of the xyz values for initial position: "))
        pos_0.append(pos)
        counter=counter+1
    
    vel_0=[]
    counter=0
    while counter<3:
        vel = input("Input one of the xyz values for initial velocity: ")
        vel_0.append(vel)
        counter=counter+1

    time_0=float(input("Input the initial time: "))
    time_f=float(input("Input the final time: "))

    x_coor = position(pos_0[0],vel_0[0],time_0,time_f)
    y_coor = position(pos_0[1],vel_0[1],time_0,time_f)
    z_coor = position(pos_0[2],vel_0[2],time_0,time_f)
    xyz_coor = [x_coor,y_coor,z_coor]

    print("The final position is", xyz_coor)

else: 
    print("Option non existent.")