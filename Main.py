# Lai Cheong Kian
# TP064962

def login_page():
    print('-' * 8, 'Welcome to FRESHCO.Sdn.Bhn', '-' * 8)
    while True:
        print('-' * 44)
        option = ['Admin', 'New Customer', 'Registered Customer', 'Quit Program']
        number = 1
        for i in option:
            print(number, ') ', i)
            number = number + 1
        answer = input('select type of login (1-4): ')          #select 1 to 4
        if answer == '1':
            admin_login_page()
            break
        elif answer == '2':
            new_customer_page()
            break
        elif answer == '3':
            customer_login_page()
            break
        elif answer == '4':
            exit()
        else:
            print('(please select number 1 to 3 only)')
            continue


def admin_login_page():
    id_key = 'LCK'
    pass_key = '1'
    print('-' * 5, 'ADMIN LOGIN', '-' * 5)
    user_id = input('ID: ').upper()
    password = input('Password: ').upper()
    if user_id == id_key and password == pass_key:      #check if id and passwrod correct anot
        admin_menu()
    else:
        print('(Wrong Id or Password)')
        login_page()


def admin_menu():
    while True:
        print('-' * 5, 'Admin Menu', '-' * 5)
        option = ['Upload', 'View Groceries', 'Update/Modify', 'Delete',
                  'Search Groceries', 'View Customer Order',
                  'Search Customer order', 'Exit']
        numbering = 1
        for i in option:
            print(str(numbering) + ') ' + i)
            numbering = numbering + 1
        select = input('Select your option: ')          #choose which operation to go 
        if select == '1':
            upload()
            break
        elif select == '2':
            view_groceries()
            break
        elif select == '3':
            modify()
            break
        elif select == '4':
            delete()
            break
        elif select == '5':
            view_specific_groceries()
            break
        elif select == '6':
            view_all_customer_order()
            break
        elif select == '7':
            search_customer_order()
            break
        elif select == '8':
            login_page()
            break
        else:
            print('Only type 1 to 8')


def upload():
    print('-' * 5, 'Upload', '-' * 5)
    print()
    item_name = []
    Serial_number = []
    file = open('groceries detail.txt', 'r')
    for i in file.readlines():
        item_name.append(i.split()[1])
        Serial_number.append(i.split()[0]) #bring data from txt into list
    item = []
    while True:         #input information
        while True:
            try:
                SN = int(input('Serial Number: '))
                break
            except:
                print('Only Number!')
        if len(str(SN)) == 4:
            if str(SN) in Serial_number:
                print('Serial number is used')
                continue
            else:
                break
        else:
            print('only 4 digit number')
            continue
    item.append(str(SN))
    while True:
        name = input('Name: ').upper()
        if name in item_name:
            print('item exist')
            continue
        else:
            break
    item.append(name)
    print('Expired date')
    import datetime
    x = True
    y = []
    while x:
        while True:
            try:
                Year = int(input("Year: "))
                Month = int(input("Month: "))
                Day = int(input("Date: "))
                y = datetime.date(Year, Month, Day)
            except:
                print("Invalid Entry")
                continue
            if Year < 2022:
                print('error year')
                continue
            else:
                x = False
                break
    expired_date = str(y)
    item.append(expired_date)
    while True:
        try:
            price = int(input('Price: '))
        except:
            print('Only Number!')
        if price < 1:
            print('minimum 1')
            continue
        else:
            break

    item.append(str(price))
    specification = input('Specification: ')
    item.append(specification)
    while True:
        try:
            amount = int(input('Amount: '))
        except:
            print('Only Number!')
        if amount < 1:
            print('minimum 1')
            continue
        else:
            break
    item.append(str(amount))
    file = open('groceries detail.txt', 'a')
    for i in item:
        file.write(i + ' ')
    file.write('\n')
    file.close()
    print('.')
    print('-' * 5, 'UPLOAD COMPLETE', '-' * 5)  #bring data back to txt from list 
    print('.')                                  
    while True:
        ask = input('1) Continue\n2) Back\n: ')
        if ask == '1':
            upload()
        elif ask == '2':
            admin_menu()


