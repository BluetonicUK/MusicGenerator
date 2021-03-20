# -*- coding: utf-8 -*-
from random import randrange
import random
import numpy as np

def scales():
    scaleList = ['aeolian', 'chinese', 'chromatic', 'custom', 'default', 'diminished', 'dorian',
                 'dorian2', 'egyptian', 'freq', 'harmonicMajor', 'harmonicMinor', 'indian',
                 'justMajor', 'justMinor', 'locrian', 'locrianMajor', 'lydian', 'lydianMinor',
                 'major', 'majorPentatonic', 'melodicMajor', 'melodicMinor', 'minor',
                 'minorPentatonic', 'mixolydian', 'phrygian', 'prometheus', 'romanianMinor', 'yu',
                 'zhi']
    return random.choice(scaleList)

def instrument():
    instrumentList = ['loop', 'stretch', 'audioin', 'noise', 'dab', 
                      'varsaw', 'lazer', 'growl', 'bass', 'dirt', 'crunch', 'rave', 'scatter',
                      'charm', 'bell', 'gong', 'soprano', 'dub', 'viola', 'scratch', 'klank',
                      'feel', 'glass', 'soft', 'quin', 'pluck', 'spark', 'blip', 'ripple', 'creep', 
                      'orient', 'zap', 'marimba', 'fuzz', 'bug', 'pulse', 'saw', 'snick', 'twang',
                      'karp', 'arpy', 'nylon', 'donk', 'squish', 'swell', 'razz', 'sitar', 'star',
                      'jbass', 'sawbass', 'prophet', 'pads', 'pasha', 'ambi', 'space', 'keys', 
                      'dbass', 'sinepad']
    return random.choice(instrumentList)


def percussion():
 
    drumbeat = ['x', '-', 'o', 'r', 't', 'y', 'u', 'i', 'p', 'a', 'd', 'f', 'h', 'k', 'l',
                'v', 'n', 'm', '=', '+', '#', '$', '%', '^', '&', '*']
    electrodrums = ['q', 'w', 'e', 'g', 'j', 'z', 'b']
    expressions = ['1', '2', '3', '4', '?', '!']

    drums = ""
    
    for i in range(4):
        drums += random.choice(drumbeat)
        
    return drums

print(percussion())

def note_sequence():
    notes = [0,7, 2,9, 4,11, 5,12, 7,14] #[0,1,2,3,4,5,6,7]
    notes_in_sequence = []
    for i in range(randrange(4, 9)):
        notes_in_sequence.append(random.choice(notes))
    
    #print(notes_in_sequence)
    return notes_in_sequence
        
   
#define beats per note in the sequence. Must end up with a correct number of beats to sound like a song.
#the maths has been done in such a way that it will always return some length/beat of notes that will
#be divisible by the correct number of beats to make the music sound familiar
def note_beats(note_sequence):    
    
    #both lists must have the same length - maybe try 2D array
    beats_per_note = []
    while len(beats_per_note) != len(note_sequence):       
        beats_per_note = []
        
        #get correct beats for sequence lengths divisible by 4 
        if len(note_sequence) % 2 == 0:                         
            for i in range(len(note_sequence)):
                if i == 0:
                    beats_per_note.append(4)                    #make the first note 4 beats
                else:
                    beats_per_note.append(random.choice([2, 4]))
                    
        #if the sequence contains 4 + (1 or 3) notes                               
        else:                                  
            for j in range(len(note_sequence)):
                if len(note_sequence) == 5:
                    if j > 4:                                   #for notes 5 & 6
                        beats_per_note.append(1)
                    else:
                        beats_per_note.append(random.choice([2, 4]))
                if len(note_sequence) == 7:
                    if j > 6:
                        beats_per_note.append(1)                #for notes 6 & 7 (indexing at 0)
                    else:
                        beats_per_note.append(random.choice([2, 4]))
                        
        if sum(beats_per_note) % 4 != 0:
            beats_per_note = []
    
    #print(beats_per_note) 
    return beats_per_note

#return a random note that is part of the root notes chord: 0 -> (2 or 4) etc..C -> E or F
#for variation the counter melody can have different notes assuming the total number of beats  is the same
def counter_melody(note_sequence):
    
    #allows for half notes or double notes (quavers or dotted crotchets)
    #LINE BUGGED> FIX THIS
    #counter_mel_size =  random.randint(len(note_sequence) - 2, len(note_sequence) + 2)
    counter_mel_size =  len(note_sequence)
    print(counter_mel_size)
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
                
    
        
    
def counter_melodyBeats(counter_melody, beats_per_note):
    counter_beats = []
    print(sum(beats_per_note))
    
    #counter_beats = note_beats(counter_melody)
    
    #ERRORS WHEN WE HAVE 4 NOTES and 2 COUNTER NOTES - CAN NEVER GET TO EQUAL NUMBER PROBABLY OTHER SHIT TOO
        
    while sum(beats_per_note) != sum(counter_beats):
        
        counter_beats = []
        print("BOO")
        counter_beats = note_beats(counter_melody)
        
        
    return counter_beats

#defines the length of the notes as list. Make the values weighted
def note_duration(beats):
    beats_length = len(beats)               #make the lists same length
   
    #durations = [0.25, 0.5, 0.75, 1, 1.5, 2]
    
    #adding weights gives the melody a more natural feel & rythm
    durations = [0.25] * 25 + [0.5] * 25 + [0.75] * 10 +  [1] * 20 + [1.5] * 10 + [2] * 10
    
    note_lengths = []
    
    while len(beats) != len(note_lengths):
    #while len(note_lengths) != 2:
        note_lengths.append(random.choice(durations))
        #note_lengths.append(weighted_choice(durations, weights))
    
    return note_lengths




def recordWithSC():
    pass
    
    




notes = note_sequence()
print("NOTES: " + str(notes))
beats = note_beats(notes)
print("NOTES BEATS: " + str(beats))
cm = counter_melody(notes)
print("COUNTER MELODY: " + str(cm))
cmBeats = counter_melodyBeats(cm, beats)
print("COUNTER_M BEATS: " + str(cmBeats))


#counterBeats = beats

#print(counterBeats)

print(note_duration(beats))

    

