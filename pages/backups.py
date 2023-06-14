import PySimpleGUI as sg
import public
import os, sys

def backups():
    content1 = [[sg.Text('Enzyme Backups:', font=('Algerian', '20'))]],
    content_s = [[sg.Text('•══════•°•〔📁〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#45ADA8'  )]],
    content2 = [[sg.Column([[sg.Button('⮚ Backup Enzyme Files ⮘', key='-BUTTON1-', size=public.LARGE_BUTTON_SIZE, )],
                           [sg.Button('⮚ Backup Personal Files ⮘',  key='-BUTTON2-', size=public.LARGE_BUTTON_SIZE, )],
                           [sg.Button('⮚ DFB for Enzyme ⮘',  key='-BUTTON3-', size=public.LARGE_BUTTON_SIZE, )],
                           [sg.Button('⮚ Run All Backups ⮘',  key='-BUTTON4-', size=public.LARGE_BUTTON_SIZE, )]])]]
    content3 = [[sg.Column([[sg.Button('⮚ My Backups ⮘',  key='-BUTTON5-', size=(20,6) )]])]]
    content4 = [[sg.Column([[sg.Button('Cancel ✘',  key='-BUTTON6-')]])]],

    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Enzyme Backups', layout=[content1, content_s, content2, content3, content4, footer], size=(500,685), resizable=True, element_justification='center', finalize = True)
    
    btnHandler = public.ButtonHandler(window)
    try:
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON6-':
                break
            elif event == '-BUTTON1-':
                os.startfile("C:\\autostart\\batchfilehome\\BatchFileBackup.exe")
            elif event == '-BUTTON2-':
                os.startfile("C:\\autostart\\batchfilehome\\DailyBackup(Configurable).bat")
            elif event == '-BUTTON3-':
                os.startfile("C:\\autostart\\batchfilehome\\DFBforEnzyme.exe")
            elif event == '-BUTTON4-':
                os.startfile("C:\\autostart\\batchfilehome\\CustomBackupFile.exe")
            elif event == '-BUTTON5-':
                os.startfile("G:\\My Drive")

            btnHandler.handleColorChange(event)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")

    window.close()