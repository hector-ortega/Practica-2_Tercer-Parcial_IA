#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
#Inicialización:

# El algoritmo comienza estableciendo un tamaño inicial para los subarreglos que se van a fusionar. Este tamaño inicial es 1, lo que significa que al principio, 
#cada elemento del arreglo se considera un subarreglo de tamaño 1.
# Iteración sobre el Arreglo:

# En cada iteración, el algoritmo fusiona pares de subarreglos de tamaño current_size. Después de cada iteración, el tamaño del subarreglo
# current_size se duplica (1, 2, 4, 8, etc.).
# Fusión de Subarreglos:

# La función de fusión (merge) se utiliza para combinar dos subarreglos ordenados en un solo subarreglo ordenado. Se crean dos subarreglos 
#temporales para almacenar los elementos y luego se combinan de manera ordenada en el arreglo original.
# Repetición:

# El proceso se repite hasta que el tamaño del subarreglo current_size es mayor o igual al tamaño del arreglo original. En este punto, el 
#arreglo completo estará ordenado.
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

def straight_merge_sort(arr):
    # Función principal que inicia el proceso de Straight Merging Sort
    current_size = 1  # Tamaño del subarreglo que se va a fusionar; comienza en 1

    # Doble bucle para dividir el arreglo en subarreglos de tamaño actual y fusionarlos
    while current_size < len(arr) - 1:
        left = 0
        # Iterar sobre los subarreglos en incrementos del tamaño actual
        while left < len(arr)-1:
            # Calcular el punto medio y el extremo derecho del subarreglo
            mid = min(left + current_size - 1, len(arr)-1)
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr)-1])
            # Fusionar los subarreglos arr[left...mid] y arr[mid+1...right]
            merge(arr, left, mid, right)
            left = left + current_size * 2

        # Incrementar el tamaño del subarreglo para la siguiente iteración
        current_size = 2 * current_size

# Ejemplo de uso
arr = [29, 10, 14, 37, 13]
straight_merge_sort(arr)
print("Arreglo ordenado:", arr)