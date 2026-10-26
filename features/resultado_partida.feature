# language: es
@HU-08
Característica: Ver resultado de la partida
  Como jugador
  quiero ver un mensaje claro de si gané o perdí al finalizar la partida
  para saber el resultado de inmediato

  @CA-1
  @CA-3
  Escenario: El jugador completa la palabra y gana la partida
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "G"
    Y el jugador ingresa la letra "A"
    Y el jugador ingresa la letra "T"
    Y el jugador ingresa la letra "O"
    Entonces se ve el mensaje de resultado "Ganaste"