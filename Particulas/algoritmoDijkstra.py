from queue import PriorityQueue


class Dijkstra:
    def __init__(self):
        self.distancias = {}
        self.camino = {}
        self.cola = PriorityQueue()
        self.route = []

    def addDis(self, grafo, origen):
        for d in grafo.keys():
            self.distancias[d] = 1000000
        self.distancias[origen] = 0

    def addCam(self, grafo):
        for c in grafo.keys():
            self.camino[c] = ''

    def ruta(self, destino, origen):
        # recorremos el diccionario de caminos
        for k, v in self.camino.items():
            # condicion de paro
            if destino == origen:
                break
            # hacemos la busqueda
            if destino == k:
                # obtenemos la arista
                arista = (k, v)
                # agregamos a la lista
                self.route.append(arista)
                # ahora destino sera el vertice adyacente
                destino = v
                # hacemos recursion
                self.ruta(destino, origen)
                break

    def algoritmoD(self, grafo, origen):
        # diccionario Distancias
        self.addDis(grafo, origen)
        # diccionario Caminos
        self.addCam(grafo)

        n = (0, origen)
        # agregamos el origen a la lista ordenada
        self.cola.put(n)

        # mientras la cola no este vacia
        while not self.cola.empty():
            # se extrae de la lista ordenada el nodo n
            minimo = self.cola.get()
            adyacente = minimo[1]
            pesoOri = minimo[0]

            # por cada arista del nodo hacer
            for arista in grafo[adyacente]:
                destino = arista[0]
                pesoDes = arista[1]
                # sacamos el peso de la lista de distancias para comparar
                for key, value in self.distancias.items():
                    nuevoP = pesoOri + pesoDes

                    if key == destino:
                        weight = value
                        # si la distancia del nodo destino + la del nodo origen
                        # es menor a la del arreglo de distancias
                        if nuevoP < weight:
                            # se coloca la nueva distancia en el arreglo de distancias
                            self.distancias[key] = nuevoP
                            elegido = (nuevoP, key)

                            # se agrega en la posicion del nodo destino el nodo extraido
                            for llave, valor in self.camino.items():
                                if llave == destino:
                                    self.camino[llave] = adyacente
                            # se agrega el nodo destino a la lista ordenada
                            self.cola.put(elegido)

        print("Diccionario Distancias")
        for k, v in self.distancias.items():
            print(k, ":", v)

        print("\n", "Diccionario Camino", "\n")
        for key, value in self.camino.items():
            print(key, ":", value)
