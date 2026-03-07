class BasicClothes:
    def __init__(self, kind, size, color, material, state, position):
        self.kind = kind
        self.size = size
        self.color = color
        self.material = material
        self.state = state
        self.position = position

    def get_kind(self):
        return self.kind
    def get_size(self):
        return self.size
    def get_color(self):
        return self.color
    def get_material(self):
        return self.material
    def get_state(self):
        return self.state
    def get_position(self):
        return self.position


