import sounddevice as sd
import numpy as np
from scipy.fft import fft

bit_duration = 0.1
sample_rate = 44100.0
freq_a = 1000.0
freq_b = 2000.0

def main():
    message = input("Enter your text: ")

    bits = "".join(format(ord(char), '08b') for char in message)

    t = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

    print(f"Sending: {message} ({bits})")

    for bit in bits:
        freq = freq_a if bit == '0' else freq_b

        audio_signal = np.sin(2 * np.pi * freq * t)

        sd.play(audio_signal, sample_rate, device=1)
        sd.wait()

if __name__ == "__main__":
    main()
