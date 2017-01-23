import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.uix.textinput import TextInput
from functools import partial

__author__ = 'Michael Nich'

class Menu_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        widget = Widget(size=Window.size)
        
        button1 = Button(width=360,
                         height=180,
                         pos = (20, 405),
                         background_normal = './Images/1v1.jpg')
        
        button2 = Button(width=360,
                         height=180,
                         pos = (20, 210),
                         background_normal = './Images/1v1.jpg')
        
        button3 = Button(width=360,
                         height=180,
                         pos = (20, 15),
                         background_normal = './Images/1v1.jpg')
        
        button1.bind(on_press=self.change)
        widget.add_widget(Image(source='./Images/background.jpg',
                                size = (400, 600)))
        widget.add_widget(button1)
        widget.add_widget(button2)
        widget.add_widget(button3)
        self.add_widget(widget)
    def change(self, *args):
        self.manager.current = 'screen2'
        
class Talent_Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_status = [0, 0]
        widget = Widget(size=Window.size)
        self.t_buttonE1 = Button(pos=(95, 450),
                           width=54, height=57,
                           background_normal='./Images/Talents/Ferocity/0.jpg',)
        self.t_buttonE1.bind(on_press=partial(self.change, 'tbe1'))
        
        self.t_buttonE2 = Button(pos=(250, 450),
                           width=54, height=57,
                           background_normal='./Images/Talents/Ferocity/1.jpg')
        self.t_buttonE2.bind(on_press=partial(self.change, 'tbe2'))  
        widget.add_widget(self.t_buttonE1)
        widget.add_widget(self.t_buttonE2)
        self.add_widget(widget)
    def change(self, name, *args):
        if name == 'tbe1':
            if self.button_status[0] == 5:
                self.button_status[0] = 0
                self.t_buttonE1.background_normal = './Images/Talents/Ferocity/0.jpg'
                self.t_buttonE1.background_down = './Images/Talents/Ferocity/0.jpg'
            else:
                self.button_status[0] += 1
                if self.button_status[0] == 0:
                    self.t_buttonE1.background_normal = './Images/Talents/Ferocity/0.jpg'
                    self.t_buttonE1.background_down = './Images/Talents/Ferocity/0.jpg'
                else:
                    self.t_buttonE1.background_normal = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[0]+14)
                    self.t_buttonE1.background_down = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[0]+14)
                    
        elif name == 'tbe2':
            if self.button_status[1] == 5:
                self.button_status[1] = 0
                self.t_buttonE2.background_normal = './Images/Talents/Ferocity/0.jpg'
                self.t_buttonE2.background_down = './Images/Talents/Ferocity/0.jpg'
            else:
                self.button_status[1] += 1
                if self.button_status[1] == 0:
                    self.t_buttonE2.background_normal = './Images/Talents/Ferocity/0.jpg'
                    self.t_buttonE2.background_down = './Images/Talents/Ferocity/0.jpg'
                else:
                    self.t_buttonE2.background_normal = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[1]+19)
                    self.t_buttonE2.background_down = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[1]+19) 
        else:
            pass
        
class x1_Screen(Screen):
    def __init__(self, top_image, nxc, **kwargs):
        self.next_screen = nxc
        if top_image == 'player':
            top_image = './Images/chooseP.jpg'
        else:
            top_image = './Images/chooseP2.jpg'
        self.image_top = top_image
        super().__init__(**kwargs)
        self.escolhido = False
        widget1 = Widget(size = (400, 600))
        label1 = Image(source=self.image_top,
                       width = 360,
                       height = 100,
                       pos = (20, 500))
        layout3 = Widget(width = 360,
                         height = 3300,
                         pos = (20, 490),
                         size_hint_y = None)
        layout3.minimum_height = layout3.setter('height')
        campeao_input = TextInput(size_hint = (None, None),
                                  size = (200, 40),
                                  pos = (100, 460),
                                  font_size = 28)
        campeoes = self.bcampeoes()
        for x in range(133):
            campeoes[x].bind(on_press=self.change)
            layout3.add_widget(campeoes[x])
        sc = ScrollView(width = 410,
                        size_hint = (None, None),
                        pos = (0, 0),
                        height = 600,
                        bar_width = 3.5,
                        effect_cls = OpacityScrollEffect)
        sc.add_widget(layout3)
        widget1.add_widget(sc)
        widget1.add_widget(label1)
        #widget1.add_widget(campeao_input)
        self.add_widget(widget1)
    def change(self, *args):
        self.manager.current = self.next_screen

    def bcampeoes(self):
        lista = []
        y = 0
        c = 0
        x = 0
        while c < 133:
            if x > 3:
                x = 0
                y += 1
            butt = Button(size_hint_y = None,
                          width=80,
                          height=80,
                          pos = (20+93*x, 3105-93*y),
                          background_normal = './Images/Campeoes2/%i.png'%c)
            x += 1
            c += 1
            lista.append(butt)
        return lista
    

class Loluoo(App):
    def build(self):
        Window.size = (400, 600)
        sm = ScreenManager(transition=FadeTransition())
        screen1 = Menu_Screen(name='screen1')
        screen2 = x1_Screen('player', 'screen3', name='screen2')
        screen3 = Talent_Screen(name='screen3')
        #screen3 = x1_Screen('inimigo', 'screen4', name='screen3')
        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)
        return sm


if __name__ == '__main__':
    Loluoo().run()
