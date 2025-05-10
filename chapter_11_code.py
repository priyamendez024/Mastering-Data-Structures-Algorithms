
# Chapter 11 Python Code - Greedy Algorithms (Knapsack)
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.ratio, reverse=True)
    total_value = 0.0
    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (capacity / item.weight)
            capacity = 0
    return total_value

items = [Item(60, 10), Item(100, 20), Item(120, 30)]
print(fractional_knapsack(50, items))  # Output: 240.0
