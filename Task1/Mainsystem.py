import ReviewClothes
import ModifyClothesAttributes
import AddOrDeleteNewClothes
import OutfitRecommendation
import sys

class Mainsystem:
    @staticmethod
    def welcome_page():
        """Home page"""
        print("Welcome to use the INTELLIGENCE wardrobe")
        print('Enter \'YES\' to continue, \'NO\' to quit.')
        choice = input("Enter your choice: ")
        print()
        if choice.lower() == 'yes':
            Mainsystem.function_selection_page()
        elif choice.lower() == 'no':
            print("Goodbye, wish you have a nice day!")
            sys.exit()
        else:
            print("invalid input, please try again.")
            print()
            Mainsystem.welcome_page()

    @staticmethod
    def function_selection_page():
        """Function selection page"""
        print("What would you like to do?")
        print("Enter 1 to review your clothes")
        print("Enter 2 to modify clothes attributes")
        print("Enter 3 to add new clothes or delete specific clothes")
        print("Enter 4 to recommend today's outfit!")
        print("Enter Q to back to initial page")
        choice = input("Enter your choice: ")
        print()
        if choice == '1':
            ReviewClothes.ReviewClothes()
            Mainsystem.function_selection_page()

        elif choice == '2':
            ModifyClothesAttributes.ModifyClothesAttributes()
        elif choice == '3':
            AddOrDeleteNewClothes.AddOrDeleteNewClothes()
        elif choice == '4':
            OutfitRecommendation.OutfitRecommendation()
        elif choice.lower() == 'q':
            Mainsystem.welcome_page()
        else:
            print("invalid input, please try again.\n")
            Mainsystem.function_selection_page()