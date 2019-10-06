# МОДУЛЬ 6

# Пушкин 1799
# Лермонтов 1814
# Достоевский 1821
# Тургенев 1818
# Толстой 1828

while True:
    questions = 5
    ok = 0
    print("******************")
    print("ВИКТОРИНА")
    print("******************")

    answer = input("Назовите год рождения Пушкина:")
    if answer.isdigit() and int(answer) == 1799:    ok += 1

    answer = input("Назовите год рождения Лермонтова:")
    if answer.isdigit() and int(answer) == 1814:    ok += 1

    answer = input("Назовите год рождения Достоевский:")
    if answer.isdigit() and int(answer) == 1821:    ok += 1

    answer = input("Назовите год рождения Тургенев:")
    if answer.isdigit() and int(answer) == 1818:    ok += 1

    answer = input("Назовите год рождения Толстого:")
    if answer.isdigit() and int(answer) == 1828:    ok += 1

    print()
    print("******************")
    print("СТАТИСТИКА")
    print("******************")
    print("Правильных ответов - ", ok)
    print("Ошибок - ", questions - ok)
    print("Процент правильных ответов - ", ok * 100 / questions, "%")
    print("Процент ошибок - ", (questions - ok) * 100 / questions, "%")

    answer = input("Хотите еще попытку (Y/n) ?")
    if not ((answer == "Y") or (answer == "y")):
        break
