# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.tracks= []

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        self.tracks.append(track)
        # print(self.tracks)
        return self.tracks

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        keyword == [self.title] or keyword == [self.artist]
        return self.tracks
        pass
