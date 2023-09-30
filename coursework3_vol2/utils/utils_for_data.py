from utils.utils_for_file import load_data


def slice_data(data: list, count_id: int = 5):
    """
    выводит последние count_id выполненных (EXECUTED) на экран.
    :param data: список со словарями
    :param count_id: количество айди для вывода
    :return: список со словарями
    """
    res = []
    for i in reversed(data):
        while len(res) != count_id:
            if i["state"] == "EXECUTED":
                res.append(i)
                break
            else:
                break
    return list(reversed(res))

print(slice_data(load_data()))

def magic_with_N_card(s: str = "MasterCard 7158300734726758"):
    """Получает строку с цифрами номера карты, вставляет в середину
    звездочки, оставляет шесть цифр слева и четыре справа"""
    s = s.split()
    return s[0] + " " + s[1][4:6] + '** ****' + s[1][-4:]


#16 цифр
# s = "MasterCard 7158300734726758"
# print(magic_with_N_card(s))

def magic_with_N_account(s: str = "Счет 64686473678894779589"):
    """Получает строку с цифрами номера счета.
    Оставляет спереди добавляет звездочки, оставляет последние
    четыре цифры"""

    return "**" + s[-4:]

# s = "Счет 64686473678894779589"
# print(len(magic_with_N_account(s)))

def magic_with_date(s: str = "2019-08-26T10:50:58.294041"):
    """Получает строку с датой. Выводит строку в формате ДД.ММ.ГГГГ"""
    s = s[0:10]
    res = s.split('-')
    return res[-1] + '.' + res[-2] + '.' + res[-3]

# s = "2019-08-26T10:50:58.294041"
# print(type(magic_with_date(s)))