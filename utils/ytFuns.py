from pytube import YouTube
import os
from pathlib import Path

def youtube2mpX (outdir, url="https://youtu.be/xvFZjo5PgG0", mpx="mp3"):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    # Extract audio with the maximum quality from video
    video = yt.streams.get_audio_only()
    print(video.abr)

    # Download the file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.{mpx}')
    os.rename(out_file, new_file)
    
    # Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
        return yt.title
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')
        return "an Error"