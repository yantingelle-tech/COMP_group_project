class SearchClothes:
    @staticmethod
    def search_clothes():
        """Provide options to users to choose a single/all clothes or a same kind of clothes or some clothes with same attributes"""
        print("Please enter your clothes code kind, or other attributes:")
        print("Enter the code of the clothes will show you the information of the single clothes")
        print("Enter any other attributes will show you all clothes that accord with")
        print("Enter all to check all clothes")
        print("e.g.:all or shirt1 or shirt or summer or cotton")
        search = input("Search here: ")
        print()
        return search