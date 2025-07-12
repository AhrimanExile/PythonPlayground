class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    def get_distance_to_origin(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        else:
            return None
    def get_distance(self, obj):
        if isinstance(obj, Point):
            if hasattr(obj, 'x') and hasattr(obj, 'y') and hasattr(self, 'x') and hasattr(self, 'y'):
                return ((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5
            else:
                print("Координаты не заданы")
                return None
        else:
            print("Передана не точка")
            return None
    def display(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            print(f'Point({self.x}, {self.y})')
        else:
            print("Координаты не заданы")

p1 = Point()
p1.set_coordinates(6, 8)
p1.display()
print(p1.get_distance_to_origin())

p2 = Point()
p2.display()
p2.set_coordinates(3, 4)
p2.display()
print(p2.get_distance_to_origin())

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
p1.display()
p2.display()
print(p1.get_distance(p2))
print(p2.get_distance(p1))

p1 = Point()
p2 = Point()
print(p1.get_distance(p2))
p1.set_coordinates(1, 2)
print(p1.get_distance(p2))
p2.set_coordinates(4, 6)
print(p1.get_distance(p2))