import PySimpleGUI as sg










infix=""
prefix=""
postfix=""
Expression=""
Layout=[
    [sg.Text("Please enter the Expression:"),sg.InputText()],
    [sg.Text(f"Infix:{infix}")],
    [sg.Text(f"Prefix:{prefix}")],
    [sg.Text(f"Postfix:{postfix}")],

    [sg.Button("Get Convert Expression"),sg.Button("Cancel")]
]
window=sg.Window("Expression Converter",Layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    Expression=values[0]
    print(Expression)

window.close()


