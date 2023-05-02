from pytube import YouTube
import PySimpleGUI as sg
import os
from pathlib import Path

def youtube2mp3 (outdir, url="https://youtu.be/xvFZjo5PgG0"):
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


url=[]
outdir="./youMusicDownloader/"

#gui start

sg.theme('DarkBrown3')   
# All the stuff inside your window.
layout = [  [sg.T('Welcome to the awful window of youMusicDownloader')],
            [sg.T('Enter some urls right there -->'), sg.Multiline(key='-SONGS-', size=(100, 15))],
            [sg.T('Remember, a lot of URL want a lot of COMA AND SPACE (, ) between each other\n[like this url1, url2, url3, ...]')],
            [sg.T('Choose the destination folder or use the default folder [{}]:'.format(outdir)), sg.Input(key='-FOLDER-'), sg.FolderBrowse(target='-FOLDER-')],
            [sg.B('Download'), sg.B('Close')] ]

# Create the Window
window = sg.Window('youMusicDownloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
        
    if event == sg.WIN_CLOSED or event == "Close": 
        break
    
    print(values.keys())
    if values['-FOLDER-'] != '' or values['-FOLDER-'] is None:
        outdir = values['-FOLDER-']
    
    songs = values['-SONGS-'].split(", ")

    for v in songs:
        url.append(v)

    cnt = 0
    for sound in url:
        ok=youtube2mp3(outdir, url=sound)
        cnt += 1
        sg.Popup('youMusicDownloader has downloaded \n[' + ok + ' ]\nand it is now at the ', (cnt / len(songs)) * 100, '%')

window.close()

#gui end
