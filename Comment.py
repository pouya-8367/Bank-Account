from datetime import datetime


class Prodcut:
    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name


class Comment:
    website_name = "sabzlearn.ir"

    def __init__(self, product, name, description, like, dislike):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like
        self.dislike = dislike

    def show(self):
        print(f"product: {self.product}\n"
              f"name: {self.name}\n"
              f"description: {self.description}\n"
              f"date: {self.date}\n"
              f"like: {self.like} and dislike {self.dislike}")


python_course = Prodcut("python expert", 0, 0)
c1 = Comment(python_course, "reza", "دوره خوب", 50, 10)

print(python_course)
c1.show()
