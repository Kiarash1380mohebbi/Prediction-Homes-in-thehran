import flet as ft


def main(page: ft.Page):
    
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("Dashboard"),
    actions=[
        ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)
        ],
        bgcolor=ft.Colors.SURFACE_CONTAINER,)
    page.title = "Prediction Home App"
    page.window.maximized = True
    page.add(ft.Text(value="پیش بینی قیمت خانه"))

ft.run(main)