def view_groceries():
    print('-' * 15, 'Groceries List', '-' * 15)
    print('No', '-' * 2, 'Serial Code', '-' * 4, 'Name', '-' * 8, 'Expired date', '-' * 4, 'Price',
          '-' * 4, 'Specification', '-' * 4, 'Amount')
    numbering = 1
    file = open('groceries detail.txt', 'r')  #bring data from txt into list and print out
    for i in file.readlines():
        data = i.split()
        print(numbering, ')', ' ',
              data[0], " " * (15 - len(data[0])),
              data[1], ' ' * (12 - len(data[1])),
              data[2], ' ' * (16 - len(data[2])),
              'RM', data[3], ' ' * (6 - len(data[3])),
              data[4], ' ' * (17 - len(data[4])),
              data[5], )
        numbering = numbering + 1
    print('-' * 88)
    while True:
        ask = input('press 1 to back \n: ')
        if ask == '1':
            admin_menu()
            break
        else:
            continue


def view_groceries_for_function():   #duplicated view groceies that can use inside function
    print('-' * 15, 'Groceries List', '-' * 15)
    print('No', '-' * 2, 'Serial Code', '-' * 4, 'Name', '-' * 8, 'Expired date', '-' * 4, 'Price',
          '-' * 4, 'Specification', '-' * 4, 'Amount')
    numbering = 1
    file = open('groceries detail.txt', 'r')
    for i in file.readlines():
        data = i.split()
        print(numbering, ')', ' ',
              data[0], " " * (15 - len(data[0])),
              data[1], ' ' * (12 - len(data[1])),
              data[2], ' ' * (16 - len(data[2])),
              'RM', data[3], ' ' * (6 - len(data[3])),
              data[4], ' ' * (17 - len(data[4])),
              data[5], )
        numbering = numbering + 1
    file.close()
    print('-' * 88)


def delete():
    view_groceries_for_function()
    while True:
        try:
            ask = int(input('which item you want to delete: ')) #ask item to delete
            break
        except:
            print('Only Number!')
    ask = ask - 1
    item_list = []
    file = open('groceries detail.txt', 'r') #bring data from txt into list
    count = 0
    position = []
    for i in file.readlines():
        item_list.append(i.split())
        if ask == count:
            position = count
        count = count + 1
    item_list.remove(item_list[position])
    file.close()
    file = open('groceries detail.txt', 'w')#bring data back to txt from list 
    for i in item_list:
        for y in i:
            file.write(y + ' ')
        file.write('\n')
    file.close()
    print()
    print()
    view_groceries_for_function()
    while True:
        ask = input('1) Continue\n2) Back\n: ')
        if ask == '1':
            delete()
        elif ask == '2':
            print('error')
            admin_menu()


def modify():
    view_groceries_for_function()
    print('which one to modify: ')
    ans = input(':')
    modify_list = []
    file = open('groceries detail.txt', 'r')   #bring data from txt into list
    for i in file.readlines():
        modify_list.append(i.split())
    file.close()
    selected_list = modify_list[int(ans) - 1]  #bring out the data of the chosen item and user choose which to edit from the data
    option = ['Serial Code', 'Name', 'Expired Date', 'Price', 'Specification', 'Amount']
    numbering = 1
    for i in option:
        print(str(numbering) + ') ' + i)
        numbering = numbering + 1
    ans_2 = input(':')
    if ans_2 == '1':
        while True:
            while True:
                try:
                    new = input('Serial Code: ')
                    break
                except:
                    print('Only Number!')
            if len(str(new)) == 4:
                selected_list[int(ans_2) - 1] = str(new)
                break
            else:
                print('only 4 digit number')
                continue

    elif ans_2 == '2':
        new = input('Name: ')
        selected_list[int(ans_2) - 1] = str(new)
    elif ans_2 == '3':
        print('Expired date')
        import datetime
        x = True
        y = []
        while x:
            while True:
                try:
                    Year = int(input("Year: "))
                    Month = int(input("Month: "))
                    Day = int(input("Date: "))
                    y = datetime.date(Year, Month, Day)
                except:
                    print("Invalid Entry")
                    continue
                if Year < 2022:
                    print('error year')
                    continue
                else:
                    x = False
                    break
        selected_list[int(ans_2) - 1] = str(y)
    elif ans_2 == '4':
        while True:
            try:
                new = int(input('Price: '))
                selected_list[int(ans_2) - 1] = str(new)
            except:
                print('Only Number!')
            if new < 1:
                print('minimum 1')
                continue
            else:
                break
    elif ans_2 == '5':
        new = input('Specification: ')
        selected_list[int(ans_2) - 1] = str(new)
    elif ans_2 == '6':
        while True:
            try:
                new = int(input('Amount: '))
                selected_list[int(ans_2) - 1] = str(new)
            except:
                print('Only Number!')
            if new < 1:
                print('minimum 1')
                continue
            else:
                break
    modify_list[int(ans) - 1] = selected_list #replace edited data with initial
    file.close()
    file = open('groceries detail.txt', 'w') #bring data from list back to txt
    for i in modify_list:
        for y in i:
            file.write(y + ' ')
        file.write('\n')
    file.close()
    while True:
        ask = input('1) Continue\n2) Back\n: ')
        if ask == '1':
            modify()
        elif ask == '2':
            admin_menu()


