import PySimpleGUI as sg

def make_window(outdir):  
    # All the stuff inside your window.
    layout = [  [sg.T('Welcome to the awful window of youMusicDownloader'), sg.Checkbox(text='If the links are for playlists click here', key='-PLAYLIST-', enable_events=True)],
                [sg.T('Enter some urls right there -->'), sg.Multiline(key='-SONGS-', size=(55, 4), autoscroll=True), sg.Input(key='-PLAYLISTURL-', visible=False)],
                [sg.T('Remember, a lot of URL want a lot of COMA AND SPACE (, ) between each other\n[like this url1, url2, url3, ...]')],
                [sg.T('Choose the destination folder or use the default folder [{}]:'.format(outdir))],
                [sg.Input(key='-FOLDER-'), sg.FolderBrowse(target='-FOLDER-')],
                [sg.ProgressBar(key='-PROGRESS-', max_value=100, s=(70, 2))],
                [sg.B('Download', key='Download'), sg.B('Close', key='Close'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, key='-THEME-')]]    
    return sg.Window('youMusicDownloader', layout, font=('Brain', 12))

