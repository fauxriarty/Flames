import flet as flet
from flames import flames


def submit_clicked(name1, name2, column, page):
    result = flames(name1, name2)
    column.controls.append(flet.Text(result))
    page.update()


def submit_button(column, name1, name2, page):
    return flet.ElevatedButton(
        "Submit",
        on_click=submit_clicked(name1, name2, column, page)
    )
