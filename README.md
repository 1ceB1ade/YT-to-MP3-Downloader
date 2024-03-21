# YT2MP3 - YouTube to MP3 Downloader

YT2MP3 is a Python tool that allows you to easily download audio from YouTube videos and save them as MP3 files. With YT2MP3, you can quickly convert your favorite YouTube videos into audio files that you can listen to anytime, anywhere.

## Features

- Download audio from YouTube videos
- Convert downloaded audio to MP3 format
- Simple and easy-to-use command-line interface
- Cross-platform compatibility

## Requirements

- Python 3.x
- pytube library
- moviepy library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/1ceB1ade/YT-to-MP3-Downloader.git
   ```

2. Install the required libraries:

   ```sh
   pip install pytube moviepy
   ```

## Usage

1. Run the `main.py` script:

   ```sh
   python main.py
   ```

2. Enter the YouTube video link when prompted.

3. Choose the download location when prompted.

4. The tool will download the audio from the provided YouTube link and save it as an MP3 file in the specified location.

5. You can choose to download another link or exit the tool after each download.

## Example

```sh
Welcome to YouTube to MP3 Downloader!
Enter the YouTube video link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Select download directory: 
Downloading audio...
Download completed successfully.
Conversion to mp3 completed successfully.
MP3 file saved at: C:/Downloads/Never_Gonna_Give_You_Up.mp3
Do you want to download another link? (y/n): n
Exiting the program.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pytube](https://github.com/pytube/pytube)
- [moviepy](https://github.com/Zulko/moviepy)
