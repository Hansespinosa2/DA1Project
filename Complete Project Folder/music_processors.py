import music21 as m21
def path_to_score(file_path: str):
    return m21.converter.parse(file_path)

def has_drums(score: m21.stream.Score):
    for part in score.parts:
        if part.pitches == []:
            return True
    return False

def get_pitchnames(score: m21.stream.Score): 
    return [pitch.name for pitch in score.pitches]

def get_diatonic_notes(key_name: str):
    return [pitch.name for pitch in m21.key.Key(key_name).pitches]


def get_score_length(score: m21.stream.Score): 
    return score.highestTime

def get_time_signature(score: m21.stream.Score):
    return score.getTimeSignatures()[0].ratioString

def get_key(score: m21.stream.Score):
    return score.analyze('key').tonicPitchNameWithCase

def get_tempo(score: m21.stream.Score):
    return score.metronomeMarkBoundaries()[0][2].number 

def get_tonality(my_list : list, my_scale : list):
    return 1- (sum(item not in my_scale for item in my_list) / len(my_list))

def get_number_of_tempo_changes(score: m21.stream.Score): 
    return len(set([tup[2].number for tup in score.metronomeMarkBoundaries()])) -1

def get_ambitus(score: m21.stream.Score):
    return score.analyze('ambitus').semitones

def get_instrument_names(score):
    the_list = [inst.instrumentName for inst in score.parts[0].getInstruments()]
    return the_list if the_list != [None] else ['Piano' , 'Guitar' , 'Vocal', 'Bass', 'Drums']

def get_mode(key_name : str):
    if key_name.istitle():
        return 'Major'
    else:
        return 'minor'
    
def get_song_length(score: m21.stream.Score, bpm: int):
    return score.highestTime/bpm

def get_song_crowdedness(time, amount):
    return amount/time

def get_artist_lists():
    Alternative_artists = ['Nirvana' , 'Foo Fighters' , 'Radiohead' , 'Red Hot Chili Peppers' , 'Weezer']
    Blues_artists = ['Chuck Berry' , 'Eric Clapton' , 'Jimi Hendrix' , 'Steely Dan' , 'Alice Cooper']
    Classical_artists = ['Andrea Bocelli' , 'Claude Debussy' , 'Ludwig Van Beethoven' , 'Scott Joplin', 'Bach Johann Sebastian']
    Country_artists = ['Alan Jackson' , 'Alabama' , 'The Doobie Brothers' , 'Cash Johnny','Brooks Garth']
    Electronic_artists = ['Jamiroquai' , 'The Prodigy' , 'Blur' , 'Abba' , 'Vangelis']
    HipHop_artists = ['The Notorious B.I.G' , 'Janet Jackson' , 'Spice Girls' , 'Zero' , 'Fugees']
    Jazz_artists = ['Nat King Cole' , 'Frank Sinatra' , 'George Benson' , 'Oscar Peterson' , 'Chaka Khan']
    Random_artists = ['Whitney Houston' , 'Michael Jackson' , 'Prince' , 'Guns N Roses' , 'Earth, Wind And Fire']
    Rap_artists = ['Britney Spears' , 'Coolio' , 'Tlc' , 'Jennifer Lopez' , 'Boyz Ii Men']
    Rock_artists = ['The Beatles' , 'Pink Floyd' , 'Queen' , 'Blink-182' , 'Billy Joel']
    return Alternative_artists, Blues_artists, Classical_artists, Country_artists, Electronic_artists, HipHop_artists, Jazz_artists, Random_artists, Rap_artists, Rock_artists

def get_artist_mapping():
    mapping = {
    'Bach Johann Sebastian' : 'Classical',
    'Brooks Garth' : 'Country',
    'Cash Johnny' : 'Country',
    'Vangelis' : 'Electronic',
    'Abba' : 'Electronic',
    'Fugees' : 'Hip-Hop',
    'Spice Girls' : 'Hip-Hop',
    'Janet Jackson' : 'Hip-Hop',
    'The Notorious B.I.G' : 'Hip-Hop',
    'Chaka Khan' : 'Jazz',
    'Frank Sinatra' : 'Jazz',
    'Boyz Ii Men' : 'Rap',
    }
    return mapping
