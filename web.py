import requests
import json
import webbrowser
from tkinter import Tk, Label, Entry, Button, Frame

# YouTube API key
YOUTUBE_API_KEY = "AIzaSyA0fTqiCRFCDgAahFW-B1wDLuBkkGpIl7M"

# Google Search API key
GOOGLE_SEARCH_API_KEY = "AIzaSyAisfjG5i3S4oCf0oX3CNCIqx7kONYojCI"

# Function to search YouTube and display results
def search_youtube(query):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults=5&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    for item in data["items"]:
        video_id = item["id"]["videoId"]
        video_title = item["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"YouTube Video Title: {video_title}")
        print(f"YouTube Video URL: {video_url}")
        print()

# Function to search Google and display results
def search_google(query):
    url = f"https://www.googleapis.com/customsearch/v1?&q={query}&num=5&key={GOOGLE_SEARCH_API_KEY}"
    response = requests.get(url)
    data = response.json()
    for item in data["items"]:
        search_title = item["title"]
        search_url = item["link"]
        print(f"Google Search Title: {search_title}")
        print(f"Google Search URL: {search_url}")
        print()

# Function to handle button click
def search():
    query = entry.get()
    search_youtube(query)
    search_google(query)

# GUI
root = Tk()
root.title("Search Tool")
root.config(background="white")

frame = Frame(root, bg="white")
frame.pack(pady=20)

label = Label(frame, text="Enter your query:", bg="white", font=("Arial", 14))
label.grid(row=0, column=0)

entry = Entry(frame, font=("Arial", 14))
entry.grid(row=0, column=1)

button = Button(frame, text="Search", font=("Arial", 14), command=search)
button.grid(row=0, column=2)

root.mainloop()
