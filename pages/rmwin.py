import PySimpleGUI as sg
import public
import pages
import os, sys
import subprocess
import yaml
import json

def rmwin():

    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\rmwin.json')
    languagedick = json.load(f)

    # Read the config.yml file
    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)

    rmwin_path = config.get("rmwin")

    content1 = [[sg.Text('Test RMWIN', font=('Algerian', '20'))]]
    content_s = [[sg.Text('•══════•°•〔🧪〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]]
    content2 = [[sg.Column([[sg.Button('⮚ RMStart 🔑 ⮘',  key='-BUTTON6-', size=(16,4)), sg.Button('⮚ RMWIN 🗄 ⮘', key='-BUTTON1-', size=(16,4))],
                           [sg.Button('⮚ RMPOS 🖳 ⮘',  key='-BUTTON2-', size=(16,4)), sg.Button('⮚ RMSpool 🖶 ⮘',  key='-BUTTON3-', size=(16,4))],
                           [sg.Button('⮚ RMReports 📰 ⮘',  key='-BUTTON4-', size=(16,4)), sg.Button('⮚ Security 🔒 ⮘',  key='-BUTTON5-', size=(16,4))]])]]
    content3 = [[sg.Column([[sg.Button('%s' % languagedick[0] + ' ✘',  key='-BUTTON7-'), sg.Button('⚙', key='-config-', button_color="dark gray", size=(2,1), tooltip="%s" % languagedick[1])]])]]

    footer = [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    window = sg.Window('Restaurant Manager', layout=[content1, content_s, content2, content3, footer], size=(475,505), resizable=True, element_justification='center', finalize=True)

    btnHandler = public.ButtonHandler(window)
    while True:
        try:
            with open(config_file_path, "r") as config_file:
                config = yaml.safe_load(config_file)
            event, values = window.read()

            rmwin_path = config.get("rmwin")

            if event == sg.WIN_CLOSED or event == '-BUTTON7-':
                break
            elif event == '-BUTTON1-':
                subprocess.Popen(os.path.join(rmwin_path, "rmwin.exe"), cwd=rmwin_path)
            elif event == '-BUTTON2-':
                subprocess.Popen(os.path.join(rmwin_path, "rmpos.exe"), cwd=rmwin_path)
            elif event == '-BUTTON3-':
                subprocess.Popen(os.path.join(rmwin_path, "rmspool.exe"), cwd=rmwin_path)
            elif event == '-BUTTON4-':
                subprocess.Popen(os.path.join(rmwin_path, "rmreports.exe"), cwd=rmwin_path)
            elif event == '-BUTTON5-':
                subprocess.Popen(os.path.join(rmwin_path, "security.exe"), cwd=rmwin_path)
            elif event == '-BUTTON6-':
                subprocess.Popen(os.path.join(rmwin_path, "rmstart.exe"), cwd=rmwin_path)
            elif event == '-config-':
                pages.settings() 
                

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[3]
            sg.popup_error(f'%s' % languagedick[1] + ' {rmwin_path}')

        btnHandler.handleColorChange(event)

    # Close the main window
    window.close()