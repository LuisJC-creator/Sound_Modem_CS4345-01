import sounddevice as sd
for i, d in enumerate(sd.query_devices()):
    print(i, d['name'], d['max_output_channels'])
