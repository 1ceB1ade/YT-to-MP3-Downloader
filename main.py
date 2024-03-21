import os
import sys
import shutil
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream is None:
            print("No audio stream available for the specified video.")
            return

        print("Downloading audio...")
        filename = audio_stream.default_filename
        filepath = os.path.join(save_path, filename)

        audio_stream.download(output_path=save_path)
        print("Download completed successfully.")

        mp4_filepath = os.path.join(save_path, filename)
        mp3_filepath = os.path.splitext(mp4_filepath)[0] + ".mp3"
        os.rename(mp4_filepath, mp3_filepath)

        print("Conversion to mp3 completed successfully.")
        print(f"MP3 file saved at: {mp3_filepath}")
    except Exception as e:
        print("An error occurred:", e)

def get_download_path():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def main():
    while True:
        clear_terminal()
        print("Welcome to YouTube to MP3 Downloader!")
        url = input("Enter the YouTube video link: ")

        save_path = get_download_path()
        if not save_path:
            print("No download path selected. Exiting.")
            sys.exit(1)

        download_video(url, save_path)

        while True:
            choice = input("Do you want to download another link? (y/n): ").strip().lower()
            if choice in ('y', 'n'):
                break
            else:
                print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

        if choice == 'n':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
