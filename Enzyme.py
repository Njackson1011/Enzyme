import PySimpleGUI as sg
import os
import pages
import public

#When building the .exe after changes ensure that
#1. You are in an adminsitrative cmd.
#2. You are within the root directory for the Enzyme Project folder
#3. use this code [pyinstaller --icon="public\images\tiredanddepressed.ico" --noconsole --onefile --hidden-import=PySimpleGUI,json,os,sys,subprocess Enzyme.py]

sg.LOOK_AND_FEEL_TABLE['Hakke'] = public.HAKKE_CSS
sg.theme('Hakke')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
sg.set_options(font=public.HEADER_FONT)
sg.set_options(icon="./public/images/iconenzymecover.ICO")

def main():

    # Define main window layout    
    page_content = [[sg.Column([[sg.Button('🔑  Start my Shift', key='-BUTTON1-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('📖  Explore Enzyme', key='-BUTTON2-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('📁  My Backups', key='-BUTTON3-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('🔍  Search Files', key='-BUTTON4-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('🧪  Test RMWIN', key='-BUTTON5-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('🔒  End my Shift', key='-BUTTON6-', size=public.LARGE_BUTTON_SIZE)]])]]
    
    footer_a = [sg.Text(("Enzyme © 2022-2023 Designed and Supported by Victor A Gurganus"), font=public.FOOTER_FONT)]
    footer_b = [sg.Text(("Enzyme App © 2023 Coded by Nicholas J Jackson"), font=public.FOOTER_FONT)]

    help_content = [sg.Button('❓', key='-BUTTON7-', size=(2,1)), sg.Button('✨', key='-BUTTON8-', size=(2,1)), sg.Button('⚙', key='-BUTTON9-', size=(2,1))]

    # Create the main window
    window = sg.Window('Enzyme', layout = [page_content, footer_a, footer_b, help_content], size=(575,760), resizable=True, element_justification='center', finalize = True)

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
        elif event == '-BUTTON7-':
            os.startfile("C:\\autostart\\batchfilehome\\INFO.bat")
        elif event == '-BUTTON8-':
            os.startfile("C:\\autostart\\batchfilehome\\EnzymeRGBLoad.bat")
        elif event == '-BUTTON9-':
            pages.settings() 

        btnHandler.handleColorChange(event)
    # Close the main window
    window.close()

if __name__ == '__main__':
    main()