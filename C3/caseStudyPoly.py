class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        # super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_beds = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("badrooms: {}".format(self.num_beds))
        print("bathrooms: {}".format(self.num_baths))
        print()
    
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    
    prompt_init = staticmethod(prompt_init)

def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs) -> None:
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
    
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        parent_init = Property.prompt_init()

        laundry = get_valid_input("What laundry facilities does this property have? ({})".format(", ".join(Apartment.valid_laundries)))
        
        balcony = get_valid_input("Does the property have a balcony? ({})".format(", ".join(Apartment.valid_balconies)))
        
        parent_init.update({"laundry": laundry, "balcony": balcony})

        return parent_init

    def get_valid_input(input_string, valid_options):
        input_string += " ({}) ".format(", ".join(valid_options))
        response = input(input_string)
        while response.lower() not in valid_options:
            response = input(input_string)
        return response
        
    prompt_init = staticmethod(prompt_init)

class House(Property):
    valid_gargae = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', gargae='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.gargage = gargae
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("gargae: {}".format(self.gargage))
        print("fenced yard: {}".format(self.fenced))
        print()

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        gargage = get_valid_input("Is there a gargae? ", House.valid_gargae)

        num_stories = input("How many stories? ")

        parent_init.update({"fenced": fenced, "garage": gargage, "num_stories": num_stories})

        return parent_init
        
    prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self, price="", taxes="", **kwargs) -> None:
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("Selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(price=input("What is the selling price? "), taxes= input("What are the estimated taxes?" ))
    
    prompt_init = staticmethod(prompt_init)

class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        
    def prompt_init():
        return dict(rent=input("What is the monthly rent? "), utilities=input("What are the estimated utilities? "), 
                    furnished=get_valid_input("Is the property furnished?", ("yes", "no")))
    
    prompt_init = staticmethod(prompt_init)

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)

class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentRental(Rental, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)

class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []
    
    def display_properties(self):
        for property in self.property_list:
            property.display()
    
    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]

        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))

# init = HouseRental.prompt_init()

# house = HouseRental(**init)
# house.display()

agent = Agent()
agent.add_property()

agent.display_properties()