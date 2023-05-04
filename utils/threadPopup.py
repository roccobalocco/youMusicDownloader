import PySimpleGUI as sg
from utils.ytFuns import youtube2mpX

def download_thread(outdir, sound, cnt):
    print("Now in the thread number ", cnt)
    ok = youtube2mpX(outdir, url=sound)