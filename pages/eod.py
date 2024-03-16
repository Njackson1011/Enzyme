import PySimpleGUI as sg
import public
import pages
import os, sys
import yaml
import json

def eod():

    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\eod.json')
    languagedick = json.load(f)

    content = [[sg.Text('%s' % languagedick[0], font=('Algerian', '20'))]],
    content_s = [[sg.Text('•════════•°•〔🔒〕•°•════════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]],
    content1 = [[sg.Column([[sg.Button('%s' % languagedick[1] + ' 🔒', key='-BUTTON1-', size=(42,4))],
                           [sg.Button('%s' % languagedick[2] + ' 🔒', key='-BUTTON2-', size=(42,4))]])]]
    content2 = [[sg.Column([[sg.Button('%s' % languagedick[3] + ' ✘', key='-BUTTON3-')]]), sg.Button('⚙', key='-config-', size=(2,1), button_color="dark gray", tooltip="%s" % languagedick[4])]]
    footer = [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    window = sg.Window('%s' % languagedick[5], layout = [content, content_s, content1, content2, footer], size=(575,390), resizable=True, element_justification='center', finalize = True)

    btnHandler = public.ButtonHandler(window)
    
    try:
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON3-':
                break
            elif event == '-BUTTON1-':
                os.startfile("C:\\autostart\\batchfilehome\\StartDailyLockdown.bat")
            elif event == '-BUTTON2-':
                os.startfile("C:\\autostart\\batchfilehome\\StartDailyLockdownWBackup.bat")
            elif event == '-config-':
                pages.settings() 

            btnHandler.handleColorChange(event)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")

    window.close()