
# Chapter 5 Python Code - Count Set Bits
def count_set_bits(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

print(count_set_bits(5))  # Output: 2
