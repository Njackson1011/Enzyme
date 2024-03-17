import PySimpleGUI as sg
import json
import public
import os, sys
import subprocess
import yaml

#


# Define the "Search" window and search feature
def search():
    config_file_path = "C:\\autostart\\Application\\Enzyme\\pages\\config.yaml"
    with open(config_file_path, "r") as config_file:
        config = yaml.safe_load(config_file)
        f = open('C:\\autostart\\Application\\Enzyme\\language\\'+config.get("language")+'\\search.json')
        languagedick = json.load(f)
    f = open('C:\\autostart\\Application\\Enzyme\\pages\\files_'+config.get("language")+'.json')
    files = json.load(f)

    with open(config_file_path, "r") as theme:
            config = yaml.safe_load(theme)
            fart = config.get("theme")
    theme_mapping = public.theme_mapping
    selected_theme = theme_mapping.get(fart)
    sg.LOOK_AND_FEEL_TABLE[fart] = selected_theme
    sg.theme(fart)

    layout = [
        [sg.Text('%s' % languagedick[0])],
        [sg.InputText(key='search', font=public.BODY_FONT)],
        [sg.Text('%s' % languagedick[1])],
        [sg.CB('⇐My PC', key="-My PC-"),
         sg.CB('⇐C', key="-C-"),
         sg.CB('⇐D', key="-D-"),
         sg.CB('⇐E', key="-E-"),
         sg.CB('⇐F', key="-F-")],
        [sg.CB('⇐CRS', key="-CRS-"),
         sg.CB('⇐GIBBS', key="-GIBBS-"),
         sg.CB('⇐TAI', key="-TAI-"),
         sg.CB('⇐DCS', key="-DCS-")],
        [sg.Button('%s' % languagedick[2] + ' 🔍', key='-BUTTON1-', bind_return_key=True), sg.Button('%s' % languagedick[3] + ' ✘', key='-BUTTON2-')],
        [sg.Listbox([], size=(65, 17), key='_output_', font=public.BODY_FONT, enable_events=True)],
        [sg.Button('%s' % languagedick[4] + ' 🔍', key='-BUTTON3-'),
         sg.Button('%s' % languagedick[5] + ' ⚙', key='-BUTTON4-')],
        [sg.Text(("Enzyme © 2022-2024"), font=public.FOOTER_FONT, text_color='#FFFFFF')]
    ]

    # Create the search window
    window = sg.Window('%s' % languagedick[6], layout, size=(700, 635), element_justification='center', finalize=True)

    btnHandler = public.ButtonHandler(window, selected_theme)

    try:
        # Creates the event loop
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '-BUTTON2-':
                break

            elif event == '-BUTTON1-':
                # Defined variables
                window.FindElement('_output_').Update('')
                search_query = values['search'].lower()
                search_terms = search_query.split()
                found_results = []
                filter = []
                term_count = {}

                if values['-My PC-']:
                    filter.append(0)
                if values['-C-']:
                    filter.append(1)
                if values['-D-']:
                    filter.append(2)
                if values['-E-']:
                    filter.append(3)
                if values['-F-']: 
                    filter.append(4)
                if values['-CRS-']:
                    filter.append(5)
                if values['-GIBBS-']:
                    filter.append(6)
                if values['-TAI-']:
                    filter.append(7)
                if values['-DCS-']:
                    filter.append(8)
                if values['search'] == "":
                    window['_output_'].update([]) 
                    window['_output_'].update(['%s' % languagedick[7]])
                else:
                    for file in files:  # Enumerate through each entry in files.json
                        count = 0
                        for search in search_terms:  # Enumerate through each search_term and see if the given index is found in a file's title, error, or name
                            if search in file['title'].lower() or search in file['error'].lower() or search in file['name'].lower():
                                count += 1
                        if count > 0:  # Assuming that the given search term is found in a file:
                            if file not in found_results:
                                found_results.append(file)
                                term_count[tuple(file.items())] = count  # Save the count for the file as a tuple

                    if len(found_results) == 0: # Assuming the search query found no matches
                        output_data = ['%s' % languagedick[8]]
                    else:
                        # Searches through each file and sees which file has the most search_terms found.
                        max_count = max(term_count.values())

                        # Displays the files given and checks to see if a filter has been applied
                        output_data = []
                        output_data.append('%s' % languagedick[9])
                        if len(filter) == 0:
                            for result in found_results:
                                if term_count[tuple(result.items())] == max_count:
                                    output_data.append(result['title'])
                        else:
                            for result in found_results:
                                if result['type'] in filter or result['type'] == -1:
                                    output_data.append(result['title'])

                    window['_output_'].update(output_data)

            elif event == '-BUTTON3-' or event == '-BUTTON4-':
                selected_entry = values['_output_'][0]
                file_path = None

                if selected_entry not in ['%s' % languagedick[7], '%s' % languagedick[8], '%s' % languagedick[9]]:
                    try:
                        for file in files: # Load the selected file's directory path
                            if file['title'] == selected_entry:
                                file_path = file['path']
                                break

                        if file_path:
                            if event == '-BUTTON3-': # Find
                                subprocess.Popen(f'explorer /select,"{file_path}"')
                            elif event == '-BUTTON4-': # Run
                                os.startfile(file_path)  

                    except Exception as e:
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n\nThe selected file", file['title'], "cannot be found or run!",
                                    "\nPlease reach out to Victor A Gurganus or Nicholas J Jackson!")

            btnHandler.handleColorChange(event)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        sg.popup_error(f"Error: {exc_type}\nFile: {fname}\nLine: {exc_tb.tb_lineno}\n\nThe provided search query", search_query, "failed",
                       "\nPlease reach out to Victor A Gurganus or Nicholas J Jackson!")

    # Close the main window
    window.close()