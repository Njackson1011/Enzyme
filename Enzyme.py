import PySimpleGUI as sg
import os
import pages
import public

#When building the .exe after changes ensure that
#1. You are in an adminsitrative windows cmd.
#2. You are within the root directory for the Enzyme Project folder
#3. use this code [pyinstaller --icon="public\images\iconenzymecover.ico" --noconsole --onefile --hidden-import=PySimpleGUI,json,os,sys,subprocess Enzyme.py]

sg.LOOK_AND_FEEL_TABLE['Hakke'] = public.HAKKE_CSS
sg.theme('Hakke')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
sg.set_options(font=public.HEADER_FONT)
sg.set_options(icon="./public/images/iconenzymecover.ICO")

def main():

    # Define main window layout
    page_content = [[sg.Column([[sg.Button('🔑  Start my Shift', key='-BUTTON1-', size=(37,3))],
                           [sg.Button('📖  Explore Enzyme', key='-BUTTON2-', size=(37,3))],
                           [sg.Button('📁  My Backups', key='-BUTTON3-', size=(37,3))],
                           [sg.Button('🔍  Search Files', key='-BUTTON4-', size=(37,3))],
                           [sg.Button('🧪  Test RMWIN', key='-BUTTON5-', size=(37,3))],
                           [sg.Button('🔒  End my Shift', key='-BUTTON6-', size=(37,3))]])]]
    
    help_content = [sg.Button('❓', key='-help-', size=(2,1), button_color='dark gray', tooltip="Opens Application Help File"),
                    sg.Button('✔', key='-info-', size=(2,1), button_color='dark gray', tooltip="Opens Version Info File"),  
                    sg.Button('✨', key='-boogie-', size=(2,1), button_color='dark gray', tooltip="10 Seconds of Fun"),
                    sg.Button('⍩⃝', key='-pac-', size=(2,1), button_color='dark gray', tooltip="waka-waka-waka"),  
                    sg.Button('⚙', key='-config-', size=(2,1), button_color="dark gray", tooltip="Enzyme File Settings")]
    
    footer_a = [sg.Text(("Enzyme © 2022-2023 Designed and Supported by Victor A Gurganus"), font=public.FOOTER_FONT)]
    footer_b = [sg.Text(("Enzyme App © 2023 Coded by Nicholas J Jackson"), font=public.FOOTER_FONT)]

    # Create the main window
    window = sg.Window('Enzyme', layout = [page_content, help_content, footer_a, footer_b], size=(550,640), resizable=True, element_justification='center', finalize = True)

    btnHandler = public.ButtonHandler(window)

    # Create an event loop
    while True:
        event, values = window.read()
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
            pages.eod()
        elif event == '-help-':
            os.startfile("C:\\autostart\\batchfilehome\\EXEINFO.exe")
        elif event == '-info-':
            os.startfile("C:\\autostart\\batchfilehome\\INFO.exe")
        elif event == '-boogie-':
            os.startfile("C:\\autostart\\batchfilehome\\EnzymeRGBLoad.exe")
        elif event == '-pac-':
            os.startfile("C:\\autostart\\batchfilehome\\EnzymeRGBPac.exe")
        elif event == '-config-':
            pages.settings() 
        

        btnHandler.handleColorChange(event)
    # Close the main window
    window.close()

if __name__ == '__main__':
    main()