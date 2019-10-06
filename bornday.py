# МОДУЛЬ 3

answer_year = input("Введите год рождения А.С. Пушкина:")

if int(answer_year) == 1799:
    print("Верно!!")
    # спросим теперь день
    answer_day = input("Введите день рождения (по новому стилю):")
    if int(answer_day) == 6:
        print("Верно!!")
    else:
        print("Неправильный день!")
else:
    print("Иди учить литературу!")