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

  @CA-2
  @CA-3
  Escenario: El jugador agota los intentos y pierde la partida
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "I"
    Y el jugador ingresa la letra "U"
    Y el jugador ingresa la letra "L"
    Y el jugador ingresa la letra "M"
    Y el jugador ingresa la letra "N"
    Entonces se ve el mensaje de resultado "Perdiste"

  @CA-4
  Escenario: El jugador no puede seguir jugando después de perder
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "I"
    Y el jugador ingresa la letra "U"
    Y el jugador ingresa la letra "L"
    Y el jugador ingresa la letra "M"
    Y el jugador ingresa la letra "N"
    Y el jugador ingresa la letra "P"
    Entonces se ve el mensaje de resultado "Perdiste"
    Y se ve el mensaje de error "La partida ya terminó"