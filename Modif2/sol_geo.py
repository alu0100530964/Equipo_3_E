#!/usr/bin/python
#!encoding: UTF-8
import sys 
import modulo
import time
import timeit
# Menu principal
argumentos = sys.argv[1:]
 # print argumentos         Imprime la lista con los parametros que le des desde la consola
if (len(argumentos) == 2):# si la lista es de dos elementos (n,p)
  n = int(argumentos[0])
  p = float(argumentos[1])
else:
    print "Introduzca el nº de pruebas necesarias para obtener un exito (n>0):"
    n = int (raw_input())
    print "Introduzca el valor p (p>0):"
    p = float(raw_input())
    nombre_fichero=raw_input("Introduzca el nombre del fichero para almacenar los resultados: ")
if (n > 0):
  print "¿Que tipo de probabilidad vas a hallar? (0=P(X=n), 1=P(X<=n), 2=P(X<n), 3=P(X>=n))"
  respuesta=int(raw_input())
  if (respuesta==0):
    start=time.time()                        #Comienza el cronómetro interno¡¡
    probabilidad=modulo.calcular_geo (n,p)
    finish=time.time()-start                 #Finaliza¡¡
    print "La probabilidad P[X= %d] con p= %f es: %f y he tardado %f segundos en calcularlo"  %(n,p,probabilidad,finish)
  elif (respuesta==1):
    start=time.time()                        #Comienza el cronómetro interno¡¡
    probabilidad=modulo.calcular_geo1(n,p)
    finish=time.time()-start                 #Finaliza¡¡
      
    print "La probabilidad P[X<= %d] con p= %f es: %f y he tardado %f segundos en calcularlo"  %(n,p,probabilidad,finish)
  elif (respuesta == 2):
    start=time.time()                        #Comienza el cronómetro interno¡¡
    probabilidad=modulo.calcular_geo1(n-1,p)
    finish=time.time()-start                 #Finaliza¡¡
      
    print "La probabilidad P[X< %d] con p= %f es: %fy he tardado %f segundos en calcularlo"  %(n,p,probabilidad,finish)
  else:
    start=time.time()                        #Comienza el cronómetro interno¡¡
    prob=modulo.calcular_geo1(n,p)
    probabilidad = 1 - prob
    finish=time.time()-start                 #Finaliza¡¡
 
    print "La probabilidad P[X>= %d] con p= %f es: %f y he tardado %f segundos en calcularlo"  %(n,p,probabilidad,finish)
   
else:
    print "No podemos hallar la probabilidad"