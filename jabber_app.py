"""Nelson Booth
Assignment 10.1: Your Own Class
Description: This program will implement a real-world object of a money-sharing app 
called Jabber that can deposit, withdraw, send, and receive to online money using OOP.
"""

import random # imports the random module

class Jabber: # creates the class called 'Jabber'

    start_message = print(f"\nWelcome to Jabber! Your #1 Money-Sharing App!\n") # class variable; stores and prints a welcome message introducing the app to the user

    def __init__(self, name, birthday, address, phone, *friends): # __init__ takes in name, birthday, address, phone, and list of friends entered by the user
        self.__name = name # private data variable storing name
        self.__birthday = birthday # private data variable storing birthday
        self.__address = address # private data variable storing address
        self.__phone = phone # private data variable storing phone
        self.__friends = friends # private data variable storing the list of friends
        self.__one_friend = random.choice(friends) # private data variable storing a randomly chosen friend from the list of friends
        self.__another_friend = random.choice(friends) # private data variable storing another randomly chosen friend from the list of friends
        self.__account_num = random.randint(100000, 999999) # private data variable storing a random integer between 100,000 and 999,999
        self.__initial_deposit = f"${0:.2f}" # private data variable that initializes zero dollars in dollar format
        self.__initial_depositv2 = 0 # private data variable initializes the number zero

    def set_funds(self, deposit): # method sets the amount of money or funds to be deposited into the user's balance
        if deposit <= 0: # if deposit is less than or equal to zero
            print(f"\nDeposits cannot be less than or equal to zero dollars.\n") # prints an error message stating that deposits cannot be less than or equal to zero
        else: # if deposit is greater than zero
            self.__initial_deposit = f"${deposit:.2f}" # stores the deposit in dollar format
            self.__initial_depositv2 = deposit # stores and updates the data variable with deposit amount
    
    def set_friend_funds(self, amount, friend, message): # method sets the amount of funds being sent to a friend tagged with a message
        if amount > self.__initial_depositv2: # if the amount of funds is greater than the user's balance
            print(f"Insufficient funds to send to {friend}.") # prints error message stating that there are not enough funds to be sent to the friend
        else: # if the amount is less than the user's balance
            print(f"\nSent ${amount:.2f} to {friend} with this message:\n\
                {message}") # prints message stating the successful transaction displaying the amount of money being sent as well as the friend and the message tagged with it
            self.__initial_depositv2 = amount - self.__initial_depositv2 # subtracts the amount from the user's balance and storing the difference
            self.__initial_depositv2 = abs(self.__initial_depositv2) # stores the absolute value of the difference
            self.__initial_deposit = f"${self.__initial_depositv2:.2f}" # stores and updates the user's balance in dollar format based on the difference

    def withdraw_funds(self, withdraw): # method allows the user to withdraw money from their balance
        if withdraw >= self.__initial_depositv2: # if the withdraw amount is greater than or equal to the user's balance
            print(f"\n${withdraw:.2f} is an insufficient balance for withdraw from {self.__initial_deposit}.\n") # prints error message stating insufficient balance to withdraw from
        else: # if the withdraw amount is less than the user's balance
            self.__initial_depositv2 = withdraw - self.__initial_depositv2 # subtracts the withdraw amount from the user's balance and stores the difference
            self.__initial_depositv2 = abs(self.__initial_depositv2) # stores the absolute value of the difference
            self.__initial_deposit = f"${self.__initial_depositv2:.2f}" # stores and updates the user's balance in dollar format based on the difference
    
    def get_balance(self): # method gets the user's balance
        return print(f"\nYour balance is {self.__initial_deposit}\n") # return prints a message displaying the user's balance
    
    def receive_friend_funds(self, response): # method allows the user to receive money from another friend and decide if they want to add the amount to their balance
        self.__other_account_num = random.randint(100000, 999999) # private data variable stores a randomly selected integer between 100,000 and 999,999
        self.__amount_sent = random.randint(0, 500) # private data variable stores a randomly selected integer between 0 and 500
        print(f"\n{self.__one_friend} from Account #{self.__other_account_num} is sending ${self.__amount_sent:.2f} to you.\n") # prints the friend and their account number who is sending what amount of money to the user
        if response in ['no', 'No']: # if the response if either 'no' or 'No'
            print(f"\nThe amount will be sent back to {self.__one_friend}.\n") # prints a message stating that the money will be sent back to the friend
        elif response in ['yes', 'Yes']: # if the response is 'yes' or 'Yes'
            self.__initial_depositv2 = self.__amount_sent + self.__initial_depositv2 # adds the sent amount to the user's balance and stores the sum
            self.__initial_deposit = f"${self.__initial_depositv2:.2f}" # stores and updates the user's balance in dollar format based on the sum
        else: # if response is another string besides 'no' or 'yes'
            print(f"\nCannot understand response. Please enter 'yes' or 'no'.\n") # prints an error message
    
    def receive_friend_fundsv2(self, response): # method allows the user to receive money from another friend and decide if they want to add the amount to their balance
        self.__other_account_numv2 = random.randint(100000, 999999) # private data variable stores a randomly selected integer between 100,000 and 999,999
        self.__amount_sentv2 = random.randint(0, 500) # private data variable stores a randomly selected integer between 0 and 500
        print(f"\n{self.__another_friend} from Account #{self.__other_account_numv2} is sending ${self.__amount_sentv2:.2f} to you.\n") # prints the friend and their account number who is sending what amount of money to the user
        if response in ['no', 'No']: # if the response if either 'no' or 'No'
            print(f"\nThe amount will be sent back to {self.__another_friend}.\n") # prints a message stating that the money will be sent back to the friend
        elif response in ['yes', 'Yes']: # if the response is 'yes' or 'Yes'
            self.__initial_depositv2 = self.__amount_sentv2 + self.__initial_depositv2 # adds the sent amount to the user's balance and stores the sum
            self.__initial_deposit = f"${self.__initial_depositv2:.2f}" # stores and updates the user's balance in dollar format based on the sum
        else: # if response is another string besides 'no' or 'yes'
            print(f"\nCannot understand response. Please enter 'yes' or 'no'.\n") # prints an error message

    def get_profile(self): # method gets the profile of the user info based on what the user entered
        return print(f"\tFull Name: {self.__name}\n\tBirthday: {self.__birthday}\n\tAddress: {self.__address}\n\tPhone Number: {self.__phone}\n\tFriends List: {self.__friends}\n\tAccount Number: #{self.__account_num}\n\tBalance: {self.__initial_deposit}")
        # return prints a long formatted string that is tabbed and newlined to display each individual section of info of the user

