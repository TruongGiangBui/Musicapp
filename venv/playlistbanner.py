from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.app import App
import kivy.utils
from kivy.uix.button import Button
from specialbuttons import ImageButtonSelectable,ImageButton
class PlaylistBanner(GridLayout):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            app.select_playlist(self.id)
            app.change_screen("listening_screen", direction='up', mode='pop')

    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()#**kwargs)
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.id = kwargs['id']
        left = FloatLayout()

        left_label = Label(font_size='20sp',text=kwargs['name'], size_hint=(1, 1), pos_hint={"top": .9, "center_x": .5},color=kivy.utils.get_color_from_hex("#FFFFFF"))
        left.add_widget(left_label)
        self.add_widget(left)
    def erase_list(self):
        self.clear_widgets()

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class MusicLayout(GridLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            app.change_song(self.id)


    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()#**kwargs)
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.id=kwargs['id']

        self.info=kwargs['music']


        left = FloatLayout()

        left_label = Label(font_size='20sp',text=self.info['track_name'], size_hint=(1, 1), pos_hint={"top": .9, "center_x": .5},color=kivy.utils.get_color_from_hex("#FFFFFF"))
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MusicLayoutSearch(GridLayout):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            app = App.get_running_app()
            app.select_search_song(self.info)
            app.change_screen("listening_screen", direction='up', mode='pop')


    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()#**kwargs)
        with self.canvas.before:
            Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.id=kwargs['id']

        self.info=kwargs['music']

        left = FloatLayout()

        left_label = Label(font_size='20sp',text=self.info['track_name'], size_hint=(1, 1), pos_hint={"top": .9, "center_x": .5},color=kivy.utils.get_color_from_hex("#FFFFFF"))
        left.add_widget(left_label)
        self.add_widget(left)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size



