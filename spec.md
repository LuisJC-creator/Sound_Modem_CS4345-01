# Sound Modem Encoding Spec

## Frequencies
- Bit 0: 1000 Hz
- Bit 1: 2000 Hz

## Timing
- Bit duration: 100ms (0.1 seconds)
- Sample rate: 44100 Hz

## Encoding
- Each character encoded as 8 bits (ASCII, MSB first)
- No padding or silence between bits

## Example
- 'A' = 65 = 01000001
- Plays: 2000, 1000, 1000, 1000, 1000, 1000, 1000, 2000 Hz tones