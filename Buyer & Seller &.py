from pprint import pprint


class UserList(list):
    def search(self, user_name: str):
        matching_users = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
        return matching_users

    def append(self, obj) -> None:
        if not isinstance(obj, User):
            raise TypeError("this list only accepts User")
        return super().append(obj)


class User:
    all_users = UserList()

    def __init__(self, user_name: str, email: str, password: str) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)

    def __str__(self):
        return f"{self.user_name} {self.email} {self.password}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"


class Seller(User):
    def __init__(self, shaba, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def order(self) -> None:
        print(f"{self.user_name}, bought a sth")


class Buyer(User):
    def __init__(self, phone: str, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r}, {self.phone!r})"


class SellerAndBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score


b = Buyer(user_name="reza", email="@gmail.com", password="0000", phone="0933")
s = Seller(user_name="mamad", email="@yahoo.com", password="0101", shaba="0933")

pprint(User.all_users)
