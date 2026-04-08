import JsonOperate
import SearchClothes


class ReviewClothes:
    def __init__(self):
        """Initialize the clothes review class, load clothing data and execute the review logic based on search results"""
        json_op = JsonOperate.JsonOperate()
        self.all_clothes = json_op.open_json()

        self.choice = SearchClothes.SearchClothes().search_clothes()

        if self.choice.lower() == 'all':
            self.review_all_clothes()

        else:
            self.review_single_clothes()




    def review_all_clothes(self):
        """Retrieve and print the detailed information of all clothing items in the wardrobe"""
        json_op = JsonOperate.JsonOperate()
        data = json_op.open_json()
        all_instance = JsonOperate.JsonOperate().rebuild_clothes_list(data)
        for i in all_instance:
            print(i)
            print()



    def review_single_clothes(self):
        """Search for a single clothing item by name and print its details, switch to series search if not found"""
        found = False
        all_clothes = self.all_clothes
        search_result = self.choice
        suitable_clothes = {}
        for target_clothes in all_clothes.keys():
            if search_result == target_clothes:
                found = True
                suitable_clothes[target_clothes] = all_clothes[target_clothes]
                all_instance = JsonOperate.JsonOperate().rebuild_clothes_list(suitable_clothes)
                for i in all_instance:
                    print(i)
                    print()
                print()


        if not found:
            self.review_series_clothes()

    def review_series_clothes(self):
        """Search for clothing series by attributes and print their details, prompt a message if no matching items are found"""
        found = False
        all_clothes = self.all_clothes
        search_result = self.choice
        suitable_clothes = {}
        for clothes_code, single_clothes_dict in all_clothes.items():
            if search_result in single_clothes_dict.values():
                found = True
                suitable_clothes[clothes_code] = all_clothes[clothes_code]
        if found:
            all_instance = JsonOperate.JsonOperate().rebuild_clothes_list(suitable_clothes)
            for i in all_instance:
                print(i)
                print()
            print()

        if not found:
            print("No such clothes found\n")

