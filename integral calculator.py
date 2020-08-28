#Recibe del usuario la función.
#Por el momento usaremos la función x^2+e^x.
#Definimos el número de Euler
e=2.7182818284

#Recibe del usuario los datos.
lower_limit=1
upper_limit=2

#Parte la distancia entre límites en 100 partes
interval=(upper_limit-lower_limit)/10000

#Suma de Riemann
#Definir variables del bucle de antemano.
step = lower_limit
Area=0

while step <= upper_limit:
    Area=(step**2+e**step)*interval+Area
    step = step+interval
    print(Area)
    print(step)
    print(step**2+e**step)
if step > upper_limit:
    print("The value is", Area)