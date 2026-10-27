# language: es
@HU-10
Característica: Jugar de nuevo
  Como jugador
  quiero tener un botón para jugar de nuevo
  para empezar otra partida sin esfuerzo

  @CA-1
  Escenario: El jugador pierde y ve el botón para jugar de nuevo
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "I"
    Y el jugador ingresa la letra "U"
    Y el jugador ingresa la letra "L"
    Y el jugador ingresa la letra "M"
    Y el jugador ingresa la letra "N"
    Entonces se ve el botón "Jugar de nuevo"

  @CA-1
  Escenario: El jugador gana y ve el botón para jugar de nuevo
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "G"
    Y el jugador ingresa la letra "A"
    Y el jugador ingresa la letra "T"
    Y el jugador ingresa la letra "O"
    Entonces se ve el botón "Jugar de nuevo"
