#!/usr/bin/env python
#coding: utf-8

import subprocess
import shlex
import time


__all__ = ['pitches', 'play']
pitches = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La',
           'La#', 'Ti']

def get_pitch_info(pitch, octave, duration):
    duration_info = pitch.split(':')
    if len(duration_info) > 1:
        duration = float(duration_info[1])
    octave_info = duration_info[0].split('-')
    if len(octave_info) > 1:
        octave = int(octave_info[1])
    name = octave_info[0]
    return name, octave, duration

def salts_from_La4(pitch):
    pitch_info = pitch.split('-')
    name = pitch_info[0]
    octave = int(pitch_info[1])
    pitch_diff = (pitches.index(name) - pitches.index('La'))
    octave_diff = 12 * (octave - 4)
    return octave_diff + pitch_diff

def get_frequency(pitch):
    return 440.0 * (2 ** (salts_from_La4(pitch) / 12.0))

def play(music, octave=4, duration=200):
    for pitch in music.split():
        name, octave, duration = get_pitch_info(pitch, octave, duration)
        if name == '_':
            time.sleep(duration / 1000.0)
        else:
            frequency = get_frequency('%s-%d' % (name, octave))
            command = 'beep -f %d -l %d' % (int(round(frequency)), duration)
            subprocess.call(shlex.split(command))
