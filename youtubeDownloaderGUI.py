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

# Textbox input
youtubeLink = customtkinter.CTkEntry(application, width=400, height=50)
youtubeLink.pack()

application.mainloop()