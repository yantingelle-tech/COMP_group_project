class SearchClothes:
    @staticmethod
    def search_clothes():
        """Provide options to users to choose a single/all clothes or a same kind of clothes or some clothes with same attributes"""
        print("Please enter your clothes code kind, or other attributes:")
        print("Enter the EXACT CODE of the clothes will select/show you the information of the single clothes")
        print("Enter ANY OTHER ATTRIBUTES will select/show you all clothes that accord with")
        print("Enter all to check all clothes (only work in the review mode)")
        print("e.g.:all or shirt1 or shirt or summer or cotton")
        search = input("Search here: ")
        print()
        return search