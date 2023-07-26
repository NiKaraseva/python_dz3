# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

arguments = [1, 2, 3, 1, 2, 4, 5, 2, 1, 5, 7]

double_arg = []
for item in arguments:
    if arguments.count(item) > 1 and item not in double_arg:
        double_arg.append(item)
print(double_arg)
