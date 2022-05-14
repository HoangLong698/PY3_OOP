from multiprocessing.sharedctypes import Value
from shutil import ExecError


class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line never executed")
    return "I won't be returned"

def call_exceptor():
    print("Call_exceptor starts here...")
    no_return()
    print("An exception was raised...")
    print("...so these lines don't run")

def funny_division(num):
    try:
        if num == 13:
            raise ValueError("13 is an unlucky number.")
        return 100 / num
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"
    except ValueError as e:
        print("No no not 13!!!\nError: {}".format(e))
        return None

# call_exceptor()
# no_return()
# try:
#     no_return()
# except:
#     print("I caught an exception")
# print("excuted after the exception")

for val in (0, 'hello', 12, 13):
    print("Testing val: {} ".format(val), end="")
    print(funny_division(val))
# print(funny_division(0))