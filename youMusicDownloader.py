from utils.ytFuns import youtubePlaylistExtractor
import PySimpleGUI as sg
from utils.drawer import make_window
from utils.threadDownloader import download_thread
import threading

def download_playlists(playlists: list[str], bar, outdir: str)-> None:
    songs = []
    for playlist in playlists:
        songs.extend(youtubePlaylistExtractor(playlist))
    download_urls(songs, bar, outdir)
    
def download_urls(songs: list[str], bar, outdir: str)-> None:
    url = []
    for v in songs:
        url.append(v)

    threads = []
    cnt = 0
    for sound in url:
        if not sound.__contains__('&list'):    
            cnt += 1
            bar.update_bar(round((cnt/len(songs)) * 100, 2))
            t = threading.Thread(target=download_thread, args=(outdir, sound, cnt-1, ), daemon=True)
            threads.append(t)
            t.start()        
            sg.popup_timed('youMusicDownloader progress {}%\nsong number {}'.format(round((cnt/len(songs)) * 100, 2), cnt), relative_location=(1000, 500), title='Progress')
        else:
            print('Playlist instead of song')
    for index, thread in enumerate(threads):
        print('thread {} finished'.format(index))
        thread.join()
    
def main():
    outdir="./youMusicDownloader/"
    sg.theme('DarkBrown3')     
    # Create the Window
    window = make_window(outdir)

    while True:    #Controller
        event, values = window.read()
            
        if event == sg.WIN_CLOSED or event == "Close": 
            break
        
        if values['-FOLDER-'] != '' or values['-FOLDER-'] is None:
            outdir = values['-FOLDER-']

        if values['-PLAYLIST-']:
            window.__getitem__('-PLAYLISTURL-').update(visible=True)
            window.__getitem__('-SONGS-').update(visible=False)
        else:    
            window.__getitem__('-PLAYLISTURL-').update(visible=False)
            window.__getitem__('-SONGS-').update(visible=True)

        if len(values['-SONGS-']) > 0 or len(values['-PLAYLISTURL-']) > 0: 
            progress_bar = window.__getitem__('-PROGRESS-')
            progress_bar.update(visible=True)
            if values['-PLAYLIST-'] :
                download_playlists(values['-PLAYLISTURL-'].split(', '), progress_bar, outdir);
            else:
                download_urls(values['-SONGS-'].split(", "), progress_bar, outdir);
            progress_bar.update(visible=False)
            
        if values['-THEME-'] is not sg.theme():
            sg.theme(values['-THEME-'])
            print("new theme is {}".format(values['-THEME-']))
            window.close()
            window = make_window(outdir)
    window.close()


main()