import PySimpleGUI as sg
import os
import pages
import public
import yaml
import json
from datetime import datetime
import pyautogui

#When building the .exe after changes ensure that
#1. You are in an adminsitrative windows cmd.
#2. You are within the root directory for the Enzyme Project folder
#3. use this code [pyinstaller --icon="public\images\iconenzymecover.ico" --noconsole --onefile --hidden-import=PySimpleGUI,json,os,sys,subprocess,yaml Enzyme.py]

config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
with open(config_file_path, "r") as language_file:
    config = yaml.safe_load(language_file)
    f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\enzyme.json')
languagedick = json.load(f)

with open(config_file_path, "r") as theme:
    config = yaml.safe_load(theme)
    fart = config.get("theme")
theme_mapping = public.theme_mapping
selected_theme = theme_mapping.get(fart)
sg.LOOK_AND_FEEL_TABLE[fart] = selected_theme

sg.theme(fart)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
sg.set_options(font=public.HEADER_FONT)
sg.set_options(icon="./public/images/iconenzymecover.ICO")

def contentbuilder():
    # Define main window layout
    clock = [[sg.Text(datetime.now().strftime('%H:%M:%S'), key='-CLOCK-')]]

    page_content = [[sg.Column([[sg.Button('🔑  %s'% languagedick[0], key='-BUTTON1-', size=(37,3))],
                        [sg.Button('📖  %s' % languagedick[1], key='-BUTTON2-', size=(37,3))],
                        [sg.Button('📁  %s' % languagedick[2], key='-BUTTON3-', size=(37,3))],
                        [sg.Button('🔍  %s' % languagedick[3], key='-BUTTON4-', size=(37,3))],
                        [sg.Button('🧪  %s' % languagedick[4], key='-BUTTON5-', size=(37,3))],
                        [sg.Button('⍩⃝  %s' % languagedick[5], key='-BUTTON6-', size=(37,3))],
                        [sg.Button('🔒  %s' % languagedick[6], key='-BUTTON7-', size=(37,3))]])]]
    
    help_content = [sg.Button('❓', key='-help-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[7]),
                    sg.Button('✔', key='-info-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[8]),  
                    sg.Button('✂️', key='-snip-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[9]),
                    sg.Button('⍩⃝', key='-pac-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[10]),
                    sg.Button('➕', key='-ticket-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[11]),
                    sg.Button('⚙', key='-config-', size=(2,1), button_color='dark gray', tooltip='%s' % languagedick[12])]
    
    footer_a = [sg.Text(('Enzyme © 2022-2024 %s' % languagedick[13]), font=public.FOOTER_FONT, text_color='#FFFFFF')]
    footer_b = [sg.Text(('Enzyme App © 2023-2024 %s' % languagedick[14]), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    return [page_content, help_content, clock, footer_a, footer_b]


def main():
    with open(config_file_path, "r") as theme_file:
        config = yaml.safe_load(theme_file)
        fart = config.get("theme")
        theme_mapping = public.theme_mapping
        selected_theme = theme_mapping.get(fart)
    # Create the main window
    window = sg.Window('Enzyme', layout = contentbuilder(), size=(550,740), resizable=True, element_justification='center', finalize=True)

    btnHandler = public.ButtonHandler(window, selected_theme)

    # Create an event loop
    while True:
        event, values = window.read(timeout=1000)
        if event == sg.WIN_CLOSED:
            break
        elif event == '-BUTTON1-':
            os.startfile("C:\\autostart\\batchfilehome\\StartDailyTasks.bat")
        elif event == '-BUTTON2-':
            pages.explore()
        elif event == '-BUTTON3-':
            pages.backups()
        elif event == '-BUTTON4-':
            pages.search()
        elif event == '-BUTTON5-':
            pages.rmwin() 
        elif event == '-BUTTON6-':
            pages.pacman()
        elif event == '-BUTTON7-':
            pages.eod()
        elif event == '-help-':
            os.startfile("C:\\autostart\\batchfilehome\\EXEINFO.exe")
        elif event == '-info-':
            os.startfile("C:\\autostart\\batchfilehome\\INFO.exe")
        elif event == '-snip-':
            os.startfile("C:\\autostart\\SnippingTool.lnk")
            pyautogui.sleep(.5)
            pyautogui.hotkey('ctrl', 'n')
        elif event == '-pac-':
            os.startfile("C:\\autostart\\batchfilehome\\EnzymeRGBPac.exe")
        elif event == '-ticket-':
            os.startfile("C:\\autostart\\batchfilehome\\NewTicket.exe")
        elif event == '-config-':
            pages.settings()

            with open(config_file_path, "r") as theme:
                config = yaml.safe_load(theme)
                fart = config.get("theme")
            theme_mapping = public.theme_mapping
            selected_theme = theme_mapping.get(fart)
            sg.LOOK_AND_FEEL_TABLE[fart] = selected_theme
            sg.theme(fart) 

            layout = contentbuilder()  # Rebuild the layout to reflect theme changes
            window.close()  # Close the old window

            window = sg.Window('Enzyme', layout=layout, size=(550, 640), resizable=True, element_justification='center', finalize=True)  # Create a new window with updated layout
            btnHandler = public.ButtonHandler(window, selected_theme)
        
        btnHandler.handleColorChange(event)
    # Close the main window
    window.close()

if __name__ == '__main__':
    main()