'''
script: class_abstract_notes.py
action: abstract classes
author: Dylan McCallum  
date: 17OCT24
'''

from abc import ABC, abstractmethod

class Phone(ABC):
    
    def __init__(self, model):
        self.model = model
    
    #method
    
    @property
    @abstractmethod
    def power(self):
        pass
    
    @abstractmethod
    def call_target(self, name):
        pass

class iBanana (Phone):
    
    def __init__(self, model):
        super().__init__(model)
    
    def getModel (self):
        return self.model
    
    @property
    def power(self):
        return ("Battery low, 5%")

    def call_target(self, name):
        raise NotImplementedError('code missing')
    
    

myBanana = iBanana('Sugar')

try:
    myBanana.call_target("GhostBusters")
except Exception as e:
    print(e)
    
print(myBanana.power)

# myPhone = Phone('iPhone 15')
# print(myPhone.model)
# myPhone.call_target('GhostBusters')