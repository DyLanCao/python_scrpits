#!/usr/bin/env python


import sys
import numpy as np

from scipy.io import wavfile


def split_channel(wav_path, left_wav_path,right_wav_path):
    
    try:
        sample_rate,wav_data = wavfile.read(wav_path)
        left = []
        right = []

        for item in wav_data:
                    left.append(item[0])
                    right.append(item[1])

        wavfile.write(left_wav_path, sample_rate, np.array(left))
        wavfile.write(right_wav_path,sample_rate,np.array(right))
    except IOError as e:
        print('error is %s' % str(e))
    except:
        print('other error',sys.exc_info())


if __name__ == '__main__':
        split_channel('./wav_nsx_3_no_agc_stero_voice.wav','output/wav_nsx_3_left.wav','output/wav_nsx_3_right.wav')

