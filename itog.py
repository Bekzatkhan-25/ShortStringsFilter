def filter_short_strings(strings):
    new_array = []
    for string in strings:
        if len(string) <= 3:
            new_array.append(string)
    return new_array

# Примеры массивов для проверки
array1 = ["Hello", "2", "world", ":-)"]
array2 = ["1234", "1567", "-2", "computer science"]
array3 = ["Russia", "Denmark", "Kazan"]

filtered_array1 = filter_short_strings(array1)
print("Новый массив 1:", filtered_array1)

filtered_array2 = filter_short_strings(array2)
print("Новый массив 2:", filtered_array2)

filtered_array3 = filter_short_strings(array3)
print("Новый массив 3:", filtered_array3)
