# -*- coding: utf-8 -*-
from random import randrange
import random


class Drums():
    def __init__(self):
        self.drumBeat = self.percussion()
        
        
    def percussion(self):
     
        drumbeat = ['x', '-', 'o', 'r', 't', 'y', 'u', 'i', 'p', 'a', 'd', 'f', 'h', 'k', 'l',
                    'v', 'n', 'm', '=', '+', '#', '$', '%', '^', '&', '*']
        electrodrums = ['q', 'w', 'e', 'g', 'j', 'z', 'b']
        expressions = ['1', '2', '3', '4', '?', '!']
    
        drums = ""
        
        for i in range(4):
            drums += random.choice(drumbeat)
            
        return drums

drum = Drums()
print(drum.drumBeat)