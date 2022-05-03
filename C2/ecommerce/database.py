class Database:
    # The database implementation
    pass

database_obj = None

def initilize_database():
    global database_obj
    print("Initilze Database!!!")
    database_obj = Database()