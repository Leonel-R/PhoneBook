# Write your solution here
phone_book = {}
while True:
    command = int(input("Command (1 search, 2 add, 3 quit):"))
    if command == 3:
        print("quitting...")
        break
    elif command == 2:
        name = input("Name:")
        number = input("Number:")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print("ok!")
    elif command == 1:
        name = input("Name:")
        if name not in phone_book:
            print("no number")
        else:
            for num in phone_book[name]:
                print(num)