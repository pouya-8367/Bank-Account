class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"{key}: {value:.2f} \n"
        print(info)

    def __str__(self):
        return self.__class__.__name__


# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = (self.length + self.width) * 2


# base, height, side1, side2
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = (self.base + self.side1 + self.side2) * 2


r = Rectangle(length= 5, width=8)
r.calculate_area()
r.calculate_perimeter()
print(r)
r.show()
print(40 * "*")

t = Triangle(base= 2, height=6, side1=3,  side2=2)
t.calculate_area()
t.calculate_perimeter()
print(t)
t.show()
print(40 * "*")


