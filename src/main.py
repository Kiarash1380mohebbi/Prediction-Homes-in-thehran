import flet as ft


def main(page: ft.Page):
    page.add(ft.Text(value="پیش بینی قیمت خانه"))
    page.window.maximized = True


if __name__ == "__main__":
    ft.run(main)
