'''
script: time_internal.py
action: time review
author: Dylan McCallum  
date: 15OCT24
'''

class Time (object):
    '''Class time with read-write properties'''
    
    def __init__(self, hour, minute, seconds):
        '''Initialize each attribute'''
        
        self._total_secs = (hour * 3600 + minute * 60 + seconds)
    
    def set_time(self, in_hour, in_minute, in_second):
        self._total_secs = (in_hour * 3600 + in_minute * 60 + in_second)
    
    @property
    def hour(self):
        '''Return hour after conversion'''
        
        return self._total_secs // 3600
    
    @property
    def minute(self):
        '''Return the minute after conversion'''
        return (self._total_secs % 3600) // 60
    
    @property
    def second(self):
        '''return second'''
        return self._total_secs % 60
    
    @property
    def total_seconds(self):
        '''returns the seconds after midnight'''
        return self._total_secs
    
    @hour.setter
    def hour(self, in_hour):
        self._total_secs = (in_hour * 3600) + (self.minute * 60) + self.second
       # set_time(in_hour, self.minute, self.second)
    
    @minute.setter
    def minute(self, in_minute):
        self._total_secs = (self.hour * 3600) + (in_minute * 60) + self.second
    
    @second.setter
    def second(self, in_second):
        self._total_secs = (self.hour * 3600) + (self.minute * 60) + in_second
    
    

        


