import sys

'''
En este archivo están los tipos de datos que hay por defecto en python y cómo se pueden operar,
ignorando los básicos que ya los conocen.
'''

def Print(*msgs, sep:str=' ', end:str='\n'):
  print(f"Línea {sys._getframe().f_back.f_lineno}: ",*msgs,'\n', sep=sep, end=end)


## Tuplas
# Son listas de elementos, pueden tener cualquier tipo de objeto (int, float, list, tuple, class, etc.)
# Son inmutables, no se puede hacer asignación de elementos después de declarar una tupla
# Ejemplo:

nombres = ('Dani', 'Pablo', 'Cata', 'JD',)

Print(nombres)

try: # Intenta correr un código, si encuentra un error, ejecuta except
    nombres[0] = 'Alejandro Marulanda'
    Print(nombres)
except:
    Print('Error, no se puede modificar una tupla.')

## Listas
# Son arreglos de elementos, igual que las tuplas, pero se pueden modificar

nombres = list(nombres) # Se puede convertir una tupla a lista
# Equivalente a nombres = ['Raúl', 'Daniel',...]


## Hay muchas funciones que tienen las listas:
nombres.append('Sergio') # Añade al final otro elemento
nombres.clear() # Limpia la lista


nombres.copy() # Crea una referencia a una copia de la lista, esto requiere un ejemplo:

# Digamos que asigno una lista diferente a una lista ya hecha:
letras = ['a', 'c', 'e']
nombres = letras

letras[0] = 'b'

Print(nombres) # La lista 'nombres' se vio afectada por un cambio en la lista 'letras'
# Esto es porque la asignación genera un apuntador a la dirección de memoria de la lista
# original, entonces ambas corresponden al mismo objeto en memoria. Ambas se afectan a la vez

nombres[0] = 'c'
Print(letras)

# Si no queremos que pase, usamos una copia de la dirección de memoria en vez de un apuntador
nombres = letras.copy()
letras[0] = 'y'

Print(nombres) # Ahora el resultado no cambió cuando modificamos 'letras'



Print(nombres.index('c')) # Devuelve el índice del primer valor que coindica con el parámetro
Print(nombres.pop(0)) # Devuelve el valor del índice puesto y quita el elemento de la lista
Print(nombres) # Se ve cómo se quitó el primer elemento

# Hay otras funciones útiles pero son muy niche.

# NOTA: Todos los 'iterables' se indexan igual: nombres[índice], el índice empieza desde 0





## Conjuntos o sets
# Son listas sin orden, en las que no pueden haber duplicados. Como sus elementos no son
# ordenados no se pueden indexar, sólo se pueden quitar, o añadir más elementos, y operaciones
# de conjuntos (union, intersección, diferencia, etc.)
# Ejemplo:

Print({0, 1, 2, 3, 4, 5})

nombres_hoy = ['Dani', 'Cata', 'Diego', 'Pablo', 'Pablo', 'Daniela', 'Diego']
Print(set(nombres_hoy)) # Cambia el orden y elimina duplicados

# Se puede convertir nuevamente en listas si se quiere tener orden luego
# de eliminar los duplicados
Print(list(set(nombres_hoy)), list(set(nombres_hoy))[0])

## Diccionarios tienen claves y elementos, muy útiles para organizar información
# Las claves pueden ser objetos inmutables (tuplas, strgs), los elementos pueden
# ser cualquier cosa, incluso otros diccionarios:
info_usuarios = {
   'Camila': {
      'Cédula': 11111111,
      'Años':40,
      'Body-count':0,
      'Nombre de la mamá': 'Manuela'
   },
   'Martín': {
      'Cédula': 101010101,
      'Años': 21,
      'Body-count':15,
      'Nombre de la mamá': 'Rexona'
   }
}
# Se indexan con claves en lugar de números:
Print(info_usuarios['Camila']['Body-count'])





### Formas de indexar
# Puedo elegir desde donde, hasta donde, con que paso y en qué dirección puedo
# indexar. Un índice negativo indica empezar a contar desde el último elemento
# Ejemplo:

digitos = [i for i in range(10)]
Print(digitos)
Print(digitos[1:5])
Print(digitos[-5:-2])
Print(digitos[-3:])
Print(digitos[:-5])
Print(digitos[:5:-1])
Print(digitos[::-1])
Print(digitos[::-2])
Print(digitos[::3])


## Usos de los iterables
# Todos los anteriores (añadiendo strings) son iterables, porque contienen varios
# elementos. Puedo usar iterables en diferentes situaciones

# Puedo usarlos para iterar sobre los elementos:
for digito in digitos[:3]:
   Print(f'Dígito: {digito}')

# Puedo usarlos para invocar funciones de múltiples parámetros:

Print(*digitos) # El asterisco es similar a tomar los elementos y separarlos por comas

# Puedo iterar sobre los items de un diccionario:

#   (key, value) las tuplas se pueden escribir sin paréntesis
for key, value in info_usuarios.items():
   Print(f'{key} tiene la siguiente información:')
   
   for key_, value_ in value.items():
      Print(f'{key_}: {value_}')


### Funciones

# Puedo hacer funciones que no tomen parámetros
def intro():
   print('\n'*10)

intro()

# Funciones que tomen parámetros fijos
def sumar(a, b):
   Print(a+b)

sumar(12, 1)

# Funciones que tengan parámetros por defecto
def amplificar(a, scale=10):
   Print(a*scale)

amplificar(10, 100)

# Funciones que acepten parámetros indefinidos
def sumar_n(*args):
   Print(sum(args))

sumar_n(10, 20, 30, 9)

# Funciones que acepten parámetros y claves

def repeat_key(**kwargs):
   for key, value in kwargs.items():
      Print(key*value)
   
   intro()

repeat_key(Holi=1, Mundo=10, Davinsony_papasito=30)

#Funciones que devuelvan valores

def tetrate(a, b):
   val = a
   for i in range(b):
      val = a**val
   return val

Print(tetrate(3, 2))

