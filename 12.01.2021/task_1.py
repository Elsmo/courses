with open('ex_1.txt', 'a', encoding='utf-8') as new_file:
    print('Вводите уже хоть что-нибудь')
    while True:
        line = input()
        new_file.write(line + '\n')
        if not line or line == '\n':
            print('Ну вот и все. Мы все записали, а дальше вы сами разбирайтесь')
            break
