class Library:
    __instance = None
    
    def __new__(cls, *args,**kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise Exception("Library have only instance")
        
    def __init__(self, lib_name = "Open Source LIbrary"):
        self.lib_name = lib_name
        self.books_amount = 459
        self.books = {}

    def __str__(self):
        return self.lib_name




