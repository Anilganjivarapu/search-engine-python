import requests
import json
import webbrowser
from tkinter import Tk, Label, Entry, Button, Frame
YOUTUBE_API_KEY = "AIzaSyA0fTqiCRFCDgAahFW-B1wDLuBkkGpIl7M"
GOOGLE_SEARCH_API_KEY = "AIzaSyAisfjG5i3S4oCf0oX3CNCIqx7kONYojCI"
def search_youtube(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=5&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    for item in data.get("items", []):
        video_id = item.get("id", {}).get("videoId", None)
        if video_id:
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            webbrowser.open(video_url)
def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?&q={query}&num=5&key={GOOGLE_SEARCH_API_KEY}"
    response = requests.get(url)
    data = response.json()
    for item in data.get("items", []):
        search_url = item.get("link", None)
        if search_url:
            webbrowser.open(search_url)
def search():
    query = entry.get()
    search_youtube(query)
    search_google(query)
root = Tk()
root.title("Search Tool")
root.config(background="gold")
frame = Frame(root, bg="silver")
frame.pack(pady=20)
label = Label(frame, text="Enter your query:", bg="Aquamarine", font=("capital", 14))
label.grid(row=0, column=0)
entry = Entry(frame, font=("Arial", 14))
entry.grid(row=0, column=1)
button = Button(frame, text="Search", font=("italic", 14), command=search)
button.grid(row=0, column=2)
root.mainloop()
