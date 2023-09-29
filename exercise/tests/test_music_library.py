from lib.music_library import MusicLibrary

# It instantiates with the right attributes 

def test_it_initiates_with_the_right_attributes():
    instance = MusicLibrary()
    assert instance.tracks == []


