# МОДУЛЬ2
attempt = 5
print(" У Вас будет ", attempt, "попыток")

while attempt > 0:
    answer = input("Введите год рождения А.С. Пушкина:")
    if answer.isdigit():  # проверяем введена ли цифра
        # если цифра , то проверяем ответ
        danswer = int(answer)
        if danswer == 1799:
            print("Верно!")
            break
        elif danswer > 1799:
            print("Много")
            attempt -= 1 # уменьшаем кол-во попыток
        else:
            print("Мало")
            attempt -= 1
        # если не цифра, то предупреждаем
    else:
        print("Введите цифры!!!")
    print("(осталось ", attempt, " попыток)")
