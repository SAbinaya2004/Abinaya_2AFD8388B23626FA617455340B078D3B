def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices


products = ["apple", "mango", "orange", "apple", "pineapple", "mango"]
target = "mango"
result = linearSearchProduct(products, target)
print(result)