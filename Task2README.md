<details type="reasoning" done="true" duration="71">
&gt; **Comprehending the Objective**
&gt; 
&gt; I&#x27;m focused on grasping the user&#x27;s need to shift from Chinese Markdown to English. The core lies in leveraging Task 2 materials – reports, requirements, alongside two Python scripts – as the foundation. My immediate aim is to accurately assess the content&#x27;s essence, paving the way for a faithful English rendition.
&gt; 
&gt; 
&gt; **Translating the Initial Draft**
&gt; 
&gt; I&#x27;ve begun the translation draft, starting with the title and introduction. I&#x27;m focusing on accurately conveying the original intent regarding the course requirements and the algorithms used, while maintaining the citation integrity. I am now proceeding to translate the first part regarding the Graph ADT implementation.
&gt; 
&gt; 
&gt; **Detailing the Implementation**
&gt; 
&gt; I&#x27;m zeroing in on detailing the Graph ADT implementation. I am now proceeding with detailing the nested dictionary&#x27;s functioning and its role in representing the graph&#x27;s vertices and edges, as well as the functionality of the methods used for the ADT. The focus remains on clear and faithful translation.
&gt; 
&gt; 
&gt; **Revising Code Explanations**
&gt; 
&gt; I&#x27;m now refining the explanations of the code snippets, focusing on clarity. I&#x27;m reviewing the function descriptions like `add_vertex` and `add_edge`, ensuring that the explanations align with the actual Python code and are clear for the reader. The use of nested dictionaries needs further elucidation.
&gt; 
&gt; 
&gt; **Finalizing Dijkstra&#x27;s Details**
&gt; 
&gt; I&#x27;m now detailing Dijkstra&#x27;s Algorithm implementation. I&#x27;m focusing on clarifying the roles of the data containers, especially `distances`, `previous_vertices`, and the `unvisited_vertices` set. I&#x27;m also ensuring the function explanations like `calculate` and `get_shortest_path` are accurate.
&gt; 
&gt; 
&gt; **Evaluating Content and Structure**
&gt; 
&gt; I&#x27;m now deeply immersed in the nuances of the original content. I have broken down all the content and am mapping the structure to ensure a faithful reproduction of the original intent and presentation. Specific attention is given to the source citations.
&gt; 
&gt; 
&gt; **Evaluating Iterative Refinements**
&gt; 
&gt; I&#x27;m now refining the draft, focusing on improving clarity of each section. I&#x27;m focusing on the descriptions of the functions, as well as the roles of the data containers used. Further, I am making sure the code snippets are consistent with the actual Python code.
&gt; 
&gt; 
&gt; **Evaluating Function Descriptions**
&gt; 
&gt; I&#x27;m now deep-diving into the function descriptions within both the `Graph` and `Dijkstra` classes. Specifically, I&#x27;m focusing on clarity and precision. I&#x27;m verifying the descriptions, such as `add_vertex` and `add_edge`, align with the Python code&#x27;s actual behavior and purpose, and are clear for the reader.
&gt; 
&gt; 
&gt; **Synthesizing Draft Refinements**
&gt; 
&gt; I&#x27;m now integrating the user&#x27;s feedback by revising the code explanations. I&#x27;m focusing on the `add_edge` method and its role in connecting vertices, ensuring the explanations reflect the undirected graph logic with accurate citations. The next step will be to verify citations.
</details>
Here is the English translation of the Markdown README file generated based on the COMP2090SEF Task 2 requirements, learning report, and your code.

***

# COMP2090SEF Task 2: Graph Data Structure & Dijkstra's Algorithm

