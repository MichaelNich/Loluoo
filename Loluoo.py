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
        button1.bind(on_press=self.change)
         
        button2 = Button(width=360,
                         height=180,
                         pos = (20, 210),
                         background_normal = './Images/1v1.jpg')
        
        button3 = Button(width=360,
                         height=180,
                         pos = (20, 15),
                         background_normal = './Images/1v1.jpg')
        
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
        
        self.talent_left_buttons_pos = [(95, 500), (250, 500), (55, 410),
                                        (175, 410), (295, 410), (95, 320),
                                        (250, 320), (55, 230), (175, 230),
                                        (295, 230), (95, 140), (250, 140),
                                        (55, 50), (175, 50), (295, 50)]
        self.talent_left_buttons = []
        
        self.button_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        widget = Widget(size=Window.size)

        for n in range(15):
            self.talent_left_buttons.append(Button(pos=self.talent_left_buttons_pos[n],
                                                   width=54, height=57,
                                                   background_normal='./Images/Talents/Ferocity/%i.jpg'%n,))
            self.talent_left_buttons[n].bind(on_press=partial(self.change, 'tbl%i'%n))
        for n in range(15):
            widget.add_widget(self.talent_left_buttons[n])
                                                   
        '''             
        self.t_buttonE1 = Button(pos=(95, 450),
                           width=54, height=57,
                           background_normal='./Images/Talents/Ferocity/0.jpg',)
        self.t_buttonE1.bind(on_press=partial(self.change, 'tbe1'))
        
        self.t_buttonE2 = Button(pos=(250, 450),
                           width=54, height=57,
                           background_normal='./Images/Talents/Ferocity/1.jpg')
        self.t_buttonE2.bind(on_press=partial(self.change, 'tbe2'))

        self.t_buttonE3 = Button(pos=(55, 360), width=54, height=57,
                                 background_normal='./Images/Talents/Ferocity/2.jpg')
        self.t_buttonE3.bind(on_press=partial(self.change, 'tbe3'))

        self.t_buttonE4 = Button(pos=(175, 360), width=54, height=57,
                                 background_normal='./Images/Talents/Ferocity/3.jpg')
        self.t_buttonE4.bind(on_press=partial(self.change, 'tbe4'))

        self.t_buttonE5 = Button(pos=(295, 360), width=54, height=57,
                                 background_normal='./Images/Talents/Ferocity/4.jpg')
        self.t_buttonE5.bind(on_press=partial(self.change, 'tbe5'))
        
        widget.add_widget(self.t_buttonE1)
        widget.add_widget(self.t_buttonE2)
        widget.add_widget(self.t_buttonE3)
        widget.add_widget(self.t_buttonE4)
        widget.add_widget(self.t_buttonE5)
        '''
        self.add_widget(widget)
    def change(self, name, *args):
        valor = None
        if name == 'tbl0':
            valor = 0
        elif name == 'tbl1':
            valor = 1
        elif name == 'tbl2':
            valor = 2
        elif name == 'tbl3':
            valor = 3
        elif name == 'tbl4':
            valor = 4
        elif name == 'tbl5':
            pass
        elif name == 'tbl6':
            pass
        elif name == 'tbl7':
            pass
        elif name == 'tbl8':
            pass
        elif name == 'tbl9':
            pass
        elif name == 'tbl10':
            pass
        elif name == 'tbl11':
            pass
        elif name == 'tbl12':
            pass
        elif name == 'tbl13':
            pass
        elif name == 'tbl14':
            pass
        else:
            pass
        
        if valor == 0 or valor == 1 or valor == 5 or valor == 6 or valor == 10 or valor == 11:
            if valor == 0 or valor == 1:
                if (self.button_status[0] + self.button_status[1]) == 5:
                    pass
                else:
                    if self.button_status[valor] == 5:
                        self.button_status[valor] = 0
                        self.talent_left_buttons[valor].background_normal = './Images/Talents/Ferocity/%i.jpg'%valor
                        self.talent_left_buttons[valor].background_down = './Images/Talents/Ferocity/%i.jpg'%valor
                    else:
                        self.button_status[valor] += 1
                        if self.button_status[valor] == 0:
                            self.talent_left_buttons[valor].background_normal = './Images/Talents/Ferocity/%i.jpg'%valor
                            self.talent_left_buttons[valor].background_down = './Images/Talents/Ferocity/%i.jpg'%valor
                        else:
                            if valor == 0:
                                self.talent_left_buttons[valor].background_normal = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[valor]+14)
                                self.talent_left_buttons[valor].background_down = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[valor]+14)
                            else:
                                self.talent_left_buttons[valor].background_normal = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[valor]+19)
                                self.talent_left_buttons[valor].background_down = './Images/Talents/Ferocity/%i.jpg'%(self.button_status[valor]+19)
        else:
            if valor == 2 or valor == 3 or valor == 4:
                if (self.button_status[0] + self.button_status[1]) == 5:
                    if valor == 2:
                        self.button_status[2] = 1
                        self.button_status[3] = 0
                        self.button_status[4] = 0
                        self.talent_left_buttons[2].background_normal = './Images/Talents/Ferocity/25.jpg'
                        self.talent_left_buttons[2].background_down = './Images/Talents/Ferocity/25.jpg'
                        self.talent_left_buttons[3].background_normal = './Images/Talents/Ferocity/3.jpg'
                        self.talent_left_buttons[3].background_down = './Images/Talents/Ferocity/3.jpg'
                        self.talent_left_buttons[4].background_normal = './Images/Talents/Ferocity/4.jpg'
                        self.talent_left_buttons[4].background_down = './Images/Talents/Ferocity/4.jpg'
                    elif valor == 3:
                        self.button_status[3] = 1
                        self.button_status[2] = 0
                        self.button_status[4] = 0
                        self.talent_left_buttons[2].background_normal = './Images/Talents/Ferocity/2.jpg'
                        self.talent_left_buttons[2].background_down = './Images/Talents/Ferocity/2.jpg'
                        self.talent_left_buttons[3].background_normal = './Images/Talents/Ferocity/26.jpg'
                        self.talent_left_buttons[3].background_down = './Images/Talents/Ferocity/26.jpg'
                        self.talent_left_buttons[4].background_normal = './Images/Talents/Ferocity/4.jpg'
                        self.talent_left_buttons[4].background_down = './Images/Talents/Ferocity/4.jpg'
                    else:
                        self.button_status[4] = 1
                        self.button_status[2] = 0
                        self.button_status[3] = 0
                        self.talent_left_buttons[2].background_normal = './Images/Talents/Ferocity/2.jpg'
                        self.talent_left_buttons[2].background_down = './Images/Talents/Ferocity/2.jpg'
                        self.talent_left_buttons[3].background_normal = './Images/Talents/Ferocity/3.jpg'
                        self.talent_left_buttons[3].background_down = './Images/Talents/Ferocity/3.jpg'
                        self.talent_left_buttons[4].background_normal = './Images/Talents/Ferocity/27.jpg'
                        self.talent_left_buttons[4].background_down = './Images/Talents/Ferocity/27.jpg'
                else:
                    pass
                    
                    
        '''
        if name == 'tbe1':
            if (self.button_status[0] + self.button_status[1]) == 5:
                pass
            else:
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
            if (self.button_status[0] + self.button_status[1]) == 5:
                pass
            else:
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
        elif name == 'tbe3':
            if (self.button_status[0] + self.button_status[1]) == 5:
                if self.button_status[2] == 0:
                    self.button_status[2] += 1
                else:
                    self.button_status[2] = 0
                if self.button_status[2] == 1:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/25.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/25.jpg'
                else:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/2.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/2.jpg'
            else:
                pass
        elif name == 'tbe4':
            if (self.button_status[0] + self.button_status[1]) == 5:
                if self.button_status[3] == 0:
                    self.button_status[3] += 1
                else:
                    self.button_status[3] = 0
                if self.button_status[3] == 1:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/26.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/26.jpg'
                else:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/3.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/3.jpg'
            else:
                pass
        elif name == 'tbe5':
            if (self.button_status[0] + self.button_status[1]) == 5:
                if self.button_status[4] == 0:
                    self.button_status[4] += 1
                    self.button_status[2] = 0
                    self.button_status[3] = 0
                else:
                    self.button_status[4] = 0
                if self.button_status[4] == 1:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/27.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/27.jpg'
                else:
                    self.t_buttonE3.background_normal = './Images/Talents/Ferocity/4.jpg'
                    self.t_buttonE3.background_down = './Images/Talents/Ferocity/4.jpg'
            else:
                pass
        
        else:
            pass
        '''
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
