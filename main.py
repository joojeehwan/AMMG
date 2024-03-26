# 모듈 import
from moviepy.editor import VideoFileClip

#변수 선언
mp4_file = "sample.mp4"
mp3_file = "target.mp3"

#object 할당
video_clip = VideoFileClip(mp4_file)
audio_clip = video_clip.audio

#음성 추출
audio_clip.write_audiofile(mp3_file)

#객체 종료
video_clip.close()
audio_clip.close()
