class BasicClothes:
    def __init__(self, name, kind, size, color, material, season, scene, state, position):
        """Initialize the basic information of the clothing"""
        self.name = name #Clothes name (The number of the clothes)
        self.kind = kind #The kind of clothes
        self.size = size #The size of clothes
        self.color = color #The color of clothes
        self.material = material #The material of clothes
        self.season = season #The applicable season of clothes
        self.scene = scene #The applicable cene of clothes
        self.state = state #The cleanliness of the clothes
        self.position = position #Storage location of clothes

    def get_name(self):
        """Get the name of the clothing"""
        return self.name
    def get_kind(self):
        """Get the type of the clothing"""
        return self.kind
    def get_size(self):
        """Get the size of the clothing"""
        return self.size
    def get_color(self):
        """Get the color of the clothing"""
        return self.color
    def get_material(self):
        """Get the material of the clothing"""
        return self.material
    def get_state(self):
        """Get the cleanliness of the clothing"""
        return self.state
    def get_position(self):
        """Get the position of the clothing"""
        return self.position
    def get_season(self):
        """Get the accessible season of the clothing"""
        return self.season
    def get_scene(self):
        """Get the accessible scene of the clothing"""
        return self.scene

    def __str__(self):
        """Return the formatted details of the garment (for print output)"""
        return (f"--- {self.name} ---\n"
                f"kind: {self.kind}\n"
                f"size: {self.size}\n"
                f"color: {self.color}\n"
                f"material: {self.material}\n"
                f"season: {self.season}\n"
                f"scene: {self.scene}\n"
                f"state: {self.state}\n"
                f"position: {self.position}")

    def return_dicts(self):
        """Convert all the attributes of the clothing to dictionary format and return it"""
        return {
            "kind": self.kind,
            "size": self.size,
            "color": self.color,
            "material": self.material,
            "season": self.season,
            "scene": self.scene,
            "state": self.state,
            "position": self.position
        }


