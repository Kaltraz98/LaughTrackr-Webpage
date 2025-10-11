class User:
    # this is the function used to create the user
    def __init__(self):
        self.user_type = 'patron'
        self.username = None
        self.password = None
        self.email = None

    def register(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        str = f"Name: {self.username}, Email: {self.email}, User type: {self.user_type}"
        return str

class FrequentPatron(User):

    def __init__(self):
        self.user_type = 'Frequent Patron'
        self.patronID = None

    def register(self, username, passwd, emailID, patronID):
        super().register(username ,passwd, emailID)
        self.patronID = patronID
    
    def __repr__(self):
        str = super().__repr__()
        str = str + f" Patron ID: {self.patronID}"
        return str