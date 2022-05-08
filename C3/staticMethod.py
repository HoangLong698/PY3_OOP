class Calculator:
    
    def add_numbers(num1, num2):
        return num1 + num2


# Convert add_numbers() to static method
Calculator.add_numbers = staticmethod(Calculator.add_numbers)

sum = Calculator.add_numbers(1, 2)
print("output of sum: {}".format(sum))

class Mathematics:

    def addNumbers(x, y):
        return x + y
    
# Create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('The sum is: {}'.format(Mathematics.addNumbers(1, 2)))

class Dates:
    def __init__(self, date) -> None:
        self.date = date

    def getDate(self):
        return self.date
    
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2022")
dateFromDB = "15/12/2022"
datewithDash = Dates.toDashDate(dateFromDB)

if (date.getDate() == datewithDash):
    print("Equal")
else:
    print("Unequal")


class Dates:
    def __init__(self, date) -> None:
        self.date = date
    
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithDash(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2022")
dateFromDB = DatesWithDash("15/12/2022")

print(date.getDate())

class BaseClass:

    def addNumbers( x, y):
        return x + y

BaseClass.addNumbers = staticmethod(BaseClass.addNumbers)

print("{} + {} = {}".format(1, 2, BaseClass.addNumbers(1, 2)))