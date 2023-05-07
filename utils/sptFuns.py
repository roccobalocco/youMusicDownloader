import spotify.sync as spt

def get_playlist(url: str):
    spotify = spt.Playlist(url=url)
    return spotify.get_all_tracks()
