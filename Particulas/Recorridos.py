
class RecorridosG():
    def __init__(self):
        self.cola = []
        self.pila = []
        self.visitados = []
        self.visitadosP = []

    def anchura(self, o, grafo):
        # se coloca el origen en la cola
        self.cola.append(o)

        # mientras la cola no este vacia
        while self.cola:
            # desencolamos el vertice, sera el vertice actual
            actual = self.cola.pop(0)

            # si actual no esta la lista de visitados
            if actual not in self.visitados:
                # imprimimos actual
                print(actual)
                # añadimos vertice actual en visitados
                self.visitados.append(actual)

            for adyacente, peso in grafo[actual]:
                if adyacente not in self.visitados:
                    # encolamos el vertice adyacente
                    self.cola.append(adyacente)

    """def profundidad(self, o, grafo):
        # Colocamos el origen en la pila
        self.pila.append(o)

        # mientras la pila no este vacia
        while self.pila:

            # desapilar el vertice, sera el actual
            actual = self.pila.pop()

            # si actual no esta en los visitados
            if actual not in self.visitadosP:
                # imprimimos el vertice actual
                print("Actual: ", actual)
                # agregamos actual en la lista de visitados
                self.visitadosP.append(actual)
                print("Visitados: " ,self.visitadosP)


                for a, p in grafo[actual]:
                    if a not in self.visitadosP:
                        # apilamos el vertice adyacente
                        self.pila.append(a)
                        print("Pila: " , self.pila)
    """

    def profundidad(self, origen, grafo):

        self.pila.append(origen)
        self.visitadosP.append(origen)

        while self.pila:
            actual = self.pila.pop()
            print(actual)

            for adyacente, peso, in grafo[actual]:
                if adyacente not in self.visitadosP:
                    self.pila.append(adyacente)
                    self.visitadosP.append(adyacente)
