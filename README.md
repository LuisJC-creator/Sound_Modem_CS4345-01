# Sound Modem

A software implementation of Frequency Shift Keying (FSK) — a physical layer 
transmission technique that encodes binary data as audio tones.

Built for CS 4345 Computer Networks at UTRGV.

## How It Works

- Bit `0` is encoded as a 1000 Hz tone
- Bit `1` is encoded as a 2000 Hz tone
- Each tone plays for 100ms
- Characters are encoded as 8-bit ASCII, MSB first
- The receiver uses FFT to detect the dominant frequency and reconstruct the message

## Requirements
- Python 3.8+
- pip

## Installation

Clone the repository:
```bash
git clone https://github.com/LuisJC-creator/Sound_Modem_CS4345-01.git
cd Sound_Modem_CS4345-01
```

Install dependencies:
```bash
pip install sounddevice numpy scipy
```

Verify installation:
```bash
python -c "import sounddevice as sd; import numpy as np; from scipy.fft import fft; print('All good')"
```

## Running the Project

**Full pipeline demo** (recommended) (linux audio troubleshooting):
```bash
python demo.py
```

**Sender only** (plays audible tones):
```bash
cd sound-modem/sender
python sender.py
```

**Receiver only** (listens and decodes):
```bash
cd sound-modem/receiver
python receiver.py
```

> Note: Run receiver before sender. For best results, both machines should be 
> on the same audio setup. See setup.md for details.

## Project Structure

Sound_Modem_CS4345-01/
sound-modem/
sender/
sender.py       # Converts text to audio tones
receiver/
receiver.py     # Detects frequencies and reconstructs text
demo.py             # End-to-end pipeline demo (no audio hardware needed)
spec.md             # Encoding specification
setup.md            # Setup and installation instructions
README.md

## Authors
Luis & Aron — UTRGV CS 4345, Spring 2026