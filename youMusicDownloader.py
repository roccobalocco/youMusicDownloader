from pytube import YouTube
import PySimpleGUI as sg
import os
from drawer import make_window
from pathlib import Path

            #sg.B('Download', border_width=0)
def youtube2mp4 (outdir, url="https://youtu.be/xvFZjo5PgG0"):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    # Extract audio with the maximum quality from video
    video = yt.streams.get_audio_only()
    print(video.abr)

    # Download the file
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp4')
    os.rename(out_file, new_file)
    
    # Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
        return yt.title
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')
        return "an Error"
    
outdir="./youMusicDownloader/"

#gui start

sg.theme('DarkBrown3') 
# Create the Window
window = make_window(outdir)
# Event Loop to process "events" and get the "values" of the inputs
while True:    
    url=[]
    event, values = window.read()
          
    if event == sg.WIN_CLOSED or event == "Close": 
        break
    
    print(values.keys())
    if values['-FOLDER-'] != '' or values['-FOLDER-'] is None:
        outdir = values['-FOLDER-']
    
    if len(values['-SONGS-']) > 0: 
        songs = values['-SONGS-'].split(", ")

        for v in songs:
            url.append(v)

        cnt = 0
        for sound in url:
            ok = youtube2mp4(outdir, url=sound)
            cnt += 1
            sg.Popup('youMusicDownloader has downloaded \n[' + ok + ' ]\nand it is now at the ', (cnt / len(songs)) * 100, '%')

    if values['-THEME-'] is not sg.theme():
        sg.theme(values['-THEME-'])
        print("new theme is {}".format(values['-THEME-']))
        window.close()
        window = make_window(outdir)
          
window.close()

#gui end
