'''
script: cis_131_time.py
action: Runs the script with the time class that utilizes read and write
        properties and string representation.
author: Dylan McCallum
date: 05OCT24
'''

class Time: 
    """Class Time with read-write properties."""
    
    def __init__(self, hour, minute, seconds):
        """Initialize each attribute"""
        
        # converts the input received into seconds
        self._total_secs = (hour * 3600 + minute * 60 + seconds)
    
    def __repr__(self):
        '''Return Time string for repr()'''
        return (f'Time({self.hour:02d}:{self.minute:02d}:{self.second:02d})')
        
    def __str__(self):
        '''Print Time in 12-hour format.'''
        
        return (('12' if self.hour in (0,12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                ('AM' if self.hour < 12 else ' PM') +
                f' or {self._total_secs} seconds after midnight')
    
    @property
    def hour(self):
        '''Return the hour after conversion'''
        
        return self._total_secs // 3600
    
    @property
    def minute(self):
        '''Return the minute after conversion'''
        return (self._total_secs % 3600) // 60

    @property
    def second(self):
        '''Return the second'''
        return self._total_secs % 60
    
    @property
    def total_seconds(self):
        '''returns the total seconds after midnight'''
        return self._total_secs
    
    @total_seconds.setter
    def total_seconds(self, input_secs):
        '''Sets the total seconds'''
        self._total_secs = input_secs
    

def main():
    '''
    Runs the entire application by receiving the user's time inputs by hour,
    minute, and second, or total seconds after midnight.
    
    action: Contains the assigned classes and runs the script
    input: None
    
    output: Displays the time by entering the hour, minute, seconds, or
            by calling the attribute total_seconds and entering the time 
            in seconds after midnight to display the time
            
    return: None
    '''
    
    # Assign a class to a new variable
    wake_up = Time(hour=23, minute=10, seconds=34)
    
    # display the converted time
    print(wake_up)
    
    # displays the converted time with total seconds
    wake_up.total_seconds = 5000
    print(wake_up)

# invokes main
main()