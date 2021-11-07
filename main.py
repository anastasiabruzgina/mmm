def rot(num):
    result = int(str(num).replace('6', '9', 1))
    print(f'Максимальное число - {result}')
    return result

num = int(input('Введите число из шестерок и девяток: '))

rot(num)