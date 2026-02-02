import module


while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")
    
    choice = int(input("Введите номер операции (1/2/3/4/5): "))

    if choice == 5:
        break
    
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if choice == 1:
        module.summa(num1, num2)
    elif choice == 2:
        module.racnost(num1, num2)
    elif choice == 3:
        module.umnozh(num1, num2)
    elif choice == 4:
        module.delenie(num1,)           
    else:
        print("Неизвестная операция. Попробуйте снова.")
