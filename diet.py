shopping_list = weekly_plan = {'яйцо': 35,
                               'овсянка': 1.4,
                               'греча':1.4,
                               'морковь': 1,
                               'бекон':1,
                               'сыр': 200,
                               'лук':500,
                               'творог':14,
                               'йогурт':1}
shopping_list_meatandbread_sep = {'фарш':2000,
                                  'курица':1000,
                                  'хлеб':1}

counter = 0
for num in range(1,8,3):
    counter += 1
    one_third_shopping = {product: round(value / 3, 1) for product, value in shopping_list_meatandbread_sep.items()}
    if num == 1 or num ==7 :
        full_basket = shopping_list| one_third_shopping
        print(f'{num} день и купи {full_basket}')
    if counter == 4:
        print(f'{one_third_shopping} день и купи мясо и курицу{one_third_shopping}')
    if num == 4:
        print(f'{num} день и купи {one_third_shopping}')
    else:
        print('сиди дома')



print()
print(f' total vizit in magaz {counter}')