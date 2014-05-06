#!/usr/bin/python
#!encoding: UTF-8
import sys 
import modulo

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
if (n > 0):
    print "¿Que tipo de probabilidad vas a hallar? (0=P(X=n), 1=P(X<=n), 2=P(X<n), 3=P(X>=n))"
    respuesta=int(raw_input())
    if (respuesta==0):
      probabilidad=modulo.calcular_geo (n,p)
      print "La probabilidad P[X= %d] con p= %f es: %f"  %(n,p,probabilidad)
    elif (respuesta==1):
      probabilidad=modulo.calcular_geo1(n,p)
      print "La probabilidad P[X<= %d] con p= %f es: %f" %(n,p,probabilidad)
    elif (respuesta == 2):
      probabilidad=modulo.calcular_geo1(n-1,p)
      print "La probabilidad P[X< %d] con p= %f es: %f" %(n,p,probabilidad)
    else:
      prob=modulo.calcular_geo1(n,p)
      probabilidad = 1 - prob
      print "La probabilidad P[X>= %d] con p= %f es: %f" %(n,p,probabilidad)   
else:
    print "No podemos hallar la probabilidad"