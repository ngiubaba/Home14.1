import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Обнуление параметров перед каждым тестом"""
    Category.product_count = 0
    Category.category_count = 0


@pytest.fixture
def product_name():
    return Product("Iphone", "Nice phone", 120_000, 1)


def test_str_product(product_name):
    """Тест на вывод продукта в виде строки"""
    assert str(product_name) == "Iphone, 120000 руб. Остаток: 1 шт."


def test_work_product(product_name):
    """Тест на нормальную работу класса"""
    assert product_name.name == "Iphone"
    assert product_name.description == "Nice phone"
    assert product_name.price == 120000
    assert product_name.quantity == 1


def test_product_dict():
    """Тест когда продукт в виде словаря, а не списка"""
    product_new = {
        "name": "Samsung",
        "description": "Work it!",
        "price": 105_000,
        "quantity": 3,
    }
    product_new = Product.new_product(product_new)
    assert product_new.name == "Samsung"
    assert product_new.description == "Work it!"
    assert product_new.price == 105000
    assert product_new.quantity == 3


def test_new_price_product(product_name):
    new_price = 100
    product_name.price = new_price
    assert product_name.price == 100


def test_new__fail_price_product(product_name):
    """Тест когда цена меньше 0"""
    new_price = -100
    product_name.price = new_price
    assert product_name.price == 120000


@pytest.fixture
def category_name(product_name):
    return Category(
        "Телефоны", "Средство для связи на дальние расстояния", [product_name]
    )


def test_work_category(category_name, product_name):
    """Тест на нормальную работу категорий"""
    assert category_name.name == "Телефоны"
    assert category_name.description == "Средство для связи на дальние расстояния"
    assert category_name.products == "Iphone, 120000 руб. Остаток: 1 шт."


@pytest.fixture
def category_count_fix():
    product1 = Product("Iphone", "Nice phone", 120_000, 1)
    product2 = Product("Samsung", "Good phone", 100_000, 1)
    product3 = Product("Xiaomi", "Cheap phone", 50_000, 1)
    return Category(
        "Telephone",
        "Средство для связи на дальние расстояния",
        [product1, product2, product3],
    )


def test_category_str(category_count_fix):
    """Тест вывода информации о категории в str"""
    assert str(category_count_fix) == "Telephone, количество продуктов: 3 шт."


def test_count_product(category_count_fix):
    """Тест на проверку работоспособности счетчиков категорий и продуктов"""
    assert category_count_fix.product_count == 3
    assert category_count_fix.category_count == 1


def test_add_product():
    """Тест на добавление продукта в категорию"""
    product1 = Product("Iphone", "Nice phone", 120_000, 1)
    category = Category(
        "Telephone", "Средство для связи на дальние расстояния", [product1]
    )
    product2 = Product("Samsung", "Good phone", 100000, 2)
    category.add_product(product2)
    assert "Iphone" in category.products
    assert "Samsung" in category.products


def test_text_product():
    """Тест на вывод продукта в категории в заданной строке"""
    product1 = Product("Iphone", "Nice phone", 120_000, 1)
    category = Category(
        "Telephone", "Средство для связи на дальние расстояния", [product1]
    )
    assert category.products == "Iphone, 120000 руб. Остаток: 1 шт."


def test_sum_product():
    """Тест на суммирование стоимости и количества продуктов"""
    product1 = Product("Iphone", "Nice phone", 120_000, 1)
    product2 = Product("Samsung", "Good phone", 100000, 2)
    assert (product1 + product2) == 320000
