def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)
print(result)  # This will print [0, 3, 5], since "Apple" is found at these indices.