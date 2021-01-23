def digit_in_card(file_name):
    with open(file_name, 'r', encoding='utf-8') as player_card:
        file = player_card.readlines()
        nums = []
        for lines in file:
            lines = lines.split()
            for elem in range(len(lines)):
                if 1 <= len(lines[elem]) <= 2:
                    nums.append(lines[elem])  # список из чисел и черточек
        if len(set(nums)) == 1:  # множество элементов в файле(если там только черточки, то заканчиваем игру)
            return False
        else:
            return True


def check_card(barrel):
    with open('player.txt') as player:
        file = player.read()
        if str(barrel) in file:
            return True
        else:
            return False
