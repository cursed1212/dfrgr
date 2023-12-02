while True:
    p = input("Введите количество прошедших минут: ")
    if p.isdigit():
        break
    else:
        print("Пожалуйста, введите только цифры.")

p = int(p)

hours = (p // 60) % 24
minutes = p % 60

print("Часы:", hours)
print("Минуты:", minutes)