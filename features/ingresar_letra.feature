# language: es
@HU-03
Característica: Ingresar letra
  Como jugador
  quiero ingresar una letra por vez
  para ir descubriendo la palabra progresivamente

  @CA-1
  Escenario: El jugador ingresa un solo carácter válido
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "A"
    Entonces no se ve ningún mensaje de error