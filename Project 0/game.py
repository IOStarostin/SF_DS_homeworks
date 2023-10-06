"""Игра угадай число"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Угадывание числа начинается со среднего значения для интервала от 1 до 100.
    Пока число не угадано, алгоритм уменьшает диапазон угадывания: если загаданное число 
    больше/меньше предложенного нами, то за наименьшее/наибольшее значение интервала
    принимаем предлагаемое нами число и считаем новое среднее.
    Функция принимает загаданное число и возвращает число попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    num_min=1
    num_max=100
    predict=(num_min+num_max)/2
    
    while number!= round(predict):
        count += 1
        if number>predict:
            num_min=predict
            predict=(num_min+num_max)/2
        elif number<predict:
            num_max=predict
            predict=(num_min+num_max)/2

    return count

def score_game(game_core) -> int:
    """За какое среднее количество попыток уградывания за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попытки")
    

#Run
if __name__ == '__main__':
    score_game(game_core_v3)