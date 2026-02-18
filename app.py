import flet as ft

def main(page: ft.Page):

    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    page_1 = ft.Container()

    page_2 = ft.Row(
        controls= [
            ft.Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding= ft.padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content= ft.Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = ft.Container (
        width=400,
        height=850,
        bgcolor= BG,
        border_radius=35,
        content= ft.Stack (
            controls= [
                page_1,
                page_2
            ]
        )
    )

    page.add(container)

ft.run(main)