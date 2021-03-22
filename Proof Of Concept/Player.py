# -*- coding: utf-8 -*-
from random import randrange
import random
from FoxDot import *
import random
import numpy as np
#from utility import *
from Instrument import *
from Drums import *
#from PyQtUI import *
#from pythonosc import udp_client
#import asyncio


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
        
        # notes = note_sequence()
        # notesBeat = note_beats(notes)
        
        # cm_ns = counter_melody(notes)
        # cm_beats = counter_melodyBeats(cm_ns, notesBeat)
        
        # var.chords = var(notes, notesBeat)
        # var.chords1 = var(cm_ns, cm_beats)
        
       
        
        # durations = note_duration(notesBeat)
        # durations2 = note_duration(cm_beats)
        
        #Lucky! Don't forget you have to cast to a SynthDef for instruments! 
        #p1 >> SynthDef(ins1)(var.chords, dur=durations, amp=1.5).stop(8)
        #p2 >> SynthDef(ins2)(var.chords, dur=durations, amp=1.5).stop(8)
        
       
        
        # p2 >> sawbass(var.chords, dur=durations).stop(16)
        # p3 >> pluck(var.chords1, dur=durations2).stop(16)
        
        #p1 >> prophet(var.chords, dur=durations2).stop(8)
        
        #############################################
        lead = Instrument('treble')
        var.testNotes = var(lead.notes, lead.beats)
        
        bass = Instrument('bass')
        var.bassNotes = var(lead.counterMelody, lead.counterMelodyBeats)
        
        backing = Instrument('sustain')
        
        drums = Percussion()
        
        i1 >> SynthDef(lead.typeOf)(var.testNotes, dur=lead.duration, pan=lead.pan, amp=1.5, sus=lead.sustain).stop(16)
        i2 >> SynthDef(bass.typeOf)(var.testNotes, dur=lead.duration, amp=2.5, sus=backing.sustain).stop(16)
        
        Clock.future(4, lambda: i3 >> SynthDef(lead.typeOf)(var.testNotes, dur=lead.duration, pan=lead.pan, amp=1.5, sus=lead.sustain).stop(16))
        Clock.future(8, lambda: p5 >> play(drums.drumBeat, amp=2).stop(16)).stop(16)
        ########################################################
        
        
        
        #i2 >> SynthDef(bass.typeOf)(var.bassNotes, dur=lead.duration, amp=1)
        #Clock.future(12, lambda: i3 >> SynthDef(bass.typeOf)(var.bassNotes, dur=lead.duration, amp=1) )
        #print(bass.typeOf)
        
        # Clock.future(4, lambda: p4 >> prophet(var.chords, amp=2.5, dur=durations2).stop(16))
        # Clock.future(8, lambda: p5 >> play(percussion(), amp=2).stop(16)).stop(16) #work around hack. 
        Go()
   
# player = Player()
# print(player.scale)
# print(player.tempo)
    
