def user_data(name, surname, birthday, city, email, phone):
    return ' '.join([name, surname, birthday, city, email, phone])


user_name = input('Имя: ')
user_surname = input('Фамилия: ')
user_birthday = input('Год рождения: ')
user_city = input('Город: ')
user_email = input('Email: ')
user_phone = input('Телефон: ')
print(user_data(name=user_name, surname=user_surname, birthday=user_birthday
                , city=user_city, email=user_email, phone=user_phone))