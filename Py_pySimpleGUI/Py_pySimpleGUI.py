
#import PySimpleGUI27

#PySimpleGUI27. main()

import PySimpleGUI as sg

#PySimpleGUI. main()

#import PySimpleGUI  as sg

#sg.popup('This is my first popup')
#sg.popup('popup')  # Shows OK button
#sg.popup_ok('popup_ok')  # Shows OK button
#sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
#sg.popup_cancel('popup_cancel')  # Shows Cancelled button
#sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
#sg.popup_error('popup_error')  # Shows red error button
#sg.popup_timed('popup_timed')  # Automatically closes
#sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed


sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()],
            [sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, values)
    sg.Popup(event, values[0])

    source_filename = values[0]     # the first input element is values[0]


#event, values = window.read()
window.close()

#sg.Popup(event, values[0])
#source_filename = values[0]     # the first input element is values[0]

