# prices = [50, 75, 46, 22, 80, 65, 8]

# prices.sort()

# print("El precio mas barato es de {} y el mas caro es de {}".format(str(prices[0]), str(prices[len(prices) - 1]) ))



prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))
# no entender