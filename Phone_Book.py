class Person:
    def __init__(self, name):
        self.__name = name
        self.__number = []
        self.__address = None
    
    def __iter__(self) -> "Person":
        self.n = 0
        return self
    
    def __next__(self) -> str:
        if self.n < len(self.__number):
            number = self.__number[self.n]
            self.n += 1
            return number
        else:
            raise StopIteration
    
    def name(self) -> str :
        return self.__name
    
    def numbers(self) -> str:
        return self.__number
    
    def address(self) -> str:
        return self.__address
    
    def add_number(self,number: str):
        self.__number.append(number)

    def add_address(self, address: str):
        self.__address = address 
    
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str) -> "Person":
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self) -> dict:
        return self.__persons


class FileHandler():
    def __init__(self, filename):
        self.__filename = filename
    
    def save_file(self, info: dict):
        with open(self.__filename, "w") as file:
            file.write(f"{'Phone Book':*^40}\n")
            file.write(f"{'Names'}{'Number(s)':^28}{'Address'}\n")
            for name, person in info.items():
                line = f"{name} {', '.join(person.numbers()):^28} {person.address()}\n"
                file.write(line)


class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phone-book.txt")

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)
    
    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person == None:
            print("number unknown")
            print("address unknown")
            return
        elif person.numbers() == []:
            print("number unknown")
        else:
            for number in person:
                print(number) 
        if person.address() is not None:
            print(person.address())  
        else:
            print("address unknown")
        
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.__filehandler.save_file(self.__phonebook.all_entries())
                print("File Created...Exiting")
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()