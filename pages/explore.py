import PySimpleGUI as sg
import public
import os, sys

sg.set_options(font=public.MONO_FONT)

def explore():
    initial_directory = 'C:/autostart'

    # Define the layout of the window
    layout = [[sg.Text("Current Directory", size=(20, 1), justification='center'),
            sg.Input(key='-DIRECTORY-', enable_events=True, default_text=initial_directory ),
            sg.FolderBrowse(button_text='Browse 🔍', target='-DIRECTORY-'), sg.Button('Cancel ✘', key = '-BUTTON1-')],
            [sg.Listbox(values=[".."], size=(3, 20), key='-DIRECTORIES-' , expand_x=True, expand_y=True, enable_events=True),
            sg.Listbox(values=[], size=(5, 20), expand_x=True, expand_y=True, key='-FILES-', enable_events=True),
            sg.Multiline(size=(67, 20), expand_x=True, expand_y=True, key='-CONTENTS-', disabled=True)]]

    # Create the window
    window = sg.Window("File Explorer", layout, font=public.MONO_FONT, size=(900, 500), resizable=True, finalize=True)
    try:
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON1-':
                break

            current_directory = values['-DIRECTORY-']

            # Update the directory list
            directories = ['..'] + [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]
            window['-DIRECTORIES-'].update(directories)

            # Update the file list (excluding .ico files)
            files = [name for name in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, name)) and not name.lower().endswith('.ico') and not name.lower().endswith('.txt')]
            window['-FILES-'].update(files)

            # Show the contents of the selected directory
            if event == '-DIRECTORIES-' and values['-DIRECTORIES-']:
                selected_directory = values['-DIRECTORIES-'][0]
                if selected_directory == '..':
                    current_directory = os.path.dirname(current_directory)
                else:
                    current_directory = os.path.join(current_directory, selected_directory)

                window['-DIRECTORY-'].update(current_directory)

                # Update the directory list for the selected directory
                directories = ['..'] + [name for name in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, name))]
                window['-DIRECTORIES-'].update(directories)

                # Update the file list for the selected directory (excluding .ico files)
                files = [name for name in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, name)) and not name.lower().endswith('.ico') and not name.lower().endswith('.txt')]
                window['-FILES-'].update(files)

            # Show the contents of the selected file
            if event == '-FILES-' and values['-FILES-']:
                selected_file = values['-FILES-'][0]
                with open(os.path.join(current_directory, selected_file), 'r') as file:
                    file_contents = file.read()
                    window['-CONTENTS-'].update(file_contents)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")

    window.close()

