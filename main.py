from math import sqrt


def direct_calculations(variant, c, result):
    '''
    Отвечает за рассчёт прямых погрешностей
    :param variant: какой вариант выбрали
    :param c: цена деления
    :param result: результат
    :return: абсолютную и относительную
    '''

    try:
        if variant == 1:
            print("Введите погрешность измеряемого прибора. Она должна быть на приборе")
            delta_device = float(input())

            absolute_p = round(delta_device + c / 2, 2)
            relative_p = round(delta_device / result) * 100

        elif variant == 2:
            print("Введите класс точности (если нет погрешности изм. прибора, класс точности быть обязан")
            accuracy_class = float(input())

            print("Введите максимальное значение измеряемого прибора")
            Max = float(input())
            delta_device = Max * (accuracy_class / 100)

            absolute_p = round(delta_device + c / 2, 2)
            relative_p = (delta_device / result)

    except variant <= 0 or variant > 2:
        print('введите 1 или 2')

    return (absolute_p, relative_p)


def staraight():
    '''
    Расчёт погрешности прямых измерений
    :return:
    '''

    print("Знаете ли вы погрешность измеряемого прибора (1 - да, 2 - нет)")
    variant = int(input())

    print("Введите цену деления прибора")
    c = float(input())

    print("Введите результат измерения")
    result = float(input())
    inaccuracy = direct_calculations(variant, c, result)
    absolut = inaccuracy[0]
    relative = inaccuracy[1]

    print("Результат с абсолютной погрешностью: ", result, "+-", round(absolut, 2))
    print("Относительная погрешность: ", round(relative * 100), "%", sep='')


def op1():
    '''
    Вычисления если в формуле только + и -
    :return:
    '''
    print("Введите количество переменных в формуле")
    count = int(input())
    lst = []

    print("Знаете ли вы абсолютные погрешности каждой из переменных в формуле? (1-да, 2 - нет)")
    var = int(input())

    if var == 1:
        for i in range(count):
            print("Введите абсолютную погрешность переменной")
            abs_p = float(input())
            lst.append(abs_p)

    elif var == 2:
        for i in range(count):
            print(f"Для {i + 1} переменной необходимо посчитать погрешность прибора и цену деления "
                  "Введите 1, если вы знаете погрешность прибора, 2, если не знаете")
            variant = int(input())

            print("Введите цену деления прибора (если она не указана на приборе, то считать ее равной нулю)")
            c = float(input())

            print(f"Введите результат измерения для {i + 1} переменной")
            result = float(input())

            inaccuracy_i = direct_calculations(variant, c, result)
            lst.append(inaccuracy_i[0])

    absolute_p = sum(lst)
    print("Введите результат искомого значения после подстановки всех переменных")

    value_result = float(input())
    relative_p = absolute_p / value_result

    print("Абсолютная погрешность: ", value_result, '+-', round(absolute_p, 2))
    print("Относительная погрешность: ", round(relative_p * 100), "%", sep='')


def op2():
    '''
    Вычисления если в формуле только * и /
    :return:
    '''
    print("Введите количество переменных в формуле")
    print(
        "Если в вашей формуле есть степени, например t^3, то количество переменных t умножается на три и для всех вычисляются одни те же значения погрешностей")
    print(
        "То есть, если ваша формула представлена в виде выражения: (mv^2)/2, то количество переменных в вашей формуле считать равным 3 "
        "Переменные: m, v, v. Для двух v вводить одинаковые значения, аналогично, если у вас кубы и т.д.")

    count = int(input())
    lst = []

    print("Знаете ли вы абсолютные погрешности каждой из переменных в формуле? (1 - да, 2 - нет)")
    var = int(input())

    if var == 1:
        for i in range(count):
            print(f"Введите абсолютную погрешность {i + 1} переменной")
            absolute_p = float(input())

            print(f"Введите результат измерения для {i + 1} переменной")
            result_1 = float(input())

            rel_p = absolute_p / result_1
            lst.append(rel_p)

    elif var == 2:
        for i in range(count):
            print(f"Для {i + 1} переменной необходимо посчитать погрешность прибора и цену деления "
                  "Введите 1, если вы знаете погрешность прибора, 2, если не знаете")
            variant = int(input())

            print("Введите цену деления прибора (если она не указана на приборе, то считать ее равной нулю)")
            c = float(input())

            print(f"Введите результат измерения для {i + 1} переменной")
            result = float(input())

            inaccuracy_i = direct_calculations(variant, c, result)
            lst.append(inaccuracy_i[1])

    relative_p = sum(lst)
    print("Введите результат искомого значения после подстановки всех переменных")

    result = float(input())
    absolute_p = result * relative_p

    print('Абсолютная погрешность: ', result, '+-', round(absolute_p, 2))
    print('Относительная погрешность: ', round(relative_p * 100), "%", sep='')


