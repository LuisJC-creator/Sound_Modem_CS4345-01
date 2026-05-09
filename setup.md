# Setup Instructions

## Requirements
- Python 3.8+
- pip

## Installation

Clone the repository:
```bash
git clone https://github.com/LuisJC-creator/Sound_Modem_CS4345-01.git
cd sound-modem
```

Install dependencies:
```bash
pip install sounddevice numpy scipy
```

## Verify Installation

Run the following to confirm everything is working:
```bash
python -c "import sounddevice as sd; import numpy as np; from scipy.fft import fft; print('All good')"
```

## Running the Project

**Sender** (converts text to sound):
```bash
cd sender
python sender.py
```

**Receiver** (listens and decodes sound to text):
```bash
cd receiver
python receiver.py
```

## Notes
- Both machines must have a working microphone and speaker
- Run receiver before sender so it is ready to listen
- Tested on Linux (Ubuntu/Arch-based) and Windows