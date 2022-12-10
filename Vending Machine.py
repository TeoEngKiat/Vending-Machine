#Author: Teo Eng Kiat Ivan
#Admin No: 211926R


#Inventory of the vending machine
inventory = {"IM": {'description': 'Iced Milo', 'price': 1.5, 'quantity': 2},
             'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 2},
             'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50},
             'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
             'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
             '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 50}}

#Below are the functions used in this program
def check_stock():
    for key in inventory:
        if inventory[key]['quantity'] == 0:
            inventory[key]['quantity'] = '***out of stock***'
        print(f'{key}. {inventory[key]["description"]}  '
              f'(S${inventory[key]["price"]})    '
              f'Qty: {inventory[key]["quantity"]}')
        if inventory[key]['quantity'] == '***out of stock***':
            inventory[key]['quantity'] = 0

# checked is used in replenish drink to make sure inventory is only displayed once
checked = False

def add_drink_type(drink_id, description, price, quantity):
    inventory.update({drink_id: {'description': description, 'price': price, 'quantity': quantity}})
    print(inventory)

def replenish_drink(drink_id, quantity):
    inventory[drink_id]['quantity'] += quantity
    print(f'{inventory[drink_id]["description"]} has been top up!')
    print(inventory)

#To ensure that only Y and N are execpted
while True:
    vendor = input('Are you a vendor (Y/N)? ')
    vendor = vendor.upper()
    if vendor == "N" or vendor == "Y":
        break
    else:
        print('Invalid Option')
        continue

print('Welcome to ABC Vending Machine. [Press 0 to exit]')
print('Select from the following choices to continue:')


if vendor.upper() == 'N':
    check_stock()
    t_cost = 0
    cost = 0
    count = 0
    while True:
        t_cost += cost
        cost = 0
        try:
            D_choice = input('Enter choice: ')
            if D_choice == '0':
                break
            else:
                D_choice = D_choice.upper()
                if inventory[D_choice]['quantity'] == 0:
                    print(f'{inventory[D_choice]["description"]} is out of stock')
                    continue
        except KeyError:
            print('Invalid option')
            continue

        inventory[D_choice]['quantity'] -= 1

        if D_choice == 'IM' or D_choice == 'IC':
            cost = 1.5
        elif D_choice == 'HM' or D_choice == 'HC':
            cost = 1.2
        elif D_choice == '1P':
            cost = 1.1
        elif D_choice == 'CC':
            cost = 1.3
        elif D_choice == '0':
            break
        else:
            print('Invalid option')
            cost = 0
            continue
        count += 1
        print(f'No. of drinks selected =  {count}')
    if t_cost == 0:
        exit()
    print(f'Please pay: ${t_cost:.2f}')
    while True:
        print('Indicate your payment:')
        while True:
            Dollar_10 = input("Enter no. of $10 notes: ")
            if not Dollar_10.isdigit():
                print('Invalid amount of notes')
                continue
            else:
                break

        Dollar_10 = int(Dollar_10)
        Dollar_10 *= 10
        if Dollar_10 == t_cost:
            print('Drinks paid. Thank you.')
            exit()
        elif Dollar_10 > t_cost:
            print(f'Please collect your change: ${Dollar_10 - t_cost:.2f}')
            print('Drinks paid. Thank you.')
            break
        else:
            amount_left = t_cost - Dollar_10
            while True:
                Dollar_5 = input('Enter no. of $5 notes: ')
                if not Dollar_5.isdigit():
                    print('Invalid amount of notes')
                    continue
                else:
                    break
            Dollar_5 = int(Dollar_5)
            Dollar_5 *= 5
            if Dollar_5 == amount_left:
                print('Drinks paid. Thank you.')
                exit()
            elif Dollar_5 > amount_left:
                print(f'Please collect your change: ${Dollar_5 - amount_left:.2f}')
                print('Drinks paid. Thank you.')
                exit()
            else:
                amount_left = amount_left - Dollar_5
                while True:
                    Dollar_2 = input('Enter no. of $2 notes: ')
                    if not Dollar_2.isdigit():
                        print('Invalid amount of notes')
                        continue
                    else:
                        break
                Dollar_2 = int(Dollar_2)
                Dollar_2 *= 2
                if Dollar_2 == amount_left:
                    print('Drinks paid. Thank you.')
                    exit()
                elif Dollar_2 > amount_left:
                    print(f'Please collect your change: ${Dollar_2 - amount_left:.2f}')
                    print('Drinks paid. Thank you.')
                    exit()
                else:
                    print('Not enough to pay for the drinks')
                    print('Take back your cash!')
                    while True:
                        redo = input('Do you want to cancel the purchase? Y/N: ')
                        if redo.upper() == 'Y' or redo.upper() == 'N':
                            break
                        else:
                            continue
                    if redo.upper() == 'Y':
                        print('Purchase is cancelled. Thank you.')
                        exit()
                    else:
                        continue
    print(inventory)


elif vendor.upper() == 'Y':
    print('''1. Add Drink Type
2. Replenish Drink
0. Exit''')
    while True:
        while True:
            action = input('Enter choice: ')
            if action == '1' or action == '2':
                break
            elif action == '0':
                exit()
            else:
                print('Invalid option.')
                continue

        if action == '1':
            while True:
                id = input('Enter drink id: ')
                id = id.upper()
                if id in inventory:
                    print('Drink id exists!')
                    continue
                else:
                    break
            desc = input('Enter description of drink: ')
            value = 0
            while True:
                try:
                    value = float(input('Enter price: $'))
                except ValueError:
                    print('Invalid pricing')
                    continue
                else:
                    break

            while True:
                quant = input('Enter quantity: ')
                if not quant.isdigit():
                    print('Invalid amount of drinks')
                else:
                    quant = int(quant)
                    break
            add_drink_type(id, desc, value, quant)

        elif action == '2':
            if checked == False:
                check_stock()
            while True:
                id = input('Enter drink id: ')
                id = id.upper()
                if id not in inventory:
                    print('No drink with this drink id. Try again.')
                    continue
                elif inventory[id]['quantity'] > 5:
                    print('No need to replenish. Quantity is greater than 5.')
                else:
                    while True:
                        try:
                            quant = int(input('Enter quantity: '))
                            replenish_drink(id, quant)
                            break
                        except ValueError:
                            print('Invalid amount.')
                break
        checked = True
        continue
