from moviepy.editor import *


def extract_mp3_from_mp4(path_mp4: str, path_mp3: str):
    clip = VideoFileClip(path_mp4)
    clip.audio.write_audiofile(path_mp3)
    clip.close()


def merge_mp3_to_mp4(path_mp4: str, path_mp3: str, save_path: str):
    clip = VideoFileClip(path_mp4)
    new_clip = clip.without_audio()

    new_audio = AudioFileClip(path_mp3)
    new_clip = new_clip.set_audio(new_audio)

    new_clip = new_clip.resize((1080, 1920))
    new_clip.write_videofile(save_path)
    new_clip.close()
    clip.close()
    new_audio.close()
