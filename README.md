# Intelligent Wardrobe Management and Outfit Recommendation System (INTELLIGENCE Wardrobe)

## Project Overview
With the accelerating pace of life, people own an increasing number of clothes, making it easy to forget where items are stored or leaving no time to plan daily outfits. This project aims to develop a multi-module Python application utilizing Object-Oriented Programming (OOP) to help users effectively manage their wardrobe information (such as location, material, and cleanliness) and provide random outfit recommendations based on specific user needs.

---
## Contents
* [System Module Descriptions](#001)                                       
* [Program Execution and Detailed Operation Guide](#002)
---

## <span id = "001">System Module Descriptions

This system follows object-oriented programming principles and consists of multiple independent modules. Below is a summary of the core functionalities of each Python file:

*   **`main.py`**  
    This file stores instances of the clothes used to initialize the wardrobe and serves as the startup file for the entire program.
    
*   **`ALLClothes.py`**  
    Clothing entity data module. Responsible for defining and initializing basic information for each clothing item (e.g., name, type, color, etc.), and providing an interface for formatted data output.

*   **`JsonOperate.py`**  
    Database interaction module. Handles all low-level operations related to JSON files, including data creation, reading, writing, and conversion between objects and dictionaries.

*   **`Mainsystem.py`**  
    Core system routing module. Controls the interaction and page navigation between the welcome page and the main function selection center.

*   **`OutfitRecommendation.py`**  
    Intelligent recommendation algorithm module. Automatically filters out dirty clothes and generates a random daily outfit recommendation based on user input of "season" or "occasion".

*   **`AddOrDeleteNewClothes.py`**  
    Clothing addition/deletion management module. Implements the entry of new clothing information and the removal of existing clothes, synchronizing updates to the database.

*   **`ModifyClothesAttributes.py`**  
    Attribute modification module. Guides the user to search and select a target clothing item, directly modifying and saving specific attributes (e.g., status, location, etc.).

*   **`SearchClothes.py` / `SelectClothes.py` / `ReviewClothes.py`**  
    Browsing and retrieval collaboration modules. Respectively responsible for: capturing user search keywords [10], accurately matching target clothing items based on keywords, and formatting and printing the search results to the user.

---

## <span id="002">Program Execution and Detailed Operation Guide

### 1. Starting the Program
The entry point of the program is `main.py`. Please run this file in your terminal or IDE:
```bash
python main.py
```
Upon startup, `JsonOperate` will automatically check if the `clothes_data.json` data file exists in the current directory. If it does not exist, the system will use a predefined list of initial clothing data to create the file. Afterward, it will display the system's welcome page (Main Menu) [4, 5]. Enter `yes` to proceed to the function selection center.

### 2. Add Clothes
*   **Navigation**: Enter `3` in the main menu to access the add/delete menu, then enter `1` to select adding new clothes.
*   **Operation Details**: The system will prompt you sequentially to enter the clothing code (e.g., `shirt5`), kind, size, color, material, season, scene, state, and position. Once all information is entered, the data will be saved automatically.
*   **Important Note (Regarding Clothing Kinds)**: When inputting the **kind**, please stick to the preset categories, such as `shirt`, `pants` or `trousers`, `shoes`, and `jackets`. **If you input a new kind that the system cannot recognize (e.g., skirt, dress, sweater, or if you make a spelling mistake), the recommendation system will default to categorizing all these unrecognizable items into `accessories` when calling the `GroupByType` method**. This may result in inaccurate outfit recommendations.

### 3. Delete Clothes
*   **Navigation**: Enter `3` in the main menu, then enter `2` to select deleting clothes.
*   **Operation Details**: Enter the exact code of the clothing item you wish to delete (e.g., `shirt1`). If the item exists in the system, it will be permanently removed from the database and the changes will be saved. If it does not exist, the system will prompt you to use the Review function to check your clothing codes first.

### 4. Modify Clothes Attributes
*   **Navigation**: Enter `2` in the main menu, then enter `2` to choose modifying attributes directly.
*   **Operation Details**:
    1. The system will first trigger the search function, asking you to enter the code or attribute of the clothes you want to modify (e.g., type `shirt1`).
    2. After successfully locating the item, the system will present a list of modifiable attributes (name, kind, size, color, material, season, scene, state, position).
    3. Type the name of the attribute you wish to change (e.g., if you washed the item, type `state`), and then type the new value (e.g., `clean`).
    4. The system will confirm that the modification was successful and automatically save the changes to the JSON file.
*   **Note**: If you modify the `kind` attribute here, you must still adhere to the input specifications for "kind" mentioned in the "Add Clothes" section above. Otherwise, the item will be incorrectly categorized under `accessories`.

### 5. Outfit Recommendation
*   **Navigation**: Enter `4` in the main menu to access the recommendation system.
*   **Operation Details**:
    *   You can request recommendations based on the **season**: input `spring`, `summer`, `autumn`, or `winter`.
    *   You can also request recommendations based on the **wearing scene**: input `formal` or `casual`.
    *   The system will automatically filter out any clothes with a `dirty` state, group the remaining clean clothes based on your input, and randomly draw one item from each category (shirts, pants, shoes, etc.) to generate a complete outfit for the day. If a particular category lacks clean clothes, the system will output a corresponding error message. Enter `q` to return to the main menu at any time.





# COMP2090SEF Task 2: Graph Data Structure & Dijkstra's Algorithm

This project is developed to fulfill the requirements of the COMP2090SEF course Task 2, mainly demonstrating the self-study and application of a new data structure (Graph) and a new algorithm (Dijkstra's Algorithm) that were not covered in class.

This project calculates the shortest path between cities using Dijkstra's algorithm by building a weighted undirected graph (implemented with nested dictionaries).

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
*   `calculate(self, start)`: The core of the algorithm. It is responsible for calculating the shortest path distance from a given starting point `start` to all other vertices in the graph, and updating the path tracking dictionary.
*   `get_shortest_path(self, end)`: Based on the path tracking dictionary generated by `calculate`, it backtracks and outputs the complete path from the starting point to the specified `end` point.

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
    Among all currently unvisited nodes, iterate to find the node `current_node` with the smallest currently known distance (`self.distances`) as the next jump point.
    
*   **`for` loop to update adjacent node paths**: 
    ```python
    neighbors = self.graph.get_neighbors(current_node)
    for neighbor, weight in neighbors.items():
        new_distance = self.distances[current_node] + weight
        if new_distance < self.distances[neighbor]:
            self.distances[neighbor] = new_distance
            self.previous[neighbor] = current_node
    ```
    Iterate through all adjacent nodes of the current node. If the "distance to reach the current node + the weight of the adjacent edge" **is less than** the "currently recorded distance to reach the adjacent node", update the minimum distance in the `distances` dictionary, and update the `previous` dictionary, recording that the predecessor node for this optimal path is `current_node`.

### 4. How the Algorithm Traces the Path

When all shortest distance calculations are completed, call `get_shortest_path(self, end)` to backtrack the path.
```python
while current is not None:
    path.append(current)
    current = self.previous[current]
path.reverse()
```
This utilizes the previously saved `previous` dictionary. Starting from the target `end` point, it continuously looks up its previous node (i.e., where it came from in the previous step) and appends them one by one to the `path` list until the previous node is `None` (i.e., it has backtracked to the starting point). Finally, use `.reverse()` to flip the list to get a forward-flowing route from the start to the end.

### 5. Data Uploading and Program Running Method

*   **Data Uploading (Main Block Initialization)**: 
    The graph and route data are hardcoded and uploaded in the `if __name__ == "__main__":` block at the bottom of the file.
    First, instantiate the graph `city_map = Graph()`. Then, pass the list containing city names into `add_vertex` through a for loop, and call `city_map.add_edge()` multiple times to manually input the distances and connections between pairs of cities [3]. Finally, instantiate `dijkstra = Dijkstra(city_map)`, pass in the prepared graph structure, and execute the calculation.
