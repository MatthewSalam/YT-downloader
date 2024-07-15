from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import os


def playlist(url):
    playlist = Playlist(url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.filter(progressive=True,
                                   file_extension='mp4').order_by(
            'resolution').desc().first().download()
    print("Done!!")


def video(url):
    video_caller = YouTube(url)
    print(video_caller.title)
    video_caller.streams.filter(progressive=True,
                                file_extension="mp4").order_by(
                                    "resolution").desc().first().download()
    print("Done!!")


def channel(url):
    channel_videos = Channel(url)
    print(f"Downloading videos by: {channel_videos.channel_name}")
    for video in channel_videos.videos:
        video.streams.filter(progresssive=True,
                             file_extension="mp4").order_by(
                                 "resolution").desc().first().download()
    print("Done!!")


def video_audio_only(url):
    video_caller = YouTube(url)
    print(video_caller.title)
    audio = video_caller.streams.filter(only_audio=True).first()
    out_path = audio.download(output_path= video_caller.title)
    new_name =os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp3")
    print("Done!!")


def video_only(url):
    video_caller = YouTube(url)
    print(video_caller.title)
    video = video_caller.streams.filter(only_video=True).first()
    out_path = video.download(output_path= video_caller.title)
    new_name =os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    print("Done!!")

def main():
    Downloadtype = input("What type of url is going to be inputted: Playlist, Video, Channel, mp3 only, mp4 only;  ")
    if Downloadtype == "Playlist":
        url = input("Enter the url of the playlist: ")
        playlist(url)
    elif Downloadtype == "Video":
        url = input("Enter the url of the video: ")
        video(url)
    elif Downloadtype == "Channel":
        url = input("Enter the url of the channel: ")
        channel(url)
    elif Downloadtype == "mp3 only":
        url = input("Enter the url of the video: ")
        video_audio_only(url)
    elif Downloadtype == "mp4":
        url = input("Enter the url of the video: ")
        video_only(url)
    else:
        print("Invalid Input!!")
        
main()