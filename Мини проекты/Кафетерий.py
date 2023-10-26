menu = {'Drinkables': ['Coffee $1.5', 'Tea $1.2', 'Juise $1.7'],
        'Bakery': ['Croissant $2.4', 'Donut $2.0', 'Cake $2.5'],
        'Desserts': ['Ice_cream $3.0', 'Tiramisu $3.5', 'Marshmallows $2.7']}
selection_menu = {1: menu['Drinkables'],
                  2: menu['Bakery'],
                  3: menu['Desserts']}
order = []
exceptions = [['yes', 'Yes', 'YES'], ['no', 'No', 'NO']]
print('We welcome you to our cafeteria!', end='\n' * 2)
answer = input('Want to place an order? -> ')
print()
while (answer not in exceptions[0]) and (answer not in exceptions[1]):
    print('Incorrect answer! Please try again...')
    answer = input('Want to place an order? -> ')
    print()
if answer in exceptions[0]:
    position = 0
    while answer in exceptions[0]:
        print("Ok, what would you like to order?")
        proposed_choice = []
        variant = 0
        for i in menu:
            variant += 1
            print(str(variant) + '.', i)
        print()
        answer2 = int(input('Your choice -> '))
        print()
        while answer2 < 1 or answer2 > 3:
            print('Incorrect answer! Please try again...', end='\n' * 2)
            answer2 = int(input('Your choice -> '))
            print()
        print('Okay we have:')
        variant = 0
        for i in selection_menu[answer2]:
            variant += 1
            print(str(variant) + '.', i)
            proposed_choice.append(i)
        print()
        print('What do you choose?')
        answer3 = int(input('Your choice -> '))
        order.append([proposed_choice[answer3 - 1]])
        print()
        print('How many?')
        answer4 = int(input('Quantity -> '))
        for f in range(answer4 - 1):
            order[position].append(proposed_choice[answer3 - 1])
        print()
        answer = input('Something else? -> ')
        print()
        position += 1
        while answer not in exceptions[0] and answer not in exceptions[1]:
            print('Incorrect answer! Please try again...')
            answer = input('Something else? -> ')
    print('Ok, your order is:')
    total = 0
    position = 0
    for j in range(len(order)):
        total += float(order[j][0][-3:]) * int(order[j].count(order[j][0]))
        print(order[j][0][:-5], order[j][0][-4:], 'x', order[j].count(order[j][0]))
    print()
    print('Total', '=', '$' + str(round(total, 2)))
elif answer in exceptions[1]:
    print('Then we wish you all the best!!! Goodbye')
