# -*- coding: utf-8 -*-
from random import randrange
import random
from FoxDot import *
from utility import *
from Instrument import *
#from PyQtUI import *
from pythonosc import udp_client
import asyncio



client = udp_client.SimpleUDPClient('172.0.0.1', 57110)

#Server.recHeaderFormat = "WAV"
# Server.prepareForRecord("C:/Users/johnn/Documents/SuperCollider/Recordings/control001.wav", 2)
#time.sleep(1)

# client.send_message("/s_new", Server.record())
# time.sleep(5)
# client.send_message("/s_new", Server.stopRecording())



def tempo():
    Clock.bpm = random.randint(20, 140)
    

#have to define a player class or individual methods wson't play simultaneously
def player():

    tempo()
    #Scale.default=scales()
    Scale.default='major'
    
    notes = note_sequence()
    notesBeat = note_beats(notes)
    
    cm_ns = counter_melody(notes)
    cm_beats = counter_melodyBeats(cm_ns, notesBeat)
    
    var.chords = var(notes, notesBeat)
    var.chords1 = var(cm_ns, cm_beats)
    
    ins1 = instrument()
    ins2 = instrument()
    print(ins1)
    
    durations = note_duration(notesBeat)
    durations2 = note_duration(cm_beats)
    
    #Lucky! Don't forget you have to cast to a SynthDef for instruments! 
    #p1 >> SynthDef(ins1)(var.chords, dur=durations, amp=1.5).stop(8)
    #p2 >> SynthDef(ins2)(var.chords, dur=durations, amp=1.5).stop(8)
    
   
    
    p2 >> sawbass(var.chords, dur=durations).stop(16)
    p3 >> pluck(var.chords1, dur=durations2).stop(16)
    
    #p1 >> prophet(var.chords, dur=durations2).stop(8)
    
    #############################################
    # lead = Instrument('treble')
    # var.testNotes = var(lead.notes, lead.beats)
    
    # bass = Instrument('bass')
    # var.bassNotes = var(lead.counterMelody, lead.counterMelodyBeats)
    
    # backing = Instrument('sustain')
    
    
    
    # i1 >> SynthDef(lead.typeOf)(var.testNotes, dur=lead.duration, pan=lead.pan, amp=1.5, sus=lead.sustain)
    # i2 >> SynthDef(backing.typeOf)(var.testNotes, dur=lead.duration, amp=2.5, sus=backing.sustain)
    ########################################################
    
    
    
    #i2 >> SynthDef(bass.typeOf)(var.bassNotes, dur=lead.duration, amp=1)
    #Clock.future(12, lambda: i3 >> SynthDef(bass.typeOf)(var.bassNotes, dur=lead.duration, amp=1) )
    #print(bass.typeOf)
    
    Clock.future(4, lambda: p4 >> prophet(var.chords, amp=2.5, dur=durations2).stop(16))
    Clock.future(8, lambda: p5 >> play(percussion(), amp=2).stop(16)).stop(16) #work around hack. 

    #Clock.future(4, lambda: p4 >> prophet(var.chords, amp=2.5, dur=durations2).stop(16))
    #Clock.future(8, lambda: p5 >> play(percussion(), amp=2).stop(16)).stop(16) #work around hack. 
    

    #client.send_message("/s_new", "default", s.record())

    #Server.record()    

    Go()
    
    # asyncio.run(test())
    

    
    #client.send_message("/s_new", "default", s.nextNodeID, 1, 1)
    
    #client.send(s.record())
    #Server.record()
    #client.send_message(57110, s.record)
    #Server.record()


#player()

print(scales())


def test(): #returns nice chords to work with
    nums = [0,2,4,6,8]
    chord1 = []
    chord2 = []
    while len(chord1) < 3:
        x = random.choice(nums)
        chord1.append(x)
        nums.remove(x)
        
    return chord1


    
print(test())


# print(SynthDefs)
# Clock.bpm = 80
# Scale.default = 'minor'

# #first list is note - second is duration in beats
# var.chords = var([0,1,6,4,5.5], [4,4,4,2,2], amp=0.5)
# var.chords1 = var([4,3,8,4], [4,4,4,4])
# var.piano = var([(7,8),(7,7),(6,7),(5.5,7)], [4,4,4,4])

# var.test = var([2,4,6,7], [2,2,4,4])

# t1 >> pluck(var.test, dur=[0.25, 0.25, 0.25, 1, 0.5])

# p1 >> pluck(var.chords, dur=[0.25,0.25, 0.5], sus=1)

# p2 >> prophet(var.chords1)
# p3 >> bass(var.chords, dur=1/4)

# d1 >> play("e")

# p4 >> spark([8,7], dur=[1/4,3.75], sus=4, amp=1.5)

# p5 >> piano(var.piano, dur=1/4, amp=1.2, sus=3, pan=(-1,1))
# p6 >> piano(var([(8,6,0),(0,2,6),(2,4,0)], [4]) + P(0), dur=PDur([3,5],8), sus=2)

# i1 >> loop([2,4,6,7])

# p1 >> pluck(var.chords, dur=[0.25,0.25, 0.5], sus=1)
# Clock.future(8, lambda: df >> play("xoxo"))

# print(Clock.now())

# Clock.clear()