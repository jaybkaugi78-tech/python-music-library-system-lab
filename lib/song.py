class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Trigger all class methods on creation
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre=None):
        # Called from __init__ via self, so we need the instance genre
        pass

    @classmethod
    def add_to_artists(cls, artist=None):
        pass

    @classmethod
    def add_to_genre_count(cls, genre=None):
        pass

    @classmethod
    def add_to_artists_count(cls, artist=None):
        pass
