import yt_dlp
import moviepy
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to convert MP4 file to MP3 format
def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = moviepy.AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

# Function to download video from URL and optionally convert to MP3
def download(url, name, mp3_format=False):
    opts = {"outtmpl": f"./Outputs/{name}.mp4",  # Output template for MP4 file
            "format": "best"}  # Download the best quality format
    
    # Use yt_dlp to download the video
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    # Convert to MP3 if mp3_format is True
    if mp3_format:
        MP4ToMP3(f"./Outputs/{name}.mp4", f"./Outputs/{name}.mp3")
    
    # Print completion message
    print("-"*16)
    print("|-- Done! --|")
    print("-"*16)

# Function to delete all MP4 files in a directory
def delete_mp4_files(directory):
    # Find all MP4 files in the directory
    mp4_files = Path(directory).glob("*.mp4")
    
    # Delete each MP4 file
    for file in mp4_files:
        file.unlink()
        print(f"Deleted: {file}")

# GUI functions
def download_manual():
    global name_entry, url_entry
    url = url_entry.get()
    name = name_entry.get()
    mp3_format = mp3_var.get()
    download(url=url, name=name, mp3_format=mp3_format)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            for line in file.readlines():
                name, url = line.strip().split('|')
                download(url=url, name=name, mp3_format=mp3_var.get())
        messagebox.showinfo("Download complete", "All videos have been downloaded.")

def main():
    global name_entry, url_entry, mp3_var

    # GUI setup
    root = tk.Tk()
    root.title("Video Downloader")
    root.geometry("350x200")  # Set window dimensions
    root.configure(bg="lightblue")  # Set window background color

    # URL and name input
    tk.Label(root, text="Enter Name:", bg="lightblue", fg="black").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5, ipadx=50, ipady=5)

    tk.Label(root, text="Enter URL:", bg="lightblue", fg="black").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    url_entry = tk.Entry(root)
    url_entry.grid(row=1, column=1, padx=5, pady=5, ipadx=50, ipady=5)

    # MP3 format option
    mp3_var = tk.BooleanVar()
    tk.Checkbutton(root, text="MP3 Format", variable=mp3_var, bg="lightblue", fg="black").grid(row=2, column=0, columnspan=2, pady=5)

    # Download buttons
    tk.Button(root, text="Download Manually", command=download_manual, bg="black", fg="white").grid(row=3, column=0, columnspan=2, pady=5, ipadx=30)
    tk.Button(root, text="Upload File", command=upload_file, bg="black", fg="white").grid(row=4, column=0, columnspan=2, pady=5, ipadx=40)

    root.mainloop()

if __name__ == "__main__":
    main()
