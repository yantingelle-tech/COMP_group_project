class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        """Add vertex"""
        if v not in self.adj_list:
            self.adj_list[v] = {}
            return True
        return False

    def add_edge(self, v1, v2, weight=1):
        """Add weighted edges. In an undirected graph,
        the default weights are the same for bidirectional edges"""
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1][v2] = weight
            self.adj_list[v2][v1] = weight
            return True
        return False

    def get_vertices(self):
        """Obtain all vertices """
        return list(self.adj_list.keys())

    def get_neighbors(self, v):
        """Obtain the adjacent vertices
        and their weights of the specified vertex"""
        return self.adj_list.get(v, {})

    def display(self):
        """Print the adjacency list structure
        of the graph for verification"""
        for vertex in self.adj_list:
            print(f"{vertex} → {self.adj_list[vertex]}")

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph   #upload graph                                                                   
        self.distances = {}  #store the shorest distance from strart vertex to other vertex                                                                   
        self.previous = {}   #record thee preverious vertex of  any of the vertex                              
        self.unvisited = []  # record the unvisited vertex                                                                   

    def calculate(self, start):
        """Calculate the shortest path from the starting point to all points"""
        # 1. Initialization
        vertices = self.graph.get_vertices()
        for vertex in vertices:
            self.distances[vertex] = float('inf')  # The initial distance is infinite
            self.previous[vertex] = None
            self.unvisited.append(vertex)

        self.distances[start] = 0  # The distance from the starting point to oneself is 0

        # 2. Traverse all unvisited nodes
        while self.unvisited: # do it if there exists unvisited node
            # Find the node with the smallest current distance
            min_distance = float('inf')
            current_node = None
            for node in self.unvisited:
                if self.distances[node] < min_distance:
                    min_distance = self.distances[node]
                    current_node = node
            # Unable to reach the remaining nodes, exit
            if current_node is None or self.distances[current_node] == float('inf'):
                break
            # 3. Remove the visited nodes
            self.unvisited.remove(current_node)
            # 4. Traverse the neighbors and update the distance
            neighbors = self.graph.get_neighbors(current_node)
            for neighbor, weight in neighbors.items():
                # make sure we are searching for outbound edges
                if neighbor not in self.unvisited:
                    continue
                # Calculate the length of the new path
                new_distance = self.distances[current_node] + weight

                if new_distance < self.distances[neighbor]:
                    self.distances[neighbor] = new_distance
                    self.previous[neighbor] = current_node

        return self.distances, self.previous

    def get_shortest_path(self, end):
        """Obtain the complete path to the target city"""
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.previous[current]

        path.reverse()
        return path


if __name__ == "__main__":
    # 1.create graph
    city_map = Graph()

    # Add city(Vertices)
    cities = ["Beijing", "Shanghai", "Hangzhou", "Guangzhou", "Shenzhen"]
    for city in cities:
        city_map.add_vertex(city)

    # Add route (edge + weight)
    city_map.add_edge("Beijing", "Shanghai", 1318)
    city_map.add_edge("Shanghai", "Hangzhou", 178)
    city_map.add_edge("Shanghai", "Guangzhou", 1212)
    city_map.add_edge("Guangzhou", "Shenzhen", 137)
    city_map.add_edge("Hangzhou", "Guangzhou", 1150)
    city_map.add_edge("Shanghai", "Shenzhen", 1210)

    # 2. Run the Dijkstra (starting point: Beijing)
    dijkstra = Dijkstra(city_map)
    distances, previous = dijkstra.calculate("Beijing")

    # 3. output
    print("The shortest distance from Beijing to all cities\n")
    for city, dist in distances.items():
        path = dijkstra.get_shortest_path(city)
        print(f"{city:10} : {dist:4} Km   Route: {' → '.join(path)}")