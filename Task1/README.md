# COMP2090SEF Task 1:Intelligent Wardrobe Management and Outfit Recommendation System

Link of Introduction Video: [https: https://drive.google.com/drive/folders/1CzCTcL7_ofcIklY2VcSbMikDKwEp5NaX?usp=sharing](https://drive.google.com/file/d/1DKauQa4QMj3jWhqwxm1nzR_QRwFe3n11/view?usp=sharing)

## <span id="002">Program Execution and Detailed Operation Guide

### <span id="0021">1. Starting the Program
The entry point of the program is `main.py`. Please run this file in your terminal or IDE (PyCharm/Vs Code)just click the Running button:
```bash
python main.py
```
Upon startup, `JsonOperate` will automatically check if the `clothes_data.json` data file exists in the current directory. If it does not exist, the system will use a predefined list of initial clothing data to create the file. Afterward, it will display the system's welcome page (Main Menu). Enter `yes` to proceed to the function selection center.

### <span id="0022">2. Add Clothes
*   **Navigation**: Enter `3` in the main menu to access the add/delete menu, then enter `1` to select adding new clothes.
*   **Operation Details**: The system will prompt you sequentially to enter the clothing code (e.g., `shirt5`), kind, size, color, material, season, scene, state, and position. Once all information is entered, the data will be saved automatically.
*   **❗️Important Note 1(Regarding Clothing Kinds)**: When inputting the **kind**, please stick to the preset categories, such as `shirt`, `pants` or `trousers`, `shoes`, and `jackets`. **If you input a new kind that the system cannot recognize (e.g., skirt, dress, sweater, or if you make a spelling mistake), the recommendation system will default to categorizing all these unrecognizable items into `accessories` when calling the `GroupByType` method**. This may result in inaccurate outfit recommendations. 
*   **❗️Important Note 2(Regarding Clothing Storage Position)** Shirt and jackets are stored at position 1, pants at position 2, shoes at position 3, all dirty clothes at position4, accessories at position 5.


### <span id="0023">3. Delete Clothes
*   **Navigation**: Enter `3` in the main menu, then enter `2` to select deleting clothes.
*   **Operation Details**: Enter the exact code of the clothing item you wish to delete (e.g., `shirt1`). If the item exists in the system, it will be permanently removed from the database and the changes will be saved. If it does not exist, the system will prompt you to use the Review function to check your clothing codes first.

### <span id="0024">4. Modify Clothes Attributes
*   **Navigation**: Enter `2` in the main menu, then enter `2` to choose modifying attributes directly.
*   **Operation Details**:
    1. The system will first trigger the search function, asking you to enter the code or attribute of the clothes you want to modify (e.g., type `shirt1`).
    2. After successfully locating the item, the system will present a list of modifiable attributes (name, kind, size, color, material, season, scene, state, position).
    3. Type the name of the attribute you wish to change (e.g., if you washed the item, type `state`), and then type the new value (e.g., `clean`). ❗️It should be noted that if the state of the clothes is changed to "dirty", they will be automatically moved to position 4, a dedicated area for dirty clothes; oppositely,if we modified the state to clean, the clothes will automatically be put in their corresponding position.
    4. The system will confirm that the modification was successful and automatically save the changes to the JSON file.
*   **Note**: If you modify the `kind` attribute here, you must still adhere to the input specifications for "kind" mentioned in the "Add Clothes" section above. Otherwise, the item will be incorrectly categorized under `accessories`.

### <span id="0025">5. Outfit Recommendation
*   **Navigation**: Enter `4` in the main menu to access the recommendation system.
*   **Operation Details**:
    *   You can request recommendations based on the **season**: input `spring`, `summer`, `autumn`, or `winter`.
    *   You can also request recommendations based on the **wearing scene**: input `formal` or `casual`.
    *   The system will automatically filter out any clothes with a `dirty` state, group the remaining clean clothes based on your input, and randomly draw one item from each category (shirts, pants, shoes, etc.) to generate a complete outfit for the day. If a particular category lacks clean clothes, the system will output a corresponding error message. Enter `q` to return to the main menu at any time.
