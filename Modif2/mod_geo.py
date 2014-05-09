###################################################################################
# mod_geo.py
###################################################################################
#
# AUTORES: María Baeza López
#         Juan Jesús Dóniz Labrador
#         Jesús Manuel Rodríguez Falcón
#
# FECHA:
#
# DESCRIPCION: Este módulo contiene dos funciones:
#             1. calcular_geo (n,p)---->calcula la probabilidad geométrica y la devuelve a sol_geo.py
#             2. calcular_geo1 (n,p)--->Calcula la probabilidad geométrica desde 1 hasta n y las va almacenando 
#                en sumaprobabilidad
###################################################################################

#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

def calcular_geo (n,p):
  if (n>1):
    q=1-p
    probabilidad=(q**(n-1))*p
  else:
    probabilidad=p
  return (probabilidad)
  
def calcular_geo1 (n,p):
  probabilidad=0
  for i in range (1,n+1):
    sumaprobabilidad=calcular_geo(i,p)
    probabilidad+=sumaprobabilidad
  return (probabilidad)
