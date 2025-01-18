import yt_dlp
import moviepy
from pathlib import Path

# Function to convert MP4 file to MP3 format
def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = moviepy.AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

# Function to download video from URL and optionally convert to MP3
def download(*, url, name, mp3_format=False):
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

def main():
    # Prompt user for MP3 format option
    mp3_format = input("Do you want to just mp3 format? (y/yes, n/no)\n> ")

    # Convert user input to boolean
    if mp3_format.lower() in ['y', 'yes']:
        mp3_format = True

    # Read URLs and names from videos_to_download.txt
    with open("videos_to_download.txt", 'r') as file:
        for line in file.readlines():
            name, url = line.split('|')
            print(f"Name= {name}, URL= {url}") 

            # Download and optionally convert to MP3
            download(url=url, name=name, mp3_format=mp3_format)

    # Delete MP4 files if mp3_format is True
    if mp3_format:
        delete_mp4_files("./Outputs")

if __name__ == '__main__':
    main()
