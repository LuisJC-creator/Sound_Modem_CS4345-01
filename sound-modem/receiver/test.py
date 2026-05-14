import sounddevice as sd
import numpy as np

recording = sd.rec(44100, samplerate=44100, channels=2, device=19, dtype='float32')
sd.wait()
print("Max amplitude:", np.max(np.abs(recording)))
