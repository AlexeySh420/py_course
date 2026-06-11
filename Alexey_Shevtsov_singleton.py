class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("The class is a singelton")

if __name__ == "__main__":
    singleton_obj = Singleton()
    print(singleton_obj)
    #print(Singleton()) That call will raise an error



class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __repr__(self):
        return f"Connection to db {self.database_name}"
