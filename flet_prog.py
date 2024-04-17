import flet as ft
import flet_fastapi

import prog

async def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dlg_non = ft.AlertDialog(
        title=ft.Text("Вы не ввели IP")
    )

    dlg_error = ft.AlertDialog(
        title=ft.Text("Вы ввели неверный IP")
    )
    
    async def button_func(e):
        if not field.value:
            e.control.page.dialog = dlg_non
            dlg_non.open = True
            await e.control.page.update_async()

        else:
            data = prog.get_info_by_ip(field.value)

            if data == "Error":
                e.control.page.dialog = dlg_error
                dlg_error.open = True
                await e.control.page.update_async()

            else:
                text.value = data

                await page.update_async()

    text = ft.Text(
        size=20
    )

    field = ft.TextField(
        label="Введите IP",
        width=260
        )

    button = ft.ElevatedButton(
        on_click=button_func,
        width=260,
        height=40,
        style=ft.ButtonStyle(
            shape={
                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
                    radius=10
                ),
            }
        ),
        content=ft.Column(
            [ft.Text(value="Выдать информацию", size=20)],
            alignment=ft.MainAxisAlignment.CENTER
            )
        )

    await page.add_async(
        field,
        button,
        text
        )

app = flet_fastapi.app(main)