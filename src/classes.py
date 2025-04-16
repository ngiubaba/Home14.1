class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(product_dict["name"],
                   product_dict["description"],
                   product_dict["price"],
                   product_dict["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price_new):
        if price_new <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_new



class Category:
    category_count = 0
    product_count = 0
    name: str
    description: str
    __products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, products: Product):
        self.__products.append(products)
        self.product_count += 1

    @property
    def products(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )
