from lib2to3.pytree import Base


class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1

class LeftSubClass(BaseClass):
    num_left_calls = 0 
    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("Calling method on Left Subclass")
        self.num_left_calls += 1

class RightSubClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1

class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0
    def call_me(self):
        # LeftSubClass.call_me(self)
        # RightSubClass.call_me(self)
        super().call_me()
        print("Calling method on subclass")
        self.num_sub_calls += 1