# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import itertools

bag_contents = {'рюкзак': 3, 'палатка': 5, 'котелок': 4, 'фонарик': 2, 'спички': 1, 'компас': 3}
MAX_LIMIT = 10
bag_weight = 0
all_var = set()

""" Вариант со всеми наборами """
perm_set = itertools.permutations(bag_contents.items())

for item in perm_set:
    current_weight_limit = MAX_LIMIT
    my_bag = set()
    for i in item:
        if i[1] <= current_weight_limit:
            my_bag.add(i[0])
            current_weight_limit -= i[1]
    all_var.add(tuple(my_bag))
print(all_var)

""" Вариант с 1 набором """
# for key, value in bag_contents.items():
#     if value <= MAX_LIMIT:
#         my_bag.append(key)
#         MAX_LIMIT -= value
# print(my_bag)