def main(): # main function allows the calling of the class
    x = Jabber('Nelson Booth', '04-21-2003', '231 Oakes Rd', '415-985-5494', 'Devesh', 'Sarvesh', 'Austin') # stores the calling of the class with the input arguments entered by the user
    x.start_message # prints the class variable(welcome message)
    x.get_profile() # calls the method to display the user's profile
    x.set_funds(300) # calls the method that allows to user to makes their first deposit
    x.get_balance() # calls the method for the user to see their balance
    x.set_friend_funds(100, 'Devesh', 'Merry Christmas and Happy Holidays!') # calls the method for the user to send another friend money with the input arguments entered by the user
    x.get_balance() # calls the method for the user to see their balance
    x.withdraw_funds(267) # calls the method allowing the user to withdraw from their balance
    x.get_balance() # calls the method for the user to see their balance
    x.withdraw_funds(167) # calls the method allowing the user to withdraw from their balance
    x.get_balance() # calls the method allowing the user to withdraw from their balance
    x.receive_friend_fundsv2('yes') # calls the method allowing the user to agree to receiving money from a friend
    x.get_balance() # calls the method allowing the user to withdraw from their balance
    x.receive_friend_funds('no') # calls the method allowing the user to disagree to receiving money from a friend
    x.get_balance() # calls the method allowing the user to withdraw from their balance
    x.get_profile() # calls the method to display the user's profile

if __name__ == "__main__": # allows the main function to call the class and its variables and methods
    main()