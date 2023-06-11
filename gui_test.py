import PySimpleGUI as sg

#Ici, key est pareil que ID
layout = [
    [sg.Text('Entrer votre age: ')],
    #enable_events permet d'enregistrer l'age qui est entré sans avoir appuyé sur Valider
    [sg.InputText(key='AGE', enable_events=True)],

    [sg.Combo(['Belge', 'Français', 'Italien', 'Autre'], 'NATION', key='NATION')],

    [sg.Checkbox("J'accepte les conditions", default=False, key='CONDITION')],

    #sg.Column Permet de remettre sur une seule ligne les radios
    [
        sg.Column([
            [sg.Radio(['Homme'], group_id='GENRE', key='HOMME')],
            ]),
        sg.Column([
            [sg.Radio(['Femme'], group_id='GENRE', key='FEMME')],
            ]),
        sg.Column([
            [sg.Radio(['Autre'], group_id='GENRE', key='AUTRE')]
            ])
    ],

    [sg.Button('Valider', key='VALIDATE')]
]

#Ma premiere Interface ==> le titre
window = sg.Window('Ma premiere Interface', layout)
#Après, l'interface graphique se ferme

#Besoin d'une boucle infinie pour que l'interface persiste
#Si la boucle n'est pas là, l'interface ne s'affiche pas
#Ceci s'appele une boucle d'évènement
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'VALIDATE':
        break

print(values)
age = int(values['AGE'])
window.close()