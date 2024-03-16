import PySimpleGUI as sg
import public
import os, sys
import yaml
import json

def backups():

    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\backups.json')
    languagedick = json.load(f)

    content1 = [[sg.Text('%s' % languagedick[0], font=('Algerian', '20'))]],
    content_s = [[sg.Text('•══════•°•〔📁〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]],
    content2 = [[sg.Column([[sg.Button('⮚ %s' % languagedick[1] + ' ⮘', key='-BUTTON1-', size=public.LARGE_BUTTON_SIZE, )],
                            [sg.Button('⮚ %s' % languagedick[2] + ' ⮘',  key='-BUTTON2-', size=public.LARGE_BUTTON_SIZE, )],
                            [sg.Button('⮚ %s' % languagedick[3] + ' ⮘',  key='-BUTTON3-', size=public.LARGE_BUTTON_SIZE, )],
                            [sg.Button('⮚ %s' % languagedick[4] + ' ⮘',  key='-BUTTON4-', size=public.LARGE_BUTTON_SIZE, )]])]]
    content3 = [[sg.Column([[sg.Button('⮚ %s' % languagedick[5] + ' 📁',  key='-BUTTON5-', size=(15,3) )]]), sg.Button('⮚ %s' % languagedick[6] + ' 📁',  key='-BUTTON7-', size=(15,3))]]
    content4 = [[sg.Column([[sg.Button('%s' % languagedick[7] + ' ✘',  key='-BUTTON6-')]])]],

    footer = [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    window = sg.Window('%s' % languagedick[8], layout=[content1, content_s, content2, content3, content4, footer], size=(500,615), resizable=True, element_justification='center', finalize = True)
    
    btnHandler = public.ButtonHandler(window)
    try:
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON6-':
                break
            elif event == '-BUTTON1-':
                os.startfile("C:\\autostart\\batchfilehome\\BatchFileBackup.exe")
            elif event == '-BUTTON2-':
                os.startfile("C:\\autostart\\batchfilehome\\DailyBackupConfigurable.bat")
            elif event == '-BUTTON3-':
                os.startfile("C:\\autostart\\batchfilehome\\DFBforEnzyme.exe")
            elif event == '-BUTTON4-':
                os.startfile("C:\\autostart\\batchfilehome\\CustomBackupFile.exe")
            elif event == '-BUTTON5-':
                os.startfile("G:\\My Drive")
            elif event == '-BUTTON7-':
                os.startfile("C:\\autostart\\DailyFileBackup")

            btnHandler.handleColorChange(event)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")

    window.close()