
choice_list = []
restaurant_list = ['','Farm Burger','Ru San\'s','Chipotle']

for i in range(0,5):
    # make list of choices
    for i in range(1, len(restaurant_list)):
        print ' %d. %s' % (i, restaurant_list[i])

    # add "create restaurant" option to end of list    
    print ' %d. Add a new restaurant to the list.' % len(restaurant_list)

    # ask which restaurant (or create new)
    choice = int(raw_input('Pick a restaurant: '))
    if choice == 0 or choice > len(restaurant_list):
        break

    # if choice is the last on list, create new restaurant
    if choice == len(restaurant_list):
        new_restaurant = raw_input('Name of restaurant: ')
        # add new rest to list
        restaurant_list.append(new_restaurant)
    choice_list.append(choice)
    choice_count = choice_list.count(choice)
    print '** %s ** (times chosen: %d)' % (restaurant_list[choice], choice_count)
    if choice_count > 2:
        break

print '\n********* Bye **********\n'