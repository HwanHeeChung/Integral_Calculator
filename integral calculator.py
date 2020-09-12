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
function=str(input("Input the integrand in terms of x. \nMake sure it does not contain 1/x of any form. \n"))

#Recibe del usuario los datos.
lower_limit=1
upper_limit=2
#Parte la distancia entre límites en 10000 partes
interval=(upper_limit-lower_limit)/10000

#El límite inferior debe ser menor al límite superior
if lower_limit > upper_limit:
    print('Switch lower and upper limits.')
elif lower_limit == upper_limit:
    print('The area is 0.')
else: #Suma de Riemann
    #Definir variables del bucle de antemano.
    step = lower_limit
    Area=0

    while step <= upper_limit:
        Area=(eval(function,{"x":step,"sin":sin, "cos":cos, "tan":tan, "e":Euler}))*interval+Area
        step = step+interval
    if step > upper_limit:
        print("The value is", Area)