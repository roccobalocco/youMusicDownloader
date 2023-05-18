import spotipy as spt
from utils.ytFuns import findSong

def getInfoSong(track):
    listArtist = list()
    for artist in track['artists']:
        listArtist.append(artist['name'])
    return {'artists': listArtist, 'title': track['name']}
        
'''
Summary: This function is used to get all the youtube links starting from a spotify playlist link
'''
def spotifyPlaylistExtractor(url: str)-> list[str]:
    #id = url[url.find('/playlist/')+10:url.find('?si=')]
    sp = spt.Spotify(auth_manager=spt.oauth2.SpotifyOAuth('1bb4c720fe8a4e12a41517c4e1b9894f', '5734ac90b7964e27832507b855cac4a8','http://localhost:8888/callback'))
    tracks = sp.playlist_tracks(url)
    dictList = list()
    for track in tracks['items']:
        dictList.append(getInfoSong(track['track']))
        
    #https://open.spotify.com/playlist/37i9dQZF1DWT888el8RDPq?si=0726bc9a953549a0
    return dictList
