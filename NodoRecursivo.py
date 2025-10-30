#INSTITUTO TECNOLOGICO DE SAN JUAN DEL RIO 
#ESTRUCTURA DE DATOS 
#UNIDAD 3
#NOMBRE : ROCIO MOLINA MONROY 
#-----------------------------------------------------------
class Nodo():
    dato = None
    siguiente = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def agregar_al_final_rec(nodo_actual, dato):
    # Si la lista está vacía, se crea un nuevo nodo como punto de partida.
    if nodo_actual is None:
        return Nodo(dato)
    
    # Si el nodo actual tiene un siguiente, seguimos recorriendo recursivamente.
    if nodo_actual.siguiente is not None:
        # Se actualiza el enlace al siguiente con el resultado de la recursión.
        nodo_actual.siguiente = agregar_al_final_rec(nodo_actual.siguiente, dato)
    # Si estamos al final de la lista, se añade el nuevo nodo.
    else:
        nodo_actual.siguiente = Nodo(dato)
        
    return nodo_actual

def imprimir_lista_rec(nodo):
    if nodo is not None:
        print(f"Tenemos {nodo.dato}")
        imprimir_lista_rec(nodo.siguiente)  # Continuamos con el siguiente nodo

def obtener_cola_rec(nodo):
    # Si el nodo es el último o la lista está vacía, lo devolvemos.
    if nodo is None or nodo.siguiente is None:
        return nodo
    
    # Si no es el último, seguimos avanzando.
    return obtener_cola_rec(nodo.siguiente)

def existe_rec(nodo, busqueda):
    # Si llegamos al final sin encontrar el valor, devolvemos False.
    if nodo is None:
        return False
    
    # Si el valor coincide con el buscado, devolvemos True.
    if nodo.dato == busqueda:
        return True
    
    # Si no coincide, seguimos buscando en el resto de la lista.
    return existe_rec(nodo.siguiente, busqueda)

def eliminar_rec(nodo, busqueda):
    # Si la lista está vacía, no hay nada que eliminar.
    if nodo is None:
        return None
        
    # Si el nodo actual contiene el dato a eliminar, lo saltamos.
    if nodo.dato == busqueda:
        return nodo.siguiente
        
    # Si no es el nodo a eliminar, seguimos con la recursión.
    nodo.siguiente = eliminar_rec(nodo.siguiente, busqueda)
    return nodo

def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

def obtener_cabeza(nodo_inicial):
    return nodo_inicial

def main():
    lista = None
    lista = agregar_al_final_rec(lista, "Luis")
    lista = agregar_al_final_rec(lista, "Leon")
    lista = agregar_al_inicio(lista, "Link")
    print("Antes de eliminar: ")
    imprimir_lista_rec(lista)
    
    lista = eliminar_rec(lista, "Link")
    print("\nDespués de eliminar 'Link': ")
    imprimir_lista_rec(lista)

    print("\nVerificaciones:")
    print(f"¿Existe 'Link'? {existe_rec(lista, 'Link')}")
    print(f"¿Existe 'Luis'? {existe_rec(lista, 'Luis')}")
    
    if lista is not None:
        print(f"Cabeza: {obtener_cabeza(lista).dato}")
        print(f"Cola: {obtener_cola_rec(lista).dato}")
    
main()