class Cliente:
    def __init__(self, nombre, correo):
        self._nombre = nombre
        self._correo = correo
        self._registrado = True

    def getCorreo(self):
        return self._correo

    def registrar(self):
        if self._registrado:
            self._registrado = False
            return True
        return False

    def __str__(self):
        return f"{self._nombre} - {self._correo}"
