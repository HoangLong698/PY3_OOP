import random
import sys
import time
some_exceptions = [ValueError, TypeError, IndexError, None]
# baseException = BaseException()
# print(baseException.__class__.__hash__)

def finally_except():
    try:
        # print("Hello Exception")
        choice = random.choice(some_exceptions)
        print("Raising {}".format(choice))
        if choice:
            raise choice("An error")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as error:
        print("Caught some other error: {}".format(error.__class__.__name__))
        # sys.exit()
    except KeyboardInterrupt:
        print("Program stop naturally. Because we use Ctrl + C")
    else:
        print("This code called if there is no exceptions")
    finally:
        print("This cleanup code is always called")

# finally_except()
num = 0
while True:
    try:
        time.sleep(1)
        finally_except()
    except KeyboardInterrupt:
        print("we use ctrl + c")
        num += 1
        print(num)
    if num == 10:
        sys.exit()
    # time.sleep(1)