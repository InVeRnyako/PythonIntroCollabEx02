# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

print("Введите число n:")
num = int(input())

fib0 = 0
fib1 = 1
fib2 = 1
i = 3
output = -1
while fib2 <= num:
    if fib2 == num:
        output = i
    fib2 = fib0 + fib1
    fib1 = fib2
    fib0 = fib1
    # print(i, ":", fib2) # Проверка правильности решения
    i += 1

print("Input:", num)
print("Output:", i)