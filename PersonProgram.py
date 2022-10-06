import PersonClass as pc

def main():
    name = "John"
    address = "123 main st"
    telephone = "123-456"
    number = 1234
    on_list = False


    person1  = pc.Person(name,address,telephone)
    customer1 = pc.Customer(name, address, telephone, number, on_list)

    person1.print_person()
    print()
    customer1.print_person()


main()
