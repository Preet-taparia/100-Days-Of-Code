import tkinter as tk
from tkinter import ttk, filedialog
import requests
import os

# https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe

class Downloader:
    def __init__(self) -> None:
        self.saveto = ""    
        self.window = tk.Tk()
        self.window.title("Downloader")
        self.url_label = tk.Label(text="Enter URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.browse_button = tk.Button(text="Browse", command=self.browse_file)
        self.browse_button.pack()
        self.download_button = tk.Button(text="Download", command=self.download)
        self.download_button.pack()
        self.window.geometry("800x400")
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=300, mode="determinate")
        self.progress_bar.pack()
        
        
        
        self.window.mainloop()

    def browse_file(self,):
        saveto = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1])
        self.saveto = saveto
        
    def download(self,):
        url = self.url_entry.get()
        response = requests.get(url, stream = True)
        total_size_in_bytes = int(response.headers.get("content-length"))
        block_size =10000
        self.progress_bar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1]
        if self.saveto == "":
            self.saveto = fileName

        with open(self.saveto, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] += (100 * block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)

if __name__ == "__main__":
    Downloader()