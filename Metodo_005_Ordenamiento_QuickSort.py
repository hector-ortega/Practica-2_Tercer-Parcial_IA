#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# Selección del Pivote:
# Se elige un elemento del arreglo como pivote. En este caso, se utiliza el primer elemento.
# Partición:

# Se divide el arreglo en dos subarreglos: uno con elementos menores o iguales al pivote (less) y otro con elementos mayores al pivote (greater).
# Recursión:

# Se aplica recursivamente el mismo proceso a los subarreglos less y greater.
# Combinación:

# Una vez que los subarreglos están ordenados, se combinan junto con el pivote para formar el arreglo ordenado final.
#-----------------------------------------------------------
def quicksort(arr):
    # Función principal que inicia el proceso de QuickSort
    if len(arr) <= 1:
        # Si el arreglo tiene uno o cero elementos, ya está ordenado
        return arr
    else:
        # Elegir el pivote (usualmente el primer elemento)
        pivot = arr[0]
        # Crear una lista para los elementos menores que el pivote
        less = [x for x in arr[1:] if x <= pivot]
        # Crear una lista para los elementos mayores que el pivote
        greater = [x for x in arr[1:] if x > pivot]
        # Recursivamente aplicar quicksort a las sublistas y combinar los resultados
        return quicksort(less) + [pivot] + quicksort(greater)

# Ejemplo de uso
arr = [29, 10, 14, 37, 13]
sorted_arr = quicksort(arr)
print("Arreglo ordenado:", sorted_arr)