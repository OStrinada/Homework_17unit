error = 'ПЕРЕЗАПУСТИТЕ ПРОГРАММУ И ВВЕДИТЕ КОРРЕКТНЫЕ ДАННЫЕ.'

sequence_num = input('Введите последовательность целых чисел через пробел: ')

while True:
    try:
        some_num = int(input('Введите любое целое число: '))
        if type(some_num) == int:
            break
    except ValueError:
        print('\nВведите число в соответствии с условиями ввода.')
def is_int(string):
    string = string.replace(' ', '')
    try:
        int(string)
        return True
    except ValueError:
        return False

if " " not in sequence_num:
    print("\nВ вводе отсутствуют пробелы. Введите числа в соответствии с условиям ввода.")
    sequence_num = input('Введите последовательность целых чисел через пробел: ')
if not is_int(sequence_num):
    print('\nВ вводе последовательности чисел содержатся не цифры либо введены не целые числа.\nВведите числа в соответствии с условиям ввода.')
    print(error)
else:
    sequence_num = sequence_num.split()

list_sequence_num = [int(item) for item in sequence_num]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_sequence_num = merge_sort(list_sequence_num)

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка.\nПерезапустите программу и введите меньшее число.'

print(f'Упорядоченный список: {list_sequence_num}')

if not binary_search(list_sequence_num, some_num, 0, len(list_sequence_num)):
    rI = min(list_sequence_num, key=lambda x: (abs(x - some_num), x))
    ind = list_sequence_num.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < some_num:
        print(f'Ближайший меньший элемент: {rI}, его индекс: {ind}')
    elif min_ind < 0:
        print(f'''В списке нет меньшего элемента.
Ближайший больший элемент: {rI}, его индекс: {list_sequence_num.index(rI)}
Перезапустите программу и введите другое число.''')
else:
    print(f'Индекс введенного элемента: {binary_search(list_sequence_num, some_num, 0, len(list_sequence_num))}')
