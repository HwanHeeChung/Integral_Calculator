# Integral_Calculator
<b>Un programa para calcular integrales definidas </b>
<p><b>Algoritmo principal</b> (suma de Riemann) 
  <p> El código recibe el límite inferior (a), límite superior (b) y el integrando (f(x)). La función "interval_test" se asegura de que a<b y pasa los valores a la función "riemann" que aproxima el área bajo la curva y=f(x) con el siguiente algoritmo:
  <p> intervalo= (límite superior-límite inferior) / 10000
  <p> return sigma (de i(entero) en i) desde 0 hasta n (f(a+i*intervalo)*intervalo)
<p> El usuario puede escoger de 3 opciones: "1) el área bajo una curva", "2) volumen de un sólido de rotación" y "3) la posición con velocidad en función de tiempo".
  La primera opción calculará el área y creará una gráfica del área utilizando matplotlib. Todas las opciones utilizan el algoritmo principal de las sumas de Riemann.
