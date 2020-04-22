
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

            # para cada vertice que el vertice actual tiene como destino
            for adyacente, peso in grafo[actual]:
                # y que no ha sido visitado
                if adyacente not in self.visitados:
                    # encolamos el vertice adyacente
                    self.cola.append(adyacente)

    def profundidad(self, origen, grafo):
        # se coloca el origen en la pila
        self.pila.append(origen)
        # y en la lista de visitados
        self.visitadosP.append(origen)

        # mientras la pila no este vacia
        while self.pila:
            # desapilar el vertice, sera el vertice actual
            actual = self.pila.pop()
            # imprimimos actual
            print(actual)

            # para cada vertice que el vertice actual tiene como destino
            for adyacente, peso, in grafo[actual]:
                # y que no ha sido visitado
                if adyacente not in self.visitadosP:
                    # apilamos vertices adyacentes
                    self.pila.append(adyacente)
                    # agregamos vertices adyacentes
                    self.visitadosP.append(adyacente)

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
