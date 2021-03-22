# -*- coding: utf-8 -*-
from random import *
import random
from FoxDot import *
#from utility import *


class Instrument:
    def __init__(self, instrument):
        #self.instrumentType = instrumentType(x)
        self.typeOf = self.randomInstrument(instrument)
        self.notes = self.randomNoteSeq()
        self.beats = self.noteBeats(self.notes)
        self.volume = self.randomVolume()
        self.pan = self.randomPan()
        self.sustain = self.randomSustain()
        self.duration = self.noteDuration(self.beats)
        self.startTime = self.randomStartTime()
        
        self.counterMelody = self.counteMelody(self.notes)
        self.counterMelodyBeats = self.counteMelodyBeats(self.counterMelody, self.beats)
        # self.stopTime
        # self.isSolo
        
    def randomInstrument(self, type):
        instrumentList = [ 
                      'varsaw', 'lazer', 'rave', 'scatter',
                      'charm', 'bell', 'gong', 'viola',  
                      'soft', 'quin', 'pluck', 'spark', 'blip',  'creep', 
                      'orient', 'zap', 'marimba', 'pulse', 'saw',  
                      'karp', 'arpy', 'nylon',   'swell', 'razz', 'sitar', 'star',
                      'pasha', 'space', 'keys', 'sinepad'
                      ]
        instrumentList = [ 'pluck', 'karp' ]
        # bassList = ['noise', 'dab', 'bass', 'dirt',   'dub', 'scratch', 'ripple',
        #             'fuzz', 'donk', 'squish', 'jbass', 'sawbass', 'dbass'] 
        bassList = ['sawbass']  
        ambienceList = ['snick', 'crunch', 'space', 'growl', 'glass']      
        sustainedList = ['scatter', 'soprano', 'klank', 'feel', 'glass', 'prophet', 'bug', 'ambi']
        if type == 'treble':
            return random.choice(instrumentList)
        elif type == 'bass':
            return random.choice(bassList)
        elif type == 'ambience':
            return random.choice(ambienceList)
        elif type == 'sustain':
            return random.choice(sustainedList)

    
    def randomVolume(self):
        volume = randint(10, 30)
        volume /= 10
        return volume
    
    def randomNoteSeq(self):
        notes = [0,7, 2,9, 4,11, 5,12, 7,14] #[0,1,2,3,4,5,6,7]
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
    
    
        #defines the length of the notes as list. Make the values weighted
    def noteDuration(self, beats):
        beats_length = len(beats)               #make the lists same length
       
        #durations = [0.25, 0.5, 0.75, 1, 1.5, 2]
        
        #adding weights gives the melody a more natural feel & rhythm
        # rather than use values between 0 - 1, used 0-100 for integer purposes
        durations = [0.25] * 25 + [0.5] * 25 + [0.75] * 10 +  [1] * 20 + [1.5] * 10 + [2] * 10       
        
        note_lengths = []
        
        while len(beats) != len(note_lengths):
        #while len(note_lengths) != 2:
            note_lengths.append(random.choice(durations))
            #note_lengths.append(weighted_choice(durations, weights))
        
        return note_lengths
    
    def randomStartTime(self):
        return random.choice([0,4,8,12])
    
    #return a random note that is part of the root notes chord: 0 -> (2 or 4) etc..C -> E or F
    #for variation the counter melody can have different notes assuming the total number of beats  is the same
    def counteMelody(self, note_sequence):
        
        #allows for half notes or double notes (quavers or dotted crotchets)
        #counter_mel_size =  random.randint(len(note_sequence) - 2, len(note_sequence) + 2)
        counter_mel_size =  len(note_sequence)
        counter_mel = []
        counterNote = random.choice([2,4]) #values for the 3rd or 5th note of the chort. try this with negative values too in future
        
        #do the logic for returning 3rds or 5ths
        for i in range(counter_mel_size):
            counterNote = random.choice([2,4])
            if counter_mel_size <= len(note_sequence):
                counter_mel.append(note_sequence[i] + counterNote) #if shorter list we can make notes sustain - so return
            else:
                if len(counter_mel) < len(note_sequence):
                    counter_mel.append(note_sequence[i] + counterNote)
                else:
                    counter_mel.append(counter_mel[i-1] + 1)
    
    
        #print(counter_mel)
        return counter_mel 
    
    
    def counteMelodyBeats(self, counter_melody, beats_per_note):
        counter_beats = []

        #counter_beats = note_beats(counter_melody) 
        #ERRORS WHEN WE HAVE 4 NOTES and 2 COUNTER NOTES - CAN NEVER GET TO EQUAL NUMBER PROBABLY OTHER SHIT TOO           
        while sum(beats_per_note) != sum(counter_beats):          
            counter_beats = []
            counter_beats = self.noteBeats(counter_melody)
                      
        return counter_beats
    
        

ins1 = Instrument('sustain')

print('Instrument is: ' + ins1.typeOf)
print('Volume: ' + str(ins1.volume))
print('Pan values: ' + str(ins1.pan))
print('Sustain: ' + str(ins1.sustain))
print('Notes: ' + str(ins1.notes))
print('Beats per note: ' + str(ins1.beats))
print('Durations: ' + str(ins1.duration))
print('Start time: ' + str(ins1.startTime))
print('Counter Melody notes: ' + str(ins1.counterMelody))
print('Counter melody beats: ' + str(ins1.counterMelodyBeats))