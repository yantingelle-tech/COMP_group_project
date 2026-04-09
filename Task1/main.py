from JsonOperate import *
if __name__ == "__main__":
    """Initialization Data"""
    initial_clothes = [
    BasicClothes("shirt1","shirt", "175", "white", "wood", "spring","formal","clean", 1),
    BasicClothes("shirt2","shirt", "170", "blue", "cotton", "summer","casual","clean", 1),
    BasicClothes("shirt3", "shirt", "175", "gray", "cotton", "winter", "formal", "clean", 1),
    BasicClothes("shirt4", "shirt", "175", "white", "wood", "autumn", "casual", "clean", 1),

    BasicClothes("trousers1","pants", "180", "black", "cotton", "winter","casual","clean", 2),
    BasicClothes("trousers2", "pants", "175", "black", "cotton", "spring", "formal", "clean", 2),
    BasicClothes("trousers3", "pants", "175", "gray", "cotton", "autumn", "casual", "clean", 2),
    BasicClothes("pants4", "pants", "175", "gray", "cotton", "summer", "casual", "clean", 2),

    BasicClothes("shoes1","shoes", "42", "black", "cloth", "summer","casual","clean", 3),
    BasicClothes("shoes2", "shoes", "42", "black", "leather", "spring", "formal", "clean", 3),
    BasicClothes("shoes3", "shoes", "41", "gray", "cloth", "winter", "formal", "clean", 3),

    BasicClothes("hat1","hat", "universal", "red", "cotton", "summer","casual","dirty", 4),
    BasicClothes("hat2", "hat", "universal", "black", "cotton", "autumn", "formal", "clean", 5),
    BasicClothes("gloves1", "gloves", "universal", "red", "cotton", "winter","casual","clean", 5),
    BasicClothes("scarf1","scarf","universal","yellow", "cotton", "winter","casual","clean", 5),

    BasicClothes("jacket1","jackets","175","black","cotton","spring","casual","clean", 1),
    BasicClothes("jacket2", "jackets", "170", "gray", "cotton", "autumn", "formal", "clean", 1),
    BasicClothes("jacket3", "jackets", "180", "green", "cotton", "winter", "casual", "clean", 1),
    ]

    begin = JsonOperate()
    begin.test_and_create_json(initial_clothes)