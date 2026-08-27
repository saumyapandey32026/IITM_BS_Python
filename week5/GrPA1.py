fruits = ["grapes", "banana", "mango", "orange", "apple"]
fruit_prices = {
    "apple": 5,
    "banana": 4,
    "mango": 6,
    "grapes": 3
}

# list(dict) gives list of keys
# my_list = list(fruit_prices)
# print(my_list)
# d = {4:40,5:"ram","radha":100}
# print(list(d))

fruit_prices[fruits[3]] = 40
print(fruit_prices)

fruit_prices[fruits[2]] = 10
print(fruit_prices)

print(sorted(fruit_prices.keys()))
print(sorted(fruit_prices.values()))




































