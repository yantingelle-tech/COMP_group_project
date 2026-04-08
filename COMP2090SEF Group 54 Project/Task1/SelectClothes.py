import JsonOperate
import SearchClothes
class SelectClothes():
    def __init__(self):
        """Initialize the clothes selection class and load all clothing data from JSON file"""
        json_op = JsonOperate.JsonOperate()
        self.all_clothes = json_op.open_json()

    def select_single_clothes(self,choice):
        """Select a single piece of clothing by exact name, return series clothes if not found"""
        tempo_dict = {}
        all_clothes = self.all_clothes
        search_result = choice
        for target_clothes in all_clothes.keys():
            if search_result == target_clothes:
                tempo_dict[target_clothes] = self.all_clothes[target_clothes]

        if len(tempo_dict) == 0:
            return self.select_series_clothes(choice)
        else:
            return tempo_dict


    def select_series_clothes(self, choice):
        """Select a series of clothes by matching attribute values, prompt message if no results found"""
        tempo_dict = {}
        all_clothes = self.all_clothes
        search_result = choice
        for clothes_code, single_clothes_dict in all_clothes.items():
            if search_result in single_clothes_dict.values():
                tempo_dict[clothes_code] = single_clothes_dict
        if len(tempo_dict) == 0:
            print("No such clothes found")
            SearchClothes.SearchClothes().search_clothes()
        else:
            return tempo_dict