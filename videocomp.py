
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

import sys

class VideoComp(BoxLayout):
    def __init__(self, **kwargs):
        super(VideoComp, self).__init__()
        
        self.video1.source = sys.argv[1]
        self.video1.state = "play"
        
        self.video2.source = sys.argv[2]
        self.video2.state = "play"
        
    def pausa(self):
        if self.video1.state == "play":
            self.video1.state = "pause"
            self.video2.state = "pause"
        else:
            self.video1.state = "play"
            self.video2.state = "play"        

class VideoCompApp(App):
    def build(self):
        return VideoComp()
        
if __name__ == "__main__":
    VideoCompApp().run()
