# Informatica
# Documento de funciones innecesarias que aún así necesito aprender.

# 1.) ENUMERATE

# Enumerate imprime el indice y el valor actual del iterado. Requiere de dos valores.
def enumeratetest(x):
    for indx, value in enumerate(x):
        print(indx, value)

# a enumerate se le puede añadir un segundo parametro que es el indice de donde empezar a enumerar en una secuencia dada.

enumeratetest(["manzana", "pera", "aguacate"])


# 2.) LIST.CLEAR()    

#En Python, list.clear() es un método de listas que se utiliza para eliminar todos los elementos de la lista, dejándola vacía.

list1 = [1,2,3,4]
print(list1)
list1.clear() # no acepta parametros, limpia todo.
print(list1)

# 3.) TYPE()

# Type no es innecesaria, es muy útil, sin embargo necesito aprenderla, asi que la anotaré aquí

# Type nos permite saber que tipo de cosa es algo, muy útil para filtrar.

tuple1 = (1,2,3,"hola",True)
numrandom = 0
#imaginemos que queremos filtrar ints y sumarlas.

for item in tuple1:
    if type(item) is int:
        numrandom = numrandom + item
    else:
        pass

print(numrandom)

# 4.) ANY()

# Any devuelve True si alguna condición de dentro es true, le puedes añadir un bucle for dentro para iterar

tuple2 = ("carlos","pedro")
if any(item == "carlos" for item in tuple2) == True: #comprueba directamente si item == "carlos", no es necesario añadir "if".
    print("true")
