from abc import ABC, abstractmethod


class BaseProduct(ABC):
    __slots__ = ["name", "description", "__price", "quantity"]

    @classmethod
    @abstractmethod
    def new_product(cls, product_dict):
        pass


class MixinPrintClass:
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    def __init__(self):
        print(self.__repr__())


class Product(BaseProduct, MixinPrintClass):
    __slots__ = ["name", "description", "__price", "quantity"]

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price_new):
        if price_new <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_new

    def __add__(self, other):
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphone(Product):
    __slots__ = ["efficiency", "model", "memory", "color"]

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    __slots__ = ["country", "germination_period", "color"]

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    __products: list[Product]
    product_quantity = 0
    quantity: int

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, products: Product):
        if isinstance(products, Product):
            self.__products.append(products)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        all_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_quantity} шт."
