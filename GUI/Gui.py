import PySimpleGUI as sg
from Converter import Convert









infix=""
prefix=""
postfix=""
Expression=""
Layout=[
    [sg.Text("Please enter the Expression:"),sg.InputText()],
    [sg.Text(f"Infix:{infix}")],
    [sg.Text(f"Prefix:{prefix}")],
    [sg.Text(f"Postfix:{postfix}")],

    [sg.Button("Get Convert Expression"),sg.Button("Cancel")
     ]
]
window=sg.Window("Expression Converter",Layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    Expression=values[0]
    infix=Convert(Expression)[1]
    prefix=Convert(Expression)[0]
    postfix=Convert(Expression)[2]



window.close()


