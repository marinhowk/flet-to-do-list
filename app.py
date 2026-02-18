import flet as ft

def main(page: ft.Page):

    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    first_page_contents = ft.Container(
        content= ft.Column(
            controls= [
                ft.Row(alignment="spaceBetween",
                    controls=[
                        ft.Container(content= ft.Icon(ft.Icons.MENU)),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.SEARCH),
                                ft.Icon(ft.Icons.NOTIFICATIONS_NONE_OUTLINED)
                            ]
                        )
                    ]
                ),
                ft.Container(height=20),
                ft.Text(value="What's up, John! "),
                ft.Text(value="CATEGORIES"),
                ft.Container( padding=ft.padding.only(top=20, bottom=20,)
                             )
            ]
        )
    )

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