# language: es
@HU-09
Característica: Ver la palabra completa al perder
  Como jugador
  quiero ver la palabra completa si pierdo
  para saber cuál era la respuesta correcta

  @CA-1
  @CA-2
  @CA-3
  Escenario: El jugador pierde y ve la palabra completa
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "I"
    Y el jugador ingresa la letra "U"
    Y el jugador ingresa la letra "L"
    Y el jugador ingresa la letra "M"
    Y el jugador ingresa la letra "N"
    Entonces se ve el mensaje de resultado "Perdiste"
    Y se ve la palabra revelada "GATO"
