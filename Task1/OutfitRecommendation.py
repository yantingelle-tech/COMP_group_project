import random
import JsonOperate
import Mainsystem

class OutfitRecommendation:
    def __init__(self):
        """Initialize the outfit recommendation class, load clothing data and provide a selection menu for recommendation types"""
        json_op = JsonOperate.JsonOperate()
        data = json_op.open_json()
        self.wardrobe = JsonOperate.JsonOperate().rebuild_clothes_list(data)

        while True:
            print("choose a recommendation type:")
            print("You can choose by four seasons: \"Spring\", \"Summer\", \"Autumn\", \"Winter\".")
            print("You can also choose by wearing scene: \"Formal\", \"Casual\"")
            print("Enter \'q\' to quit")

            choice = input("Input recommendation type:")
            print()
            seasonlist = ["spring", "summer", "autumn", "winter"]
            scenelist = ["formal", "casual"]

            if choice.lower() in seasonlist:
                identify = choice.lower()
                reco = self.RecommendBySeason(identify)
                # print(reco)
                self.output(reco)
                print()

            elif choice.lower() in scenelist:
                identify = choice.lower()
                reco= self.RecommendByOccasion(identify)
                # print(reco)
                self.output(reco)
                print()

            elif choice.lower() == "q":
                print()
                Mainsystem.Mainsystem().function_selection_page()

            else:
                print("Invalid input, please try again.")
                print()
                OutfitRecommendation()

    def GetCleanClothes(self):
        """Retrieve and return all clean clothing items from the wardrobe"""
        return [c for c in self.wardrobe if c.state == "clean"]

    def GroupByType(self, clothes):
        """Group the given clothes by their types (shirt, pants, shoes, etc.)
        and return the grouped dictionary"""
        groups = {
            "shirt": [],
            "pants": [],
            "shoes": [],
            "jackets": [],
            "accessories": []
        }
        for c in clothes:
            if c.kind == "shirt":
                groups["shirt"].append(c)
            elif c.kind == "trousers":
                groups["pants"].append(c)
            elif c.kind == "pants":
                groups["pants"].append(c)
            elif c.kind == "shoes":
                groups["shoes"].append(c)
            elif c.kind == "jackets":
                groups["jackets"].append(c)
            else:
                groups["accessories"].append(c)
        return groups

    def RecommendBySeason(self, season):
        """Filter clean clothes by season and generate a random matching outfit"""
        clean = self.GetCleanClothes()
        if not clean:
            return {"error": "there are no clean clothes in the wardrobe!"}

        valid = [c for c in clean if c.season == season]
        if not valid:
            return {"error": f"there are no clean clothes for {season} season!"}

        groups = self.GroupByType(valid)

        shirts = groups["shirt"]
        pants = groups["pants"]
        shoes = groups["shoes"]
        jackets = groups.get("jackets", [])
        accessories = groups.get("accessories", [])

        if not (shirts and pants):
            return {"error": f"{season} season is missing shirts or pants!"}

        shirt = random.choice(shirts)
        pant = random.choice(pants)
        shoe = random.choice(shoes) if shoes else None
        jacket = random.choice(jackets) if jackets else None
        accessory = random.choice(accessories) if accessories else None

        outfit = {
            "shirt": shirt.name,
            "pant": pant.name,
            "shoe": shoe.name if shoe else None,
            "jacket": jacket.name if jacket else None,
            "accessory": accessory.name if accessory else None
        }
        print(f"{season} seasonal recommendation:")
        return {"outfit": outfit, "season": season}

    def RecommendByOccasion(self, occasion):
        """Filter clean clothes by occasion (formal/casual) and generate a random matching outfit"""
        style_map = {
            "formal": "formal",
            "casual": "casual",
            "sporty": "sporty"
        }

        if occasion not in style_map:
            return {"error": f"unsupported occasion: {occasion}"}

        clean = self.GetCleanClothes()

        style_clothes = [c for c in clean if c.scene == style_map[occasion]]

        if not style_clothes:
            return {"error": f"there is no clean clothes for {occasion} occasion!"}

        groups = self.GroupByType(style_clothes)

        shirts = groups["shirt"]
        pants = groups["pants"]
        shoes = groups["shoes"]
        jackets = groups.get("jackets", [])
        accessories = groups.get("accessories", [])

        if not (shirts and pants):
            return {"error": f"{occasion} occasion is missing shirts or pants!"}

        shirt = random.choice(shirts)
        pant = random.choice(pants)
        shoe = random.choice(shoes) if shoes else None
        jacket = random.choice(jackets) if jackets else None
        accessory = random.choice(accessories) if accessories else None

        outfit = {
            "shirt": shirt.name,
            "pant": pant.name,
            "shoe": shoe.name if shoe else None,
            "jacket": jacket.name if jacket else None,
            "accessory": accessory.name if accessory else None
        }
        print(f"{occasion} occasional recommendation:")
        return {"outfit": outfit, "occasion": occasion}

    def output(self, outcoming):
        """Print the generated outfit result or error message to the console"""
        if "outfit" in outcoming:
            outcome = outcoming["outfit"]
            for outfit_key, outfit_value in outcome.items():
                print(f"{outfit_key}: {outfit_value}")
        else:
            outcome = outcoming["error"]
            print(outcome)













