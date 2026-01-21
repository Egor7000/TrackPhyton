numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим сумму всех чисел, кроме None
total_sum = sum(num for num in numbers if num is not None)

# Количество элементов берём ВСЕ, включая пропуск
count = len(numbers)

# Среднее арифметическое
average = total_sum / count

# Заменяем None на среднее значение
numbers[numbers.index(None)] = average

print("Измененный список:", numbers)
