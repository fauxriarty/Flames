import flet as flet
from flames import flames


def main(page: flet.page):
    def on_submit(e):
        if your_name_input.value and their_name_input.value == "":
            your_name_input.error_text = "Enter Values"
            their_name_input.error_text = "Enter Values"
            page.update()
        else:
            answer = flames(your_name_input.value, their_name_input.value)
            relationship.value = "Your relationship with " + their_name_input.value + " can be " + answer
            your_name_input.error_text = ""
            their_name_input.error_text = ""
            page.update()

    page.appbar = flet.AppBar(
        title=flet.Text("Flames 🔥"),
        center_title=True,
    )

    your_name_input = flet.TextField(
        label="Your Name"
    )

    their_name_input = flet.TextField(
        label="Their Name"
    )
    submit_button = flet.ElevatedButton(
        "Check",
        on_click=on_submit
    )
    relationship = flet.Text(
        text_align=flet.TextAlign.CENTER,
        value="",
        weight=flet.FontWeight.BOLD,
        color=flet.colors.ORANGE,
        size=32
    )

    column = flet.Column(
        expand=True,
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        controls=[
            your_name_input,
            their_name_input,
            submit_button,
        ]
    )

    main_column = flet.Column(
        alignment=flet.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        expand=True,
        controls=[
            column,
            relationship
        ]
    )
    page.add(
        main_column
    )


flet.app(target=main)
