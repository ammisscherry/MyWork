import flet as ft
class AsistenciaView:
    def __init__(self, page:ft.page):
        self.page=page

        self.page.title="Sistema de asistencia"
        self.page.window_width=500
        self.page.window_height=600
        self.page.padding=20

        self.txt_nombre=ft.Textfield(
            label="Nombe del alumno",
            width=400
        )

        self.chk_presente= ft.Checkbox(
            label="Presente"
        )

        self.btn_registrar=ft.ElevatedButton(
            "Registrar asistencia",
            width=250
        )

        self.lbl_mensaje=ft.Text(
            value="",
            size=16
        )

        self.lista_registros=ft.Column()

    def construirInterfaz(self):
        