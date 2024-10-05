'''
script: cis_131_accounts.py
action: This script displays the Account class characteristics
author: Dylan McCallum
date: 04OCT24
'''

# import required modules
from decimal import Decimal

class Account:
    '''Account Class'''
    
    # method called when we instantiate an object
    def __init__(self, name, balance):      
        '''Initialize an Account Object'''
        
        self._name = name
        self._balance = balance     # denotes a private variable in python
        
    def deposit(self, amount):
        '''Deposit Money'''
        
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self._balance += amount     # returns the updated amount
    
    @property
    def get_balance(self):       
        # Utilize the method to return the private variable _balance
        return self._balance
    
    @property
    def get_name(self):
        # Utilize the method to return the private variable _name
        return self._name

def main():
    '''Assigns an account to an individual and utilizes methods to 
       retrieve information
    '''
    
    print ("Looking at Account \n")
    
    # assigns an account to an individual
    
    account1 = Account('John Green', Decimal('50.00'))
    
    # method used to deposit money
    account1.deposit(12)
    
    # methods utilized to get the name and current balance
    print("The account of", account1.get_name, "is:", account1.get_balance)  

main()