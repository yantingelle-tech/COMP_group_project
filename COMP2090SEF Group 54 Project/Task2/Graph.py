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


if __name__ == "__main__":
    city_map = Graph()
    cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou"]
    for city in cities:
        city_map.add_vertex(city)
    """Add weighted edge"""
    city_map.add_edge("Beijing", "Shanghai", 1318)
    city_map.add_edge("Shanghai", "Hangzhou", 178)
    city_map.add_edge("Shanghai", "Guangzhou", 1212)
    city_map.add_edge("Guangzhou", "Shenzhen", 137)
    city_map.add_edge("Hangzhou", "Guangzhou", 1150)
    city_map.add_edge("Shanghai", "Shenzhen", 1210)
    """Print graph"""
    print("City →{Adjacent cities: Distance}）：")
    city_map.display()

    theVertex = city_map.get_vertices()
    print(theVertex)

    theNeighbor = city_map.get_neighbors("Shanghai")
    print(theNeighbor)

