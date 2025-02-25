import os
# pip install yt-dlp
import yt_dlp

def download_video(url, save_path="downloads", quality="best"):
    try:
        os.makedirs(save_path, exist_ok=True)

        ydl_opts = {
            'format': quality,
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Starting download...")
            ydl.download([url])
            print("Download completed successfully!")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    url = input("Enter YouTube URL: ")
    download_video(url)

if __name__ == '__main__':
    main()
