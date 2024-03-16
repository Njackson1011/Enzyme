import PySimpleGUI as sg
import public
import os, sys
import yaml
import json

sg.set_options(font=public.MONO_FONT)

def pacman():
    
    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\pacman.json')
    languagedick = json.load(f)

    initial_directory = 'C:/autostart/PacmanInfo'

    # Define the layout of the window
    layout = [[sg.Text("%s" % languagedick[0], size=(20, 1), justification='center'),
               sg.Input(key='-DIRECTORY-', enable_events=True, default_text=initial_directory ),
               sg.FolderBrowse(button_text='%s' % languagedick[1] + ' 🔍', target='-DIRECTORY-'), sg.Button('%s' % languagedick[2] + ' ✘', key = '-BUTTON1-')],
            [sg.Listbox(values=[], size=(5, 20), expand_x=True, expand_y=True, key='-FILES-', enable_events=True),
             sg.Multiline(size=(67, 20), expand_x=True, expand_y=True, key='-CONTENTS-', disabled=True)]]

    # Create the window
    window = sg.Window("%s" % languagedick[3], layout, font=public.MONO_FONT, size=(900, 500), resizable=True, finalize=True)
    
    btnHandler = public.ButtonHandler(window)
    
    try:
        current_directory = initial_directory
        files = [name for name in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, name)) and not name.lower().endswith('.ico') and not name.lower().endswith('.txt')]
        window['-FILES-'].update(files)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON1-':
                break

            btnHandler.handleColorChange(event)

            if event == '-DIRECTORY-' and values['-DIRECTORY-']:
                current_directory = values['-DIRECTORY-']
                
                try:
                    files = [name for name in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, name)) and not name.lower().endswith('.ico') and not name.lower().endswith('.txt')]
                    if len(files) == 0: 
                        raise ValueError
                    window['-FILES-'].update(files)
                    window['-CONTENTS-'].update("")
                except ValueError as e:
                    window['-CONTENTS-'].update("%s" % languagedick[4])
                    window['-FILES-'].update("")
                except Exception as e:
                    window['-CONTENTS-'].update("%s" % languagedick[5])
                    window['-FILES-'].update("")

            if event == '-FILES-' and values['-FILES-']:
                selected_file = values['-FILES-'][0]
                with open(os.path.join(current_directory, selected_file), 'r') as file:
                    file_contents = file.read()
                    window['-CONTENTS-'].update(file_contents)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n")
        
        btnHandler.handleColorChange(event)

    window.close()