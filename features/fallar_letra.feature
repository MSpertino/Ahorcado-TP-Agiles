# language: es
@HU-05
Característica: Descontar intento
  Como jugador
  quiero que se descuente un intento cuando ingreso una letra incorrecta
  para que el juego tenga tensión y límites

  @CA-1
  Escenario: El jugador falla una letra
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Entonces se ven 5 intentos restantes