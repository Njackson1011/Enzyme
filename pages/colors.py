import PySimpleGUI as sg
import public
import yaml
import json

def colors():
    global theme
    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\colors.json')
    languagedick = json.load(f)

    theme = config.get("theme")

    content = [[sg.Text('%s' % languagedick[0], font=('Algerian', '20'))]],
    content_s = [[sg.Text('•════════•°•〔🎨〕•°•════════•', font=('Algerian', '14', 'bold'), text_color='#FFFFFF')]],
    theme_selection_layout = [
                            [sg.Text('%s' % languagedick[1])],
                            [sg.Radio('Hakke', 'COLOR', key='HKE' )],
                            [sg.Radio('Sunflower', 'COLOR', key='SNFLWR')],
                            [sg.Radio('Bubblegum', 'COLOR', key='BBGM')],
                            [sg.Radio('Light Mode', 'COLOR', key='LM')],
                            [sg.Radio('Dark Mode', 'COLOR', key='DM')],
                            [sg.Radio('Redrock', 'COLOR', key='RR')],
                            [sg.Radio('Forest', 'COLOR', key='FRST')],
                            [sg.Radio('Tangerine', 'COLOR', key='TNGRN')],
                            [sg.Radio('Royal Purple', 'COLOR', key='RP')],
                            [sg.Radio('Bluebird', 'COLOR', key='BB')]]
    content2 = [[sg.Column([[sg.Button('%s' % languagedick[2] + ' ✔', key='-BUTTON1-')]]), sg.Button('%s' % languagedick[3] + ' ✘', key='-BUTTON3-')]]
    footer = [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]

    window = sg.Window('%s' % languagedick[4], layout = [content, content_s, theme_selection_layout, content2, footer], size=(575,790), resizable=True, element_justification='center', finalize = True)

    btnHandler = public.ButtonHandler(window)

    # Creates the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-BUTTON3-':
            break

        elif event == '-BUTTON1-':
            selected_theme = None
            for theme_key, theme_value in values.items():
                if theme_value is True:
                    selected_theme = theme_key
                    break
            if selected_theme is not None:
                config["theme"] = theme = selected_theme
                with open(config_file_path, "w") as config_file:
                    yaml.dump(config, config_file, default_flow_style=False)  # Indentation added for better readability
                sg.popup('Theme set! \nUpdate requires restart', title='Success')
                window.close()
            else:
                sg.popup('Please select a theme first!', title='Error')

        elif event == '-BUTTON4-':
            if values['HKE'] == True:
                config["theme"] = theme 
            elif values['SNFLWR'] == True:
                config["theme"] = theme 
            elif values['BBGM'] == True:
                config["theme"] = theme 
            elif values['LM'] == True:
                config["theme"] = theme 
            elif values['DM'] == True:
                config["theme"] = theme 
            elif values['RR'] == True:
                config["theme"] = theme 
            elif values['FRST'] == True:
                config["theme"] = theme
            elif values['TNGRN'] == True:
                config["theme"] = theme 
            elif values['RP'] == True:
                config["theme"] = theme 
            elif values['BB'] == True:
                config["theme"] = theme    
                
            with open(config_file_path, "w") as config_file:
                yaml.dump(config, config_file, default_flow_style=False)  # Indentation added for better readability
            sg.popup('Theme set! \nUpdate requires restart', title='Success')
            window.close()

        btnHandler.handleColorChange(event)

    # Close the main window
    window.close()

def themeChecker(them):
    global theme
    return theme == them
