"""
- A class will wrap our methods and properties
- properties are variables of that object.
- Example:
            Methods are like a fuel calculator where fuel status is a properties.
"""


class CarClass:
    year = 2000
    print(year)

audi_a3 = CarClass() #This is an instance of the above object



####################################
class Employee:
    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance

    def show_Employee_details(self):
        print("Name: ", self.name, "Salary: ", self.salary)

Sara = Employee("Sara", 3000, True)
Sara.show_Employee_details()    #method is always called out by using instance name (Sara) following by a dot(.)


#############################

class buildings:

    def __init__(self,season_in_year, apartment_number, apartment_size):
        self.season_in_year = season_in_year
        self.apartment_number = int(apartment_number)
        self.apartment_size = int(apartment_size)

    def rent_calculator(self):
        base_price_per_month = 2000
        season_price_buffer = 0
        if self.season_in_year == "summer":
            season_price_buffer = 1.5
        elif self.season_in_year == "winter":
            season_price_buffer = 1.1
        elif self.season_in_year == "spring":
            season_price_buffer = 1.6
        else:
            season_price_buffer = 1.3

        if self.apartment_size > 130:
            season_price_buffer += 0.1
        print("Bufer is : " +str(season_price_buffer))
        total_rent = base_price_per_month * season_price_buffer
        # print("Total rent in the " +self.season_in_year +" is : " +str(total_rent))
        print("Total rent for %s apartment number %s. Apartment's size is : %s meters" %(total_rent,self.apartment_number, self.apartment_size))
        return total_rent


    def monthly_maintenance_pay(self,total_rent):
        manitenance = 0
        if total_rent > 2500:
            manitenance = 100
        else:
            manitenance = 50
        print("Maintenance is %s" %(str(manitenance)))



lease_contract_1 = buildings("summer", "4", "135")
total_rent = lease_contract_1.rent_calculator()

lease_contract_1.monthly_maintenance_pay(total_rent)

print("\n")

lease_contract_2 = buildings("winter", "5", "135")
total_rent = lease_contract_2.rent_calculator()

lease_contract_2.monthly_maintenance_pay(total_rent)





#######################################################
class Car():

    def __init__ (self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_price(self):

        year_of_release = self.car_data_list[0]
        car_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if 2010 <= year_of_release <= 2020 and 6000 <= car_price <= 17000:
            calculated_insurance = car_price * 0.05

        else:
            calculated_insurance = car_price * 0.07


        print("The insurance price for %s is : %s" % (model, calculated_insurance))


    def doors_closed(self):

        doors_status = self.car_data_list[-1]
        if doors_status:
            print("Doors are closed")

        elif doors_status == False:
            print("Doors are open")

        else:
            print("Wrong value inserted")


    def get_car_data(self):
        print("The car model is : %s, it was released at the year %s, and it costs : %s" %(self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))

# List of 'Ford'
ford_focus_list = [2005, 5000, "ford_focus", True]

# Instance of an object - 'Ford'
ford_focus = Car(ford_focus_list)

# Methods execution upon 'ford_focus' instance of an object
ford_focus.get_car_data()
ford_focus.insurance_price()
ford_focus.doors_closed()


print("\n")


# List of 'Audi'
audi_a3_list = [2011, 15000, "audi_a3", False]

# Instance of an object - Audi
audi_a3 = Car(audi_a3_list)

# Methods execution upon 'audi_a3' instance of an object
audi_a3.get_car_data()
audi_a3.insurance_price()
audi_a3.doors_closed()