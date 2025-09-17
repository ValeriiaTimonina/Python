class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = (float('inf'))
        self.edges = []
        self.previousVertex = None
 
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight 
 
class Dijkstra:
    def __init__(self):
        self.vertexes = []
    def computePath(self, sourceId):
        dist = dict()
        prev = dict()
        self.vertexes_id = dict()
        #Q = dict()
        unvisited = []
        counter = 0
        for v in self.vertexes:
            dist[v.id] = (float('inf'))
            prev[v.id] = None
            unvisited.append(counter)
            counter += 1
            self.vertexes_id[v.id] = v
        dist[sourceId] = 0
        while (len(unvisited) != 0):
            min_key = -1
            min_value = float('inf')
            min_index = -1
            for i in range(len(unvisited)):
                temp_value = dist[unvisited[i]]
                if (temp_value <= min_value):
                    min_value = temp_value
                    min_key = unvisited[i]
                    min_index = i
            del unvisited[min_index]
            for i in self.graph_dict[min_key]:
                if i in unvisited:
                    alt = dist[min_key] + self.graph_dict[min_key][i]
                    if alt < dist[i]:
                        dist[i] = alt
                        prev[i] = min_key
        for i in range (len(self.vertexes)):
            self.vertexes[i].minDistance = dist[self.vertexes[i].id]
            if prev[self.vertexes[i].id] != None:
                self.vertexes[i].previousVertex = self.vertexes_id[prev[self.vertexes[i].id]]
 
    def getShortestPathTo(self, targetId):
        shortest_path = []
        shortest_path.append(self.vertexes_id[targetId])
        curr_target = targetId
        while (self.vertexes_id[curr_target].previousVertex != None):
            shortest_path.append(self.vertexes_id[curr_target].previousVertex)
            if self.vertexes_id[curr_target].previousVertex == None:
                break
            curr_target = self.vertexes_id[curr_target].previousVertex.id
        shortest_path.reverse()
        return shortest_path
 
    def createGraph(self, vertexes, edgesToVertexes):
        for i in range(len(edgesToVertexes)):
            for j in range(len(vertexes)):
                if (edgesToVertexes[i].source == vertexes[j].id):
                    vertexes[j].edges.append(edgesToVertexes[i])
                    break
        self.vertexes = vertexes
        graph = dict()
        for i in vertexes:
            for j in edgesToVertexes:
                if (j.source == i.id):
                    if (i.id in graph) == False:
                        graph[i.id] = dict()
                    graph[vertexes[j.source].id][vertexes[j.target].id] = j.weight
        self.graph_dict = graph
 
    def resetDijkstra(self):
        for i in range (len(self.vertexes)):
            self.vertexes[i].minDistance = (float('inf'))
            self.vertexes[i].previousVertex = None
 
    def getVertexes(self):
        return self.vertexes