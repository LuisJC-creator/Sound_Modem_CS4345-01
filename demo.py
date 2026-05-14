import numpy as np
from scipy.fft import fft

sample_rate = 48000
bit_duration = 0.1
freq_a = 1000.0
freq_b = 2000.0

def generate_tone(freq):
    t = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t).astype('float32')

def detect_frequency(chunk):
    spectrum = fft(chunk)
    freqs = np.fft.fftfreq(len(chunk), 1 / sample_rate)
    index = np.argmax(np.abs(spectrum))
    return freqs[index]

message = "Hi"
bits = "".join(format(ord(c), '08b') for c in message)
print(f"Sending: {message} -> {bits}")

decoded_bits = []
for bit in bits:
    freq = freq_a if bit == '0' else freq_b
    tone = generate_tone(freq)
    detected = detect_frequency(tone)
    decoded_bits.append('0' if abs(detected) < 1500 else '1')

decoded = ""
for i in range(0, len(decoded_bits), 8):
    byte = decoded_bits[i:i+8]
    decoded += chr(int(''.join(byte), 2))

print(f"Received: {decoded}")
