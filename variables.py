# МОДУЛЬ 1

# Наименование овоща
name = "Картофель"

#  Количество мешков
q_packs = 3

# Общий вес, кг
weight = 172.4

# Мытый или нет
is_clear = True
# чтобы по-русски отвечал да или нет
rus_yesno = lambda x: "да" if x else "нет"

print(name, "количество мешков:", q_packs, "общий вес:", weight, "кг.", "чистый:", rus_yesno(is_clear))

print("Типы переменных:")
print("name ", type(name))
print("q_packs ", type(q_packs))
print("weight ", type(weight))
print("is_clear ", type(is_clear))
