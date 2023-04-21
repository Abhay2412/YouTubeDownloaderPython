import tkinter
import customtkinter
from pytube import YouTube

# UI Design and Settings 
customtkinter.set_appearance_mode("System") # Set the appearance based on the system 
customtkinter.set_default_color_theme("blue")

# Frame Settings 
application = customtkinter.CTk() # Initialize the application 
application.geometry("800x400")
application.title("YouTube Video Downloader")

# Add in UI elements
title = customtkinter.CTkLabel(application, text="Paste a YouTube video link")
title.pack(padx=15, pady=15)

def startDownload():
    try:
        linkToDownload = youtubeLink.get()
        youTubeVideoObject = YouTube(linkToDownload)
        video = youTubeVideoObject.streams.get_highest_resolution()
        video.download()
        videoTitle = youTubeVideoObject.title
    except:
        print("YouTube Link is Invalid")
    statusMessageText = customtkinter.CTkLabel(application, text="The video:" + videoTitle + " is downloaded!")
    statusMessageText.pack(padx=25, pady=25)

# Textbox input
youtubeURL = tkinter.StringVar()
youtubeLink = customtkinter.CTkEntry(application, width=400, height=50, textvariable=youtubeURL)
youtubeLink.pack()

# Download Button 
downloadButton = customtkinter.CTkButton(application, text="Download", command=startDownload)
downloadButton.pack(padx=15, pady=15)

application.mainloop()