import JsonOperate
import SearchClothes


class ReviewClothes:
    def __init__(self):
        """Initialize the clothes review class, load clothing data and convert to instances"""
        json_op = JsonOperate.JsonOperate()
        clothes_dict = json_op.open_json()
        self.all_clothes_instances = json_op.rebuild_clothes_list(clothes_dict)
        self.choice = SearchClothes.SearchClothes().search_clothes()

        if self.choice.lower() == 'all':
            self.review_all_clothes()
        else:
            self.review_single_clothes()

    def review_all_clothes(self):
        """Retrieve and print the detailed information of all clothing items in the wardrobe"""
        for cloth in self.all_clothes_instances:
            print(cloth)
            print()

    def review_single_clothes(self):
        """Search for a single clothing item by name and print its details,
        switch to series search if not found"""
        found = False
        search_result = self.choice

        for cloth in self.all_clothes_instances:
            if search_result == cloth.get_name():
                found = True
                print(cloth)
                print()

        if not found:
            self.review_series_clothes()

    def review_series_clothes(self):
        """Search for clothing series by attributes and print their details,
        prompt a message if no matching items are found"""
        found = False
        search_result = self.choice

        for cloth in self.all_clothes_instances:
            attributes = [
                cloth.get_kind(),
                cloth.get_size(),
                cloth.get_color(),
                cloth.get_material(),
                cloth.get_season(),
                cloth.get_scene(),
                cloth.get_state(),
                str(cloth.get_position())
            ]

            if search_result in attributes:
                found = True
                print(cloth)
                print()

        if not found:
            print("No such clothes found\n")

