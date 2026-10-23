# language: es
@HU-07
Característica: Validar letra repetida
  Como jugador
  quiero que el sistema me avise si ya ingresé esa letra antes
  para no desperdiciar intentos repitiendo jugadas

  @CA-1
  @CA-3
  Escenario: El jugador ingresa una letra que ya usó
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "E"
    Entonces se ve el mensaje de error "Ya ingresaste esa letra"

  @CA-2
  @CA-3
  Escenario: Repetir una letra fallada no descuenta otro intento
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "I"
    Y el jugador ingresa la letra "E"
    Entonces se ven 4 intentos restantes
