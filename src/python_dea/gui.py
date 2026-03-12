#!/usr/bin/env python
import os
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from pathlib import Path

import yt_dlp

class VideoDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python DEA - Video Downloader")
        self.root.geometry("600x400")
        
        self.downloading = False
        
        # URL Entry
        tk.Label(root, text="Video URL:").pack(pady=10)
        self.url_entry = tk.Entry(root, width=70)
        self.url_entry.pack(pady=5)
        
        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        self.download_btn = tk.Button(button_frame, text="Download", command=self.start_download, bg="green", fg="white")
        self.download_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_log)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Progress
        self.progress = ttk.Progressbar(root, mode='indeterminate')
        self.progress.pack(pady=10, fill=tk.X, padx=20)
        
        # Output Log
        self.log_text = scrolledtext.ScrolledText(root, height=15, width=70)
        self.log_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        self.log("Ready. Enter URL and click Download.")
    
    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def clear_log(self):
        self.log_text.delete(1.0, tk.END)
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            self.log(f"Progress: {percent}")
        elif d['status'] == 'finished':
            self.log(f"Downloaded: {os.path.basename(d['filename'])}")
    
    def download_worker(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Enter a URL!")
            return
        
        try:
            os.makedirs("downloads", exist_ok=True)
            ydl_opts = {
                'format': 'best[height<=1080]/best',
                'outtmpl': 'downloads/%(title)s.%(ext)s',
                'progress_hooks': [self.progress_hook],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.log("Download complete!")
            messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            self.log(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
        finally:
            self.downloading = False
            self.progress.stop()
            self.download_btn.config(state=tk.NORMAL, text="Download")
    
    def start_download(self):
        if self.downloading:
            return
        self.downloading = True
        self.progress.start()
        self.download_btn.config(state=tk.DISABLED, text="Downloading...")
        thread = threading.Thread(target=self.download_worker)
        thread.daemon = True
        thread.start()

def main():
    root = tk.Tk()
    app = VideoDownloaderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

