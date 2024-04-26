import pandas as pd  # Importa la biblioteca pandas para trabajar con datos tabulares
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para trazar gráficos

# Definición de la clase Libro
class Libro:
    def __init__(self, id, titulo, autor, estadoAct):
        self.id = id  # Identificador del libro
        self.titulo = titulo  # Título del libro
        self.autor = autor  # Autor del libro
        self.estadoAct = estadoAct  # Estado actual del libro

# Definición de la clase NodoAVL
class NodoAVL:
    def __init__(self, libro):
        self.root=None  # Nodo raíz del árbol AVL (no utilizado en este caso)
        self.libro = libro  # Libro asociado al nodo
        self.izquierda = None  # Referencia al hijo izquierdo del nodo
        self.derecha = None  # Referencia al hijo derecho del nodo
        self.altura = 1  # Altura del nodo (utilizada para el balanceo del árbol AVL)

# Definición de la clase AVL
class AVL:
    def __init__(self):
        self.raiz = None  # Nodo raíz del árbol AVL
        self.indice_titulo = {}  # Índice para buscar libros por título
        self.indice_autor = {}  # Índice para buscar libros por autor

    # Función para trazar el árbol AVL
    def plot_avl(self, nodo, x=0, y=0, depth=1):
        if nodo:
            # Agrega el identificador del libro como texto en la posición (x, y) del gráfico
            plt.text(x, y, str(nodo.libro.id), bbox=dict(facecolor='white', alpha=0.5), horizontalalignment='center')
            # Si el nodo tiene un hijo izquierdo, traza una línea desde el nodo actual al hijo izquierdo
            if nodo.izquierda:
                left_x = x - 2 ** (5 - depth)  # Calcula la posición x del hijo izquierdo
                left_y = y - 1  # Calcula la posición y del hijo izquierdo
                plt.plot([x, left_x], [y, left_y], 'k-')  # Trazar línea desde el nodo actual al hijo izquierdo
                self.plot_avl(nodo.izquierda, left_x, left_y, depth + 1)  # Llama recursivamente a la función para el hijo izquierdo
            # Si el nodo tiene un hijo derecho, traza una línea desde el nodo actual al hijo derecho
            if nodo.derecha:
                right_x = x + 2 ** (5 - depth)  # Calcula la posición x del hijo derecho
                right_y = y - 1  # Calcula la posición y del hijo derecho
                plt.plot([x, right_x], [y, right_y], 'k-')  # Trazar línea desde el nodo actual al hijo derecho
                self.plot_avl(nodo.derecha, right_x, right_y, depth + 1)  # Llama recursivamente a la función para el hijo derecho


        # Función para trazar el árbol AVL
    
    def plot_tree(self):
        plt.figure(figsize=(10, 6))  # Crea una nueva figura para el gráfico con tamaño 10x6 pulgadas
        self.plot_avl(self.raiz)  # Llama al método plot_avl para trazar el árbol AVL a partir de la raíz
        plt.show()  # Muestra el gráfico

    # Función para obtener la altura de un nodo
    def altura(self, nodo):
        if not nodo:  # Si el nodo no existe (es None), devuelve 0
            return 0
        return nodo.altura  # Devuelve la altura del nodo

    # Función para calcular el balance de un nodo
    def balance(self, nodo):
        if not nodo:  # Si el nodo no existe (es None), devuelve 0
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)  # Calcula el balance del nodo

    # Función para realizar una rotación a la derecha
    def rotacion_derecha(self, y):
        x = y.izquierda  # El nodo izquierdo de y se convierte en x
        T2 = x.derecha  # El subárbol derecho de x se convierte en T2

        # Realiza la rotación a la derecha
        x.derecha = y  # y se convierte en el subárbol derecho de x
        y.izquierda = T2  # T2 se convierte en el subárbol izquierdo de y

        # Actualiza las alturas de los nodos
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        # Actualiza las alturas de los nodos
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))

        return x  # Devuelve el nuevo nodo raíz del subárbol rotado

    # Función para realizar una rotación a la izquierda
    def rotacion_izquierda(self, x):
        y = x.derecha  # El nodo derecho de x se convierte en y
        T2 = y.izquierda  # El subárbol izquierdo de y se convierte en T2

        # Realiza la rotación a la izquierda
        y.izquierda = x  # x se convierte en el subárbol izquierdo de y
        x.derecha = T2  # T2 se convierte en el subárbol derecho de x

        # Actualiza las alturas de los nodos
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y  # Devuelve el nuevo nodo raíz del subárbol rotado


        # Función para insertar un nuevo libro en el árbol AVL
    
    def insertar(self, nodo, libro):
        if not nodo:  # Si el nodo no existe (es None), crea un nuevo nodo con el libro y lo devuelve
            return NodoAVL(libro)
        elif libro.id < nodo.libro.id:  # Si el ID del libro es menor que el ID del nodo actual
            nodo.izquierda = self.insertar(nodo.izquierda, libro)  # Inserta el libro en el subárbol izquierdo
        else:
            nodo.derecha = self.insertar(nodo.derecha, libro)  # Inserta el libro en el subárbol derecho

        nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))  # Actualiza la altura del nodo

        balance = self.balance(nodo)  # Calcula el balance del nodo

        # Realiza rotaciones si el árbol se ha desequilibrado
        if balance > 1:
            if libro.id < nodo.izquierda.libro.id:
                return self.rotacion_derecha(nodo)
            else:
                nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
                return self.rotacion_derecha(nodo)

        if balance < -1:
            if libro.id > nodo.derecha.libro.id:
                return self.rotacion_izquierda(nodo)
            else:
                nodo.derecha = self.rotacion_derecha(nodo.derecha)
                return self.rotacion_izquierda(nodo)

        return nodo  # Devuelve el nodo actualizado

    # Función para eliminar un libro del árbol AVL
    def eliminar(self, raiz, id):
        if not raiz:  # Si la raíz es None, devuelve None
            return raiz

        # Busca el libro a eliminar según su ID
        if id < raiz.libro.id:
            # Si el ID del libro es menor que el ID del nodo actual, busca en el subárbol izquierdo
            raiz.izquierda = self.eliminar(raiz.izquierda, id)
        # Si el ID del libro es mayor que el ID del nodo actual, busca en el subárbol derecho    
        elif id > raiz.libro.id:
            # Si el ID del libro es mayor que el ID del nodo actual, busca en el subárbol derecho
            raiz.derecha = self.eliminar(raiz.derecha, id)
        # Si el ID del libro es igual al ID del nodo actual, elimina el nodo    
        else:
            # Si el nodo tiene un solo hijo o ninguno, elimina el nodo y ajusta el árbol
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            # Si el nodo tiene dos hijos, encuentra el sucesor inmediato, lo copia y elimina el nodo sucesor
            temp = self.nodo_min_value(raiz.derecha)
            raiz.libro = temp.libro
            raiz.derecha = self.eliminar(raiz.derecha, temp.libro.id)

        # Actualiza la altura del nodo raíz y realiza rotaciones si el árbol se ha desequilibrado
        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.balance(raiz)

        if balance > 1:
            if self.balance(raiz.izquierda) >= 0:
                return self.rotacion_derecha(raiz)
            else:
                raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
                return self.rotacion_derecha(raiz)

        if balance < -1:
            if self.balance(raiz.derecha) <= 0:
                return self.rotacion_izquierda(raiz)
            else:
                raiz.derecha = self.rotacion_derecha(raiz.derecha)
                return self.rotacion_izquierda(raiz)

        return raiz  # Devuelve el nodo raíz actualizado


       # Función para encontrar el nodo con el valor mínimo en un subárbol
    
    # Función para encontrar el nodo con el valor mínimo en un subárbol
    def nodo_min_value(self, nodo):
        # Encuentra el nodo más a la izquierda en el subárbol
        actual = nodo
        # Mientras haya nodos a la izquierda, sigue avanzando
        while actual.izquierda is not None:
            # Actualiza el nodo actual al nodo a la izquierda
            actual = actual.izquierda
        # Devuelve el nodo con el valor mínimo
        return actual

    # Función para buscar un libro por su ID en el árbol AVL
    def buscar(self, nodo, id):
        # Si el nodo es None, devuelve None
        if not nodo:
            return None
        # Si el ID del libro es igual al ID del nodo actual, devuelve el libro
        elif nodo.libro.id == id:
            # Devuelve el libro
            return nodo.libro
        # Si el ID del libro es menor que el ID del nodo actual, busca en el subárbol izquierdo
        elif id < nodo.libro.id:
            # Llama recursivamente a la función para el subárbol izquierdo
            return self.buscar(nodo.izquierda, id)
        else:
            # Llama recursivamente a la función para el subárbol derecho
            return self.buscar(nodo.derecha, id)

    # Función para prestar un libro según su ID
    def prestar_libro(self, nodo, id):
        # Busca el libro por su ID
        libro = self.buscar(nodo, id)
        # Si el libro existe
        if libro:
            # Si el libro está disponible, lo presta
            if libro.estadoAct == "Disponible":  # Si el libro está disponible
                print(f"\nLibro '{libro.titulo}' prestado correctamente.\n")
            # Si el libro está prestado, muestra un mensaje
            elif libro.estadoAct == "reservado":  # Si el libro está reservado
                print(f"\nLo siento, el libro '{libro.titulo}' ya se encuentra reservado.\n")
        else:
            # Si el libro no existe, muestra un mensaje
            print("Libro no encontrado.")

    # Función para devolver un libro prestado según su ID
    def devolver_libro(self, nodo, id):
        # Busca el libro por su ID
        libro = self.buscar(nodo, id)
        # Si el libro existe
        if libro:
            # Si el libro está prestado, lo devuelve
            if libro.estadoAct == "disponible":
                # Si el libro está disponible, muestra un mensaje
                print(f"El libro '{libro.titulo}' no estaba prestado.")
            # Si el libro está prestado, lo devuelve    
            else:
              print(f"Libro '{libro.titulo}' devuelto correctamente.")  
        # Si el libro no existe, muestra un mensaje      
        else:
            print("Libro no encontrado.")

    # Función para recorrer el árbol en orden (izquierda, raíz, derecha)   
    def recorrer_inorden(self, nodo):
        # Si el nodo no es None
        if nodo:
            self.recorrer_inorden(nodo.izquierda)  # Recorre el subárbol izquierdo
            # Imprime los detalles del libro actual
            print(f"ID: {nodo.libro.id}, \n Título: {nodo.libro.titulo}, \n Autor: {nodo.libro.autor}, \n Estado: {nodo.libro.estadoAct}\n")
            self.recorrer_inorden(nodo.derecha)  # Recorre el subárbol derecho

    # Función para recorrer el árbol en preorden (raíz, izquierda, derecha)
    def recorrer_preorden(self, nodo):
        if nodo:
            # Imprime los detalles del libro actual
            print(f"ID: {nodo.libro.id}, \n Título: {nodo.libro.titulo}, \n Autor: {nodo.libro.autor}, \n Estado: {nodo.libro.estadoAct}\n")
            self.recorrer_preorden(nodo.izquierda)  # Recorre el subárbol izquierdo
            self.recorrer_preorden(nodo.derecha)  # Recorre el subárbol derecho

    # Función para recorrer el árbol en postorden (izquierda, derecha, raíz)
    def recorrer_postorden(self, nodo):
        if nodo:
            self.recorrer_postorden(nodo.izquierda)  # Recorre el subárbol izquierdo
            self.recorrer_postorden(nodo.derecha)  # Recorre el subárbol derecho
            # Imprime los detalles del libro actual
            print(f"ID: {nodo.libro.id}, \n Título: {nodo.libro.titulo}, \n Autor: {nodo.libro.autor}, \n Estado: {nodo.libro.estadoAct}\n")

    # Función para cargar libros desde un archivo Excel en el árbol AVL
    def cargar_libros_desde_excel(self, archivo):

        df = pd.read_excel(archivo)  # Lee el archivo Excel y carga los datos en un DataFrame
        for index, row in df.iterrows():  # Itera sobre cada fila del DataFrame
            id = int(row['id'])  # Obtiene el ID del libro de la fila
            titulo = row['titulo']  # Obtiene el título del libro de la fila
            autor = row['autor']  # Obtiene el autor del libro de la fila
            estado = row['estado']  # Obtiene el estado del libro de la fila
            libro_instance = Libro(id, titulo, autor, estado)  # Crea una instancia de libro con los datos de la fila
            self.raiz = self.insertar(self.raiz, libro_instance)  # Inserta el libro en el árbol AVL

            # Construye un índice por título
            if titulo in self.indice_titulo:
                self.indice_titulo[str(titulo)].append(libro_instance)
            else:
                self.indice_titulo[str(titulo)] = [libro_instance]

            # Construye un índice por autor
            if autor in self.indice_autor:
                self.indice_autor[autor].append(libro_instance)
            else:
                self.indice_autor[autor] = [libro_instance]

                
        # Función para buscar libros por autor en el árbol AVL
    
    def buscar_por_autor(self, autor):
        if autor in self.indice_autor:  # Verifica si hay libros del autor en el índice
            libros = self.indice_autor[autor]  # Obtiene la lista de libros del autor
            for libro in libros:  # Itera sobre cada libro del autor
                # Imprime los detalles del libro (ID, título, autor, estado)
                print(f" \nID: {libro.id},\n Título: {libro.titulo},\n Autor: {libro.autor},\n Prestado: {libro.estadoAct}\n")
        else:
            print("No se encontraron libros de ese autor.")  # Imprime un mensaje si no se encuentran libros del autor

    # Función para buscar libros por título en el árbol AVL
    def buscar_por_titulo(self, titulo):
        if titulo in self.indice_titulo:  # Verifica si hay libros con el título en el índice
            libros = self.indice_titulo[titulo]  # Obtiene la lista de libros con el título
            for libro in libros:  # Itera sobre cada libro con el título
                # Imprime los detalles del libro (ID, título, autor, estado)
                print(f" \nID: {libro.id}\n Título: {libro.titulo}\n Autor: {libro.autor},\n Estado: {libro.estadoAct}\n")
        else:
            print("No se encontraron libros con ese título.")  # Imprime un mensaje si no se encuentran libros con el título

    # Función para verificar si el árbol está vacío
    def esta_vacio(self):
        return self.raiz is None  # Retorna True si la raíz del árbol es None (vacío), False de lo contrario

    # Función para contar el número de nodos en el árbol
    def contar_nodos(self, nodo):
        # Si el nodo es None, devuelve 0
        if nodo is None:
            return 0
        # Si el nodo no es None, cuenta el nodo actual y los nodos de los subárboles izquierdo y derecho
        else:
            return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    # Función para contar el número de hojas en el árbol
    def factor_balance(self, nodo):
            # Si el nodo es None, devuelve 0
            if nodo is None:
                return 0
            # Si el nodo no es None, calcula el factor de balance del nodo
            return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    # Función para obtener la altura de un nodo
    def altura(self, nodo):
            # Si el nodo es None, devuelve 0
            if nodo is None:
                return 0
            # Si el nodo no es None, devuelve la altura del nodo
            return nodo.altura
    
    # Función para buscar un libro por su título y autor en el árbol AVL
    def buscar_libro_por_titulo_autor(self, titulo, autor):
        """
        Busca un libro por su título y autor en el árbol AVL.
        Devuelve True si encuentra un libro con el mismo título y autor, False en caso contrario.
        """
        # Inicializa una cola para el recorrido BFS
        cola = [self.raiz]

        # Realiza un recorrido BFS hasta encontrar el libro o agotar todos los nodos
        while cola:
            # Extrae el primer nodo de la cola
            nodo_actual = cola.pop(0)

            # Verifica si el libro en el nodo actual coincide con el título y autor buscados
            if nodo_actual.libro.titulo == titulo and nodo_actual.libro.autor == autor:
                return True

            # Agrega los hijos del nodo actual a la cola si existen
            if nodo_actual.izquierda:
                # Si el hijo izquierdo existe, lo agrega a la cola
                cola.append(nodo_actual.izquierda)
            # Agrega el hijo derecho del nodo actual a la cola si existe    
            if nodo_actual.derecha:
                # Si el hijo derecho existe, lo agrega a la cola
                cola.append(nodo_actual.derecha)

        # Si se recorrió todo el árbol y no se encontró el libro, devuelve False
        return False