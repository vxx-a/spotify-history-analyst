class Song:
    class MetaInfo:
        played_ms: int
        timestamp_iso: str

        def __init__(self, played_ms, timestamp_iso):
            self.played_ms = played_ms 
            self.timestamp_iso = timestamp_iso

    __artist: str
    __name: str
    __album: str
    __track_uri: str
    meta: list[MetaInfo] | MetaInfo | None

    def __init__(self, artist, name, album, track_uri, meta):
        self.__artist = artist
        self.__album = album
        self.__name = name
        self.__track_uri = track_uri
        self.meta = meta

    @classmethod
    def fromRawStats(cls, d: dict):
        artist = d['master_metadata_album_artist_name']
        album = d['master_metadata_album_album_name']
        name = d['master_metadata_track_name']
        track_uri = d['spotify_track_uri']
        meta = cls.MetaInfo(d['ms_played'], d['ts'])

        if artist == None or \
            album == None or \
            name == None or \
            track_uri == None:
            raise Exception('Failed to get song info from dict')

        return cls(artist, name, album, track_uri, meta)

    @property
    def artist(self) -> str:
        return self.__artist
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def album(self) -> str:
        return self.__album
    
    @property
    def track_uri(self) -> str:
        return self.__track_uri