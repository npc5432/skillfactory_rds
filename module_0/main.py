import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
print("Загадано число от 1 до 100")

def game_core_v3(number):
    '''При каждой попытке делим интервал пополам.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    lower, upper = 1, 100
    predict = (lower + upper) // 2
    while number != predict:
        count += 1
        if number > predict:
            lower, upper = predict+1, upper
        else:
            lower, upper = lower, predict-1
        predict = (lower + upper) // 2
    return count

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
score_game(game_core_v3)
