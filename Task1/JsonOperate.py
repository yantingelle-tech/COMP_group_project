import json
import Mainsystem
import os
from ALLClothes import BasicClothes, Shirt, Pants, Shoes, Jackets, Accessories

class JsonOperate:
    def __init__(self):
        """Initialize the JSON operation class and set the file path"""
        self.json_filename = "clothes_data.json"
        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.json_full_path = os.path.join(self.current_folder, self.json_filename)


    def test_and_create_json(self, initial_clothes):
        """Check if the JSON file exists. Create it with initial data if it does not exist, then jump to the welcome page"""
        if os.path.exists(self.json_full_path):
            Mainsystem.Mainsystem().welcome_page()

        else:
            all_clothes = {}
            for clothes_instance in initial_clothes:
                all_clothes[clothes_instance.name] = {
                    "kind": clothes_instance.kind,
                    "size": clothes_instance.size,
                    "color": clothes_instance.color,
                    "material": clothes_instance.material,
                    "season": clothes_instance.season,
                    "scene": clothes_instance.scene,
                    "state": clothes_instance.state,
                    "position": clothes_instance.position
                }

            with open(self.json_full_path, "w", encoding="utf-8") as f:
                json.dump(all_clothes, f, ensure_ascii=False, indent=4)
            Mainsystem.Mainsystem().welcome_page()

    def open_json(self):
        """Read and return all data from the JSON file"""
        with open(self.json_full_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def add_json(self, message):
        """Append new data to the end of the JSON file"""
        with open(self.json_full_path, "a", encoding="utf-8") as f:
            json.dump(message, f, ensure_ascii=False, indent=4)

    def save_json(self, data):
        """Overwrite and save the complete data to the JSON file"""
        with open(self.json_full_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def rebuild_clothes_list(self, theDict):
        """Convert dictionary-formatted clothing data into a list of specific clothes instances"""
        clothes_list = []
        for code, attribute in theDict.items():
            kind = attribute["kind"].lower()
            if kind == "shirt":
                cloth = Shirt(code, attribute["size"], attribute["color"],
                              attribute["material"], attribute["season"],
                              attribute["scene"], attribute["state"], attribute["position"])
            elif kind == "pants" or kind == "trousers":
                cloth = Pants(code, attribute["size"], attribute["color"],
                              attribute["material"], attribute["season"],
                              attribute["scene"], attribute["state"], attribute["position"])
            elif kind == "shoes":
                cloth = Shoes(code, attribute["size"], attribute["color"],
                              attribute["material"], attribute["season"],
                              attribute["scene"], attribute["state"], attribute["position"])
            elif kind == "jackets":
                cloth = Jackets(code, attribute["size"], attribute["color"],
                                attribute["material"], attribute["season"],
                                attribute["scene"], attribute["state"], attribute["position"])
            else:
                cloth = Accessories(code, kind, attribute["size"], attribute["color"],
                                    attribute["material"], attribute["season"],
                                    attribute["scene"], attribute["state"], attribute["position"])

            clothes_list.append(cloth)
        return clothes_list



