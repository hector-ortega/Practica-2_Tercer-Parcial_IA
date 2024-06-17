#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# Identificación de Subarreglos Naturales:

# El algoritmo recorre el arreglo y divide los elementos en subarreglos naturales. Un subarreglo natural es una secuencia de elementos que ya están en orden ascendente.
# Fusión de Subarreglos Naturales:

# Después de identificar los subarreglos naturales, el algoritmo fusiona estos subarreglos de manera iterativa hasta que todo el arreglo esté ordenado.
# En cada paso de fusión, se combinan pares de subarreglos naturales adyacentes en un solo subarreglo ordenado.
#-----------------------------------------------------------------
def merge(arr, left, mid, right):
    # Crear subarreglos temporales para la fusión
    n1 = mid - left + 1  # Tamaño del primer subarreglo
    n2 = right - mid  # Tamaño del segundo subarreglo

    # Crear arreglos temporales
    L = [0] * n1
    R = [0] * n2

    # Copiar datos a los arreglos temporales L[] y R[]
    for i in range(n1):
        L[i] = arr[left + i]  # Copia los elementos del subarreglo izquierdo
    for j in range(n2):
        R[j] = arr[mid + 1 + j]  # Copia los elementos del subarreglo derecho

    # Fusionar los arreglos temporales de nuevo en arr[left..right]
    i = 0  # Índice inicial del primer subarreglo
    j = 0  # Índice inicial del segundo subarreglo
    k = left  # Índice inicial del arreglo fusionado

    # Copiar los datos de L[] y R[] de vuelta a arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:  # Si el elemento en L es menor o igual que el elemento en R
            arr[k] = L[i]  # Copiar el elemento de L en arr
            i += 1
        else:
            arr[k] = R[j]  # Copiar el elemento de R en arr
            j += 1
        k += 1

    # Copiar los elementos restantes de L[], si los hay
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R[], si los hay
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def natural_merge_sort(arr):
    # Función principal que inicia el proceso de Natural Merging Sort
    if len(arr) <= 1:
        return arr # Si el arreglo tiene uno o cero elementos, ya está ordenado.
    
    # Dividir el arreglo en subarreglos naturales
    runs = []
    new_run = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            new_run.append(arr[i])
        else:
            runs.append(new_run)
            new_run = [arr[i]]
    
    runs.append(new_run)

    # Fusionar los subarreglos hasta que solo quede uno
    while len(runs) > 1:
        new_runs = []
        
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                # Fusionar dos subarreglos consecutivos
                merged_run = merge_runs(runs[i], runs[i + 1])
                new_runs.append(merged_run)
            else:
                new_runs.append(runs[i])
        
        runs = new_runs
    
    return runs[0]

def merge_runs(left, right):
    # Fusionar dos listas ordenadas en una lista ordenada
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Copiar los elementos restantes de left[], si los hay
    result.extend(left[i:])
    
    # Copiar los elementos restantes de right[], si los hay
    result.extend(right[j:])
    
    return result

# Ejemplo de uso
arr = [29, 10, 14, 37, 13, 33, 21, 19]
sorted_arr = natural_merge_sort(arr)
print("Arreglo ordenado:", sorted_arr)