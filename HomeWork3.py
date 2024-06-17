import requests

url = "https://fakestoreapi.com/products"

<<<<<<< HEAD

=======
>>>>>>> 29c1b7c27f374a0b4c2c5df7abe1a2e017625b8e
def get_categories():
    response = requests.get(url)
    products = response.json()
    categories = set(product['category'] for product in products)
    return categories

<<<<<<< HEAD

=======
>>>>>>> 29c1b7c27f374a0b4c2c5df7abe1a2e017625b8e
def get_products_by_category(category):
    response = requests.get(url)
    products = response.json()
    filtered_products = [product for product in products if product['category'].lower() == category.lower()]

    if filtered_products:
        for product in filtered_products:
            print(f"Название: {product['title']}")
            print(f"Категория: {product['category']}")
            print(f"Цена: ${product['price']}")
            print(f"Описание: {product['description']}")
            print("-------------------------")
    else:
        print(f"Нет товаров в категории '{category}'.")

<<<<<<< HEAD

=======
>>>>>>> 29c1b7c27f374a0b4c2c5df7abe1a2e017625b8e
categories = get_categories()
print("Доступные категории товаров:")
for cat in categories:
    print(cat)

user_category = input("Введите категорию товаров, которую вы хотите просмотреть: ")

print(f"\nТовары в категории '{user_category}':")
get_products_by_category(user_category)
