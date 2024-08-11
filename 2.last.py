def get_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (j + i) == 0:
                password += str(i) + str(j)
    return password


n = int(input("Введите число от 3 до 20: "))
if 3 <= n and n <= 20:
    password = get_password(n)
    print(f"Для числа {n} сгенерирован пароль: {password}")
else:
    print("для данного числа нет пароля :(")