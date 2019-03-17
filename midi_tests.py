import mido



# name  of the file
file_name = "ashover_simple_chords_17.mid"

# open the file
mid = mido.MidiFile(file_name)

# Prints the reconstruted track
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
