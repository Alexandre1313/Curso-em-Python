import PySimpleGUI as Sg

Sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[Sg.Text('Some text on Row 1')],
          [Sg.Text('Enter something on Row 2'), Sg.InputText('Digite aqui...')],
          [Sg.Button('Ok'), Sg.Button('Cancel')]]

# Create the Window
window = Sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == Sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
