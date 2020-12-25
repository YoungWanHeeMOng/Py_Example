
import PySimpleGUI as sg

tab1_layout=[[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]
#pane=sg.Pane([col5, sg.Column([[sg.Pane([col1, col2, col4], handle_size=15,
#                 orientation='v',  background_color=None, show_handle=True, 
#                 visible=True, key='_PANE_', border_width=0,  
#                 relief=sg.RELIEF_GROOVE),]]),col3 ], orientation='h', 
#                  background_color=None, size=(160,160), 
#                  relief=sg.RELIEF_RAISED, border_width=0)

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
                  [sg.Button('Read')]]

window = sg.Window('Example TAB' ,layout)

event, value = window.read()

window.close()
