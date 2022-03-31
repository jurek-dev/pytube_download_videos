from pytube import YouTube

def videoSearch():
    print("Enter with video's URL:")
    videoURL = input()
    yt = YouTube(
        videoURL,
        on_progress_callback = print("Please, wait... downloading video...")
    )
    videoDownload(yt)

def videoDownload(yt):
    video = yt.streams.get_highest_resolution()
    video.download()
    downloadInfo(yt.title, yt.author, yt.length)

def finishMain():
    print("Do you want download other video? (Y/N)")
    reply = input()
    if(reply == 'y'):
        videoSearch()
    else:
        print("YouTube MP4 Downloader has been finished")
        exit()

def downloadInfo(title, author, length):
    print(title, "video has been downloaded from", author, "channel in YouTube.com", length)
    finishMain()

videoSearch()