def view_specific_groceries():
    view_groceries_for_function()
    ask = input('Search an item(Specification): ').lower() #type item name
    file = open('groceries detail.txt', 'r') #bring data from txt to list
    print('Serial Code', '-' * 4, 'Name', '-' * 4, 'Expired date', '-' * 4, 'Price',
          '-' * 4, 'Specification', '-' * 4, 'Amount')
    x = True
    y = False
    for i in file.readlines():
        if i.split()[4] == ask:
            search = i.split()
            print(search[0], ' ' * 11, search[1], ' ' * (8 - len(search[1])),
                  search[2], ' ' * (16 - len(search[2])),
                  'RM', search[3], ' ' * (6 - len(search[3])),
                  search[4], ' ' * (17 - len(search[4])),
                  search[5])
            x = False
            y = True
        else:
            continue
    file.close()
    if x:
        print('Item Not found')
        while True:
            ask = input('1) Continue\n2) Back\n: ')
            if ask == '1':
                view_specific_groceries()
                break
            elif ask == '2':
                admin_menu()
                break
    elif y:
        while True:
            ask = input('1) Continue\n2) Back\n: ')
            if ask == '1':
                view_specific_groceries()
                break
            elif ask == '2':
                admin_menu()
                break



def view_all_customer_order():
    print('Name', ' ' * 11, 'Serial Code', ' ' * 12, 'name', ' ' * 9, 'Expired date', ' ' * 8, 'Price',
          ' ' * 11, 'Quantity')
    customer_name = []
    file = open('customer details.txt', 'r')
    for i in file.readlines():
        customer_name.append(i.split()[0])
    file.close()
    file = open('order list.txt', 'r')
    order = []
    for y in file.readlines():
        order.append(y.strip().split())
    for z in customer_name:
        for q in order:
            if z == q[0]:
                print(q[0], ' ' * (12 - len(q[0])),
                      q[1], ' ' * (23 - len(q[1])),
                      q[2], ' ' * (13 - len(q[2])),
                      q[3], ' ' * (20 - len(q[3])),
                      'RM' + q[4], ' ' * (14 - len(q[4])),
                      q[6], ' ' * (10 - len(q[6])), )
    file.close()
    while True:
        ask = input('1) Back\n: ')
        if ask == '1':
            admin_menu()


def search_customer_order():
    file = open('customer details.txt', 'r')
    name = []
    for y in file.readlines():
        name.append(y.strip().split()[0])
    count = 1
    for x in name:
        print(str(count) + ')' + x)
        count = count + 1
    while True:
        try:
            choose_customer = int(input('Select a customer: '))
            break
        except:
            print('Only Number!')
    file = open('order list.txt', 'r')
    order = []
    for y in file.readlines():
        order.append(y.strip().split())
    print('Name', ' ' * 11, 'Serial Code', ' ' * 12, 'name', ' ' * 9, 'Expired date', ' ' * 8, 'Price',
          ' ' * 11, 'Quantity')
    for q in order:
        if q[0] == name[choose_customer - 1]:
            print(q[0], ' ' * (12 - len(q[0])),
                  q[1], ' ' * (23 - len(q[1])),
                  q[2], ' ' * (13 - len(q[2])),
                  q[3], ' ' * (20 - len(q[3])),
                  'RM' + q[4], ' ' * (14 - len(q[4])),
                  q[6], ' ' * (10 - len(q[6])), )
    file.close()
    while True:
        ask = input('1) Continue\n2) Back\n: ')
        if ask == '1':
            search_customer_order()
        elif ask == '2':
            admin_menu()


