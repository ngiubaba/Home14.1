import pytest

from src.classes import Category, Product


@pytest.fixture
def product_name():
    return Product("Iphone", "Nice phone", 120_000, 1)


def test_work_product(product_name):
    """Тест на нормальную работу класса"""
    assert product_name.name == "Iphone"
    assert product_name.description == "Nice phone"
    assert product_name.price == 120000
    assert product_name.quantity == 1


@pytest.fixture
def category_name(product_name):
    return Category(
        "Телефоны", "Средство для связи на дальние расстояния", [product_name]
    )


def test_work_category(category_name, product_name):
    """Тест на нормальную работу категорий"""
    assert category_name.name == "Телефоны"
    assert category_name.description == "Средство для связи на дальние расстояния"
    assert category_name.products == [product_name]


@pytest.fixture
def category_count_fix():
    product1 = Product("Iphone", "Nice phone", 120_000, 1)
    product2 = Product("Samsung", "Good phone", 100_000, 1)
    product3 = Product("Xiaomi", "Cheap phone", 50_000, 1)
    return Category(
        "Telefone",
        "Средство для связи на дальние расстояния",
        [product1, product2, product3],
    )


def test_count_product(category_count_fix):
    """Тест на проверку работоспособности счетчиков категорий и продуктов"""
    assert category_count_fix.product_count == 4
    assert category_count_fix.category_count == 2
