#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# El algoritmo de ordenamiento por intercambio se basa en la comparación de todos los pares posibles 
# de elementos en el arreglo y en el intercambio de sus posiciones si no están en el orden correcto. 
# Este proceso se repite hasta que todos los elementos estén ordenados.

#-----------------------------------------------------------
def interchange_sort(arr):
    # Recorrer todo el arreglo desde el primer elemento hasta el penúltimo
    for i in range(len(arr) - 1):
        # Recorrer desde el siguiente elemento al actual hasta el final del arreglo
        for j in range(i + 1, len(arr)):
            # Comparar el elemento actual con el siguiente
            if arr[i] > arr[j]:
                # Intercambiar si el elemento actual es mayor que el siguiente
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# Ejemplo de uso
arr = [29, 10, 14, 37, 13]
sorted_arr = interchange_sort(arr)
print("Arreglo ordenado:", sorted_arr)