from scipy.io import wavfile

# Convert `data` to 32 bit integers:
y = (np.iinfo(np.int32).max * (data/np.abs(data).max())).astype(np.int32)

wavfile.write(wav_path, fs, y)
