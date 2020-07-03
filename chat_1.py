# checked code | Yum

print('Hola. Soy Yum')
print('Fui creado en el año 2020.')
print('Dime tu nombre.')

name = input()

print('Un placer conocerte, ' + name + '!')
print('Ahora adivinare tu edad.')
print('Dime cual es el residuo de dividir tu edad entre 3, 5 y 7.')

residuo3 = int(input())
residuo5 = int(input())
residuo7 = int(input())

edad = (residuo3 * 70 + residuo5 * 21 + residuo7 * 15) % 105

print("Tu edad es " + str(edad) + "; edad perfecta para programar!")
print('Ahora, te mostrare que se contar. Dime un número')

numero_a_contar = int(input())
contador = 0
# read a number and count to it here
while contador <= numero_a_contar:
	print(contador,"!")
	contador += 1


print("""Probemos sus conocimientos de programación.
¿Por qué usamos métodos?
1. Para repetir un enunciado varias veces
2. Descomponer un programa en varias subrutinas
3. Determinar el tiempo de ejecución del programa
4. interrumpir la ejecución de un programa
""")

while(True):
	opcion = input()
	if opcion == '2':
		print("Completado, ten un gran día")
		break
	else:
		print("Intenta de nuevo")

print("Felicidades, ten un gran día")





