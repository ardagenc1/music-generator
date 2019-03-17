import mido
import numpy as np 

output_file = mido.MidiFile()
output_track1 = mido.MidiTrack()
output_track2 = mido.MidiTrack() 

# <meta message set_tempo tempo=500000 time=0>
# <meta message key_signature key='E' time=0>
# <meta message time_signature numerator=4 denominator=4 clocks_per_click=48 notated_32nd_notes_per_beat=8 time=0>
# <meta message track_name name='Falling About' time=0>
# <meta message end_of_track time=61465>
# output_track.append(mido.Message("set_tempo", set_tempo))



def construct_major_key_from_random_note(note):
	tonal = note
	major_second = note + 2
	major_third = note + 4
	perfect_four = note + 5
	perfect_fifth = note + 7 
	major_sixth = note + 9
	major_seventh =  note + 11
	perfect_octave = note + 12
	notes_in_key = [tonal, major_second, major_third, perfect_four, perfect_fifth, major_sixth, major_seventh, perfect_octave]
	return notes_in_key 

def construct_minor_key_from_random_note(note):
	tonal = note
	major_second = note + 2
	major_third = note + 3
	perfect_four = note + 5
	perfect_fifth = note + 7 
	major_sixth = note + 8
	major_seventh =  note + 10
	perfect_octave = note + 12
	notes_in_key = [tonal, major_second, major_third, perfect_four, perfect_fifth, major_sixth, major_seventh, perfect_octave]
	return notes_in_key

def pick_random_note_in_key(note):
	'''
	takes the tonal, returns the index of a random note in the notes_in_key array
	'''
	note_index = (int(np.random.rand() * 1000) % 8)
	return note_index


start_note = int(np.random.rand() * 41) + 40
notes_in_minor_key = construct_minor_key_from_random_note(start_note)
print(notes_in_minor_key)
time = 479
for _ in range(64):
	note_value = notes_in_minor_key[pick_random_note_in_key(start_note)]
	randomize = np.random.randn()
	if randomize > 0.8:
		note_value = note_value - 12
	if _ % 8 == 0:
		note_value = notes_in_minor_key[0]
	time_ = (int(np.random.randn() * 1000)  % 17 )
	time_ = max(int(time_) * 60- 1, 119)
	print(time_)
	velocity_ = int((np.random.randn() * 1000) % 26) + 100
	on = mido.Message('note_on', note=note_value, velocity=velocity_, time=1)
	off = mido.Message('note_off', note=note_value, velocity=0, time=time_)

	output_track1.append(on)
	output_track1.append(off)

	

'''
random_notes = (np.random.rand(64) * 41) + 40
random_notes = [int(random_notes[i]) for i in range(len(random_notes))]
print(random_notes)
time = 479
for note in random_notes:
	note_value = note
	time_ = (int(np.random.randn() * 1000)  % 17 )
	time_ = max(int(time_) * 60- 1, 119)
	print(time_)
	velocity_ = int((np.random.randn() * 1000) % 26) + 100
	on = mido.Message('note_on', note=note_value, velocity=velocity_, time=1)
	off = mido.Message('note_off', note=note_value, velocity=0, time=time_)
	
	output_track1.append(on)
	output_track1.append(off)

for i,note in enumerate(random_notes):
	note = random_notes[i % 9]
	note_value = note - 24
	time_ = (int(np.random.randn() * 1000) % 17 )
	time_ = max(int(time_) * 60- 1, 239)
	print(time_)
	on = mido.Message('note_on', note=note_value, velocity=120, time=1)
	off = mido.Message('note_off', note=note_value, velocity=0, time=time_)
	
	output_track2.append(on)
	output_track2.append(off)
'''


print("ARDA'S SONG'S MIDI REPRESENTATION")
print("=========================================================================")
print(output_track1)
print("=========================================================================")



output_file.tracks.append(output_track1)

output_file.save("arda-test.mid")

print("reconstruted track")
print("=========================================================================")
# Prints the reconstruted track
for i, track in enumerate(output_file.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)








