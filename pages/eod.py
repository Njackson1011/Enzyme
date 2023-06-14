import PySimpleGUI as sg
import public 
import os, sys

def eod():
    content = [[sg.Column([[sg.Button('Lockdown my PC 🔒', key='-BUTTON1-', size=public.LARGE_BUTTON_SIZE)],
                           [sg.Button('Backup and Lockdown my PC 🔒', key='-BUTTON2-', size=public.LARGE_BUTTON_SIZE)]])]]
    content2 = [[sg.Column([[sg.Button('Cancel ✘', key='-BUTTON3-')]])]]
    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Enzyme', layout = [content, content2, footer], size=(380,280), resizable=True, element_justification='center', finalize = True)

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

            btnHandler.handleColorChange(event)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")

    window.close()