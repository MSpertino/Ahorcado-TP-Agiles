class EntradaInvalida(Exception):
    pass

PALABRAS = ["GATO", "PERRO", "CASA", "ARBOL", "LIBRO", "MESA", "SILLA", "PLAYA", "TREN", "FLOR"]

def elegir_palabra(anterior):
    return PALABRAS[0]

class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_arriesgadas = set()
        self.intentos_restantes = 6

    def arriesgar(self, letra):
        if self.resultado() != "":
            raise EntradaInvalida("La partida ya terminó")
        if len(letra) > 1:
            raise EntradaInvalida("Solo se permite una letra por vez")
        if not letra.isalpha():
            raise EntradaInvalida("Solo se permiten letras")
        letra = letra.upper()
        if letra in self.letras_arriesgadas:
            raise EntradaInvalida("Ya ingresaste esa letra")
        self.letras_arriesgadas.add(letra)
        if letra not in self.palabra:
            self.intentos_restantes -= 1

    def palabra_enmascarada(self):
        return " ".join(letra if letra in self.letras_arriesgadas else "_" for letra in self.palabra)

    def resultado(self):
        if all(letra in self.letras_arriesgadas for letra in self.palabra):
            return "Ganaste"
        if self.intentos_restantes == 0:
            return "Perdiste"
        return ""

    def palabra_revelada(self):
        if self.resultado() == "Perdiste":
            return self.palabra
        return ""