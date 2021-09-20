# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
sub_tex_1 = palabra_1[:3]

# De la segunda palabra tome las primeras dos letras, utilice el operador :
sub_tex_2 = palabra_2[:2]

# Formar una nueva palabra con los recortes solicitados
palabra_3 = sub_tex_1 + sub_tex_2

# Imprima en pantalla los resultados
print("El recorte de la primera palabra es:", sub_tex_1)
print("El recorte de la segunda palabra es:", sub_tex_2)
print("La nueva palabra formada es:", palabra_3)
