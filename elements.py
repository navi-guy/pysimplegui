#aquí irán Buttons, Column, Text, 
#Proponer elementos reutilizables

import PySimpleGUI as sg

#COLORS
AZUL_PRUSIA = '#1B2631'
BLANCO_DEFAULT = "#F7F7F7"

#MEDIDAS PIXELES
WIDTH_SIDE_BAR = 208
WIDTH_MAIN = 752

WIDTH_WINDOW = 960 #SIDEBAR + MAIN -no border ni pad
HEIGHT_WINDOW = 640

#MEDIDAS CARACTERES
WIDTH_SIDE_BAR_CHARS = (25,2)

# file path IMAGES
LOGO_IMAGE = './img/icon_left.png'
PANEL_CONTROL_BTN_IMAGE = './img/panel_control.png'
PANEL_CONTROL_BTN_PRESSED_IMAGE = './img/panel_control_pressed.png'
REPORTES_BTN_IMAGE = './img/ver_reportes.png'
REPORTES_BTN_PRESSED_IMAGE ='./img/ver_reportes_pressed.png'
CONFIGURACION_BTN_IMAGE ='./img/config.png'
CONFIGURACION_BTN_PRESSED_IMAGE = 'img/config_pressed.png'

#ELEMENTS
#COMMON BUTTON ELEMENTS 
panel_control = {   
        'key': '-CONTROL-',
        'file':  PANEL_CONTROL_BTN_IMAGE,
        'file_effect': PANEL_CONTROL_BTN_PRESSED_IMAGE,
        'main_key': '-CONTROL_MAIN-'    
        }
reportes = {
        'key': '-REPORTE-',
        'file':  REPORTES_BTN_IMAGE,
        'file_effect': REPORTES_BTN_PRESSED_IMAGE,
        'main_key': '-REPORTE_MAIN-'    
        }

salir = {
    'key': 'Salir',
    'file': None,
    'main_key': 'None'
}

#SIDEBAR
logo_element = sg.Image( background_color=AZUL_PRUSIA, 
                filename=LOGO_IMAGE,  size=(WIDTH_SIDE_BAR, 224))

default_text_element = sg.Text('', text_color='white',
                                background_color=AZUL_PRUSIA)

line_text_element = sg.Text('_'*28, text_color='white',
                                background_color=AZUL_PRUSIA)

btn_panel_control = sg.Button( image_filename=panel_control['file'],                
                key=panel_control['key'], border_width=0, pad=(0, 0) )

btn_reportes = sg.Button( image_filename=reportes['file'],
                key=reportes['key'], border_width=0, pad=(0, 0) )

default_text_element_long = sg.Text(size=(14,14), background_color=AZUL_PRUSIA)

btn_salir = sg.Button('Salir', size=(25,2),border_width=0, pad=(0, 0))

side_bar_elements = [[logo_element], [default_text_element],
                     [line_text_element], [btn_panel_control],
                     [btn_reportes],[default_text_element_long], [btn_salir]] #more buttons

side_bar =  sg.Column(side_bar_elements, background_color=AZUL_PRUSIA, 
                        size=(WIDTH_SIDE_BAR, HEIGHT_WINDOW))


#MAIN
text_row1_Control= sg.Text('PANEL DE CONTROL Row 1', text_color='black', background_color='white')
text_row2_Control= sg.Text('cPANEL DE CONTROL Row 2', text_color='black', background_color='white')
text_row3_Control= sg.Text('cPANEL DE CONTROL Row 3', text_color='black', background_color='white')

co2 = [[text_row1_Control], [text_row2_Control], [text_row3_Control]]

co2_reporte = [[sg.Text('REPORTE Row 1', text_color='black', background_color='white')],      
       [sg.Text('REPORTE Row 2', text_color='black', background_color='white')],      
       [sg.Text('REPORTE Row 3', text_color='black', background_color='white')]]

main_panel_control = sg.Column(co2, background_color=BLANCO_DEFAULT,
                        size=(WIDTH_MAIN, HEIGHT_WINDOW), 
                        key=panel_control['main_key'], visible = True)

main_ver_reporte =  sg.Column(co2_reporte, background_color=BLANCO_DEFAULT,
                        size=(WIDTH_MAIN, HEIGHT_WINDOW),
                        key=reportes['main_key'], visible = False) 


side_bar_buttons = [panel_control,reportes, salir]
