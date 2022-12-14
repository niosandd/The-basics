class Circle:
    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def get_area(self):
        return self.r * self.r * self.pi

    def get_perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2

g = Circle()
print(g.get_area(), g.get_perimeter(), g.scale(2), g.is_intersect(g))



