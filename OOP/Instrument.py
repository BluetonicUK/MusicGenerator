# -*- coding: utf-8 -*-
from random import *
import random
from FoxDot import *
#from utility import *


class Instrument:
    def __init__(self):
        self.typeOf = self.randomInstrument()
        self.notes = self.randomNoteSeq()
        self.beats = self.noteBeats(self.notes)
        self.volume = self.randomVolume()
        self.pan = self.randomPan()
        self.sustain = self.randomSustain()
        # self.duration
        # self.startTime
        # self.stopTime
        # self.isSolo
        
    def randomInstrument(self):
        instrumentList = ['loop', 'stretch', 'audioin', 'noise', 'dab', 
                      'varsaw', 'lazer', 'growl', 'bass', 'dirt', 'crunch', 'rave', 'scatter',
                      'charm', 'bell', 'gong', 'soprano', 'dub', 'viola', 'scratch', 'klank',
                      'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip', 'ripple', 'creep', 
                      'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick', 'twang',
                      'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star',
                      'jbass', 'sawbass', 'prophet', 'pasha', 'ambi', 'space', 'keys', 
                      'dbass', 'sinepad']
        return random.choice(instrumentList)
    

    
    def randomVolume(self):
        volume = randint(10, 30)
        volume /= 10
        return volume
    
    def randomNoteSeq(self):
        notes = [0,8, 2,10, 4,12, 5,13, 7,15] #[0,1,2,3,4,5,6,7]
        notes_in_sequence = []
        for i in range(randrange(4, 9)):
            notes_in_sequence.append(random.choice(notes))
        
        return notes_in_sequence
    

    def noteBeats(self, noteSequence):         
        beats_per_note = []
        while len(beats_per_note) != len(noteSequence):       
            beats_per_note = []
            
            #get correct beats for sequence lengths divisible by 4 
            if len(noteSequence) % 2 == 0:                         
                for i in range(len(noteSequence)):
                    if i == 0:
                        beats_per_note.append(4)                    #make the first note 4 beats
                    else:
                        beats_per_note.append(random.choice([2, 4]))
                        
            #if the sequence contains 4 + (1 or 3) notes                               
            else:                                  
                for j in range(len(noteSequence)):
                    if len(noteSequence) == 5:
                        if j > 4:                                   #for notes 5 & 6
                            beats_per_note.append(1)
                        else:
                            beats_per_note.append(random.choice([2, 4]))
                    if len(noteSequence) == 7:
                        if j > 6:
                            beats_per_note.append(1)                #for notes 6 & 7 (indexing at 0)
                        else:
                            beats_per_note.append(random.choice([2, 4]))
                            
            if sum(beats_per_note) % 4 != 0:
                beats_per_note = []
        
        return beats_per_note
    
    def randomPan(self):
        pan = randint(-10, -1)
        pan /= 10
        return ([pan, 0, -pan])
    
    def randomSustain(self):
        return randint(-10, 20) / 10
    
    
        

ins1 = Instrument()

print('Instrument is: ' + ins1.typeOf)
print('Volume: ' + str(ins1.volume))
print('Pan values: ' + str(ins1.pan))
print('Sustain: ' + str(ins1.sustain))
print('Notes: ' + str(ins1.notes))
print('Beats per note: ' + str(ins1.beats))