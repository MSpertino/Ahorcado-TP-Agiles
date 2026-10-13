class EntradaInvalida(Exception):
    pass

class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_arriesgadas = set()
        self.intentos_restantes = 6

    def arriesgar(self, letra):
        if len(letra) > 1:
            raise EntradaInvalida("Solo se permite una letra por vez")
        if not letra.isalpha():
            raise EntradaInvalida("Solo se permiten letras")
        self.letras_arriesgadas.add(letra)

    def palabra_enmascarada(self):
        return " ".join(letra if letra in self.letras_arriesgadas else "_" for letra in self.palabra)