def customer_login_page():
    print('-' * 4, 'Login', '-' * 4)
    file = open('customer details.txt', 'r')
    ID = []
    password = []
    name = []
    for i in file.readlines():
        ID.append(i.split()[6])
        password.append(i.split()[7])
        name.append(i.split()[0])
    file.close()
    ask_id = input('ID: ')
    ask_pass = input('Password: ')
    if ask_id in ID and ask_pass in password:
        print('login success')
        file = open('Current customer.txt', 'w')
        file.write(name[ID.index(ask_id)])  # find the name using index of id
        file.close()
        customer_menu_page()
    else:
        print('id or password incorrect')
        login_page()


def new_customer_page():
    while True:
        print('-' * 5, 'Guest Page', '-' * 5)
        question = ['View Groceries', 'Register Member', 'Exit']
        numbering = 1
        for i in question:
            print(str(numbering) + ') ' + i)
            numbering = numbering + 1
        answer = input('select your option: ')
        if answer == '1':
            view_groceries_for_function()
            while True:
                ask = input('1) Back\n: ')
                if ask == '1':
                    new_customer_page()
                    break
                else:
                    continue
            break
        elif answer == '2':
            print('registration')
            name = input('Name: ').upper()
            file = open('customer details.txt', 'r')
            customer_detail = file.readlines()
            detail_list = []
            id_list = []
            for i in customer_detail:
                detail_list.append(i.split())
                id_list.append(i.split()[6])
                if name == i.split()[0]:
                    print('User exist')
                    new_customer_page()
            file.close()
            new_customer = []
            address = input('Address :')
            email = input('Email: ')
            while True:
                try:
                    cont_numb = int(input('Phone Number: '))
                    break
                except:
                    print('Only Number!')
            while True:
                gender = input('Gender(female/male): ').lower()
                if gender == 'male':
                    break
                elif gender == 'female':
                    break
                else:
                    print('only female and male')
                    continue
            print('Birth date')
            import datetime
            x = True
            y = []
            while x:
                while True:
                    try:
                        year = int(input("Year: \n"))
                        month = int(input("Month: \n"))
                        day = int(input("Date: \n"))
                        y = datetime.date(year, month, day)
                    except:
                        print("Invalid Entry")
                        continue
                    if year < 1900:
                        print('error year')
                        continue
                    else:
                        x = False
                        break
            dob = y
            while True:
                ID = input('user ID:')
                if ID in id_list:
                    print('ID has been used')
                else:
                    break
            pw = input('password:')
            while True:
                pw2 = input('Rewrite password:')
                if pw2 != pw:
                    print('password not match')
                    continue
                else:
                    break
            new_customer.append(name.replace(' ', '_'))
            new_customer.append(address.replace(' ', '_'))
            new_customer.append(email)
            new_customer.append(str(cont_numb))
            new_customer.append(gender)
            new_customer.append(str(dob))
            new_customer.append(ID)
            new_customer.append(pw2)
            file = open('customer details.txt', 'a')
            for i in new_customer:
                file.write(i + ' ')
            file.write('\n')
            file.close()
            file = open('Current customer.txt', 'w')
            file.write(new_customer[0])
            file.close()
            customer_menu_page()
            break
        elif answer == '3':
            login_page()
            break
        else:
            print('number 1 to 3')


