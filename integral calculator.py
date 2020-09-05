#Definimos el número de Euler
Euler=2.7182818284

#Definimos las funciones seno, coseno y tangente utilizando la serie de Taylor hasta el 5to término.

def sin(var):
    value=var-(var**3)/6+(var**5)/120-(var**7)/5040
    return value
   
def cos(var):
    value=1-(var**2)/2+(var**4)/24-(var**6)/720
    return value

def tan(var):
    value=sin(var)/cos(var)
    return value

#Recibe del usuario la función. Por el momento usaremos la función sin(x)/x.

#Recibe del usuario los datos.
lower_limit=1
upper_limit=2

#Parte la distancia entre límites en 1000 partes
interval=(upper_limit-lower_limit)/10000

#Suma de Riemann
#Definir variables del bucle de antemano.
step = lower_limit
Area=0

while step <= upper_limit:
    Area=(sin(step)/step)*interval+Area
    step = step+interval
    print(Area)
    print(step)
    print(sin(step)/step)
if step > upper_limit:
    print("The value is", Area)