import PySimpleGUI as sg
import public
import subprocess

def settings():

    content_a = [[sg.Text('Select file to modify:')]],
    content_b = [[sg.Column([[sg.CB('⇐StartDailyTasks', key="-1-")],
                 [sg.CB('⇐StartDailyLockdown', key="-2-")],
                 [sg.CB('⇐StartDailyLockdownwBackup', key="-3-")],
                 [sg.CB('⇐DailyBackup(Configurable)', key="-4-")],
                 [sg.CB('⇐Reader Settings', key="-5-")]])]] 
    content_c = [sg.Button('Edit ✎', key='-BUTTON1-', bind_return_key=True), sg.Button('Cancel ✘', key='-BUTTON2-')],
    footer = [sg.Text(("Enzyme © 2022-2023"), font=public.FOOTER_FONT)]

    window = sg.Window('Enzyme Settings', layout= [content_a, content_b, content_c, footer], size=(450, 300), element_justification='center', finalize=True)

    btnHandler = public.ButtonHandler(window)

    # Creates the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-BUTTON2-':
            break

        if event == '-BUTTON1-':
            selected_files = [key for key, value in values.items() if value]
            if selected_files:
                for file_key in selected_files:
                    file_path = get_file_path(file_key)
                    subprocess.Popen(["notepad.exe", file_path])
            else: 
                sg.popup_error("No file selected")

            btnHandler.handleColorChange(event)

    # Close the main window
    window.close()

def get_file_path(file_key):
    file_paths = {
        "-1-": "C:\\autostart\\batchfilehome\\StartDailyTasks.BAT",
        "-2-": "C:\\autostart\\batchfilehome\\StartDailyLockdown.BAT",
        "-3-": "C:\\autostart\\batchfilehome\\StartDailyLockdownwBackup.BAT",
        "-4-": "C:\\autostart\\batchfilehome\\DailyBackup(Configurable).BAT",
        "-5-": "C:\\autostart\\batchfilehome\\Reader Settings.txt",
    }
    return file_paths.get(file_key)