def customer_menu_page():
    file = open('Current customer.txt', 'r')
    customer_name = file.readline()
    print('-' * 4, 'Welcome', '', customer_name, '-' * 4)
    option = ['View Groceries', 'Place Order', 'Payment', 'View Order', 'Personal information', 'Exit']
    numbering = 1
    for i in option:
        print(str(numbering) + ') ' + i)
        numbering = numbering + 1
    answer = input('Select your choices: ')
    if answer == '1':
        view_groceries_for_function()
        while True:
            ask = input('1) Back\n: ')
            if ask == '1':
                customer_menu_page()
                break
            else:
                continue
    elif answer == '2':
        place_order()
    elif answer == '3':
        payment()
    elif answer == '4':
        view_own_order()
    elif answer == '5':
        view_personal_info()
    elif answer == '6':
        login_page()


def place_order():
    print('ORDER')
    file = open('Current customer.txt', 'r')
    customer_name = file.read()
    file.close()
    item_list = []
    count = 0
    file = open('groceries detail.txt', 'r')
    for i in file.readlines():
        item_list.append(i.strip().split())
        count = count + 1
    file.close()
    print('Name: ' + customer_name)
    view_groceries_for_function()
    while True:
        while True:
            try:
                ask = int(input('Choose your order: '))
                break
            except:
                print('Only Number!')
        if ask > count or ask < 1:
            print('Item not exist')
            continue
        else:
            break
    selected_list = item_list[ask - 1]
    while True:
        while True:
            try:
                quantity = int(input('How many: '))
                break
            except:
                print('Only Number!')
        if quantity > int(selected_list[5]) or quantity < 0:  # if is 0 make it return
            print('Error')
            continue
        elif quantity == 0:
            print('Error')
            place_order()
        else:
            break
    print('Order added')
    selected_list[5] = str(int(selected_list[5]) - quantity)  # left over item
    item_list[ask - 1] = selected_list
    file = open('groceries detail.txt', 'w')
    for i in item_list:
        for y in i:
            file.write(y + ' ')
        file.write('\n')
    file.close()

    selected_list[5] = str(quantity)  # selected how many item
    order_list = []
    file = open('order list.txt', 'r')
    for i in file.readlines():
        order_list.append(i.strip().split())
    file.close()
    x = 1
    y = 0
    if len(order_list) == 0:
        file = open('order list.txt', 'a')
        file.write(customer_name.strip() + ' ')
        for i in selected_list:
            file.write(i + ' ')
        file.write('\n')
        file.close()
    else:
        for i in order_list:
            if i[0] == customer_name.strip() and i[2] == selected_list[1]:
                i[6] = str(int(i[6]) + int(selected_list[5]))  # overlap quantity
                i[6] = str(i[6])
                x = 0
                y = 1
            else:
                continue
    if x == 1:
        file = open('order list.txt', 'a')
        file.write(customer_name.strip() + ' ')
        for i in selected_list:
            file.write(i + ' ')
        file.write('\n')
        file.close()
    if y == 1:
        file = open('order list.txt', 'w')
        print(order_list)
        print(selected_list)
        for i in order_list:
            for y in i:
                file.write(y + ' ')
            file.write('\n')
        file.close()
    while True:
        ask = input('1) Continue\n2) Back\n: ')
        if ask == '1':
            place_order()
        elif ask == '2':
            customer_menu_page()


