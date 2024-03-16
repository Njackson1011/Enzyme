import PySimpleGUI as sg
import public
import pages
import subprocess
import yaml
import json

def settings():

    global rmwin_path, language
    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\settings.json')
    languagedick = json.load(f)

    rmwin_path = config.get("rmwin")
    language = config.get('language')

    content_a = [[sg.Text('%s' % languagedick[0], font=('Algerian', '20'))]]
    content_s = [[sg.Text('•══════•°•〔⚙〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]]
    content_b = [[sg.Column([[sg.CB('⇐ %s' % languagedick[1], key="-1-")],
                 [sg.CB('⇐ %s' % languagedick[2], key="-2-")],
                 [sg.CB('⇐ %s' % languagedick[3], key="-3-")],
                 [sg.CB('⇐ %s' % languagedick[4], key="-4-")],
                 [sg.CB('⇐ %s' % languagedick[5], key="-5-")],
                 [sg.CB('⇐ %s' % languagedick[6], key="-6-")],
                 [sg.CB('⇐ %s' % languagedick[7], key="-7-")]])]] 
    content_s1 = [[sg.Text('•══════•°•〔⚙〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]]
    content_c = [sg.Button('%s' % languagedick[8] + ' ✎', key='-BUTTON1-', bind_return_key=True), sg.Button('%s' % languagedick[9] + ' ✘', key='-BUTTON2-')]
    content_d = [[sg.Column([[sg.Button('%s' % languagedick[10] + '\n%s' % languagedick[11], key='-BUTTON3-', size=(16, 2)),
                              sg.Button('%s' % languagedick[12] + '\n%s' % languagedick[13], key='-BUTTON4-', size=(16, 2))]])]]
    content_s2 = [[sg.Text('•══════•°•〔⚙〕•°•══════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]]
    lang_selection_layout = [
                            [sg.Text('%s' % languagedick[14])],
                            [sg.Radio('English', 'LANG', key='en', default=languageChecker('en'))],
                            [sg.Radio('Español', 'LANG', key='es', default=languageChecker('es'))],
                            [sg.Button('%s' % languagedick[15], key = '-BUTTON5-', size=(10, 1))]]
    
    footer = [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    window = sg.Window('Enzyme Settings', layout= [content_a, content_s, lang_selection_layout, content_s1, content_b, content_c, content_s2, content_d, footer], size=(450, 725), element_justification='center', resizable=True, finalize=True)

    btnHandler = public.ButtonHandler(window)

    # Creates the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-BUTTON2-':
            break

        if event == '-BUTTON1-':
            selected_files = [key for key, value in values.items() if value and not key.startswith('e')]
            if selected_files:
                for file_key in selected_files:
                    file_path = get_file_path(file_key)
                    if file_path is not None:
                        subprocess.Popen(["notepad.exe", file_path])

        elif event == '-BUTTON3-':
            new_path = sg.popup_get_folder("Select Path")
            if new_path:
                config["rmwin"] = new_path
                with open(config_file_path, "w") as config_file:
                    yaml.dump(config, config_file)
                rmwin_path = new_path
                sg.popup('Settings saved', title='Success')

        elif event == '-BUTTON4-':
            pages.colors()
            window.close()

        elif event == '-BUTTON5-':
            if values['en'] == True:
                config["language"] = language = 'en'
            elif values['es'] == True:
                config["language"] = language = 'es'
                
            with open(config_file_path, "w") as config_file:
                    yaml.dump(config, config_file)
            sg.popup('Language set! \nUpdate requires restart', title='Success')
            window.close()

        btnHandler.handleColorChange(event)

    # Close the main window
    window.close()

def get_file_path(file_key):
    file_paths = {
        "-1-": "C:\\autostart\\batchfilehome\\StartDailyTasks.BAT",
        "-2-": "C:\\autostart\\batchfilehome\\StartDailyLockdown.BAT",
        "-3-": "C:\\autostart\\batchfilehome\\StartDailyLockdownwBackup.BAT",
        "-4-": "C:\\autostart\\batchfilehome\\DailyBackupConfigurable.BAT",
        "-5-": "C:\\autostart\\Greeting.txt",
        "-6-": "C:\\autostart\\batchfilehome\\ConfigureStation.BAT",
        "-7-": "C:\\autostart\\batchfilehome\\Reader Settings.txt",
    }
    return file_paths.get(file_key, None)

def languageChecker(lang):
    global language
    return language == lang