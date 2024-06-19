#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-----------------------------------------------------------
def insertion_sort(arr):
    # Recorrer desde el segundo elemento hasta el final del arreglo
    for i in range(1, len(arr)):
        # Guardar el valor actual en una variable clave
        key = arr[i]
        # Inicializar j con el índice anterior a i
        j = i - 1
        # Mover los elementos del arreglo que sean mayores que la clave,
        # a una posición adelante de su posición actual
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Colocar la clave en su posición correcta en el subarreglo ordenado
        arr[j + 1] = key
    return arr

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
print("Arreglo Original: ", arr)
sorted_arr = insertion_sort(arr)
print("Arreglo ordenado:", sorted_arr)
