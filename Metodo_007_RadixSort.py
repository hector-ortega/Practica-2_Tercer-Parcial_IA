#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# Funcionamiento del Algoritmo
# División en Dígitos:

# Radix Sort procesa cada número desde el dígito menos significativo hasta
# el dígito más significativo (esto se llama "Least Significant Digit first" o LSD Radix Sort).
# Ordenamiento por Dígitos:

# Para cada posición de dígito (unidades, decenas, centenas, etc.), el algoritmo utiliza Counting Sort para ordenar los números según ese dígito.
# Counting Sort:

# Counting Sort se usa para ordenar los números basándose en un dígito específico. Este subalgoritmo cuenta las ocurrencias de cada
# dígito y luego coloca los números en su posición correcta.
# Repetición:

# El proceso se repite para cada posición de dígito, desde las unidades hasta el dígito más significativo. Después de ordenar por el último dígito,
# el arreglo completo está ordenado.
#-----------------------------------------------------------
def counting_sort_for_radix(arr, exp):
    # Inicializar el conteo y el arreglo de salida
    n = len(arr) # Obtiene la longitud del arreglo.
    output = [0] * n #Inicializa el arreglo de salida con ceros.
    count = [0] * 10 # Inicializa el arreglo de conteo con ceros para cada dígito (0-9).
    
    # Contar las ocurrencias de cada dígito en la posición actual (exp)
    for i in range(n): #Recorre cada elemento del arreglo.
        index = arr[i] // exp # Obtiene el dígito correspondiente a la posición exp.
        count[index % 10] += 1 #Incrementa el conteo para ese dígito.
    
    # Actualizar count[i] para contener la posición actual de este dígito en output[]
    for i in range(1, 10): #Actualiza el conteo acumulado.
        count[i] += count[i - 1] # Suma el conteo actual al anterior para obtener la posición correcta en el arreglo de salida.
    
    # Construir el arreglo de salida
    i = n - 1 #Inicializa el índice i al final del arreglo
    while i >= 0: #Recorre el arreglo de derecha a izquierda.
        index = arr[i] // exp #Obtiene el dígito correspondiente
        output[count[index % 10] - 1] = arr[i] #Coloca el elemento en su posición correcta en el arreglo de salida.
        count[index % 10] -= 1 #Decrementa el conteo.
        i -= 1 # Decrementa el índice.
    
    # Copiar el arreglo de salida a arr[], para que arr[] ahora contenga los números ordenados según el dígito actual
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número máximo para saber el número de dígitos
    max1 = max(arr)
    
    # Hacer counting sort para cada dígito. Nota que en lugar del dígito, se pasa exp.
    # exp es 10^i donde i es el dígito actual
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Arreglo ordenado:", arr)