#  Hecho por: 
# Hector Alejandro Ortega Gacria
# Registro: 21310248.
# Grupo: 6E
#-------------------------TEORIA--------------------------------
# Inserta cada elemento del arreglo en un árbol binario de búsqueda. Durante la inserción, el árbol se organiza de manera que para cualquier nodo, 
# todos los valores en su subárbol izquierdo son menores que el nodo y todos los valores en su subárbol derecho son mayores.
# Recorrido en Inorden:

# Una vez que todos los elementos están en el árbol, se realiza un recorrido en inorden. Este recorrido visita los nodos en orden ascendente:
# primero visita el subárbol izquierdo, luego el nodo actual, y finalmente el subárbol derecho. Esto garantiza que los elementos se recogen 
# en orden ascendente.
#-----------------------------------------------------------
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # Si el árbol está vacío, retornar un nuevo nodo
    if root is None:
        return TreeNode(key)
    
    # De lo contrario, recurrir hacia abajo en el árbol
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    
    # Retornar el (sub)árbol raíz
    return root

def inorder_traversal(root, res):
    # Si el nodo actual no es nulo, recorrer el subárbol izquierdo
    if root:
        inorder_traversal(root.left, res)
        # Agregar el valor del nodo a la lista de resultados
        res.append(root.val)
        # Recorrer el subárbol derecho
        inorder_traversal(root.right, res)

def tree_sort(arr):
    # Crear un árbol binario de búsqueda vacío
    if not arr:
        return []
    
    root = None
    # Insertar cada elemento del arreglo en el árbol binario de búsqueda
    for key in arr:
        root = insert(root, key)
    
    # Realizar un recorrido en inorden para obtener los elementos en orden
    sorted_arr = []
    inorder_traversal(root, sorted_arr)
    return sorted_arr

# Ejemplo de uso
arr = [29, 10, 14, 37, 13]
sorted_arr = tree_sort(arr)
print("Arreglo ordenado:", sorted_arr)