import PySimpleGUI as sg
from elements import *

side_bar_state = "-CONTROL-"

layout = [[ side_bar, main_panel_control, main_ver_reporte ]]  

window = sg.Window('Nayade', layout, size= (WIDTH_WINDOW,HEIGHT_WINDOW),
                   margins=(0, 0), element_padding=((0, 0),(0,0)))


while True:
    event, values = window.read()

    if event in ('Salir', None):
        break;
        
    else:
        print ('Estado anterior:{}'.format(side_bar_state))
        print ('Evento:{}'.format(event))
        for btn in side_bar_buttons:
            if event == btn['key']:
                side_bar_state = btn['key']
                no_focus_btns = list(filter(lambda i: i['key'] != event,
                                    side_bar_buttons)) #remove btn selected
                #add efects SELECTED 
                print('BTN1:{}'.format(btn))
                window.FindElement(btn['key']).update(
                                            image_filename=btn['file_effect'])
                window.FindElement(btn['main_key']).update(visible=True)

        #quitar effectos OTHERS     
        for btn in no_focus_btns:
            if btn['key']=='Salir':
                pass
            else:
                print(btn)
                window.FindElement(btn['key']).update(
                                                    image_filename=btn['file'])
                window.FindElement(btn['main_key']).update(visible=False)
        print ('Estado actual:{}'.format(side_bar_state))

window.close()
