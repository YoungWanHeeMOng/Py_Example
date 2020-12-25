
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [
            [sg.Text('Please enter your Name, Address, Phone')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='-NAME-')],
            [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='-ADDRESS-')],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='-PHONE-')],
            [sg.Submit(), sg.Cancel()]
            ]

window = sg.Window('Simple data entry window', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    sg.Popup(event, values, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])

window.close()

