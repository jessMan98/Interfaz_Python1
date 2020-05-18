
class Kruskal:
    def __init__(self):
<<<<<<< Updated upstream
        #lista que contiene las aristas ordenadas
=======
        # lista que contiene las aristas ordenadas
>>>>>>> Stashed changes
        self.ordena = []
        # lista que contiene los conjuntos
        self.disjoint = []
        # contiene el grafo resultante
        self.grafo = []

    def Makeset(self, graph):
        # agregamos cada vertice a una lista(conjunto)
        for vertice in graph.keys():
            self.disjoint.append([vertice])

    def findSet(self, vertex):
        # recorremos los conjuntos
        for i in range(0, len(self.disjoint), 1):
            if vertex in self.disjoint[i]:
                # retornamos la posicion en la que esta el vertice
                return i

    def kruskalAR(self, particulas, graph):
        # recorremos las particulas
        for p in particulas:
            oX = p['origen']['x']
            oY = p['origen']['y']
            # almacenamos el origen
            origen = (oX, oY)

            dX = p['destino']['x']
            dY = p['destino']['y']
            # almacenamos el destino
            destiny = (dX, dY)

            for k in graph.keys():
                # si la llave es igual al origen
                if k == origen:
                    # almacenamos la velocidad
                    v = p['velocidad']
                    # agregamos la velocidad con su origen-destino
                    arista = (v, origen, destiny)
                    # agregamos la arista a la lista
                    self.ordena.append(arista)

                # mas si la llave es destino
                elif k == destiny:
                    v = p['velocidad']
                    # agregamos la velocidad con su destino-origen
                    arista2 = (v, destiny, origen)
                    # agregamos la arista a la lista
                    self.ordena.append(arista2)

        # Hacemos el Makeset a los vertices
        self.Makeset(graph)
        print(self.disjoint)

        # ordenamos nuestras arista Descendentemente
        self.ordena.sort(key=lambda a: a[0], reverse=True)

        # mientras la lista no este vacia
        while self.ordena:
            # eliminamos el mayor
            minimo = self.ordena.pop(0)
            print("Arista:", minimo)

            # sacamos el origen y destino
            vOrigen = minimo[1]
            vDestino = minimo[2]

            # buscamos en que conjunto estan los vertices
            o = self.findSet(vOrigen)
            d = self.findSet(vDestino)

            # si el vertice origen esta en diferente conjunto que el destino
            if o != d:
                # agregamos la arista al grafo resultante
                self.grafo.append(minimo)
                # Union de Conjuntos
                for union in range(len(self.disjoint)):
                    if union == o:
                        # unimos los conjuntos
                        self.disjoint[union].extend(self.disjoint[d])
                        # removemos el conjunto que se unio
                        self.disjoint.remove(self.disjoint[d])

            print(self.disjoint)
