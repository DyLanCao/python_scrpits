# coding: utf-8
import sounddevice as sd
duration = 10
fs = 16000
rec = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='int16')
sd.wait()
pcm = rec.tostring()
with open('test.raw', 'wb') as w:
    w.write(pcm)

# Use following sox command to play it
# play -r 16000 -e signed-integer -b 16 test.raw
