from lib.track import Track

def test_it_instantiates_with_right_attributes():
    instance = Track("title", "artist")
    assert instance.title == "title"
    assert instance.artist == "artist"
