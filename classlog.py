from prettytable import PrettyTable

l=[]
class abc:

    def __init__(self):
        self.table = PrettyTable()
        
    def show(self):        
        self.table.field_names = ["email", "password"]
        for i in l:
            self.table.add_row([i["email"], i["password"]])
        print(self.table)
        
    def signup(self):
        print("Create a new account.")
        email = input("Enter the email: ")
        
        if not email.endswith("@gmail.com"):
            print("Invalid pattern")   
                              
            return self.signup()
        password = input("Enter the password: ")
        
        for user in l:
            if user["email"] == email:
                print("Account already exists. You need to sign in.")
        a = {"email": email, "password":  password}
        l.append(a)
        # print(l)
        print("Account created successfully.")
        
    def signin(self):   
        email = input("Enter the email: ")
        password = input("Enter the password: ")
        
        for user in l:
            if user["email"]==email and user["password"]==password:
                print("Signed in successfully")
        print("Invalid details")


            
            
