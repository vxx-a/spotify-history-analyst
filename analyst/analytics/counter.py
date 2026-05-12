from song import Song
from dataclasses import dataclass

class Counter:
    @dataclass
    class SongCount:
        song: Song
        count: int

        def print(self):
            print(f'💿 {self.song.name} by {self.song.artist} [{self.song.album}]')
            
            total_playtime = sum([d.played_ms for d in self.song.meta])
            print(f'🕰️  {int(total_playtime / 60000)}min')
            print(f'🔄 {self.count}')
    
    # use track uri as identifier
    counts: dict[str, SongCount] = { }

    def __init__(self, songs: list[Song]):
        for song in songs:
            if song.track_uri in self.counts:
                self.counts[song.track_uri].song.meta.append(song.meta)
                self.counts[song.track_uri].count += 1
            else:
                song.meta = [song.meta]
                self.counts[song.track_uri] = self.SongCount(song, 1)

    def __matcher(q: str, s: Song) -> bool:
        song_str = f'{s.album} {s.artist} {s.name}'

        return q.lower() in song_str.lower()

    def count_sort(songs: list[SongCount]) -> list[SongCount]:
        songs.sort(key=lambda s: s.count, reverse=True)
        return songs
    
    def count_print(songs: list[SongCount]):
        for song in songs:
            song.print()
            print()

    def match(self, q: str) -> list[SongCount]:
        return list(filter(lambda s: Counter.__matcher(q, s.song), self.counts.values()))