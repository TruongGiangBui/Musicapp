from kivy.uix.button import ButtonBehavior,Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle,Rectangle
import kivy.utils


class ImageButton(Button):
    def __init__(self, **kwargs):

        super().__init__()


class ImageButtonSelectable(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__()
        # with self.canvas.before:
        #     self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#35477d")))
        #     self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[5,])
        # self.bind(pos=self.update_rect, size=self.update_rect)
        # self.bind(state=self.update_color)

    def update_color(self, *args):

        if self.state == 'normal':
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#35477d")))
        else:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#6C5B7B")))
        with self.canvas.before:
            Color(rgb=self.canvas_color.rgba)#self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#FFFFFF")))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[5,])

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size



class LabelButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        # super(ImageButtonSelectable, self).__init__(**kwargs)
        super().__init__()
        with self.canvas.before:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20, ])
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(state=self.update_color)
    def update_color(self, *args):
        print("self.canvas_Color: ", self.canvas_color.rgb)
        print("STATE IS ", self.state)
        print("self.canvas_Color: ", self.canvas_color.rgb)
        if self.state == 'normal':
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
        else:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#6C5B7B")))
        with self.canvas.before:
            Color(rgb=self.canvas_color.rgba)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20,])
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
class LabelSquareButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__()
        with self.canvas.before:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        self.bind(state=self.update_color)
    def update_color(self, *args):
        if self.state == 'normal':
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#4BB864")))
        else:
            self.canvas_color = Color(rgb=(kivy.utils.get_color_from_hex("#6C5B7B")))
        with self.canvas.before:
            Color(rgb=self.canvas_color.rgba)
            self.rect = Rectangle(size=self.size, pos=self.pos)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size