class EntradaInvalida(Exception):
    pass


class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra

    def arriesgar(self, letra):
        if len(letra) > 1:
            raise EntradaInvalida("Solo se permite una letra por vez")
        if not letra.isalpha():
            raise EntradaInvalida("Solo se permiten letras")
