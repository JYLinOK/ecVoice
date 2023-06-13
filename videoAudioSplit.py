# Split the audio from video
import moviepy
import moviepy.editor as mp



# Input: .mp4 format video file path
def splitAudioFromVideo(video_path, audio_save_path=''):
    mp4_video = mp.VideoFileClip(video_path)
    if audio_save_path == '':
        audio_path = video_path[:-(video_path[::-1].index('.'))]+'wav'
    else:
        audio_path = audio_save_path
    mp4_audio = mp4_video.audio.write_audiofile(audio_path)
    return audio_path



if __name__ == "__main__":
    video_path = './video/v2.mp4'
    print(f'{splitAudioFromVideo(video_path=video_path) = }')

