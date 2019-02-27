import os
import subprocess

class EncodeJob:
    def __init__(self, vid_path=None, sub_path=None, out_path=None):
        self.video_path = vid_path
        self.output_path = out_path
        self.subtitle_path = sub_path

    # ffmpeg -i in.mp4 -filter_complex "subtitles=in.srt:force_style='OutlineColour=&H80000000,BorderStyle=3,Outline=1,Shadow=1,MarginV=20'" out.mp4
    def start(self):
        subprocess.run([
            'ffmpeg',
            '-i',
            self.video_path,
            '-filter_complex',
            f"subtitles={self.subtitle_path}:force_style=\'OutlineColour=&H80000000,BorderStyle=3,Outline=1,Shadow=1,MarginV=20\'\"",
            self.output_path])