def payment():
    print('-' * 4, 'Payment', '-' * 4)
    print('Serial Number', ' ' * 6, 'Name', ' ' * 6, 'price', ' ' * 8, 'Quantity')
    file = open('Current customer.txt', 'r')
    login_customer = file.read().strip()
    file.close()
    price = []
    all_order = []
    quantity = []
    count_list = []
    count = 0
    file = open('order list.txt', 'r')
    for i in file.readlines():
        all_order.append(i.strip().split())
        if i.split()[0] == login_customer:
            count_list.append(count)
            price.append(i.split()[4])
            quantity.append(i.split()[6])
            print(i.split()[1], ' ' * (19 - len(i.split()[1])),
                  i.split()[2], ' ' * (10 - len(i.split()[2])),
                  'RM', i.split()[4], ' ' * (16 - len(i.split()[6])),
                  i.split()[6], ' ' * (16 - len(i.split()[6])))
        count = count + 1
    print()
    total_price = 0
    count = 0
    for i in price:
        total_price = total_price + (int(quantity[count]) * int(i))
        count = count + 1
    print('total price: RM' + str(total_price))
    while True:
        ask = input('press 1 proceed to payment\n'
                    'press 2 to back\n'
                    ':')
        if ask == '1':
            print('please choose your payment type')
            option = ['Bank Transfer', 'TNG E-Wallet', 'Credit/debit card']
            numbering = 1
            for i in option:
                print(str(numbering) + ') ' + i)
                numbering = numbering + 1
            while True:
                while True:
                    try:
                        answer = int(input('Select your option: '))
                        break
                    except:
                        print('Only Number!')
                if answer < 1 or answer > len(option):
                    print('Error payment choice')
                else:
                    break
            if answer == 1:
                print('Bank Transfer')
                input('ID:')
                input('Password: ')
            elif answer == 2:
                print('TNG E-Wallet')
                input('ID:')
                input('Password: ')
            elif answer == 3:
                print('Credit/Debit Card')
                input('ID:')
                input('Password: ')
            while True:
                while True:
                    try:
                        amount_paying = int(input('Amount you want to pay: '))
                        break
                    except:
                        print('Only Number!')
                if amount_paying < total_price:
                    print('payment unsuccessful,not enough money')
                else:
                    print('here is your balance')
                    print('RM', amount_paying - total_price)
                    break
            updated_list = []
            for i in all_order:
                if i[0] != login_customer:
                    updated_list.append(i)
            print()
            print('Payment Success')
            new_order_list = []
            remove_list = []
            file = open('order list.txt', 'r')
            for i in file.readlines():
                new_order_list.append(i.split())
            for y in new_order_list:
                if y[0] == login_customer:
                    remove_list.append(y)
            for a in remove_list:
                new_order_list.remove(a)
            file.close()
            file = open('order list.txt', 'w')
            for i in new_order_list:
                for y in i:
                    file.write(y + ' ')
                file.write('\n')
            file.close()

            # need add write file
            customer_menu_page()

            break

        elif ask == '2':
            customer_menu_page()
            break


def view_own_order():
    file = open('Current customer.txt', 'r')
    customer_name = file.read().strip()
    file.close()
    print('NO ', 'Serial Code', ' ' * 4, 'Name', ' ' * 4, 'Expired Date', ' ' * 4, 'Price', ' ' * 7, 'Quantity')
    count = 1
    file = open('order list.txt', 'r')
    for i in file.readlines():
        if i.strip().split()[0] == customer_name:
            print(count, ')', i.split()[1], ' ' * (15 - len(i.split()[1])),
                  i.split()[2], ' ' * (8 - len(i.split()[2])),
                  i.split()[3], ' ' * (16 - len(i.split()[3])),
                  'RM', i.split()[4], ' ' * (9 - len(i.split()[4])),
                  i.split()[6], ' ' * (9 - len(i.split()[6])))
            count = count + 1
        else:
            continue
    while True:
        ask = input('press 1 to back \n: ')
        if ask == '1':
            customer_menu_page()
            break
        else:
            continue
    file.close()


def view_personal_info():
    file = open('Current customer.txt', 'r')
    customer_name = file.readline().strip()
    file.close()
    file = open('customer details.txt', 'r')
    print('Name', ' ' * 15, 'Address', ' ' * 21, 'Email', ' ' * 18, 'Phone Number', ' ' * 8, 'Gender', ' ' * 8, 'ID',
          ' ' * 8, 'password')
    for i in file.readlines():
        if i.strip().split()[0] == customer_name:
            print(i.split()[0], ' ' * (19 - len(i.split()[0])),
                  i.split()[1], ' ' * (28 - len(i.split()[1])),
                  i.split()[2], ' ' * (23 - len(i.split()[2])),
                  i.split()[3], ' ' * (20 - len(i.split()[3])),
                  i.split()[4], ' ' * (14 - len(i.split()[4])),
                  i.split()[6], ' ' * (10 - len(i.split()[6])),
                  i.split()[7])
        else:
            continue
    while True:
        ask = input('press 1 to back \n: ')
        if ask == '1':
            customer_menu_page()
            break
        else:
            continue
    file.close()

login_page()
