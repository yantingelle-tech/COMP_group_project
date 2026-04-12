import JsonOperate
import ReviewClothes
import Mainsystem
import SearchClothes
import SelectClothes


class ModifyClothesAttributes:
    def __init__(self):
        """Initialize the clothes attribute modification class, load clothing data and display the operation menu"""
        json_op = JsonOperate.JsonOperate()
        self.all_clothes = json_op.open_json()

        print("Select 1 to check clothes")
        print("Select 2 to modify clothes attributes directly")
        print("Select q to back")
        choice = input("Enter your choice: ")
        while True:
            if choice == "1":
                print()
                ReviewClothes.ReviewClothes()
                ModifyClothesAttributes()
            elif choice == "2":
                print()
                self.select_clothes()
                break
            elif choice.lower() == "q":
                print()
                Mainsystem.Mainsystem().function_selection_page()
            else:
                print("Invalid choice")
                continue

    def select_clothes(self):
        """Guide the user to select target clothes through search function, and get the clothes to be modified"""
        print("Please select your target clothes, or series of clothes:")
        choice = SearchClothes.SearchClothes().search_clothes()

        select_target_clothes = SelectClothes.SelectClothes()
        targets = select_target_clothes.select_single_clothes(choice)
        return self.modify_attributes(targets)


    def modify_attributes(self, targets):
        """Modify the attributes of the specified clothing
        and save the updated data to the json file"""
        print("Please enter your the attributes you want to modify:")
        print("Optional attributes: name, kind, size color, material, season, scene, state position")
        want_to_modify = input("Enter your choice: ")

        json_op = JsonOperate.JsonOperate()


        target_objects = json_op.rebuild_clothes_list(targets)

        for obj in target_objects:
            target_clothes_code = obj.get_name()


            if not hasattr(obj, want_to_modify):
                print(f"Warning: {want_to_modify} not found in this item.")
                self.modify_attributes(targets)
                return
            else:
                print()
                print(f"You are changing the {want_to_modify} of {target_clothes_code}.")
                modified_value = input("Enter your modified value: ")

                obj.change_attribute(want_to_modify, modified_value)

                self.all_clothes[target_clothes_code] = obj.return_dicts()
                print(f"{target_clothes_code}'s {want_to_modify} has been modified to the {modified_value}.")

        json_op.save_json(self.all_clothes)
        print("The modify attribute has been saved.")
        print()
        Mainsystem.Mainsystem().function_selection_page()