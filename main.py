import yt_dlp
import moviepy
from pathlib import Path

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = moviepy.AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def dowload(*, url, name, mp3_format=False):
    opts = {"outtmpl": f"./Outputs/{name}.mp4",
            "format": "best"}
    
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])

    if mp3_format:
        MP4ToMP3(f"./Outputs/{name}.mp4", f"./Outputs/{name}.mp3")
    
    print("-"*16)
    print("|-- Done! --|")
    print("-"*16)

def delete_mp4_files(directory):
    # Find all MP4 files in the directory
    mp4_files = Path(directory).glob("*.mp4")
    
    # Delete each MP4 file
    for file in mp4_files:
        file.unlink()
        print(f"Deleted: {file}")

def main():
    mp3_format = input("Do you want to just mp3 format? (y/yes, n/no)\n> ")

    if mp3_format.lower() in ['y', 'yes']:
        mp3_format = True

    with open("videos_to_download.txt", 'r') as file:
        for line in file.readlines():
            name, url = line.split('|')
            print(f"Name= {name}, URL= {url}") 

            dowload(url=url, name=name, mp3_format=mp3_format)

    if mp3_format:
        delete_mp4_files("./Outputs")

if __name__ == '__main__':
    main()
