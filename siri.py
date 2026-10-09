
class PARENT:
    Asset1 = "3BHK house"
    Asset2 = "Audi car"

    def parentMtd(self):
        print("This is the method from parent class")
        print("Asset1:", self.Asset1)
        print("Asset2:", self.Asset2)

class Child(PARENT):
    def electricityBill(self):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        consumer_no = input("Enter consumer number: ")
        units = float(input("Enter electricity units consumed: "))

        if (units < 0):
            print("Units cannot be negative.")
            return
        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = 100 * 2 + (units - 100)
        elif units <= 300:
            bill = 100 * 2 + 100 * 3 + (units - 200) 
        else:
            bill = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300)

        print("----- ELECTRICITY BILL -----")
        print("Customer Name:", name)
        print("Customer Email:", email)
        print("Consumer Number:", consumer_no)
        print("Units Consumed:", units)
        print("Total Bill Amount: ", bill)

obj = Child()
obj.parentMtd ()
obj.electricityBill()
