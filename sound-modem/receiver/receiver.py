import sounddevice as sd
import numpy as np
from scipy.fft import fft

bit_duration = 0.1
sample_rate = 44100.0
freq_a = 1000.0
freq_b = 2000.0



def detect_frequency(chunk):
    spectrum = fft(chunk)
    freq = np.fft.fftfreq(len(chunk), 1 / sample_rate)
    index = np.argmax(np.abs(spectrum))
    return freq[index] 

def main():
    samples_per_bit = int(sample_rate * bit_duration)
    bits = []
    while(true):
        chunk = sd.rec(samples_per_bit, samplerate=sample_rate, channels=1)
        sd.wait()
        tmp = detect_frequency(chunk.flatten())
        if tmp < 1500:
            bit = 0
        else:
            bit = 1
        
        bits.append(bit)
        
        if len(bits) == 8:
            char = chr(int(''.join(map(str, bits)), 2))
            print(char)
            bits = []

if __name__ == "__main__":
    main()
