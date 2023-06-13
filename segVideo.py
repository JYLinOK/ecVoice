from moviepy.editor import *


video_F = './video/v2.mp4'
video_save_F = './video/v2_1.mp4'

start_second = 2
end_second = 23

video_clip = CompositeVideoClip([VideoFileClip(video_F).subclip(start_second, end_second)])

video_clip.write_videofile(video_save_F)


