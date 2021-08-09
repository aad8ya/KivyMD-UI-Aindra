import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

class Mainapp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        return Builder.load_file('md.kv')
    
    def home(self):
        return
    
    def health_check(self):
        return
    
    def st_acq(self):
        return
    
    def vid_feed(self):
        return

    def x_up_press(self, ts, s):
        print(ts, s)
        return

    def x_down_press(self, ts, s):
        print(ts, s)
        return
    
    def y_up_press(self, ts, s):
        print(ts, s)
        return
    
    def y_down_press(self, ts, s):
        print(ts, s)
        return
    
    def z_up_press(self, ts, s):
        print(ts, s)
        return
    
    def z_down_press(self, ts, s):
        print(ts, s)
        return
        
Window.size = (720, 480)
Mainapp().run()