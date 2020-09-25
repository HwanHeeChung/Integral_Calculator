import math

def riemann(integrand,lower,upper):
    Area = 0
    step = lower
    interval = (upper-lower)/10000
    
    while step < upper:
        Area = Area + eval(integrand,{"x":step,"e":math.e,"pi":math.pi,"sin":math.sin,"cos":math.cos,"tan":math.tan})*interval
        step = step + interval
    return Area

#Recibe valores del usuario.
integrand = str(input("Input the integrand in terms of x. \nMake sure it does not contain 1/x of any form. \n"))
lower_limit = float(input("Input the value of the lower limit:"))
upper_limit = float(input("Input the value of the upper limit:"))

#El límite inferior debe ser menor al límite superior
if lower_limit > upper_limit:
    print('Upper limit is smaller than lower limit.')

elif lower_limit == upper_limit:
    print('The value is 0')

else:
    print("The value is", riemann(integrand,lower_limit,upper_limit))