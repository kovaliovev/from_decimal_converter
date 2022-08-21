def replacing(list):
    for i in range(len(list)):
        if 9 < int(list[i]) < 36:
            list[i] = chr(int(list[i]) + 55)
    return list


def converting(number, base):
    result = list()
    while number >= 1:
        result.append(str(number % base))
        number //= base
    replacing(result)
    return ''.join(result[::-1])


num = int(input('Input your decimal number \n'))
base = int(input('Input base you need (2 = binar) \n'))
print(f'Your number: {converting(num, base)}')
input('Input something to exit')
