# Created by: David Wang
# Created on: 15-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit0-04
# This program displays Hello World international program

import ui

def english_touch_up_inside(sender):
    view['hello_world_label'].text = ('Hello, World!')
    
def french_touch_up_inside(sender):
    view['hello_world_label'].text = ('Bonjour le monde!')
    
def spanish_touch_up_inside(sender):
    view['hello_world_label'].text = ('Hola Mundo!')

view = ui.load_view()
view.present('full_screen')
