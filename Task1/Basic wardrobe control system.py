import json
import os
from ALLClothes import BasicClothes
from prompt_toolkit.shortcuts import yes_no_dialog


class JsonOperate:
    def __init__(self):
        self.json_filename = "clothes_data.json"
        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.json_full_path = os.path.join(self.current_folder, self.json_filename)



    def test_and_create_json(self, initial_clothes):
        if os.path.exists(self.json_full_path):
            Mainsystem.welcome_page(self)

        else:
            all_clothes = {}
            for key, clothes_instance in initial_clothes.items():
                all_clothes[key] = {
                    "kind": clothes_instance.kind,
                    "size": clothes_instance.size,
                    "color": clothes_instance.color,
                    "material": clothes_instance.material,
                    "state": clothes_instance.state,
                    "position": clothes_instance.position
                }

            with open(self.json_full_path, "w", encoding="utf-8") as f:
                json.dump(all_clothes, f, ensure_ascii=False, indent=4)

    def open_json(self):
        with open(self.json_full_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def add_json(self, message):
        with open(self.json_full_path, "a", encoding="utf-8") as f:
            json.dump(message, f, ensure_ascii=False, indent=4)


class Mainsystem:

    def welcome_page(self):
        print("Welcome to use the INTELLIGENCE wardrobe")
        print('Enter \'YES\' to continue, \'NO\' to quit.')
        choice = input("Enter your choice: ")
        print()
        if choice.lower() == 'yes':
            Mainsystem.function_selection_page(self)
        if choice.lower() == 'no':
            print("Goodbye, wish you have a nice day!")

    def function_selection_page(self):
        print("What would you like to do?")
        print("Enter 1 to review your clothes")
        print("Enter 2 to create a new clothe")
        print("Enter 3 to customize on your outfit for today")
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            review_clothes = ReviewClothes()

        # elif choice == '2':
        #     create_a_new_clothes()
        # elif choice == '3':
        #     costomize_today_outfit()

class SearchClothes:
    def search_clothes(self):
        print("Please enter your clothes code kind, or other attributes:")
        print("Enter the code of the clothes will show you the information of the single clothes")
        print("Enter any other attributes will show you all clothes that accord with")
        print("e.g.:shirt1 or shirt")
        search = input("Search here: ")
        print()  
        return search


class ReviewClothes:
    def __init__(self):
        json_op = JsonOperate()
        self.all_clothes = json_op.open_json()

        self.choice = SearchClothes().search_clothes()

        if self.choice.lower() == 'all':
            self.review_all_clothes()
        else:
            self.review_single_clothes()


    def review_all_clothes(self):
        all_clothes = self.all_clothes
        for clothes_code, single_clothes_dict in all_clothes.items():
            print(f"{clothes_code}:")
            for key, value in single_clothes_dict.items():
                print(f"{key}: {value}")
            print()
    def review_single_clothes(self):
        found = False
        all_clothes = self.all_clothes
        search_result = self.choice
        for target_clothes in all_clothes.keys():
            if search_result == target_clothes:
                found = True
                #print(f"{target_clothes}: {self.all_clothes[target_clothes]}")   #***old ones***
                clothes_dict = self.all_clothes[target_clothes]   #***new changes***
                for key, value in clothes_dict.items():   #***new changes***
                    print(f"{key}: {value}")   #***new changes***
                break
        if not found:
            self.review_series_clothes()

    def review_series_clothes(self):
        found = False
        all_clothes = self.all_clothes
        search_result = self.choice
        for clothes_code, single_clothes_dict in all_clothes.items():
            if search_result in single_clothes_dict.values():
                found = True
                #print(f"{clothes_code}: {single_clothes_dict}")   #***old ones***
                print(f"{clothes_code}:")   #***new changes***
                for key, value in single_clothes_dict.items():   #***new changes***
                    print(f"{key}: {value}")   #***new changes***
                print()   #***new changes***

        if not found:
            print("No such clothes found")

# class Create_clothes:
#     #ready to finish
#
# class Costomize_today_outfit:
#     #ready to finish



if __name__ == "__main__":
    initial_clothes = {"shirt1":BasicClothes("shirt", "175", "white", "wood", "clean", 1),
    "shirt2" : BasicClothes("shirt", "170", "blue", "cotton", "clean", 1),
    "trousers1" : BasicClothes("trousers", "180", "black", "cotton", "clean", 2),
    "shoes1": BasicClothes("shoes", "42", "black", "cloth", "clean", 3),
    "hat1": BasicClothes("hat", "universal", "red", "cotton", "dirty", 4)}


    begin = JsonOperate()
    begin.test_and_create_json(initial_clothes)







