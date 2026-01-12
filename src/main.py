import flet as ft


def main(page: ft.Page):
    
    page.appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("Dashboard"),
    actions=[
        ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)
        ],
        bgcolor=ft.Colors.SURFACE_CONTAINER,)
    page.title = "Home Price App"
    page.window.maximized = True
    

    page.add(ft.ResponsiveRow(ft.Column(col={"sm": 6},controls=[ft.TextField(label="Search...",),
                 ft.ElevatedButton(icon=ft.Icons.SEARCH)]),rtl=True))
    page.add(ft.ResponsiveRow([ft.Column(col={"sm": 6}, controls=[ft.Text("نمودار قیمت خانه های تهران")]),
                     ft.Column(col={"sm": 6}, controls=[ft.Text("لیست قیمت خانه ها")])],rtl=True))

    
ft.run(main)
