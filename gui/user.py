import PySimpleGUI as sg

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class UserWindow:
    def __init__(self, user):
        self._user = user
        self._title = "Interface utilisateur"
        self._layout = [
            [sg.Text("Nom d'utilisateur: ", key="USER")],
            [sg.InputText(default_text=self._user.first_name, key='NAME')],
            [sg.Button('Valider', key='VALIDATE')]
        ]
        self._window = None

    def run(self):
        self._window = sg.Window(self._title, self._layout)
        while True:
            event, value = self._window.read()
            if event == sg.WINDOW_CLOSED or event == "VALIDATE":
                break
        self._user.first_name = value["NAME"]
        self._window.close()

usr = User("Romeo", "Rel")

win = UserWindow(usr)
win.run()
print(usr.first_name)