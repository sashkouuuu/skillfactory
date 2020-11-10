import numpy as np

def get_new_predict(min_value, max_value):
    """Функция получает максимальное и минимальное число, на основе
    которых генерируется и возвращается новое предполагаемое число.

    """
    return (min_value+max_value) // 2


def game_core(number, min_number, max_number):
    """Сначала устанавливаем половини значения от максимальное значения 
    в диапазоне, а потом генерируем новое число в функции
    get_new_predict.

       Функция принимает загаданное число, минимальное и максимальное 
    значение диапазона и возвращает число попыток.

    """
    count = 1
    predict = max_number // 2

    while number != predict:
        count += 1

        if number > predict:
            min_number = predict
            predict = get_new_predict(min_number, max_number)
        elif number < predict:
            max_number = predict
            predict = get_new_predict(min_number, max_number)

    return(count)
        

def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра
    угадывает число.

    """
    min_number = 1
    max_number = 101
    count_ls = []
    # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)  
    random_array = np.random.randint(min_number,max_number, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number, min_number, max_number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


def main():
    score_game(game_core)


if __name__ == '__main__':
    main()
