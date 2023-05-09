from pytube import YouTube, Playlist, Search
import os
from pathlib import Path

def youtube2mpX (outdir: str, url: str ="https://youtu.be/xvFZjo5PgG0", mpx: str="mp3")-> str:
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    # Extract audio with the maximum quality from video
    video = yt.streams.get_audio_only()
    print(video.abr)

    # Download the file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.{mpx}')
    
    try:
        os.rename(out_file, new_file)
    except FileNotFoundError as _:
        print('Rename is failed due to the presence of duplicate song url, don\'t worry the song will be in your directory')
        
    # Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
        return yt.title
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')
        return "an Error"
    
def youtubePlaylistExtractor(url: str)-> list[str]:
    if not url.__contains__('&list'):
        return []
    playlist =  Playlist(url)
    return playlist.video_urls
    
def findSong(infos: dict())-> str:
    #https://www.youtube.com/watch?v=sbwPp-H4RHw&pp=ygUYc29uZ25hbWUgYXV0aG9yMSBhdXRob3Iy
    query = infos['title']
    for artist in infos['artists']:
        query += ' ' + artist
    return Search(query).results[0].watch_url