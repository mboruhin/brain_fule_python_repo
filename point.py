class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"

    def dist_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

