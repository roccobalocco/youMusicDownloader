from utils.ytFuns import youtube2mpX
import PySimpleGUI as sg
from utils.drawer import make_window
from utils.threadPopup import download_thread
import threading
    
outdir="./youMusicDownloader/"

#gui start

sg.theme('DarkBrown3') 
# Create the Window
window = make_window(outdir)
# Event Loop to process "events" and get the "values" of the inputs

threads = list()
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
            cnt += 1
            t = threading.Thread(target=download_thread, args=(outdir, sound, cnt-1, ), daemon=True)
            threads.append(t)
            t.start()        
            popmsg = 'youMusicDownloader progress {}%\nsong number {}'.format(round((cnt/len(songs)) * 100, 2), cnt)
            print(popmsg)
            sg.popup_timed(popmsg, relative_location=(1000, 500), title='Progress')
            
        for index, thread in enumerate(threads):
            print('thread {} finished'.format(index))
            thread.join()
            
    if values['-THEME-'] is not sg.theme():
        sg.theme(values['-THEME-'])
        print("new theme is {}".format(values['-THEME-']))
        window.close()
        window = make_window(outdir)
    
          
window.close()

#gui end
