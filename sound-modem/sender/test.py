import sounddevice as sd
import numpy as np

sample_rate = 48000
t = np.linspace(0, 1.0, sample_rate, endpoint=False)
tone = np.sin(2 * np.pi * 1000 * t).astype('float32')
sd.play(tone, sample_rate, device=19)
sd.wait()
