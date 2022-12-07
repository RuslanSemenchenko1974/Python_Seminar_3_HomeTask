"""Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""
def function():
    while True:
        try:
            x = int(input("Введите число : "))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        else:
            return x

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
us_namber = function()
#print(fibonacci(us_namber))
for i in range(us_namber):
    print(fibonacci(i+1))
"""Для отрицательных индексов чуть позже, не хватает времени """