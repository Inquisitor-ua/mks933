def ask_number(callback):
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    return callback(num1, num2)

def main():
    action = input("Выберите действие (1 - умножить, 2 - возвести в степень): ")
    if action == '1':
        print(ask_number(lambda x, y: x * y))
    elif action == '2':
        print(ask_number(lambda x, y: x ** y))
    else:
        print("Не понял тебя")
        return main()
    
if __name__ == "__main__":
    main()