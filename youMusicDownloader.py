from utils.ytFuns import youtube2mpX
import PySimpleGUI as sg
from utils.drawer import make_window
    
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
            ok = youtube2mpX(outdir, url=sound)
            cnt += 1
            sg.Popup('youMusicDownloader has downloaded \n[' + ok + ' ]\nand it is now at the ', (cnt / len(songs)) * 100, '%')

    if values['-THEME-'] is not sg.theme():
        sg.theme(values['-THEME-'])
        print("new theme is {}".format(values['-THEME-']))
        window.close()
        window = make_window(outdir)
          
window.close()

#gui end