This project is developed to fulfill the requirements of the COMP2090SEF course Task 2, mainly demonstrating the self-study and application of a new data structure (Graph) and a new algorithm (Dijkstra's Algorithm) that were not covered in class [1], [2].

This project calculates the shortest path between cities using Dijkstra's algorithm by building a weighted undirected graph (implemented with nested dictionaries) [2], [3].

---

## Part 1: Graph ADT (Abstract Data Type Implementation)

In this project, the Graph is implemented using an **Adjacency List** format, specifically adopting the **Nested Dictionaries** structure in Python [2].

### 1. Explanation of Functions (def) in the `Graph` Class

*   `__init__(self)`: Initializes the graph structure, creating an empty parent dictionary `self.adj_list` to store graph information [3], [4].
*   `add_vertex(self, v)`: Adds a new vertex to the graph. If the vertex does not exist, it is added to the dictionary as a key [2], [3].
*   `add_edge(self, v1, v2, weight=1)`: Adds a weighted edge. It is used to connect two vertices in the graph and record the weight between them [3], [4].
*   `get_vertices(self)`: Retrieves the set of all vertices in the current graph [3], [4].
*   `get_neighbors(self, v)`: Gets all adjacent vertices and their corresponding weights for a specified vertex [3], [4].
*   `display(self)`: Prints and outputs the complete adjacency list structure of the current graph, which is used to verify whether the data is stored correctly [3], [4].

### 2. The Role and Working Principle of Nested Dictionaries

The core of our graph structure relies on a nested dictionary: `self.adj_list = {}`.
*   **Parent Dictionary**: The key is every **Vertex** in the graph.
*   **Sub-dictionary**: The value is another dictionary. The key of this sub-dictionary is the **Neighbor** of that vertex, and the value is the **Weight** between them [2].

**Explanation with Code**:
```python
def add_vertex(self, v):
    if v not in self.adj_list:
        self.adj_list[v] = {} # Allocate an empty sub-dictionary for the newly added vertex to store adjacent nodes and weights later
        return True
```
Here, the empty dictionary `{}` plays an extremely important role; it ensures that when a new node is introduced to the graph, the graph has a container to receive and record its adjacent connection relationships [2].

### 3. How Graph Data is Uploaded and Information is Obtained

*   **Uploading Data (Adding vertices and edges)**: 
    Use `add_vertex(v)` to add nodes to the graph (the program internally avoids adding duplicate vertices via an `if` statement). Then use `add_edge(v1, v2, weight)` to establish connections [2]. Because this is an undirected graph, the code will mutually record each other and the weight in the sub-dictionaries of the two connected vertices:
    ```python
    self.adj_list[v1][v2] = weight
    self.adj_list[v2][v1] = weight
    ```
*   **Getting Vertices**: 
    Extract all keys from the parent dictionary using the `.keys()` method, and convert them to a list to return `return list(self.adj_list.keys())` [2], [3].
*   **Getting Neighbors and Edges**: 
    Use `self.adj_list.get(v, {})` to get the sub-dictionary of the corresponding vertex. If the vertex does not exist, an empty dictionary is returned to prevent errors [2], [3].
*   **Getting All Information**: 
    The `display(self)` method uses a `for` loop to iterate through the parent dictionary `self.adj_list`, printing out each vertex and its corresponding sub-dictionary (i.e., all adjacent vertices and distance weights) [2], [3].

### 4. Method to Run the Program
For solely testing the Graph ADT structure (e.g., `Graph.py`), you only need to open the script file using any Python IDE (such as PyCharm, VSCode, etc.), and **directly click the Run button**. You will then see the graph structure, node list, and adjacent node information of a specified node in the console [4].

---

## Part 2: Dijkstra's Algorithm

After building the graph data structure, we use Dijkstra's algorithm to find the shortest path between any two points (e.g., cities).

### 1. Explanation of Functions (def) in the `Dijkstra` Class

*   `__init__(self, graph)`: Receives a graph object, initializes it, and declares data containers used for the algorithm's calculation [3].
*   `calculate(self, start)`: The core of the algorithm. It is responsible for calculating the shortest path distance from a given starting point `start` to all other vertices in the graph, and updating the path tracking dictionary [3].
*   `get_shortest_path(self, end)`: Based on the path tracking dictionary generated by `calculate`, it backtracks and outputs the complete path from the starting point to the specified `end` point [3].

### 2. The Role of Data Containers During Initialization

In the initialization phase of `__init__` and `calculate`, we set up three key data containers:
*   **`self.distances = {}` (Dictionary)**: Used to record the currently known shortest distance from the starting point to all other vertices in the graph. Initially, the distance of the starting point is 0, and the distances to the rest are set to infinity `float('inf')` [3].
*   **`self.previous = {}` (Dictionary)**: Used to record the **previous vertex** (i.e., the last node) on the shortest path to the current vertex. This is crucial for tracing the complete path at the end. Initially, all values are `None` [3].
*   **`self.unvisited = []` (List)**: Records all vertices that have not yet completed the shortest path calculation. Initially, all vertices in the graph are stored in this list [3].

### 3. The Core Loop Logic of the Algorithm (Combined with Code)

*   **Outer `while` loop**: 
    ```python
    while self.unvisited:
    ```
    As long as there are unvisited nodes, the loop continues, ensuring every reachable node is fully evaluated [3].
    
*   **`for` loop to find the shortest path node**: 
    ```python
    for node in self.unvisited:
        if self.distances[node] < min_distance:
            ...
    ```
    Among all currently unvisited nodes, iterate to find the node `current_node` with the smallest currently known distance (`self.distances`) as the next jump point [3].
    
*   **`for` loop to update adjacent node paths**: 
    ```python
    neighbors = self.graph.get_neighbors(current_node)
    for neighbor, weight in neighbors.items():
        new_distance = self.distances[current_node] + weight
        if new_distance < self.distances[neighbor]:
            self.distances[neighbor] = new_distance
            self.previous[neighbor] = current_node
    ```
    Iterate through all adjacent nodes of the current node. If the "distance to reach the current node + the weight of the adjacent edge" **is less than** the "currently recorded distance to reach the adjacent node", update the minimum distance in the `distances` dictionary, and update the `previous` dictionary, recording that the predecessor node for this optimal path is `current_node` [3].

### 4. How the Algorithm Traces the Path

When all shortest distance calculations are completed, call `get_shortest_path(self, end)` to backtrack the path.
```python
while current is not None:
    path.append(current)
    current = self.previous[current]
path.reverse()
```
This utilizes the previously saved `previous` dictionary. Starting from the target `end` point, it continuously looks up its previous node (i.e., where it came from in the previous step) and appends them one by one to the `path` list until the previous node is `None` (i.e., it has backtracked to the starting point). Finally, use `.reverse()` to flip the list to get a forward-flowing route from the start to the end [3].

### 5. Data Uploading and Program Running Method

*   **Data Uploading (Main Block Initialization)**: 
    The graph and route data are hardcoded and uploaded in the `if __name__ == "__main__":` block at the bottom of the file.
    First, instantiate the graph `city_map = Graph()`. Then, pass the list containing city names into `add_vertex` through a for loop, and call `city_map.add_edge()` multiple times to manually input the distances and connections between pairs of cities [3]. Finally, instantiate `dijkstra = Dijkstra(city_map)`, pass in the prepared graph structure, and execute the calculation.
    
*   **Program Running Method**:
    Ensure you have configured your Python environment. Open the `Dijkstra_Algorithm.py` file in your code editor or IDE, and **click the "Run" button at the top of the code editor**, or type `python Dijkstra_Algorithm.py` in your terminal. The program will automatically print the shortest distances and detailed routes from Beijing to all other cities in the terminal [3].
