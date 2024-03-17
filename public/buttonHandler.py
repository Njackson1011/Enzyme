class ButtonHandler:
    def __init__(self, window, theme):
        self.window = window
        self.btnEventMouseOver = []
        self.btnEventMouseAway = []
        self.theme = theme

        for el in self.window.AllKeysDict:
            if 'BUTTON' in el:
                self.window[el].bind('<Enter>', '+MOUSE OVER+')
                self.window[el].bind('<Leave>', '+MOUSE AWAY+')

                self.btnEventMouseOver.append(el + '+MOUSE OVER+')
                self.btnEventMouseAway.append(el + '+MOUSE AWAY+')

    def handleColorChange(self, event):
        hover_color = self.theme.get('BUTTON_HOVER', 'BUTTON')
        
        if event in self.btnEventMouseOver:
            if '✘' in self.window[event[:9]].get_text():
                self.window[event[:9]].update(button_color=('#000000', '#b22222'))
            elif '🔒  End my Shift' in self.window[event[:9]].get_text():
                self.window[event[:9]].update(button_color=('#000000', '#b22222'))
            elif '🔑  Start my Shift' in self.window[event[:9]].get_text():
                self.window[event[:9]].update(button_color=('#000000', 'forestgreen'))
            else:
                self.window[event[:9]].update(button_color=hover_color)
        elif event in self.btnEventMouseAway:
            self.window[event[:9]].update(button_color=self.theme.get('BUTTON'))
