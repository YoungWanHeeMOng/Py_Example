
#import PySimpleGUI as sg

#gui_rows = [[sg.Text('Robotics Remote Control')],
#            [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
#            [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
#            [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
#            [sg.T('')],
#            [sg.Quit(button_color=('black', 'orange'))]
#            ]

#window = sg.Window('Robotics Remote Control', gui_rows)

##
## Some place later in your code...
## You need to perform a Read or Refresh call on your window every now and then or
## else it will apprear as if the program has locked up.
##
## your program's main loop
#while (True):
#    # This is the code that reads and updates your window
#    event, values = window.read(timeout=50)
#    print(event)
#    if event in ('Quit', sg.WIN_CLOSED):
#        break

#window.close()  # Don't forget to close your window!

import PySimpleGUI as sg

def ChatBot():
    layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
              [sg.Output(size=(80, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=True),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Chat Window', layout, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == 'SEND':
            print(value)
        else:
            break
    window.close()
ChatBot()