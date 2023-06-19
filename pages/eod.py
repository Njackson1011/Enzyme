import PySimpleGUI as sg
import public
import pages
import os, sys

def eod():
<<<<<<< HEAD
    content = [[sg.Text('End of Day', font=('Algerian', '20'))]],
    content_s = [[sg.Text('•════════•°•〔🔒〕•°•════════•', font=('Algerian', '14', 'bold'), text_color='#45ADA8'  )]],
    content1 = [[sg.Column([[sg.Button('Lockdown my PC 🔒', key='-BUTTON1-', size=(42,4))],
                           [sg.Button('Backup and Lockdown my PC 🔒', key='-BUTTON2-', size=(42,4))]])]]
    content2 = [[sg.Column([[sg.Button('Cancel ✘', key='-BUTTON3-')]]), sg.Button('⚙', key='-config-', size=(2,1), button_color="dark gray", tooltip="Enzyme File Settings")]]
    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Enzyme', layout = [content, content_s, content1, content2, footer], size=(575,390), resizable=True, element_justification='center', finalize = True)
=======
    content = [[sg.Column([[sg.Button('Lockdown my PC 🔒', key='-BUTTON1-', size=(42,4))],
                           [sg.Button('Backup and Lockdown my PC 🔒', key='-BUTTON2-', size=(42,4))]])]]
    content2 = [[sg.Column([[sg.Button('Cancel ✘', key='-BUTTON3-')]])]]
    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Enzyme', layout = [content, content2, footer], size=(575,320), resizable=True, element_justification='center', finalize = True)
>>>>>>> 88831cb7e028b98a7974326effaec5f81cee6456

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