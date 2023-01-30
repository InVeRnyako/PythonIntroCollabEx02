# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

print("Введите неотрицательное число N: ")
num = int(input())

print("Input:", num)
# fact = 1
# while num > 1:
#     fact *= num # fact = fact * num
#     num -= 1

fact = 1
for i in range(1,num+1):
    fact *= i # fact = fact * i

print("Output: ", fact)

