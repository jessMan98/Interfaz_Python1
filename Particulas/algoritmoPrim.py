from queue import PriorityQueue


class Algoritmos:
    def __init__(self):
        self.cola = PriorityQueue()
        self.visitados = []
        self.grafoN = []

    def arbolEM(self, graph, origen):
        # agregar el nodo inicial a la lista de visitados
        self.visitados.append(origen)

        # agregar sus adyacentes a la cola de prioridad
        for edge in graph[origen]:
            destino = edge[0]
            peso = edge[1]
            arista = (peso, origen, destino)
            self.cola.put(arista)

        # mientras la cola no este vacia
        while not self.cola.empty():
            # tomar la arista minima y eliminarla
            minimo = self.cola.get()
            # guardamos el destino de minimo
            d = minimo[2]

            # si el destino no esta en la lista de visitados
            if d not in self.visitados:
                # agregar el nodo destino a la lista de visitados
                self.visitados.append(d)
                # agregamos la arista el grafo resultante
                self.grafoN.append(minimo)

                # agregar los adyacentes que no han sido visitados a la cola
                for i in graph[d]:
                    vertice = i[0]
                    weigth = i[1]
                    adyacente = (weigth, d, vertice)

                    if vertice not in self.visitados:
                        self.cola.put(adyacente)