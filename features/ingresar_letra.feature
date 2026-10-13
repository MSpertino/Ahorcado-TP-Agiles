# language: es
@HU-03
Característica: Ingresar letra
  Como jugador
  quiero ingresar una letra por vez
  para ir descubriendo la palabra progresivamente

  @CA-1
  Escenario: El jugador ingresa una letra y se revela en la palabra
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "A"
    Entonces se ve la palabra "_ A _ _"

  @CA-2
  @CA-3
  Escenario: El jugador intenta ingresar más de un carácter
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "AB"
    Entonces se ve un mensaje de entrada rechazada