def op3():
    '''
    Вычисления, если в формуле +, -, *, /
    :return:
    '''
    print(
        "Разделите формулу на произведение и/или деление скобок и напишите сколько всего знаков * и / содержится в формуле? "
        "например: в формуле t = (m+j)*(n+k)/(x+z)*b всего 3 таких знака "
        "Если в вашей формуле имеются квадраты или другие степени, например, f = (x+y)^3, представляете данную формулу как (x+y)*(x+y)*(x+y), кол-во знаков = 3 ")

    count = int(input())
    list_of_rel_p = []

    for i in range(1, count + 2):
        list_of_c = []
        list_of_delta_devices = []

        print(f"Сколько переменных в {i} скобке?")
        n = int(input())

        for j in range(n):
            print(f"Для {j + 1} переменной найдите погрешность прибора и цену деления (см. на приборе) "
                  "p.s. Они может быть одинаковая для некоторых переменных")
            delta_device = float(input())
            c = float(input())

            list_of_delta_devices.append(delta_device)
            list_of_c.append(c)

        list_of_abs_p = []
        print(list_of_c)

        for k in range(len(list_of_c)):
            abs_p_k = list_of_delta_devices[k] + list_of_c[k]
            list_of_abs_p.append(abs_p_k)
            # print(f"абсолютная погрешность {k+1} переменной в скобке = {abs_p_k}")

        print("Введите результат суммы или разности в скобке")
        result = float(input())

        abs_p_result = sum(list_of_abs_p)

        print(abs_p_result, list_of_abs_p)
        rel_p_result = abs_p_result / result
        list_of_rel_p.append(rel_p_result)

    relative_p = sum(list_of_rel_p)

    print("Введите результат формулы после подстановки всех значений")
    res = float(input())
    absolute_p = relative_p * res

    print('Абсолютная погрешность: ', result, '+-', round(absolute_p, 2))
    print('Относительная погрешность: ', round(relative_p * 100), "%", sep='')


def rand():
    '''
    Данная функция вычисляет погрешность случайных измерений
    :return:
    '''

    print("Введите количество измерений")

    count = int(input())
    lst = []

    for i in range(count):
        print("Введите результат измерения")
        result = float(input())
        lst.append(result)

    x_average = sum(lst) / count

    lst2 = []
    for i in range(count):
        lst2.append((lst[i] - x_average) ** 2)

    sigma = sqrt(sum(lst2) / (count - 1))

    absolute_p = (3 * sigma) / sqrt(count)
    relative_p = (absolute_p / x_average) * 100

    print("Результат с абсолютной погрешностью: ", round(x_average), "+-", round(absolute_p))
    print("Относительная погрешность: ", round(relative_p), "%", sep='')


def main():
    print(
        "Какую погрешность вам необходимо расчитать? "
        "(1 - прямую, 2 - косвенную, 3 - случайную (погрешность многократных измерений))")

    var = int(input())

    if var == 1:
        staraight()

    if var == 2:
        print(
            "Введите 1, если в искомой формуле есть только знаки + или -, 2, "
            "если в искомой формуле присутствуют только знаки * или /, 3, если в искомой формуле присутствуют "
            "знаки +, -, * или /")
        option = int(input())

        if option == 1:
            op1()

        elif option == 2:
            op2()

        elif option == 3:
            op3()



    elif var == 3:
        rand()


main()
