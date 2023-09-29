from unittest.mock import Mock
from lib.music_library import MusicLibrary
from lib.track import Track

# def test_fake_tracks_are_added_to_library():
#     library = MusicLibrary() 
#     track_entry = Track("Purple rain", "Prince")
#     track_instance = library.add(track_entry)
#     fake_track_entry1 = Mock() 
#     fake_track_entry1.add(track_instance)== [track_instance] 
#     # fake_track_entry2 = Mock()
#     # fake_track_entry2.search(track_instance).return_value == ["Purple rain", "Prince"] 
    


#     library.add(fake_track_entry1)
#     # library.add(fake_track_entry2)
#     assert library.add(fake_track_entry1) == [fake_track_entry1]


def test_fake_keyword_is_used_to_search_for_tracks():
    library = MusicLibrary()
    track_instance = Track("purple rain", "prince")
    fake_track_entry1 = Mock() 
    fake_track_entry1.add(track_instance).return_value == [track_instance] 
    library.add(fake_track_entry1)
    assert library.add(fake_track_entry1) == [fake_track_entry1]

