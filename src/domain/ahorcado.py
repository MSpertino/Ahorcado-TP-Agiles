class EntradaInvalida(Exception):
    pass


class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra

    def arriesgar(self, letra):
        raise EntradaInvalida("Solo se permiten letras")
