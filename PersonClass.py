class Person:
    def __init__(self,name,address,telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

    def print_person(self):
        print("The name is", self.__name)
        print("The address is", self.__address)
        print("The telephone number is", self.__telephone)

class Customer(Person):
    def __init__(self,name,address,telephone,number,on_list):
        Person.__init__(self,name,address,telephone)

        self.__number = number
        self.__on_list = on_list

    #def get_number(self):
        #return self.__number

    #def get_on_list(self):
        #return self.__on_list

    def print_person(self):
        print("The name is", Person.get_name(self))
        print("The address is", Person.get_address(self))
        print("The telephone number is", Person.get_telephone(self))
        print("The customer number is", self.__number)
        
        if self.__on_list:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")
        

    
