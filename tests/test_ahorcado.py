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
