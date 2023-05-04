import PySimpleGUI as sg
import utils.df as df
from PIL import Image

def roundButtonImg(text: str, key: str):
    w, h = df.getSize(text, df.fontDefiner('./media/ARIAL.TTF', 25))
    w += 10; h += 10

    color, highlighted = '#FFFFFF', sg.theme_background_color(),
    OUT = df.backgroundPNG(w*5, h*5)
    OUT = df.roundCorners(OUT[0], 20*3)
    IN = df.replaceColor(OUT, highlighted, color)
    OUT = OUT.resize((w,h), resample=Image.LANCZOS)
    IN = IN.resize((w,h), resample=Image.LANCZOS)
    OUT, IN = [df.image_to_data(each) for each in [OUT, IN]]

    button = sg.Button(text, border_width=0, button_color=sg.theme_background_color(), image_data=OUT, key=key)

    return button, IN, OUT

def make_window(outdir):   
    # All the stuff inside your window.
    layout = [  [sg.T('Welcome to the awful window of youMusicDownloader'), sg.Checkbox(text='If the links are for playlists click here', key='-PLAYLIST-', enable_events=True)],
                [sg.T('Enter some urls right there -->'), sg.Multiline(key='-SONGS-', size=(55, 4), autoscroll=True), sg.Input(key='-PLAYLISTURL-', visible=False)],
                [sg.T('Remember, a lot of URL want a lot of COMA AND SPACE (, ) between each other\n[like this url1, url2, url3, ...]')],
                [sg.T('Choose the destination folder or use the default folder [{}]:'.format(outdir))],
                [sg.Input(key='-FOLDER-'), sg.FolderBrowse(target='-FOLDER-')],
                [sg.ProgressBar(key='-PROGRESS-', max_value=100, s=(70, 2))],
                [roundButtonImg("Download", "Download")[0], roundButtonImg("Close", "Close")[0], sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, key='-THEME-')]]
    return sg.Window('youMusicDownloader', layout, font=('Brain', 12))

