import pytest

from src.domain.ahorcado import Ahorcado, EntradaInvalida


def test_arriesgar_un_numero_se_rechaza_porque_solo_se_permiten_letras():
    juego = Ahorcado("GATO")
    with pytest.raises(EntradaInvalida, match="Solo se permiten letras"):
        juego.arriesgar("3")


def test_arriesgar_una_letra_no_se_rechaza():
    juego = Ahorcado("GATO")
    juego.arriesgar("A")
