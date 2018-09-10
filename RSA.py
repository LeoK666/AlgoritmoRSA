import sys
import os
import random
'''codigo para RSA'''
c = True;
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
'''numeros primos al azar para la generacion del codigo'''
x = random.choice(primos);
y = random.choice(primos);
while c:
    if (y!=x):
        c = False;
    else:
        y = random.choice(primos);
'''se calcula n, el modulo para ambas claves'''
n = x * y;
#se calcula la funcion de euler
'''calculo de fi'''
fi = ((x-1)*(y-1)) + 1;
'''seleccionamos un coprimo para fi que servira para nuestra clave publica'''
e = random.choice(primos);
while fi % e != 0 and e != fi:
    e = random.choice(primos);
d = fi / e;
'''nuestra clave publica es (n,e) la cual es el modulo y el exponente del cifrado
nuestra clave privada es (n,d) la cual es el modulo y el exponente del descifrado'''
tupla = x,y,n,fi,e,d
print tupla;
clavepublica = (n,e);
claveprivada = (n,d)
print "La clave publica es " + str(clavepublica);
print "La clave privada es " + str(claveprivada);
mensaje = int(input("ingrese un numero menor a " + str(n) + " (EL MENSAJE A ENCRIPTAR)\n"))
encriptado = str((mensaje ** e)%n);
print "El mensaje encriptado es " + encriptado;
print ("La formula para desencriptar es (mensaje encriptado)^"+str(d)+" mod("+str(n)+")"); 
