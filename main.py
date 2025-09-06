import yt_dlp
import os


def download(url):
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(
            download_dir,
            '%(playlist_index)s - %(title)s.%(ext)s'
        ),
        'ignoreerrors': True,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        is_playlist = 'entries' in info

    if is_playlist:
        print("Detected playlist. Downloading all videos in the playlist...")
        ydl_opts['noplaylist'] = False
    else:
        print("Detected single video. Downloading the video...")
        ydl_opts['noplaylist'] = True
        ydl_opts['outtmpl'] = os.path.join(download_dir, '%(title)s.%(ext)s')

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Enter a YouTube video or playlist URL: ").strip()
    download(url)
