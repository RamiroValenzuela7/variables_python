# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación

from typing import NoReturn


numero_1 = float(input('Ingrese el primer número decimal a operar: '))

numero_2 = float(input('Ingrese el segundo número decimal a operar: '))

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)

print("El primer numero igresado es: ", numero_1)
print("El segundo numero igresado es: ", numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma
suma = numero_1 + numero_2
print("El resultado de la suma entre", numero_1, "y", numero_2, "es:", suma)

# Resta
resta = numero_1 - numero_2
print("El resultado de la resta entre", numero_1, "y", numero_2, "es:", resta)

# División
div = numero_1 / numero_2
print("El resultado de la division entre", numero_1, "y", numero_2, "es:", div)

# Multiplicación
mult = numero_1 * numero_2
print("El producto entre", numero_1, "y", numero_2, "es:", mult)