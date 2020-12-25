
import PySimpleGUI as sg

#def Canvas(canvas - a tkinter canvasf if you created one. Normally not set
#         background_color - canvas color
#         size - size in pixels
#         pad - element padding for packing
#         key - key used to lookup element
#         tooltip - tooltip text)

figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    # define the window layout
layout = [[sg.Text('Plot test')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.Button(button_text='OK',    size=(4, 2))]]

    # create the window and show it without the plot
window = sg.Window
fig_photo = draw_figure(window['canvas'].TKCanvas, fig)

    # show it all again and get buttons
event, value = window.read()

window.close()