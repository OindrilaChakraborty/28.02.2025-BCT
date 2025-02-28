from classlog import abc
cc=abc()

def main():
    while True:  
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        print("4.Show data")
        
        c = input("Enter your choice: ")
        
        if c == "1":
            cc.signup()
        elif c == "2":
            cc.signin()
        elif c == "4":
            cc.show()
        elif c == "3":
            print("Exit")
            break
        else:
            print("Invalid choice.")
        
            
main()