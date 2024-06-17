#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-----------------------------------------------------------
def selection_sort(arr):
    # Recorrer todo el arreglo
    for i in range(len(arr)):
        # Suponer que el primer elemento no ordenado es el menor
        min_idx = i
        # Recorrer el resto del arreglo para encontrar el verdadero menor
        for j in range(i + 1, len(arr)):
            # Si encontramos un elemento menor, actualizamos min_idx
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el menor elemento encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Arreglo ordenado:", sorted_arr)