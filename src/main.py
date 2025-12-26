import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(value="پیش بینی قیمت خانه"))
    page.window.maximized = True


ft.run(main)
