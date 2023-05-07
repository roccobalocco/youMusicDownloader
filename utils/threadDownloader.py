from utils.ytFuns import youtube2mpX

def download_thread(outdir: str, sound: str, cnt: int)-> str:
    print("Now in the thread number ", cnt)
    print(sound)
    youtube2mpX(outdir, url=sound)