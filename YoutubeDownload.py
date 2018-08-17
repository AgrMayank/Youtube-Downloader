from pytube import YouTube
import os
import time

# Sample 2 Second Video Link
# https://www.youtube.com/watch?v=c0ruHxX7r3M

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


# def progress_check():
#     percent = (100*(file_size - remaining))/file_size
#     resultText.set("{:00.0f}% downloaded".format(percent))

def file_path():
	home = os.path.expanduser('~')
	download_path = os.path.join(home, 'Downloads')
	return download_path

def start():

    yt_url = link.get()
    resultText.set('Video downloaded to : {}'.format(file_path()))
    try:
        video = YouTube(yt_url)
    except:
        resultText.set("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")

    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()

    #Gets the title of the video
    # title = video.title

    #Prepares the file for download
    global file_size
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(file_path())


# Setting Up mainWindow
mainWindow = tkinter.Tk()

mainWindow.title('Youtube Video Downloader')
mainWindow.geometry('480x360+100+50')
mainWindow.configure(background = 'maroon')
mainWindow['padx']=15

# Result text
resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable = resultText)
result.grid(row = 0, column = 0, sticky = 'nsew', pady = '10')

# Setting up Download Button
buttonFrame = tkinter.Button(mainWindow, text = 'Download', command = start)
buttonFrame.grid(row = 2, column = 0, sticky = 'nsew', padx = '70', pady = '10')

# Getting Download link
link = tkinter.Entry(mainWindow)
link.grid(row = 1, column = 0, sticky = 'nsew', pady = '10')

mainWindow.columnconfigure(0,weight=10)

mainWindow.rowconfigure(0,weight=3)
mainWindow.rowconfigure(1,weight=1)
mainWindow.rowconfigure(2,weight=1)

resultText.set('Your video will be saved to : {}\n\n## Keep Patience, It may take some Time! ##\n\nEnter The Download Link Below :'.format(file_path()))

file_size = 0

mainWindow.mainloop()
