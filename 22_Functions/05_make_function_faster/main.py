def calculating_math_func(data):
    if data in factorials:
        result = factorials[data]
    else:
        result = max(factorials.values())
        for index in range(max(factorials.keys()) + 1, data + 1):
            result *= index
            factorials[index] = result
    result /= data ** 3
    result = result ** 10
    return result


factorials = {1: 1}
while True:
    print(calculating_math_func(int(input('Введите число: '))))
    print(sorted(factorials.items()))