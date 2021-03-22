# -*- coding: utf-8 -*-
from random import randrange
import random
from FoxDot import *
import random
import numpy as np
from Instrument import *
from Drums import *
#from utility import *



class Player1():
    def __init__(self):
        self.tempo = self.tempo()
        self.scale = self.scales()
    
    def play(self):
        #self.compileMusic()
        Go()
        
    def stop(self):
        Clock.clear()
    
    def tempo(self):
        # tempo = random.randint(20, 140)
        # return tempo
        Clock.bpm = random.randint(20, 140)
    
    def scales(self):
        scaleList = ['aeolian', 'chinese', 'chromatic', 'custom', 'default', 'diminished', 'dorian',
                     'dorian2', 'egyptian', 'freq', 'harmonicMajor', 'harmonicMinor', 'indian',
                     'justMajor', 'justMinor', 'locrian', 'locrianMajor', 'lydian', 'lydianMinor',
                     'major', 'majorPentatonic', 'melodicMajor', 'melodicMinor', 'minor',
                     'minorPentatonic', 'mixolydian', 'phrygian', 'prometheus', 'romanianMinor', 'yu',
                     'zhi']
        return random.choice(scaleList)
        
    def compileMusic(self):
        Clock.bpm = random.randint(20, 140)
        #Scale.default=scales()
        Scale.default='major'
               
        #############################################
        lead = Instrument('treble')
        var.testNotes = var(lead.notes, lead.beats)
        
        bass = Instrument('bass')
        var.bassNotes = var(lead.counterMelody, lead.counterMelodyBeats)
        
        backing = Instrument('sustain')
        
        drums = Drums()
        
        i1 >> SynthDef(lead.typeOf)(var.testNotes, dur=lead.noteDuration(lead.counterMelodyBeats), pan=lead.pan, amp=2, sus=lead.sustain).stop(16)
        i2 >> SynthDef(bass.typeOf)(var.testNotes, dur=lead.duration, amp=1, sus=backing.sustain).stop(16)
        
        Clock.future(4, lambda: i3 >> SynthDef(backing.typeOf)(var.testNotes, dur=lead.duration, pan=lead.pan, amp=2.5, sus=1).stop(16))
        
        print("DRUMSSSSS: " + drums.drumBeat)
        Clock.future(4, lambda: i4 >> play(drums.drumBeat, amp=2).stop(16)).stop()
        #Clock.future(4, lambda: i5 >> play(drums.drumBeat, amp=2).stop(16)).stop(16)
        
        
        ########################################################
        

        Go()
   
# player = Player1()
# player.compileMusic()
    
