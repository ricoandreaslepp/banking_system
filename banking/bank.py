class bankAccount:
    
    def __init__(self, name, password):
        self.balance = 0
        self.name = name
        self.password = password
    
    def deposit(self, amount):
        self.balance += amount
        print(str(amount) + "€ deposited")
        
    def withdraw(self):
        return None
        
    def display(self):
        print("current balance: " + str(self.balance) + "€")

def welcomeScreen():
    choice = input("do you have an account (y/n): ")
    file = open("data.txt", "r")
    usernames, passwords = 

    if choice.strip() == "y":
        
        while True:
            usr = input("username: ")
            pwd = input("password: ")

            if usr in usernames:
                choiceScreen() # kas jääb taustal mängima??
            else:
                print("wrong username or password")
                print("try again")

    elif choice.strip() == "n":
        return None
    else:
        return None
        
    return None

def choiceScreen():
    flag = False
    choices = ["withdraw", "deposit", "display"]
    
    while not flag:
        ans = input("what would you like to do: ")
        
        if ans in choices:   
            flag = True
        else:
            print("wrong input")
            print("try again")
    
    return None
    
def run():
    welcomeScreen()
    
run()
