import sys
def func1(grade,name,main):  # Функція, яка реалізує додавання ім'я учня до словника
    if grade == str(1):      # у випадку, якщо дитина є учнем молодшої школи
        main['1'].append(name)
        return main
    elif grade == str(2):
        main['2'].append(name)
        return main
    elif grade == str(3):
        main['3'].append(name)
        return main
    elif grade == str(4):
        main['4'].append(name)
        return main
    else:
        print('error')
def flag1(choice):                              # Функція яка реалізує реалізує взаємодію між
    if choice != str(0) and choice != str(1):   # програмою та користувачем
        raise ValueError
    elif choice == str(0):
        return True
    else:
        return False
def func():                                      # Головна функція
    main = {'1': [], '2': [], '3': [], '4': []}  # Словник, у якому зберігаються імена учнів та їх клас
    for i in range(99999):
        print('Для того, щоб додати учня введіть 0, закінчити роботу - 1: ')
        choice = input()
        while flag1(choice) == True:

            print('Введіть ПІБ: ')
            name = input()
            print('Введіть класс: ')
            grade = input()
            if grade != str(1) and grade != str(2) and grade != str(3) and grade != str(4):
                raise ValueError
            main = func1(grade,name,main)
            print('Учні 1 класу: ' , main['1'])
            print('Учні 2 класу: ' , main['2'])
            print('Учні 3 класу: ' , main['3'])
            print('Учні 4 класу: ' , main['4'])
            print('Для того, щоб додати учня введіть 0, закінчити роботу - 1: ')
            choice = input()
        else:
            sys.exit()
    
if __name__ == '__main__':
    func()