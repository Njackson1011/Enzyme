# Don't fucking touch this or everything will break
class ButtonHandler:

    def __init__(self, window):
        self.window = window
        self.btnEventMouseOver = []
        self.btnEventMouseAway = []

        for el in self.window.AllKeysDict:
            if 'BUTTON' in el:
                self.window[el].bind('<Enter>', '+MOUSE OVER+')
                self.window[el].bind('<Leave>', '+MOUSE AWAY+')

                self.btnEventMouseOver.append(el + '+MOUSE OVER+')
                self.btnEventMouseAway.append(el + '+MOUSE AWAY+')

    def handleColorChange(self, event):
        if event in self.btnEventMouseOver:
            self.window[event[:9]].update(button_color=('#000000', '#547980'))
        elif event in self.btnEventMouseAway:
            self.window[event[:9]].update(button_color=('#000000', '#45ADA8'))