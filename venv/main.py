import sys
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,NoTransition, CardTransition
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from kivy.utils import platform
from specialbuttons import LabelButton
from playlistbanner import PlaylistBanner,MusicLayout,MusicLayoutSearch
from kivy.core.audio import SoundLoader
from kivy.uix.slider import Slider
import requests
from pprint import pprint
BASE_URL=BASE="http://127.0.0.1:5000/"

class HomeScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class ListeningScreen(Screen):
    pass
class HistoryScreen(Screen):
    pass
class SearchScreen(Screen):
    pass




GUI=Builder.load_file("main.kv")
class MainApp(App):
    logedin=False
    played=False
    userID=None
    playlist_index='0'
    music_index='0'
    recommend=None
    history=None

    def build(self):
        return GUI

    def change_screen(self,screen_name, direction='forward', mode = ""):

        screen_manager = self.root.ids['screen_manager']
        if direction == 'forward':
            mode = "push"
            direction = 'left'
        elif direction == 'backwards':
            direction = 'right'
            mode = 'pop'
        elif direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)

        screen_manager.current = screen_name

    def on_start(self):
        global loggedin
        global played
        loggedin=False
        played=False
        if(loggedin==True):
            self.setup()
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current="login_screen"

        banner_grid=self.root.ids['home_screen'].ids['banner_grid']
        for i in range(5):
            P=PlaylistBanner(name=f"Playlist {i}",id=str(i))
            banner_grid.add_widget(P)

    def login(self):
        global loggedin
        global userID
        username=self.root.ids['login_screen'].ids['login_username'].text
        password=self.root.ids['login_screen'].ids['login_password'].text
        #login request
        response = requests.get(BASE + "login", {"username": username, "password": password})
        result=response.json()
        if True:
            loggedin=True
            # userID=result['user_id']
            userID='34e191b5e3ac4d0b86b100e3325aa46c34998248'
            self.setup()


            self.root.ids['login_screen'].ids['login_message'].text = ""
            self.change_screen("home_screen")
        else:
            self.root.ids['login_screen'].ids['login_message'].text="Invalid username or password"

    def setup(self):
        global userID
        global recommend
        global history
        global musiclist
        print(userID)
        try:
            response = requests.get(BASE + "recommend", {'id': userID})
            recommend = response.json()
            print(recommend)
            response = requests.get(BASE + "history", {'id': userID})
            history=response.json()
            # print(history)
        except:
            return
        #cai dat danh sach bai hat trong playlist
        music_list_banner = self.root.ids['listening_screen'].ids['music_list']
        musiclist = recommend['data'][0]['playlist']
        # print(musiclist)

        for i in range(len(musiclist)):
            music = musiclist[i]
            P = MusicLayout(music=music, id=str(i))
            music_list_banner.add_widget(P)

    def select_playlist(self, id):
        global playlist_index
        global music_index
        global recommend
        global musiclist
        playlist_index = int(id)
        print(type(playlist_index))

        print(f'playlist {playlist_index}')

        music_list_banner = self.root.ids['listening_screen'].ids['music_list']
        music_list_banner.clear_widgets()

        print(recommend['data'])
        musiclist = recommend['data'][playlist_index]['playlist']
        # print(musiclist)

        for i in range(len(musiclist)):
            music = musiclist[i]
            P = MusicLayout(music=music, id=str(i))
            music_list_banner.add_widget(P)

        songname=self.root.ids['listening_screen'].ids['song_name']
        songname.text=musiclist[0]['track_name']
        music_index=0

    def playsong(self):
        global played
        if played==True:
            print("paused")
            played=False
        else:
            played=True
            print("play")

    def nextsong(self):
        global music_index
        global recommend
        global musiclist
        music_index+=1
        if music_index<len(musiclist):
            self.change_song(music_index)

    def prevsong(self):
        global music_index
        music_index-=1
        if(music_index>=0):
            self.change_song(music_index)

    def change_song(self,id):
        global music_index
        global recommend
        global playlist_index
        global musiclist
        music_index = int(id)
        print(music_index)
        songname = self.root.ids['listening_screen'].ids['song_name']
        songname.text = musiclist[music_index]['track_name']

    def load_history(self):
        global history
        musiclist = history['data']
        pprint(musiclist)

        history_banner = self.root.ids['history_screen'].ids['history_list']
        for i in range(len(musiclist)):
            music = musiclist[i]
            P = MusicLayoutSearch(music=music, id=str(i))
            history_banner.add_widget(P)
        self.change_screen("history_screen")

    def search_music(self):
        global searchcontent
        text_input=self.root.ids['search_screen'].ids['search_content']
        print(text_input.text)
        response = requests.get(BASE + "search", {'content': text_input.text})
        searchcontent = response.json()
        # print(searchcontent)
        banner_grid = self.root.ids['search_screen'].ids['banner_grid']
        banner_grid.clear_widgets()
        for i in range(len(searchcontent['data'])):
            music=searchcontent['data'][i]
            P = MusicLayoutSearch(music=music, id=str(i))
            banner_grid.add_widget(P)

    def select_search_song(self,track):
        global searchcontent
        global music_index
        global musiclist


        print("select ", track['track_name'])
        music_list_banner = self.root.ids['listening_screen'].ids['music_list']
        music_list_banner.clear_widgets()


        response = requests.get(BASE + "playlistfortrack", {'content': track['echonest_track_id']})
        musiclist = response.json()['data']
        # print(musiclist)
        for i  in range(len(musiclist)):
            music=musiclist[i]
            P = MusicLayout(music=music, id=str(i))
            music_list_banner.add_widget(P)

        songname = self.root.ids['listening_screen'].ids['song_name']
        songname.text = musiclist[0]['track_name']
        music_index = 0

MainApp().run()