# -*- coding: utf-8 -*-

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd
import IPython.display as ipd #use this for playing the audio on a player

from IPython.display import display
from PIL import Image

path = 'control001.wav'
path2 = '20210320-145741.aiff'

class Analysis:
    
    def __init__(self, file):
        self.file = file
        

    def displayWaveGraph(self):
        audio, sampleRate = librosa.load(self.file)
        time = np.arange(0, len(audio)) / sampleRate
        fig, ax = plt.subplots()
        ax.plot(time, audio)
        ax.set(xlabel = 'Time(s)', ylabel = 'Sound Amplitutde')
        plt.show()
 
        fig = plt.Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.plot(time, audio)
        ax.set(title = 'Simple Wave Plot', xlabel = 'Time(s)', ylabel = 'Sound Amplitutde')
        fig.savefig('graphs/waveplot.png')
        
        image = Image.open(r'graphs/waveplot.png') #object
        imagePath = 'graphs/waveplot.png'
        
        return image

    
    #logarithmic amplitude more perceptually significant
    def displaySTFT(self): # Short-Time Fourier Transform
        y, sr = librosa.load(self.file)
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(D, y_axis='linear', x_axis='time',
                                       sr=sr, ax=ax[0])
        ax[0].set(title='Linear-frequency power spectrogram')
        ax[0].label_outer()
        
        hop_length = 1024
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y, hop_length=hop_length)),
                                    ref=np.max)
        librosa.display.specshow(D, y_axis='log', sr=sr, hop_length=hop_length,
                                 x_axis='time', ax=ax[1])
        ax[1].set(title='Log-frequency power spectrogram')
        ax[1].label_outer()
       
        fig.colorbar(img, ax=ax, format="%+2.f dB")       
        plt.savefig('graphs/spectogram.png')
        
        image = Image.open(r'graphs/spectogram.png') #object
        imagePath = 'graphs/spectogram.png'
        
        return image
        
        
    def displayHarmonicsPercussive(self):
        y, sr = librosa.load(self.file)
        fig, ax = plt.subplots()
        y_harm, y_perc = librosa.effects.hpss(y)
        librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
        librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
        ax.set(title='Harmonic + Percussive', xlabel = 'Time(s)', ylabel = 'Sound Amplitutde')
        
        plt.savefig('graphs/harmonics.png')
        
        image = Image.open(r'graphs/harmonics.png') #object
        imagePath = 'graphs/harmonics.png'
        
        return image
        

#test = Analysis(path);
# test.displaySTFT()
# test.displayWaveGraph()
# test.displayHarmonicsPercussive()