def summa(n):
    a = 0
    s = 0
    while n > 0:
        a = n % 10
        n //= 10
        if a % 2 == 1:
            s += a
    return s

try:
    n = int(input('Введите число: '))
except ValueError:
    print('Введите целое число')
else:
    if n != 0:
        if n < 0:
            n *= -1
        print('Сумма всех цифр числа -', summa(n))
    else:
        print('Cумма всех цифр числа равна нулю.')