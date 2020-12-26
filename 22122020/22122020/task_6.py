goods = {'название': None, 'цена': None, 'количество': None, 'ед': 'шт' } # для товаров, кот вносит пользователь
analytics = goods.copy() # для создания сводки по харак-кам
goods_in_store = []
name, coast, k = [], [], [] # для записи каждой из характеристик
num = int(input('Введите количество разных наименований на складе: ')) # решение проблемы с вводом данных
i = 0
while i < num :
    goods['название'] = input('Введите наименование товара: ') # спрашиваем у пользователя
    name.append(goods.get('название')) # добавляем полученную инфу в список
    goods['цена'] = int(input('Введите цену товара: '))
    coast.append(goods.get('цена'))
    goods['количество'] = int(input('Введите количество товара: '))
    k.append(goods.get('количество'))
    goods_in_store.append(goods.copy())
    i += 1
structure = enumerate(goods_in_store, 1) # чтобы при желании можно было посмотреть по отдельной позиции
analytics.update({'название': name, 'цена': coast, 'количество': k, 'ед': 'шт' })
print(analytics.items())