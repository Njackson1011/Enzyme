import PySimpleGUI as sg
import public
import os,sys
import subprocess

def rmwin():

    content2 = [[sg.Column([[sg.Button('⮚ RMStart 🔑 ⮘',  key='-BUTTON7-', size=(16,6)), sg.Button('⮚ RMWIN 🗄 ⮘', key='-BUTTON1-', size=(16,6), )],
                           [sg.Button('⮚ RMPOS 🖳 ⮘',  key='-BUTTON2-', size=(16,6)), sg.Button('⮚ RMSpool 🖶 ⮘',  key='-BUTTON3-', size=(16,6))],
                           [sg.Button('⮚ SplSetup ⚙ ⮘',  key='-BUTTON5-', size=(16,6)), sg.Button('⮚ Security 🔒 ⮘',  key='-BUTTON6-', size=(16,6))]])]]
    content3 = [[sg.Column([[sg.Button('Cancel ✘',  key='-BUTTON8-' )]])]],

    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Restaurant Manager', layout=[content2, content3, footer], size=(475,550), resizable=True, element_justification='center', finalize = True)
    
    btnHandler = public.ButtonHandler(window)
    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON8-':
                break
            elif event == '-BUTTON1-':
                subprocess.Popen(r"C:\\rmwin\\rmwin.exe", cwd=r"C:\\rmwin")
            elif event == '-BUTTON2-':
                subprocess.Popen(r"C:\\rmwin\\rmpos.exe", cwd=r"C:\\rmwin")
            elif event == '-BUTTON3-':               
                subprocess.Popen(r"C:\\rmwin\\rmspool.exe", cwd=r"C:\\rmwin")                              
            elif event == '-BUTTON5-':                
                subprocess.Popen(r"C:\\rmwin\\splsetup.exe", cwd=r"C:\\rmwin")                
            elif event == '-BUTTON6-':                
                subprocess.Popen(r"C:\\rmwin\\security.exe", cwd=r"C:\\rmwin")               
            elif event == '-BUTTON7-':                
                subprocess.Popen(r"C:\\rmwin\\rmstart.exe", cwd=r"C:\\rmwin")
                
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n\nYou must first extract your template for RM!")

        btnHandler.handleColorChange(event)

    # Close the main window
    window.close()