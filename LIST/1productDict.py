products = {'amul': 100, 'biscuts': 200, 'colgate': 150}

bill = sum(products.values())

print("Products Purchased:")
for item, price in products.items():
    print(f"{item}: {price}")

print(f"\nTotal Bill: {bill}")
