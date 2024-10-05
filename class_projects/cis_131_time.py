'''
script: cis_131_time.py
action: Runs the script with the time class that utilizes read and write
        properties and string representation.
author: Dylan McCallum
date: 05OCT24
'''

class Time: 
    """Class Time with read-write properties."""
    
    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute"""
        
        self._hour = hour       # 0-23
        self._minute = minute   # 0-59
        self._second = second   # 0-59
    
    def __repr__(self):
        '''Return Time string for repr()'''
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')
        
    def __str__(self):
        '''Print Time in 12-hour format.'''
        
        return (('12' if self._hour in (0,12) else str(self._hour % 12)) +
                f':{self.minute:0>2}:{self._second:0>2}' +
                ('AM' if self._hour < 12 else ' PM'))
    
    @property
    def hour(self):
        '''Return the hour'''
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        '''Set the hour'''
        
        if not (0 <= hour < 24):
            raise ValueError(f'Hour({hour}) must be 0-23')
        
        self._hour = hour 
    
    @property
    def minute(self):
        '''Return the minute'''
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        '''Set the minute.'''
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        
        self._minute = minute
    
    @property
    def second(self):
        '''Return the second'''
        return self._second
    
    @second.setter
    def second(self, second):
        '''Set the record'''
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        
        self._second = second
    
    def set_time(self, hour=0, minute=0, second=0):
        '''Set values of hour, minute, and second'''
        
        self._hour = hour
        self._minute = minute
        self._second = second
    
    
        

def main():
    
    wake_up = Time(hour=7, minute=45, second=30)
    
    print(wake_up)
    
    wake_up.hour = 23
    wake_up.minute = 10
    wake_up.second = 34
    
    print(wake_up)

main()