from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.properties import ObjectProperty

Window.size = (320, 580)

class DynamicButtonsApp(MDApp):
    def build(self):
        return Builder.load_file("showshortlistedatudentstopo.kv")

if __name__ == '__main__':
    LabelBase.register(name='MPoppins', fn_regular=("Poppins Medium 500.ttf"))
    LabelBase.register(name='BPoppins', fn_regular=("Poppins Light 300.ttf"))
    LabelBase.register(name='CPoppins', fn_regular=("Poppins ExtraBold Italic 800.ttf"))
    LabelBase.register(name='DPoppins', fn_regular=("Poppins SemiBold 600.ttf"))
    DynamicButtonsApp().run()