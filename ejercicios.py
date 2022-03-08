#convertidor centimtros a pulgadas
centimetros = int(input('ingrese longitud en centimetros : '))
pulgadas =  2.54

resultado = centimetros / pulgadas

print(centimetros ,' cm = ', resultado)

#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso

numeros = (input('ingrese un entero de tres digitos: '))
print(numeros[:: -1])


#escriba un programa que calcule la hipotenuza segun el teorma de pitagoras

a = int(input('ingrese cateto a:'))
b = int(input('ingrese cateto b: '))

hipotenusa = ((a**2 +b**2)**(1/2))

print(hipotenusa)


##hora futura
hora1 = int(input('Hora actual: '))
cantidad = int(input('Cantidad horas: '))

hora_futura =   hora1 + cantidad

print('En ', cantidad, 'horas el reloj marcara las ',hora_futura)

#numero decimal
numero_real = float(input('ingrese un numero: '))
numero_entero= int(numero_real)
decimal = numero_real-numero_entero

print(decimal)


#numero par
numero = int(input('ingrese un nuemro:'))
multiplo = 4
if numero % multiplo ==  0:
   print('es par')
else:
   print('no es par')

#año bisiesto
def bisiesto(x):
    if x% 4 ==0 or x%400==0:
       return 'es bisiesto'
    else:
       return 'no es bisiesto' 
       

x = int(input('introduzca un año:'))
print(x,bisiesto(x))

#ordenar numeros
a = int(input('escribe un nuemro: '))
b = int(input('escribe otro numero: '))
c = int(input('escribe otro numero: '))

f = min(a,b,c)
j = (a+b+c)-a-c
g = max(a,b,c)
print(f'los numero orenados son {f}, {g}, {j}')




   
    
