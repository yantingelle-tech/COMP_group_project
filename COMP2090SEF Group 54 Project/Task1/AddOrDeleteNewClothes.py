import JsonOperate
import Mainsystem
import ReviewClothes
from ALLClothes import BasicClothes

class AddOrDeleteNewClothes:
    def __init__(self):
        """Load data and choose functions"""
        json_op = JsonOperate.JsonOperate()
        self.all_clothes = json_op.open_json()
        print("Select 1 to add a new clothes")
        print("Select 2 to delete a specified clothes")
        print("Select 3 to check the clothes")
        print("Select q to back")
        choose = input("Enter your choice: ")
        if choose == "1":
            print()
            self.adding_new_clothes()
        elif choose == "2":
            print()
            self.delete_specified_clothes()
        elif choose == "3":
            print()
            ReviewClothes.ReviewClothes()
            AddOrDeleteNewClothes()

        elif choose == "q":
            print()
            Mainsystem.Mainsystem().function_selection_page()
        else:
            print("Invalid choice, please try again.")
            AddOrDeleteNewClothes()

    def adding_new_clothes(self):
        """Adding new clothes"""
        name = input("Enter the code of your clothes (eg: shirt5/trousers3): ")
        if name in self.all_clothes:
            print("You already have this clothes.")
            print()
            AddOrDeleteNewClothes()
        kind = input("Please input the kind of your new clothes (shirt, pants, jackets, shoes, accessories):")
        size = input("Please input the size of your new clothes:")
        color = input("Please input the color of your new clothes:")
        material = input("Please input the material of your new clothes (e.g: cotton, woolen):")
        season = input("Please input the season of your new clothes (spring, summer, autumn, winter):")
        scene = input("Please input the scene of your new clothes (formal, casual):")
        state = input("Please input the state of your new clothes(clean, dirty):")
        position = input("Please input the position of your new clothes \n(shirt in 1, jacket in 1, pants in 2, shoes in 3, dirty clothes in 4, accessories in 5):")

        new_clothes = BasicClothes(name, kind, size, color, material, season, scene, state, position)
        new_clothes_dict = new_clothes.return_dicts()
        self.all_clothes[name] = new_clothes_dict
        json_op = JsonOperate.JsonOperate()
        json_op.save_json(self.all_clothes)
        print("The new clothes has been saved.")
        print()
        Mainsystem.Mainsystem().function_selection_page()

    def delete_specified_clothes(self):
        """Delete the clothes you choose"""
        choice = input("Please select the clothes' code you want to delete(e.g:shirt1): ")
        if choice in self.all_clothes:
            del self.all_clothes[choice]
            print("The clothes has been deleted.")
            print()
            json_op = JsonOperate.JsonOperate()
            json_op.save_json(self.all_clothes)
            print("The clothes has been deleted.")
            print()
            Mainsystem.Mainsystem().function_selection_page()

        else:
            print("No such clothes found, you can use the review function to check the clothes' code")
            print()
            AddOrDeleteNewClothes()
