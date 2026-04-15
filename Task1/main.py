from JsonOperate import *
if __name__ == "__main__":
    """Initialization Data"""
    initial_clothes= [
    Shirt("shirt1","175", "white", "wood", "spring","formal","clean", 1),
    Shirt("shirt2", "170", "blue", "cotton", "summer","casual","clean", 1),
    Shirt("shirt3",  "175", "gray", "cotton", "winter", "formal", "clean", 1),
    Shirt("shirt4",  "175", "white", "wood", "autumn", "casual", "clean", 1),

    Pants("trousers1", "180", "black", "cotton", "winter","casual","clean", 2),
    Pants("trousers2",  "175", "black", "cotton", "spring", "formal", "clean", 2),
    Pants("trousers3", "175", "gray", "cotton", "autumn", "casual", "clean", 2),
    Pants("pants4", "175", "gray", "cotton", "summer", "casual", "clean", 2),

    Shoes("shoes1", "42", "black", "cloth", "summer","casual","clean", 3),
    Shoes("shoes2",  "42", "black", "leather", "spring", "formal", "clean", 3),
    Shoes("shoes3",  "41", "gray", "cloth", "winter", "formal", "clean", 3),

    Accessories("hat1","hat", "universal", "red", "cotton", "summer","casual","dirty", 4),
    Accessories("hat2", "hat", "universal", "black", "cotton", "autumn", "formal", "clean", 5),
    Accessories("gloves1", "gloves", "universal", "red", "cotton", "winter","casual","clean", 5),
    Accessories("scarf1","scarf","universal","yellow", "cotton", "winter","casual","clean", 5),

    Jackets("jacket1","175","black","cotton","spring","casual","clean", 1),
    Jackets("jacket2",  "170", "gray", "cotton", "autumn", "formal", "clean", 1),
    Jackets("jacket3",  "180", "green", "cotton", "winter", "casual", "clean", 1),
    ]

    begin = JsonOperate()
    begin.test_and_create_json(initial_clothes)