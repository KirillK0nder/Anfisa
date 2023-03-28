import datetime as dt
import dataBase as d


# Все вопросы Анфисе
# количество друзей
# кто мои друзья (Имена)
# склонять по количеству (3 друга, 10 друзей)
# выдача место положение друзей
# выдача часового пояса друзей

def place_frend():
    # это функция нужна для определения города наших друзей
    x = []
    for i, j in d.DATABASE.items(): # items это ключ и его значения одновременно
        x.append(f"{i} - место жительства ")
        x.append(f"{j}\n")
    r = "".join(x)

    return r
def who_my_frend():
    # Функция для выдачи имени друга
    x = []

    for i in d.DATABASE.keys():
        x.append(i)
    y = ",".join(x)  # список преобразуем в строку
    return y


def key_frend():
    # функция для знания количество друзей(количество склоняется)
    if len(d.DATABASE) == 1:
        return f"{len(d.DATABASE)} друг"

    elif 1 < len(d.DATABASE) <= 4:
        return f"{len(d.DATABASE)} друга"

    elif len(d.DATABASE) >= 5:
        return f"{len(d.DATABASE)} друзей"

    else:
        return "К сожалению у вас нет ни одного друга"


def question(x):
    # Функция для обработки вопросов
    if x == "Сколько у меня друзей?" or x == "Сколько у меня друзей":
        return key_frend()

    elif x == "Кто мои друзья?" or x == "Как зовут моих друзей?" or x == "Кто мои друзья" or x == "Как зовут моих друзей":
        return who_my_frend()

    elif x == "Где живут мои друзья?" or x == "Откуда мои друзья?" or x == "Где проживают мои друзья?" \
            or "Где живут мои друзья" or x == "Откуда мои друзья" or x == "Где проживают мои друзья":
        return place_frend()

    else:
        return "Некорректный вопрос!"


print(question("Сколько у меня друзей"))





