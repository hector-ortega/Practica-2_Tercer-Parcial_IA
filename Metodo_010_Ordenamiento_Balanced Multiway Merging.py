#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# División Inicial:

# El arreglo se divide en num_ways subarreglos de tamaño similar.

# Recursividad:

# Se aplica recursivamente balanced_multiway_merge a cada subarreglo hasta que los subarreglos sean lo suficientemente
# pequeños para ser considerados ordenados (tamaño 1).

# Fusión con Heap:

# Los subarreglos ordenados se fusionan utilizando un heap, que permite mantener los elementos en orden mientras se combinan múltiples listas ordenadas.
#-----------------------------------------------------------------
import heapq

def balanced_multiway_merge(arr, num_ways):
    # Si el arreglo tiene uno o cero elementos, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # Función para dividir el arreglo en subarreglos de tamaño similar
    def split_into_runs(arr, num_ways):
        n = len(arr)
        size = n // num_ways
        runs = []
        for i in range(num_ways):
            if i == num_ways - 1:
                runs.append(arr[i*size:])  # Último subarreglo
            else:
                runs.append(arr[i*size:(i+1)*size])
        return runs

    # Función para fusionar múltiples listas ordenadas utilizando un heap
    def merge_runs(runs):
        heap = [] #Inicializa un heap vacío.
        result = [] #Inicializa una lista para almacenar el resultado de la fusión.
        
        # Inicializar el heap con el primer elemento de cada subarreglo
        for i, run in enumerate(runs): #  Recorre cada subarreglo.
            if run:
                heapq.heappush(heap, (run[0], i, 0)) # Agrega el primer elemento de cada subarreglo al heap.
        
        # Extraer el mínimo del heap y agregarlo al resultado
        while heap: #Mientras el heap no esté vacío
            val, run_idx, elem_idx = heapq.heappop(heap) #Extrae el mínimo del heap.
            result.append(val) #Agrega el valor extraído al resultado.
            
            # Si el subarreglo tiene más elementos, agregar el siguiente elemento al heap
            if elem_idx + 1 < len(runs[run_idx]):
                next_tuple = (runs[run_idx][elem_idx + 1], run_idx, elem_idx + 1)
                heapq.heappush(heap, next_tuple) #Si el subarreglo tiene más elementos, agrega el siguiente elemento al heap.
        
        return result

    # Dividir el arreglo en subarreglos de tamaño similar
    runs = split_into_runs(arr, num_ways)
    
    # Aplicar Merge Sort recursivamente a cada subarreglo
    sorted_runs = [balanced_multiway_merge(run, num_ways) for run in runs]
    
    # Fusionar todos los subarreglos ordenados en un solo arreglo
    sorted_arr = merge_runs(sorted_runs)
    
    return sorted_arr

# Ejemplo de uso
arr = [29, 10, 14, 37, 13, 33, 21, 19]
num_ways = 3  # Número de subarreglos para la fusión
sorted_arr = balanced_multiway_merge(arr, num_ways)
print("Arreglo ordenado:", sorted_arr)