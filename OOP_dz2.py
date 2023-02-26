from pprint import pprint

with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        quan_prod = int(f.readline())
        prod = []
        for i in range(quan_prod):
            ingrid = f.readline().strip()
            product, quantity, unit = ingrid.split(' | ')
            prod.append(
                {'ingredient_name': product, 'quantity': quantity, 'measure': unit})
        cook_book[dish] = prod
        f.readline()

pprint(cook_book, width=100)
print()

list_dishes = ['Омлет', 'Фахитос']
def get_shop_list_by_dishes(list_, person):
    result = {}
    list_keys = []
    for i in list_:
        for j in cook_book[i]:
            ing_ = j['ingredient_name']
            mes_ = j['measure']
            quan_ = int(j['quantity'])
            if j['ingredient_name'] not in list_keys:
                list_keys.append(j['ingredient_name'])
                res = {ing_: {'measure': mes_, 'quantity': quan_ * person}}
                result.update(res)
            else:
                my_dict = result[j['ingredient_name']]
                quantity_1 = int(my_dict['quantity'])
                res = {ing_: {'measure': mes_, 'quantity': quan_ * person + quantity_1}}
                result.update(res)
    return pprint(result)

get_shop_list_by_dishes(list_dishes, 3)
