#!/usr/bin/env python3

import os
import subprocess
import time
import math

def rojo(skk): print("\033[91m {}\033[01m" .format(skk))

verde="\x1b[1;32m"
rojo_var="\x1b[1;31m"
amarillo="\x1b[1;33m"
azul="\x1b[1;34m"
rosado="\x1b[1;35m"
celeste="\x1b[1;36m"
plomo="\x1b[1;30m"
cs_color='\033[0;m'

#Menú de usuario
while (True):
	opción = input("""\n¿Qué operación quieres hacer?
	(1) Suma
  	(2) Resta
	(3) Multiplicación
	(4) División
	(5) Promedio
	(6) Potenciacion
	(7) Fracciones
	(8) Raiz Cuadrada
	(9) Ecuaciones Cuadraticas
	(10) Salir

inserta la opcion: """)
#suma
	if opción == '1' :
		ub = float(input("inserte numero: "))
		h = float(input("numero a sumar: "))
		print (ub+h)
		os.system('bash lector.sh')
#resta
	elif opción == '2' :
		ub = float(input("inserte numero: "))
		h = float(input("numero a restar: "))
		print (ub-h)
		os.system('bash lector.sh')
#multiplicación
	elif opción == '3' :
		ub = float(input("inserte numero: "))
		h = float(input("numero a multiplicar: "))
		print (ub*h)
		os.system('bash lector.sh')
#división
	elif opción == '4' :
		ub = float(input("inserte numero: "))
		h = float(input("numero a dividir: "))
		print (ub/h)
		os.system('bash lector.sh')
#promedio
	elif opción == '5' :
#asignamos la cabtidad d numeros
		cant_num = int(input("¿Cúantos números deseas ingresas?: \n \t"))
		suma = 0
		for e in range(cant_num):
	        	suma += float(input("\n Introduce un número: \n \t"))
		print(f"\n Se han introducidon {cant_num} números que en total suman {suma}. \n El promedio es: {suma/cant_num}.")
		os.system('bash /data/data/com.termux/files/home/operaciones/script/lector.sh')
#potenciacion
	elif opción == '6' :
		x = float(input('inserte numero: '))
		y = float(input('inserte el valor de la potencia: '))
		print (x**y)
		os.system('bash lector.sh')
#operaciones
	elif opción == '7' :
#asignando variables
		a = float(input('introduce el numerador: '))
		b = float(input('introduce el denominador: '))
		c = float(input('introduce el numerador: '))
		d = float(input('introduce el denominador: '))
#operaciones
		print ('resultado de la fraccion 1 :')
		print (a/b)
		print ('resultado de la fraccion 2 :')
		print (c/d)
#suma
		print ('suma')
		print ((a/b)+(c/d))
#resta
		print ('resta')
		print ((a/b)-(c/d))
#multiplicacion
		print ('multiplicacion')
		print ((a/b)*(c/d))
#división
		print ('division')
		print ((a/b)/(c/d))
#pruba para ver si se puede poner el valor en fraccion y no decimales
#asignando variables
		print ('suma en fraccion')
		e = (a*d)
		f = (c*b)
		print (e+f)
		print ('-----')
		g = (b*d)
		print (g)
		print ('')
		os.system('bash lector.sh')
#raiz cuadrada
	elif opción == '8' :
		numero = float(input('inserte numero: '))
		raiz = math.sqrt(numero)
		print (raiz)
		os.system('bash lector.sh')
#ecuaciones cuadraticas
	elif opción == '9' :
		print ('ejemplo de ecuación: a(x)²+b(x)+c')
		print ('nota: para restar solo pon -')
		print ('si la solucion no es real dara error')
		os.system ('bash lector.sh')
#asignamos variables
		a= int(input('numero a: '))
		b= int(input('numero b: '))
		c= int(input('numero c: '))
#calculamos discriminante
		e=(b*b)-4*a*c
#condicionante
		if e<0:
        		print ('no hay soluciones reales')
#solución
		else :
	        	x1=(-b+math.sqrt(e))//(2*a)
       			x2=(-b-math.sqrt(e))//(2*a)
		print ('..........soluciones..........')
		print ('solución x1: ',x1)
		print ('solución x2: ',x2)
		os.system('bash lector.sh')
#salir
	elif opción == '10' :
		print ('bye')
		break
