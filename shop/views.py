from .models import Category, Product
from .serializers import ProductSerializer
from abstract.utils import get_obj_or_404


def product_list():
    serializer = ProductSerializer()
    print(serializer.serialize_objects())

def create_product():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    print("Выберите категорию:")
    for cat in Category.objects:
        print(cat.title)
    cat_title = input()

    cat = get_obj_or_404(Category, 'title', cat_title)
    Product(title, price, cat)

def delete_product():
    p_id = int(input("Введите id продукта для удаления: "))
    product = get_obj_or_404(Product, 'id', p_id)
    Product.objects.remove(product)

def product_details():
    p_id = int(input("Введите id продукта: "))
    product = get_obj_or_404(Product, 'id', p_id)
    serializer = ProductSerializer()
    print(serializer.serialize_obj(product))

def product_update():
    p_id = int(input("Введите id продукта: "))
    product = get_obj_or_404(Product, 'id', p_id)

    field = input("Введите поле, которое хотите изменить: ")
    if field in dir(product):
        value = input(f"{field} = ")
        field_type = type(getattr(product, field))
        setattr(product, field, field_type(value))
    else:
        print("Такого поля нет")

cat1 = Category('some category')
Product('1 product', 34.0, cat1)
Product('2 product', 45.5, cat1)
