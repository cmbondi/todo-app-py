import functions
import PySimpleGUI as sg
import time

sg.theme("Dark")

clock = sg.Text('', key='clock')
label_title = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("Todo App",
                   layout=[[clock], [label_title],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=10)
    window["clock"].Update(value=time.strftime("%A %B %d %I:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 16))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].Update(value="")
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 16))

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
