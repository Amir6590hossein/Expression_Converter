import PySimpleGUI as sg
from Converter import Convert









infix=""
prefix=""
postfix=""
Expression=""
Layout=[
    [sg.Text("Please enter the Expression:"),sg.InputText()],
    [sg.Text("prefix:", key="prefix")],
    [sg.Text("infix:",key="infix")],

    [sg.Text("postfix:",key="postfix")],

    [sg.Button("Get Convert Expression"),sg.Button("Cancel")
     ]
]
window=sg.Window("Expression Converter",Layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event== "Get Convert Expression":
     Expression=values[0]
     window["infix"].Update(f"infix: {Convert(Expression)[1]}")
     window["postfix"].Update(f"postfix: {Convert(Expression)[2]}")
     window["prefix"].Update(f"prefix: {Convert(Expression)[0]}")





window.close()


