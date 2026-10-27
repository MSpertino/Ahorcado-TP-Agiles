import pytest

from src.domain.ahorcado import Ahorcado, EntradaInvalida, PALABRAS, elegir_palabra

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

@pytest.mark.parametrize("entrada", ["3", "#", " "], ids=["numero", "simbolo", "espacio"])
def test_arriesgar_entrada_invalida_no_descuenta_intento(entrada):
    juego = Ahorcado("GATO")
    with pytest.raises(EntradaInvalida):
        juego.arriesgar(entrada)
    assert juego.intentos_restantes == 6

def test_arriesgar_letra_minuscula_revela_sin_descontar_intento():
    juego = Ahorcado("GATO")
    juego.arriesgar("a")
    assert juego.palabra_enmascarada() == "_ A _ _"
    assert juego.intentos_restantes == 6

def test_arriesgar_letra_repetida_se_rechaza():
    juego = Ahorcado("GATO")
    juego.arriesgar("E")
    with pytest.raises(EntradaInvalida, match="Ya ingresaste esa letra"):
        juego.arriesgar("E")

def test_ganar_partida_al_adivinar_todas_las_letras():
    juego = Ahorcado("GATO")
    juego.arriesgar("G")
    juego.arriesgar("A")
    juego.arriesgar("T")
    juego.arriesgar("O")
    assert juego.resultado() == "Ganaste"

def test_partida_en_curso_no_tiene_resultado():
    juego = Ahorcado("GATO")
    juego.arriesgar("G")
    assert juego.resultado() == ""

def test_perder_partida_al_agotar_intentos():
    juego = Ahorcado("GATO")
    for letra in ["E", "I", "U", "L", "M", "N"]:
        juego.arriesgar(letra)
    assert juego.resultado() == "Perdiste"

def test_arriesgar_con_la_partida_perdida_se_rechaza():
    juego = Ahorcado("GATO")
    for letra in "EIULMN":
        juego.arriesgar(letra)
    with pytest.raises(EntradaInvalida, match="La partida ya terminó"):
        juego.arriesgar("P")

def test_arriesgar_con_la_partida_ganada_se_rechaza():
    juego = Ahorcado("GATO")
    for letra in "GATO":
        juego.arriesgar(letra)
    with pytest.raises(EntradaInvalida, match="La partida ya terminó"):
        juego.arriesgar("E")

def test_perder_partida_revela_la_palabra():
    juego = Ahorcado("GATO")
    for letra in "EIULMN":
        juego.arriesgar(letra)
    assert juego.palabra_revelada() == "GATO"

def test_partida_en_curso_no_revela_la_palabra():
    juego = Ahorcado("GATO")
    juego.arriesgar("G")
    assert juego.palabra_revelada() == ""

def test_ganar_partida_no_revela_la_palabra():
    juego = Ahorcado("GATO")
    for letra in "GATO":
        juego.arriesgar(letra)
    assert juego.palabra_revelada() == ""

def test_elegir_palabra_devuelve_una_palabra_de_la_lista():
    assert elegir_palabra("GATO") in PALABRAS