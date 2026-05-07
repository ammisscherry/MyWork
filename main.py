import flet as ft
from vista.asistenciaView import AsistenciaView

def main(page: ft.Page):
    vista=AsistenciaView(page)

    page.add(
        vista.construirInterfaz()
    )
ft.app(target=main)