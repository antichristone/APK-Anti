import os
import re
import sys
import time
import requests
import threading
import webbrowser
import kivy.utils

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.core.clipboard import Clipboard

from StructService import Distribution_Service

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
attack_number_phone=Distribution_Service()

data_dead = {'hours':144, 'minutes':13, 'sec':13}

def ads(target='https://t.me/adsantichristblog'):
    try:
        ads_channel=requests.get(target)
        content=ads_channel.content.decode('UTF-8')
        result_text_ads=content[230:280]
        result_text_ads=result_text_ads[:result_text_ads.rfind('*')]
        return result_text_ads
    except Exception:
        return 't.me/antichristone'

def send_call():
    attack_number_phone.call_next_service()

def send_message(only_sms=None):
    if only_sms == None:
        attack_number_phone.random_service()

    elif only_sms == True:
        attack_number_phone.sms_random_service()

def send_message_next(only_sms=None):
    if only_sms == None:
        attack_number_phone.next_service()

    elif only_sms == True:
        attack_number_phone.sms_next_service()


class AntichristApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configuration_screen = {'special_abilities':None, 'style':None, 'hell':None, 'my_style':None}
        self.start_hell = None;self.queries_color = None;self.storage = None
        self.configuration_app(way='/storage/emulated/0/AntichristOne')

        if self.configuration_screen['hell'] == ['True']:
            self.dead_time = {'sec':1, 'minute':60, 'hour':3600}
            self.start_hell = True
            self.link_th = False

            hell_activity=open('style.kv', 'r').read()
            hell_activity=hell_activity.replace("source: 'image_files/lilith.jpg'", "source: 'hell.jpg'")

            self.screen = Builder.load_string(hell_activity)
            self.screen.ids.title.pos_hint = {"center_x": 8, "center_y": 8}
            self.screen.ids.target.pos_hint = {"center_x": 8, "center_y": 8}
            self.screen.ids.menu_button.pos_hint = {"center_x": 8, "center_y": 8}
            self.screen.ids.button_attack_cancel.pos_hint = {"center_x": 8, "center_y": 8}
            self.screen.ids.what_button.pos_hint = {"center_x": 8, "center_y": 8}
            self.screen.ids.link_tg.pos_hint = {"center_x": 8, "center_y": 8}

            self.screen.ids.you_dead_data.pos_hint = {"center_x": 0.5, "center_y": 0.6}

            with open('style_configuration/hell', 'w') as stop_hell:
                stop_hell.write('None')

            self.you_dead()

        if self.start_hell == None:

            if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:

                start_my_style=open('style.kv', 'r').read()

                photo=self.configuration_screen['my_style'][11][self.configuration_screen['my_style'][11].rfind(':')+1:]
                if os.path.isfile(photo) == True:
                    start_my_style=start_my_style.replace("source: 'image_files/lilith.jpg'", f"source: '{photo}'")

                    self.title = str(self.configuration_screen['my_style'][1][self.configuration_screen['my_style'][1].rfind(':')+1:])
                    start_my_style=start_my_style.replace('text: "[color=#fedcff]Antichrist[/color]"' ,f'text: "[color={self.title}]Antichrist[/color]"')

                    phone_number_color = str(self.configuration_screen['my_style'][2][self.configuration_screen['my_style'][2].rfind(':')+1:])
                    start_my_style=start_my_style.replace('line_color_focus: utils.get_color_from_hex(self.phone_number_color)', f'line_color_focus: utils.get_color_from_hex("{phone_number_color}")')
                    start_my_style=start_my_style.replace('line_color_normal: utils.get_color_from_hex(self.phone_number_color)', f'line_color_normal: utils.get_color_from_hex("{phone_number_color}")')

                    menu_mode = str(self.configuration_screen['my_style'][3][self.configuration_screen['my_style'][3].rfind(':')+1:])
                    start_my_style=start_my_style.replace('md_bg_color: utils.get_color_from_hex(self.menu_mode_color)', f'md_bg_color: utils.get_color_from_hex("{menu_mode}")')

                    menu_mode_text = str(self.configuration_screen['my_style'][4][self.configuration_screen['my_style'][4].rfind(':')+1:])
                    start_my_style=start_my_style.replace('text_color: utils.get_color_from_hex(self.menu_mode_color_text)', f'text_color: utils.get_color_from_hex("{menu_mode_text}")')

                    attack_color = str(self.configuration_screen['my_style'][5][self.configuration_screen['my_style'][5].rfind(':')+1:])
                    start_my_style=start_my_style.replace('md_bg_color: utils.get_color_from_hex(self.attack_color)', f'md_bg_color: utils.get_color_from_hex("{attack_color}")')

                    attack_color_text = str(self.configuration_screen['my_style'][6][self.configuration_screen['my_style'][6].rfind(':')+1:])
                    start_my_style=start_my_style.replace('text_color: utils.get_color_from_hex(self.attack_color_text)', f'text_color: utils.get_color_from_hex("{attack_color_text}")')

                    what_color = str(self.configuration_screen['my_style'][7][self.configuration_screen['my_style'][7].rfind(':')+1:])
                    start_my_style=start_my_style.replace('md_bg_color: utils.get_color_from_hex(self.what_color)', f'md_bg_color: utils.get_color_from_hex("{what_color}")')

                    what_color_text = str(self.configuration_screen['my_style'][8][self.configuration_screen['my_style'][8].rfind(':')+1:])
                    start_my_style=start_my_style.replace('text_color: utils.get_color_from_hex(self.what_color_text)', f'text_color: utils.get_color_from_hex("{what_color_text}")')

                    self.queries_color = str(self.configuration_screen['my_style'][9][self.configuration_screen['my_style'][9].rfind(':')+1:])

                    self.link_tg_color = self.configuration_screen['my_style'][10][self.configuration_screen['my_style'][10].rfind(':')+1:]
                    start_my_style=start_my_style.replace("text: '[color=#fedcff]t.me/antichristone[/color]'", f"text: '[color={self.link_tg_color}]t.me/antichristone[/color]'")

                    self.screen = Builder.load_string(start_my_style)
                else:
                    self.screen = Builder.load_file('style.kv')
            else:
                self.screen = Builder.load_file('style.kv')
            self.link_th = True

        self.target_status_666 = True
        self.status = None
        self.click = 0
        self.mode = 'Ultra'
        self.what = 'Mix'
        self.attack_number_phone = attack_number_phone
        self.label = self.screen.ids.label
        self.links = self.screen.ids.link_tg
        self.open = 'https://t.me/antichristone'

        if self.configuration_screen['hell'] == ['False']:
            threading.Thread(target=self.target_666).start()

        if self.link_th == True:
            threading.Thread(target=self.start_link, args=(10,)).start()

    def configuration_app(self, way='/storage/emulated/0/AntichristOne'):
        self.configuration_screen['hell'] = open('style_configuration/hell', 'r').read().split()
        self.configuration_screen['my_style'] = open('style_configuration/my_style', 'r').read().split()
        self.configuration_screen['special_abilities'] = open('style_configuration/special_abilities', 'r').read().split()

        if self.configuration_screen['special_abilities'] == ['False']:
            pass

        else:
            if os.path.isdir(way) == False:
                try:
                    os.mkdir(way)
                    with open(f'{way}/my_style', 'w') as config:
                        config.write(open('style_configuration/my_style', 'r').read())

                    self.storage = True
                except Exception:
                    self.storage = False

            elif os.path.isdir(way) == True:
                try:
                    self.configuration_screen['my_style'] = open(f'{way}/my_style', 'r').read().split()
                    self.storage = True
                except Exception:
                    self.storage = False


    def link(self):
        webbrowser.open(self.open)

    def welcom_to_hell_activity(self, action=None):
        if action == 'hell':
            self.screen.ids.title.font_size = 95

            if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                if self.title == None:
                    self.screen.ids.title.text = f"[color=#fedcff]Dangerously[/color]"
                else:
                    self.screen.ids.title.text = f"[color={self.title}]Dangerously[/color]"
            else:
                self.screen.ids.title.text = f"[color=#fedcff]Dangerously[/color]"

            self.screen.ids.button_attack_cancel.text = 'Death awaits you'

            Animation(welcome_to_hell=0.5, duration=1.0).start(self.screen.ids.button_attack_cancel)
            Animation(what_button_anim=6.0, duration=3.0).start(self.screen.ids.what_button)
            Animation(menu_button_anim=-6.0, duration=3.0).start(self.screen.ids.menu_button)


        elif action == 'cancel':
            self.screen.ids.title.font_size = 120

            if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                if self.title == None:
                    self.screen.ids.title.text = f"[color=#fedcff]Antichrist[/color]"
                else:
                    self.screen.ids.title.text = f"[color={self.title}]Antichrist[/color]"
            else:
                self.screen.ids.title.text = f"[color=#fedcff]Antichrist[/color]"

            self.screen.ids.button_attack_cancel.text = 'Attack'

            Animation(welcome_to_hell=0.3, duration=1.0).start(self.screen.ids.button_attack_cancel)
            Animation(what_button_anim=0.8, duration=2.0).start(self.screen.ids.what_button)
            Animation(menu_button_anim=0.2, duration=2.0).start(self.screen.ids.menu_button)


    def target_666(self):
        self.hell666_status = None
        while self.target_status_666:
            time.sleep(0.5)
            if self.screen.ids.target.text == '666':
                if self.hell666_status == True:
                    pass
                else:
                    self.welcom_to_hell_activity(action='hell')
                    self.hell666_status = True
            else:
                if self.hell666_status == True:
                    self.welcom_to_hell_activity(action='cancel')
                    self.hell666_status = False

    def left_to_live(self, date):
        if date == 'hours':
            while self.you_dead_status:
                time.sleep(self.dead_time['hour'])
                data_dead['hours']=data_dead['hours'] - 1

        elif date == 'minutes':
            while self.you_dead_status:
                time.sleep(self.dead_time['minute'])
                if data_dead['minutes'] == 0:
                    data_dead['hours']=data_dead['hours'] - 1
                    data_dead['minutes']=data_dead['minutes'] = 60

                data_dead['minutes']=data_dead['minutes'] - 1

        elif date == 'sec':
            while self.you_dead_status:
                time.sleep(self.dead_time['sec'])
                if data_dead['sec'] == 0:
                    if data_dead['minutes'] == 0:
                        if data_dead['hours'] == 0:
                            break;self.you_dead_status=False
                        data_dead['hours']=data_dead['hours'] - 1
                        data_dead['minutes']=data_dead['minutes'] = 60

                    data_dead['minutes']=data_dead['minutes'] - 1
                    data_dead['sec']=data_dead['sec'] = 60

                data_dead['sec']=data_dead['sec'] - 1

                self.label.text = f"[color=#cc235f]{data_dead['hours']}:{data_dead['minutes']}:{data_dead['sec']}[/color]"

    def you_dead(self):
        self.you_dead_status = True
        threading.Thread(target=self.left_to_live, args=('sec',)).start()
        threading.Thread(target=self.left_to_live, args=('minutes',)).start()
        threading.Thread(target=self.left_to_live, args=('hours',)).start()

    def start_link(self, timer):
        time.sleep(timer)

        while self.link_th:
            new_text=ads()
            self.open='http://'+new_text[new_text.rfind(':')+2:]

            if self.link_th == False:
                break

            time.sleep(6);Animation(center_y_1=-2, duration=2).start(self.links)
            if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                self.links.text = f'[color={self.link_tg_color}]'+str(new_text)+'[/color]'

            else:
                self.links.text = f'[color=#fedcff]'+str(new_text)+'[/color]'

            time.sleep(9);Animation(center_y_1=0.2, duration=2).start(self.links)


    def hell_666(self):
        self.click += 1

        if self.click > 13:
            if self.click == 66:
                self.link_th = False
                
                with open('style_configuration/special_abilities', 'w') as special_abilities:
                    special_abilities.write('True')

                self.status = False
                self.link_th = False
                self.target_status_666 = False
                sys.exit(1)

            toast(f'{66-self.click}')

    def bufer(self, bufer=None, widget=None):
        if self.configuration_screen['special_abilities'] == ['False']:
            if self.configuration_screen['hell'] in [['False'],['None']]:
                self.hell_666()

        if self.screen.ids.target.text.lower() == 'antichrist':
            widget.text = 'I love you!'

        if bufer == True:
            phone=''
            for xxx in re.findall(r"[0-9]+", Clipboard.paste()):
                phone+=xxx
            phone='+'+phone

            try:
                if isinstance(int(phone[1:]), int):
                    if widget.text == '':
                        if len(phone) > 6:
                            widget.text = phone
            except Exception:
                pass


    def label_threading(self, timer):
        time.sleep(timer)
        toast('Clear')
        self.label.text = ' '

    def modes(self, mode_widget=None):
        if mode_widget.text == 'Ultra':
            toast('Mode: Light')
            mode_widget.text = 'Light'
            self.mode = 'Light'

        elif mode_widget.text == 'Light':
            toast('Mode: Hard')
            mode_widget.text = 'Hard'
            self.mode = 'Hard'

        elif mode_widget.text == 'Hard':
            toast('Mode: Ultra')
            mode_widget.text = 'Ultra'
            self.mode = 'Ultra'

    def whats(self, what_widget=None):
        if what_widget.text == 'Mix':
            toast('Only Call')
            what_widget.text = 'Call'
            self.what = 'Call'

        elif what_widget.text == 'Call':
            toast('Only SMS')
            what_widget.text = 'SMS'
            self.what = 'SMS'

        elif what_widget.text == 'SMS':
            toast('All inclusive')
            what_widget.text = 'Mix'
            self.what = 'Mix'

    def threding_attack_ultra(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    x_count += 4
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"

                        threading.Thread(target=send_message_next).start()
                        x_count += 1

                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"

                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"

                        threading.Thread(target=send_message_next).start()
                        x_count += 1

                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"

                except Exception:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'Call':
            while self.status:
                try:
                    self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    threading.Thread(target=send_call).start()
                    x_count += 1
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    time.sleep(0.5)
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'SMS':
            while self.status:
                try:
                    threading.Thread(target=send_message, args=(True, )).start()
                    threading.Thread(target=send_message, args=(True, )).start()
                    threading.Thread(target=send_message, args=(True, )).start()
                    threading.Thread(target=send_message, args=(True, )).start()
                    x_count += 4

                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"

                        threading.Thread(target=send_message_next, args=(True, )).start()
                        x_count += 1
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"

                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                        threading.Thread(target=send_message_next, args=(True, )).start()
                        x_count += 1
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"

                except Exception:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

    def threding_attack_hard(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    threading.Thread(target=send_message).start()
                    threading.Thread(target=send_message).start()
                    x_count += 2
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'Call':
            while self.status:
                try:
                    threading.Thread(target=send_call).start()
                    x_count += 1
                    time.sleep(3)
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'SMS':
            while self.status:
                try:
                    threading.Thread(target=send_message, args=(True, )).start()
                    threading.Thread(target=send_message, args=(True, )).start()
                    x_count += 2
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"


    def threding_attack_light(self):
        x_count = 0
        if self.what == 'Mix':
            while self.status:
                try:
                    threading.Thread(target=send_message_next).start()
                    time.sleep(0.6)
                    x_count += 1
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    time.sleep(0.9)
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'Call':
            while self.status:
                try:
                    threading.Thread(target=send_call).start()
                    x_count += 1
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    time.sleep(6)
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"

        elif self.what == 'SMS':
            while self.status:
                try:
                    threading.Thread(target=send_message_next, args=(True,)).start()
                    time.sleep(0.6)
                    x_count += 1
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]{str(x_count)}[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]{str(x_count)}[/color]"
                    time.sleep(0.9)
                except Exception as e:
                    if [self.configuration_screen['my_style'][0], self.storage] == ['True', True]:
                        self.label.text = f"[color={self.queries_color}]ERROR[/color]"
                    else:
                        self.label.text = f"[color=#fdb3ff]ERROR[/color]"


    def attack(self, attack=None):
        self.button_attack_cancel = self.screen.ids.button_attack_cancel
        if self.button_attack_cancel.text == 'Attack':
            try:
                if isinstance(int(attack.text[1:]), int):
                    toast('Start spam-attack!')
                    if self.mode == 'Ultra':
                        self.button_attack_cancel.text = 'Stop'
                        self.status = True
                        self.target = attack.text
                        self.attack_number_phone.phone(self.target)
                        self.thred_z=threading.Thread(target=self.threding_attack_ultra)
                        self.thred_z.start()

                    elif self.mode == 'Hard':
                        self.button_attack_cancel.text = 'Stop'
                        self.status = True
                        self.target = attack.text
                        self.attack_number_phone.phone(self.target)
                        self.thred_z=threading.Thread(target=self.threding_attack_hard)
                        self.thred_z.start()

                    elif self.mode == 'Light':
                        self.button_attack_cancel.text = 'Stop'
                        self.status = True
                        self.target = attack.text
                        self.attack_number_phone.phone(self.target)
                        self.thred_z=threading.Thread(target=self.threding_attack_light)
                        self.thred_z.start()
            except Exception:
                pass

        elif self.button_attack_cancel.text == 'Stop':
            toast('Stop spam-attack!')
            self.button_attack_cancel.text = 'Attack'
            self.status = False
            threading.Thread(target=self.label_threading, args=(10, )).start()
            self.button_attack_cancel.text = 'Attack'

        elif self.button_attack_cancel.text == 'Death awaits you':
            with open('style_configuration/hell', 'w') as death:
                self.status = False
                self.link_th = False
                self.target_status_666 = False
                death.write('True')

            sys.exit(1)

    def build(self):
        return self.screen

if __name__ == '__main__':
    AntichristApp().run()
