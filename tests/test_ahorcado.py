import pytest

from src.domain.ahorcado import Ahorcado, EntradaInvalida

@pytest.mark.parametrize("entrada", ["3", "#", " "], ids=["numero", "simbolo", "espacio"])
def test_arriesgar_algo_que_no_es_letra_se_rechaza(entrada):
    juego = Ahorcado("GATO")
    with pytest.raises(EntradaInvalida, match="Solo se permiten letras"):
        juego.arriesgar(entrada)

def test_arriesgar_una_letra_no_se_rechaza():
    juego = Ahorcado("GATO")
    juego.arriesgar("A")

def test_arriesgar_mas_de_una_letra_se_rechaza():
    juego = Ahorcado("GATO")
    with pytest.raises(EntradaInvalida, match="Solo se permite una letra por vez"):
        juego.arriesgar("AB")

def test_arriesgar_letra_acertada_revela_letra():
    juego = Ahorcado("GATO")
    juego.arriesgar("A")
    assert juego.palabra_enmascarada() == "_ A _ _"

def test_una_partida_nueva_tiene_6_intentos_restantes():
    juego = Ahorcado("GATO")
    assert juego.intentos_restantes == 6


def test_arriesgar_letra_revela_multiples_ocurrencias():
    juego = Ahorcado("PERRO")
    juego.arriesgar("R")
    assert juego.palabra_enmascarada() == "_ _ R R _"

def test_arriesgar_letra_no_presente_no_revela_nada():
    juego = Ahorcado("GATO")
    juego.arriesgar("Z")
    assert juego.palabra_enmascarada() == "_ _ _ _"

def test_fallar_letra_descuenta_intento():
    juego = Ahorcado("GATO")
    juego.arriesgar("E")
    assert juego.intentos_restantes == 5

def test_acertar_letra_no_descuenta_intento():
    juego = Ahorcado("GATO")
    juego.arriesgar("A")
    assert juego.intentos_restantes == 6
