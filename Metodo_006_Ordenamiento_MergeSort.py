
#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# División Recursiva:

# El arreglo se divide recursivamente en mitades hasta que cada subarreglo tenga uno o cero elementos (caso base).
# Mezcla:

# Los subarreglos se combinan (o "mezclan") de nuevo en orden ascendente.
#-----------------------------------------------------------
def merge_sort(arr):
    # Función principal que inicia el proceso de MergeSort
    if len(arr) > 1:
        # Encontrar el punto medio del arreglo
        mid = len(arr) // 2
        # Dividir el arreglo en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursivamente aplicar merge_sort a la primera mitad
        merge_sort(left_half)
        # Recursivamente aplicar merge_sort a la segunda mitad
        merge_sort(right_half)
        
        # Inicializar índices para las sublistas y el arreglo principal
        i = j = k = 0
        
        # Mezclar las sublistas de nuevo en el arreglo principal
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Copiar los elementos restantes de left_half, si los hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Copiar los elementos restantes de right_half, si los hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
    # No se necesita un retorno explícito porque estamos modificando el arreglo original

# Ejemplo de uso
arr = [29, 10, 14, 37, 13]
merge_sort(arr)
print("Arreglo ordenado:", arr)