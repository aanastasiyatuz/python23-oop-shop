# found = False
# for product in Product.objects:
#     if product.id == p_id:
#         found = True
#         break

# if not found:
#     print(f"Продукт с id {p_id} не найден")

def get_obj_or_404(model, field, value):
    found = False
    for product in model.objects:
        if getattr(product, field) == value:
            found = True
            break

    if not found:
        raise Exception(f"404: {model.__name__} с {field} {value} не найден")
    return product
