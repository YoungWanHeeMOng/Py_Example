
import PySimpleGUI as sg

window = sg.Window('Testing the Debugger', [[sg.Text('Debugger Tester'), sg.In('Input here'), sg.B('Push Me')]])

while True:
    event, values = window.read(timeout=500)
    if event == sg.TIMEOUT_KEY:
        continue
    if event == sg.WIN_CLOSED:
        break
    print(event, values)
window.close()