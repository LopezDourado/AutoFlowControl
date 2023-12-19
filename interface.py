import flet as ft


def interface(page: ft.Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    row1 = ft.Row([
        ft.Container(
            ft.Text('ADD ACTION'),
            width= 200,
            height= 50,
            alignment= ft.alignment.center,

            bgcolor=FG,
            border_radius=35
        ),
        ft.Container(
            ft.Text('REMOVE ACCTION'),
            width= 200,
            height= 50,
            alignment= ft.alignment.center,
            
            bgcolor=FG,
            border_radius=35
        )
    ], alignment=ft.MainAxisAlignment.CENTER)

    row2 = ft.Row([
        ft.Container(
        ft.Text('LIST HERE'),
        width= 350,
        height= 500,
        alignment= ft.alignment.center,

        bgcolor=FG,
        border_radius=35
        ),

        ft.Container(
        ft.Text('UP \n AND \n DOWN'),
        width= 50,
        height= 200,
        alignment= ft.alignment.center,

        bgcolor=FG,
        border_radius=35
        ),



    ],alignment=ft.MainAxisAlignment.CENTER)

    row3 = ft.Row([
        ft.Container(
        ft.Text('RUN >:)'),
        width= 200,
        height= 50,
        alignment= ft.alignment.center,

        bgcolor=FG,
        border_radius=35
        ),



    ], alignment=ft.MainAxisAlignment.CENTER)
    
    #action in list
    container = ft.Container(
        width= page.width,
        height= page.height,
        bgcolor=FG,
        border_radius=35
    )


    

    page.add(row1)
    page.add(row2)
    page.add(row3)
    page.update()

    def check():
        while True:
            row2.update()

ft.app(target=interface)