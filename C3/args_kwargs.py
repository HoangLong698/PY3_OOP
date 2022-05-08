def adder(x, y, z):
    print("sum : {}".format(x+y+z))

adder(1,2,3)

# Error because we pass 4 arg instead of 3
# adder(1,2,3,4)

# We use *args and **kwargs as an argument when we are unsure about the member of arguments to pass in the functions
def adder_args(*num):
    sum = 0
    for n in num:
        sum += n
    print("Sum : {}".format(sum))

adder_args(1,2,)
adder_args(1,2,3)
adder_args(1,2,3,4)

def intro(**data):
    print("\nData type of argument: {}".format(type(data)))

    for key, value in data.items():
        print("{}: {}".format(key, value))

intro(firstname="Long", lastname="Tran", age=22, phone=1234)
intro(firstname="Long", lastname="Nguyen", age=21, phone=4444)


# Things to Remember:
# *args and **kwargs are special keyword which allows function to take variable length argument.
# *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# *args and **kwargs make the function flexible.