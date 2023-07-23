with open('recipe.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        components = int(file.readline())
        components_list = []
        for i in range(components):
            product, quantity, measure = file.readline().strip().split(' | ')
            components_list.append({
                'product': product,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = components_list

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrediente in cook_book[dish]:
                if ingrediente['product'] in result:
                    result[ingrediente['product']]['quantity'] += int(ingrediente['quantity']) * person_count
                else:
                    result[ingrediente['product']] = {'measure': ingrediente['measure'],'quantity': (int(ingrediente['quantity']) * person_count)}
        else:
            print('Такого блюда нет в кулинарной книге')
    print(result)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
