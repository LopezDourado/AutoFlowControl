import flet as ft


pageWidth = 600
pageHeight = 800


def interface(page: ft.Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    def page_resize(e):
        page.update()

    page.on_resize = page_resize

    addActButton = ft.ElevatedButton(
        text="ADD ACTION",
        col={"sm": 6, "md": 4, "xl": 2}
        )
    removeActButton = ft.ElevatedButton(
        text="REMOVE ACTION",
        col={"sm": 6, "md": 4, "xl": 2}
        )
    runButton = ft.ElevatedButton(
        text="RUN >:)",
        col={"sm": 6, "md": 4, "xl": 2}
        )
    

    listAcctionsToDo = ft.DataTable(
        col={"sm": 1, "md": 1, "xl": 1},
        columns=[    
                ft.DataColumn(ft.Text("TypeAction")),
                ft.DataColumn(ft.Text("Acction")),
                ft.DataColumn(ft.Text("time"), numeric=True),
            ],
    )
    
    row1 = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER)

    row1.controls.append(addActButton)
    row1.controls.append(removeActButton)

    row2.controls.append(listAcctionsToDo)

    row3.controls.append(runButton)

    page_resize(None)

    page.add(row1)
    page.add(row2)
    page.add(row3)

    page.update()

ft.app(target=interface)