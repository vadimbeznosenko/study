"""
Для приготовления пирога необходимы следующие ингредиенты: масло, мука, сахар, яйца, сливки, орехи, вишня и ванилин.
Маша составила список имеющихся у нее продуктов: сахар, яблоки, груши, орехи, яйца, мука, крахмал, маргарин, молоко, мед.
Проверьте, сможет ли Маша приготовить пирог и выведите соответствующее сообщение на экран.
"""
# решение через множества

ingr = {'масло', 'мука', 'сахар', 'яйца', 'сливки', 'орехи', 'вишня', 'ванилин'}
exist_ingr = {'сахар', 'яблоки', 'груши', 'орехи', 'яйца', 'мука', 'крахмал', 'маргарин', 'молоко', 'мед'}

if exist_ingr >= ingr:
    print('Yes')
else:
    print('No')

# решение через циклы

for elem in ingr:
    if elem not in exist_ingr:
        print('No')
        break
else:
    print('Yes')
