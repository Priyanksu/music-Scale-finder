import numpy as np

NOTE_MAP = {'C':0,'C#':1,'Db':1,'D':2,'D#': 3,'Eb':3,'E':4,'F':5,'F#':6,'Gb':6,'G':7,
            'G#':8,'Ab':8,'A':9,'A#':10,'Bb':10,'B':11}

#INTERVALS
# MAJOR SCALE: ROOT WHOLE WHOLE HALF WHOLE WHOLE WHOLE HALF, 0,2,4,5,7,9,11,0
SCALES = {
    'Major (Ionian)': [0, 2, 4, 5, 7, 9, 11],
    'Natural Minor (Aeolian)': [0, 2, 3, 5, 7, 8, 10],
    'Dorian Mode': [0, 2, 3, 5, 7, 9, 10],
    'Phrygian Mode': [0, 1, 3, 5, 7, 8, 10],
    'Lydian Mode': [0, 2, 4, 6, 7, 9, 11],
    'Mixolydian Mode': [0, 2, 4, 5, 7, 9, 10],
    'Locrian Mode': [0, 1, 3, 5, 6, 8, 10]
}

def scale_finder(user_notes):
    input_notes_map = set()
    for notes in user_notes:
        notes_clean = (notes.strip()).capitalize()
        number = NOTE_MAP[notes_clean]
        input_notes_map.add(number)
    
    result = []
    
    for root_name,root_val in NOTE_MAP.items():

        if "#" in root_name or  "b" in root_name:
            continue

        for scale_name,scale_intervals in SCALES.items():
            current_scale_notes = set()
            for i in scale_intervals:
                note_index = (root_val+i)%12
                current_scale_notes.add(note_index)
            
            if input_notes_map.issubset(current_scale_notes):
                result.append(f"{root_name},{scale_name}")

    return result

def get_user_input():
    print("......................Welcome to scale finder program............")
    print("Enter the notes seperated by a space (eg: C D E)")

    note_string = input()

    # first repacing any commas with space and splitting it to make a list
    notes_list = note_string.replace(',',' ').split()

    return notes_list


user_notes = get_user_input()

result = scale_finder(user_notes)

print(f"Notes {user_notes} belong to this scales")

for f in result:
    print(f)

