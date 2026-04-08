# Intelligent Wardrobe Management and Outfit Recommendation System (INTELLIGENCE Wardrobe)

## Project Overview
With the accelerating pace of life, people own an increasing number of clothes, making it easy to forget where items are stored or leaving no time to plan daily outfits. This project aims to develop a multi-module Python application utilizing Object-Oriented Programming (OOP) to help users effectively manage their wardrobe information (such as location, material, and cleanliness) and provide random outfit recommendations based on specific user needs [12, 13].

---

## Core Classes and OOP Features

This system adheres to object-oriented programming principles and consists of several independent modules. Below is an introduction to the functions of each class, emphasizing their OOP features:

*   **`BasicClothes` (ALLClothes.py)**
    *   **Function**: The clothing entity class, responsible for initializing the basic information of each clothing item (name, kind, size, color, material, season, scene, state, position) [2].
    *   **OOP Feature - Encapsulation & Magic Methods**: This class encapsulates the attributes and provides secure interfaces to access the data (e.g., `get_size()`) [2, 12]. More importantly, it heavily utilizes the Python magic method `__str__`. When an object is printed (for instance, when `print(i)` is called in the Review module), the system automatically invokes this method to format the dictionary data cleanly and modularly into readable string outputs, avoiding the need for complex loops [2, 12].

*   **`JsonOperate` (JsonOperate.py)**
    *   **Function**: Handles all input/output operations related to the JSON file, including creating, reading, saving, and appending data [4].
    *   **OOP Feature - Encapsulation**: This class hides the file path state (`self.json_full_path`) internally. It bundles file operations like `open_json()`, `save_json()`, and the complex dictionary-to-object conversion logic `rebuild_clothes_list()` together, preventing external interference with the file manipulation process [4, 12].

*   **`Mainsystem` (Mainsystem.py)**
    *   **Function**: The core routing class of the system, responsible for controlling transitions between the welcome page and the function selection interface [6].
    *   **OOP Feature - Static Methods**: The system extensively applies the `@staticmethod` decorator (e.g., for `welcome_page()` and `function_selection_page()`). This demonstrates excellent memory management, as these are basic routing functions that can be called directly without instantiating an object [6, 12].

*   **`OutfitRecommendation` (OutfitRecommendation.py)**
    *   **Function**: The core algorithmic class of the recommendation system, responsible for providing outfit suggestions based on the season or occasion [8].
    *   **OOP Feature - Abstraction**: This is a prime example of abstraction. When a user requests an outfit recommendation, this class processes highly complex logic internally: it filters out dirty clothes via `GetCleanClothes()`, groups them via `GroupByType()`, and executes a random algorithm to assemble a matching outfit. The rest of the application (as well as the user) is entirely isolated from these algorithmic complexities, only interacting to retrieve the final output [8, 12].

*   **`AddOrDeleteNewClothes` (AddOrDeleteNewClothes.py)**
    *   **Function**: Implements the addition of new clothes and the deletion of specified clothes, synchronously updating the JSON database [1].

*   **`ModifyClothesAttributes` (ModifyClothesAttributes.py)**
    *   **Function**: Guides the user to search for and select a target clothing item, then directly modifies its specified attributes (such as state, position, etc.) [7].

*   **`SearchClothes`, `SelectClothes`, `ReviewClothes`**
    *   **Function**: These three classes work collaboratively to form the system's browsing and retrieval functions. `SearchClothes` uses a static method to capture user search keywords [10]; `SelectClothes` precisely matches a single item or a series of clothes based on those keywords [11]; and `ReviewClothes` formats the retrieval results using the `__str__` method to print them for the user [9].

---

## Program Execution and Detailed Operation Guide

### 1. Starting the Program
The entry point of the program is `main.py`. Please run this file in your terminal or IDE:
```bash
python main.py
```
Upon startup, `JsonOperate` will automatically check if the `clothes_data.json` data file exists in the current directory. If it does not exist, the system will use a predefined list of initial clothing data to create the file. Afterward, it will display the system's welcome page (Main Menu) [4, 5]. Enter `yes` to proceed to the function selection center [6].

### 2. Add Clothes
*   **Navigation**: Enter `3` in the main menu to access the add/delete menu, then enter `1` to select adding new clothes [1].
*   **Operation Details**: The system will prompt you sequentially to enter the clothing code (e.g., `shirt5`), kind, size, color, material, season, scene, state, and position. Once all information is entered, the data will be saved automatically.
*   **Important Note (Regarding Clothing Kinds)**: When inputting the **kind**, please stick to the preset categories, such as `shirt`, `pants` or `trousers`, `shoes`, and `jackets`. **If you input a new kind that the system cannot recognize (e.g., skirt, dress, sweater, or if you make a spelling mistake), the recommendation system will default to categorizing all these unrecognizable items into `accessories` when calling the `GroupByType` method** [8, 12]. This may result in inaccurate outfit recommendations.

### 3. Delete Clothes
*   **Navigation**: Enter `3` in the main menu, then enter `2` to select deleting clothes [1].
*   **Operation Details**: Enter the exact code of the clothing item you wish to delete (e.g., `shirt1`). If the item exists in the system, it will be permanently removed from the database and the changes will be saved. If it does not exist, the system will prompt you to use the Review function to check your clothing codes first [1].

### 4. Modify Clothes Attributes
*   **Navigation**: Enter `2` in the main menu, then enter `2` to choose modifying attributes directly [7].
*   **Operation Details**:
    1. The system will first trigger the search function, asking you to enter the code or attribute of the clothes you want to modify (e.g., type `shirt1`).
    2. After successfully locating the item, the system will present a list of modifiable attributes (name, kind, size, color, material, season, scene, state, position).
    3. Type the name of the attribute you wish to change (e.g., if you washed the item, type `state`), and then type the new value (e.g., `clean`).
    4. The system will confirm that the modification was successful and automatically save the changes to the JSON file [7].
*   **Note**: If you modify the `kind` attribute here, you must still adhere to the input specifications for "kind" mentioned in the "Add Clothes" section above. Otherwise, the item will be incorrectly categorized under `accessories` [8, 12].

### 5. Outfit Recommendation
*   **Navigation**: Enter `4` in the main menu to access the recommendation system [6].
*   **Operation Details**:
    *   You can request recommendations based on the **season**: input `spring`, `summer`, `autumn`, or `winter`.
    *   You can also request recommendations based on the **wearing scene**: input `formal` or `casual`.
    *   The system will automatically filter out any clothes with a `dirty` state, group the remaining clean clothes based on your input, and randomly draw one item from each category (shirts, pants, shoes, etc.) to generate a complete outfit for the day [8]. If a particular category lacks clean clothes, the system will output a corresponding error message [8]. Enter `q` to return to the main menu at any time.
