from numpy import kaiser
from contact_class import Contact

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs) -> None:
        super().__init__(**kwargs)        
        self.phone = phone

# f1 = Friend("somebody", "sombody@gmail.com", "0931345973")
# print(f1.name, f1.email, f1.phone)

class MailSender:
    def send_mail(self, message):
        print("Sending mail to {}. Message: {}".format(self.email, message))

class EmailableContact(Contact, MailSender):
    pass

