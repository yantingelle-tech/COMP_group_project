import random

class OutfitRecommendation:
  def __inint__(self, wardrobe):
    self.wardrobe = wardrobe

  def GetCleanClothes(self):
    return [c for c in self.wardrobe.clothes if c.is_clean]

  def GroupByType(self, clothes):
    groups = {
      "tops": [], "pants": [], "shoes": [], "jackets": [], "accessories": []
    }
    for c in clothes:
      if c.c_type == "tops":
        groups["tops"].append(c)
      elif c.c_type == "pants":
        groups["pants"].append(c)
      elif c.c_type == "shoes":
        groups["shoes"].append(c)
      elif c.c_type == "jackets":
        groups["jackets"].append(c)
      elif c.c_type == "accessories":
        groups["accessories"].append(c)
    return groups
    
  def RecommendBySeason(self, season):
    clean = self.GetCleanClothes()
    if not clean:
      return {"error": "there are no clean clothes in the wardrobe!"}
  
    valid = [c for c in clean if c.season in (c.season, "season")]
    if not valid:
      return {"error": f"there are no clean clothes for {season} season!"}
      
    groups = self.GroupByType(vaild)
    
    outfits = []
    tops = groups ["tops"]
    pants = groups ["pants"]
    shoes = groups ["shoes"]
    jackets = groups.get("jackets", [])
    accessories = groups.get("accessories", [])

    if not(tops and pants):
      return {"error": f"{season} season is missing tops or pants!"}
    else:
      top = tops[random.randint(0, len(tops)-1)]
      pant = pants[random.randint(0, len(pants)-1)]
      shoe = shoes[random.randint(0, len(shoes)-1)] if shoes else None
      jacket = jackets[random.randint(0, len(jackets)-1)] if jackets else None
      accessory = accessories[random.randint(0, len(accessories)-1)] if accessories else None

      outfit = {
        "top": top.name,
        "pant": pant.name,
        "shoe": shoe.name if shoe else None,
        "jacket": jacket.name if jacket else None,
        "accessory": accessory.name if accessory else None
      }
      outfits.append(outfit)
      print(f"{season} seasonal recommendation:")
      return {"outfit": outfit, "season": season}

  def RecommendByOccasion(self, occasion):
    style_map = {
      "formal": "formal",
      "casual": "casual",
      "sporty": "sporty"
    }

    if occasion not in style_map:
      return {"error": f"unsupported occasion: {occasion}"}

    clean = self.GetCleanClothes()
    style_clothes = [c for c in clean if c.style == style_map[occasion]]
        
    if not style_clothes:
      return {"error": f"there is no clean clothes for {occasion} occasion!"}

    groups = self.GroupByType(style_clothes)

    tops = groups["tops"]
    pants = groups["pants"]
    shoes = groups["shoes"]
    jackets = groups.get("jackets", [])
    accessories = groups.get("accessories", [])

    if not (tops and pants):
      return {"error": f"{occasion} occasion is missing tops or pants!"}
    else:
      top = tops[random.randint(0, len(tops)-1)]
      pant = pants[random.randint(0, len(pants)-1)]
      shoe = shoes[random.randint(0, len(shoes)-1)] if shoes else None
      jacket = jackets[random.randint(0, len(jackets)-1)] if jackets else None
      accessory = accessories[random.randint(0, len(accessories)-1)] if accessories else None

      outfit = {
        "top": top.name,
        "pant": pant.name,
        "shoe": shoe.name if shoe else None,
        "jacket": jacket.name if jacket else None,
        "accessory": accessory.name if accessory else None
      }
      outfits.append(outfit)
      print(f"{occasion} occasional recommendation:")
      return {"outfit": outfit, "occasion": occasion}
















