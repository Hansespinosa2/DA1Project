import music21 as m21
def path_to_score(file_path: str): #add functionality to make sure it turns to one score with different parts
    return m21.converter.parse(file_path)

def remove_drums(score: m21.stream.Score): #remove the drum part from the score
    for part in score.parts:
        if part.pitches == []:
            score.remove(part)

def get_drum_parts(score: m21.stream.Score): #return the drum parts as a list of parts
    drum_parts = []
    for part in score.parts:
        if part.pitches == []:
            drum_parts.append(part.voicesToParts())
    return drum_parts

def get_drum_pattern_list(part: m21.stream.Part): #return the drum parts as a list of parts
    measure_list = []
    for m in part.recurse().getElementsByClass('Measure'):
        n_list =[]
        for n in m.notesAndRests:
            if type(n) == m21.note.Unpitched:
                n_list.append((m21.percussion.PercussionChord([n]),n.offset))
            else:
                n_list.append((n, n.offset))
        measure_list.append(n_list)
    return measure_list



def get_full_chord_progression(score: m21.stream.Score, the_key: str): #iterate through the score and find the most commonly used chord progression
    remove_drums(score)
    full_chord_progression = []
    print(the_key)
    sChords = score.chordify()
    for c in sChords.recurse().getElementsByClass(m21.chord.Chord):
        rn = m21.roman.romanNumeralFromChord(c, m21.key.Key(the_key))
        length = c.quarterLength
        full_chord_progression.append((rn.figure,length))
    return full_chord_progression

def get_score_length(score: m21.stream.Score): #not correct
    return score.highestTime

def get_time_signature(score: m21.stream.Score):
    return score.getTimeSignatures()[0].ratioString

def get_key(score: m21.stream.Score):
    return score.analyze('key').tonicPitchNameWithCase

def get_base_chord_progression(score: m21.stream.Score): #iterate through the score and find the most commonly used chord progression
    pass

def get_chord_progression_variance(score: m21.stream.Score): #this will take the base chord progression and see how many times it appears versus how many chords are in the song
    pass

def get_melody_hook(score: m21.stream.Score): #find the most common melody hook using any repeated measures
    pass

def get_melody_variance(score: m21.stream.Score): #this will take the melody hook and see how many times it appears versus how many measures are in the song
    pass

def get_drum_beat(score: m21.stream.Score): #find the most common drum beat using any repeated measures
    pass

def get_drum_beat_variance(score: m21.stream.Score): #this will take the drum beat and see how many times it appears versus how many measures are in the song
    pass

