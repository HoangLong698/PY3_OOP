# import ecommerce.products
# product = ecommerce.products.Product()

# from ecommerce.products import Product
# product = Product()

# from ecommerce import products
# product = products.Product()

from ecommerce import database


database.initilize_database()
print(database.database_obj)


class UsefulClass:
    '''This class might be useful to other modules.'''
    pass


def main():
    '''Creates a useful class and does something with it four our module.'''
    useful = UsefulClass()
    print(useful)

if __name__ == "__main__":
    main()
